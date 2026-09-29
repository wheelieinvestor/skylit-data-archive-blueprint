#!/usr/bin/env python3
"""Offline checks for this documentation repository. No network or data access."""

import json
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
ROLES = {
    "00-platform": 4,
    "01-atlas": 9,
    "02-flow": 20,
    "03-contracts": 16,
    "04-market": 6,
    "05-dark-pool": 2,
    "06-heat": 6,
    "07-tempest": 14,
    "08-dashboard": 0,
}
ALLOWED_SUFFIXES = {".md", ".json", ".py", ".yml"}
ALLOWED_SPECIAL = {"LICENSE", ".gitignore", ".env.example"}
FORBIDDEN_CONTENT = {
    "private machine path": r"/(?:Users|Volumes)/",
    "private resource UUID": r"\b[0-9a-fA-F]{8}-(?:[0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}\b",
    "private key": r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
    "GitHub token": r"\b(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,})\b",
    "AWS access key": r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b",
    "credential-bearing URL": r"https?://[^\s/@]+:[^\s/@]+@",
}


def main():
    errors = []
    git = subprocess.run(
        ["git", "ls-files", "-z"], cwd=ROOT, capture_output=True, check=False
    )
    if git.returncode != 0:
        raise SystemExit("Run this check from a Git checkout or initialize and stage the blueprint first.")
    names = [name for name in git.stdout.decode().split("\0") if name]
    if not names:
        raise SystemExit("No tracked/staged files. Stage the reviewed blueprint before checking.")
    for name in names:
        path = ROOT / name
        if path.is_symlink() or not path.is_file():
            errors.append(name + ": must be an ordinary file")
            continue
        if path.name not in ALLOWED_SPECIAL and path.suffix not in ALLOWED_SUFFIXES:
            errors.append(name + ": file type outside this documentation repository's allowlist")
        if ".local." in name or any(
            part in {"data", "raw", "curated", "results", "outputs", "logs"}
            for part in path.relative_to(ROOT).parts
        ):
            errors.append(name + ": runtime/local material is not publishable here")
        if path.stat().st_size > 250_000:
            errors.append(name + ": unexpectedly large file")
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeError:
            errors.append(name + ": non-text content")
            continue
        for label, pattern in FORBIDDEN_CONTENT.items():
            if re.search(pattern, content):
                errors.append(name + ": detected " + label)
        if path.suffix == ".json":
            try:
                json.loads(content)
            except ValueError:
                errors.append(name + ": invalid JSON")
        if path.suffix == ".md":
            if len(re.findall(r"^```", content, re.MULTILINE)) % 2:
                errors.append(name + ": unbalanced code fence")
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
                target = target.strip("<>")
                if urlsplit(target).scheme or target.startswith("#"):
                    continue
                linked = (path.parent / unquote(target.split("#")[0])).resolve()
                if ROOT not in linked.parents or not linked.is_file():
                    errors.append(name + ": broken/outside local link " + target)
    for line in (ROOT / ".env.example").read_text().splitlines():
        if line and not line.startswith("#") and "=" in line:
            if line.split("=", 1)[1].strip():
                errors.append(".env.example: populated value")
    inventory = json.loads((ROOT / "config/endpoint-inventory.json").read_text())
    operations = inventory["operations"]
    keys = {(op["service"], op["method"], op["path"]) for op in operations}
    if len(operations) != 77 or len(keys) != 77:
        errors.append("Inventory must contain 77 uniquely service-qualified routes in this dated revision")
    for role, expected in ROLES.items():
        if sum(op["owner"] == role for op in operations) != expected:
            errors.append(role + ": endpoint ownership count mismatch")
        if not (ROOT / "agents" / (role + ".md")).is_file():
            errors.append(role + ": missing role prompt")
    for op in operations:
        if op["owner"] not in ROLES or op["method"] != "GET":
            errors.append("Unexpected owner or method in route inventory")
    budget = json.loads((ROOT / "config/budget.example.json").read_text())
    if sum(budget["envelopes"].values()) != budget["monthly_cap"]:
        errors.append("Budget envelopes do not equal the total cap")
    operator = json.loads((ROOT / "config/operator.example.json").read_text())
    if operator["collection_enabled"] or operator["collection_start_confirmation"] is not None:
        errors.append("Operator template must keep collection disabled and unconfirmed")
    if any(operator["authority"].values()):
        errors.append("Operator template must not preauthorize actions")
    if errors:
        for error in errors:
            print("FAIL:", error)
        raise SystemExit(1)
    print(
        "PASS: {} reviewed file types; local links, JSON, nine roles, 77 unique routes, "
        "budget totals, empty secrets and collection-off defaults verified.".format(len(names))
    )
    print("This bounded check supplements manual diff review; it does not prove arbitrary content contains no data.")


if __name__ == "__main__":
    main()
