import os
import subprocess
from datetime import datetime, timedelta
import random

# Config for git progile
GITHUB_REPO = "https://github.com/YOUR_USERNAME/github-activity.git"  # change this
LOCAL_REPO = "temp-repo"
USER_NAME = "YOUR_USERNAME"  # change this
USER_EMAIL = "your.email@example.com"  # change this
DAYS_BACK = 365
MAX_COMMITS_PER_DAY = 3

# Step 1: Set up local repo
if not os.path.exists(LOCAL_REPO):
    subprocess.run(["git", "clone", GITHUB_REPO, LOCAL_REPO])

os.chdir(LOCAL_REPO)

subprocess.run(["git", "config", "user.name", USER_NAME])
subprocess.run(["git", "config", "user.email", USER_EMAIL])

# Step 2: Generate commits
start_date = datetime.now() - timedelta(days=DAYS_BACK)

for day in range(DAYS_BACK):
    commit_date = start_date + timedelta(days=day)
    commits_today = random.randint(0, MAX_COMMITS_PER_DAY)

    for _ in range(commits_today):
        timestamp = commit_date.strftime("%Y-%m-%dT%H:%M:%S")
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = timestamp
        env["GIT_COMMITTER_DATE"] = timestamp

        with open("activity.txt", "a") as f:
            f.write(f"Commit on {timestamp}\n")

        subprocess.run(["git", "add", "activity.txt"])
        subprocess.run(["git", "commit", "-m", f"Commit on {timestamp}"], env=env)

# Step 3: Push to GitHub
subprocess.run(["git", "push", "origin", "main"])
