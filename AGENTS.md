# Public blueprint boundaries

This repository documents an archive architecture. It does not contain or operate a collector runtime. Keep it portable and free of real data, credentials, private infrastructure identifiers, account payloads, local machine paths, and private repository references.

Read LAUNCHPAD_CONTEXT.md before changing the guide. Implementation prompts target a separately selected operator repository. Do not deploy this documentation repository to Railway or use its sample budget as authorization to spend.

Do not copy an existing private Git history. Use original explanations, metadata-only templates, and links to public provider documentation. Preserve the distinction between reference implementation observations, design requirements, and software actually shipped here.

Required check: `python3 scripts/check_blueprint.py`. Review links, instructions, placeholder configuration and the staged file list. Do not fetch market data to validate documentation changes. Add runtime tests only if real runtime behavior is deliberately introduced in a separately authorized task.
