import csv
import subprocess

# === CONFIGURATION ===
REPO = "JoVanMontfort/issues"  # 🔧 Replace with your GitHub repo (e.g. johndoe/data-project)
CSV_FILE = "data_driven_behaviour_backlog_cp.csv"

# === IMPORT ISSUES FROM CSV ===
with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        title = row["Title"]
        body = row["Description"]
        labels = row["Labels"].split(",")

        print(f"Creating issue: {title}")
        result = subprocess.run([
            "gh", "issue", "create",
            "--repo", REPO,
            "--title", title,
            "--body", body,
            "--label", *labels
        ])

        if result.returncode != 0:
            print(f"❌ Failed to create issue: {title}")
        else:
            print(f"✅ Issue created: {title}")
