# Pushing krino-commitments to GitHub (operator action)

This folder is ready to become the public commitment repo. Claude cannot create the repo or push for you — you do:

1. Create a new **public** repo on GitHub named `krino-commitments` (empty — do not add a README; this folder has one).
2. In this folder, run:
   ```
   git init
   git add .
   git commit -m "Founding pre-registration 2026-07-06 (Y1 v15, Success Scorer v1.0)"
   git branch -M main
   git remote add origin https://github.com/<your-username>/krino-commitments.git
   git push -u origin main
   ```
3. The push timestamp (git history + GitHub) is the tamper-evidence. Thereafter, each issue's source hash is
   appended to `COMMITMENTS.md` and pushed **before** the issue publishes.

Keep the internal briefing and trackers **private** — only their hashes belong here. This repo holds the
methodology, the scorer, and the hash log; never the raw internal working data.
