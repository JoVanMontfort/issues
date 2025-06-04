import csv
import subprocess

# === CONFIGURATION ===
REPO = "JoVanMontfort/issues"  # 🔧 Replace with your GitHub repo
CSV_FILE = "triggeriq_issues_with_assignees.csv"

# === IMPORT ISSUES FROM CSV ===
with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        title = row["Title"]
        body = row["Description"]
        labels = [label.strip() for label in row["Labels"].split(",") if label.strip()]
        assignee = row.get("Assignee", "").strip()
        milestone = row.get("Milestone", "").strip()

        print(f"📌 Creating issue: {title}")

        command = [
            "gh", "issue", "create",
            "--repo", REPO,
            "--title", title,
            "--body", body
        ]

        if labels:
            command.extend(["--label", *labels])
        if assignee:
            command.extend(["--assignee", assignee])
        if milestone:
            command.extend(["--milestone", milestone])

        result = subprocess.run(command)

        if result.returncode != 0:
            print(f"❌ Failed to create issue: {title}")
        else:
            print(f"✅ Issue created: {title}")
