# Standing publish workflow (adopted 2026-07-11)

Each issue: upload the "KRINO commitments" folder to the session → Claude returns a zip
mirroring the repo layout with ONLY new/changed files → extract INTO the krino-commitments
folder (merge/overwrite — NEVER delete the folder itself: .git lives there and holds the
tamper-evidence history) → then:

    git add -A
    git commit -m "REPORT-NNN: commit + reveal"
    git push

One push per issue is sufficient while the repo is the publication venue (the push timestamp
proves the artifact existed then). If an external channel (e.g. Substack) goes live, the
two-step returns: push the COMMITMENTS.md entry FIRST, publish externally SECOND.

Verify any revealed artifact anytime:
    certutil -hashfile revealed\<file> SHA256   (Windows)
and compare to its line in COMMITMENTS.md.

Keep internal briefings/trackers private — only hashes belong here.
