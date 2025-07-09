import os
import subprocess
import random
from datetime import datetime, timedelta

# === CONFIG ===
start_date = datetime(2024, 5, 1)
end_date = datetime(2025, 5, 1)  # day before today
min_commits = 2
max_commits = 4

commit_messages = [
    "Fix bug in main logic",
    "recent commit",
    "new commit",
    "new commit"
    "Improve documentation",
    "Update README",
    "Optimize algorithm",
    "Minor update to file"
]

file_names = ["video_capt_code.ipynb" , "report.docx"]

# === SIMULATION ===

# Create dummy files
for file in file_names:
    with open(file, 'w') as f:
        f.write(f"Initial content for {file}\n")

subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "Initial commit"])

current_date = start_date

while current_date <= end_date:
    num_commits = random.randint(min_commits, max_commits)

    for _ in range(num_commits):
        commit_time = current_date + timedelta(
            days=random.randint(0, 6),
            hours=random.randint(0, 23),
            minutes=random.randint(0, 59)
        )

        # Pick a random file and update it
        file = random.choice(file_names)
        with open(file, 'a') as f:
            f.write(f"Work done on {commit_time.isoformat()}\n")

        subprocess.run(["git", "add", file])

        # Use random commit message
        message = random.choice(commit_messages)

        # Set author and committer date
        env = os.environ.copy()
        iso_date = commit_time.strftime("%Y-%m-%dT%H:%M:%S")
        env["GIT_AUTHOR_NAME"] = "futurepanther786"
        env["GIT_COMMITTER_NAME"] = "futurepanther786"
        env["GIT_AUTHOR_EMAIL"] = "aryanrbsingh2012@gmail.com"
        env["GIT_COMMITTER_EMAIL"] = "aryanrbsingh2012@gmail.com"


        subprocess.run(["git", "commit", "-m", f"{message}"], env=env)

    current_date += timedelta(weeks=1)

print("✅ Fake commit history generated!")
