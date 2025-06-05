# This file is for CLI (terminal/command line) based commits. 
# Replace place holder info under Config section
# Refer to README for troubleshooting
# A temporary repo called "temp-repo" will be initialized when running the program in the same folder
# You can delete it or leave it, doesn't matter

import os
import subprocess
from datetime import datetime, timedelta
import random

# Configuration for git profile
GITHUB_REPO = "https://github.com/YOUR_USERNAME/github-activity.git"  # change this to repo URL 
LOCAL_REPO = "temp-repo" # ignore this (a temp repo for local machine)
USER_NAME = "YOUR_USERNAME"  # change this to github username
USER_EMAIL = "your.email@example.com"  # change this to github email
DAYS_BACK = 365 # configure how many days history from current to write commits to (max 365)
MAX_COMMITS_PER_DAY = 3 # configure this to the max desired commits per day (recommend no more than 15)

# ==== COMMIT LOGIC ====

# Step 1: Set up local repo
if not os.path.exists(LOCAL_REPO):
    subprocess.run(["git", "clone", GITHUB_REPO, LOCAL_REPO])

os.chdir(LOCAL_REPO)

# Gather user config settings
subprocess.run(["git", "config", "user.name", USER_NAME])
subprocess.run(["git", "config", "user.email", USER_EMAIL])

# Step 2: Generate commits
# Calculates starting day by going back DAYS_BACK from datetime.now()
start_date = datetime.now() - timedelta(days=DAYS_BACK)

# Array for day in DAYS_BACK 
for day in range(DAYS_BACK):
    # Calculare the date for commit_date logging, plus random amount of commits for that date 
    commit_date = start_date + timedelta(days=day)
    commits_today = random.randint(0, MAX_COMMITS_PER_DAY)

    # for number commits_today -> each commit: "Commit on {timestamp}"
    for _ in range(commits_today):
        timestamp = commit_date.strftime("%Y-%m-%dT%H:%M:%S")
        env = os.environ.copy()
        env["GIT_AUTHOR_DATE"] = timestamp
        env["GIT_COMMITTER_DATE"] = timestamp

        # Adds commit text to activity.txt file 
        with open("activity.txt", "a") as f:
            f.write(f"Commit on {timestamp}\n")

        # Runs command to git commit activity.txt with new commit history
        # Technically this is Step 3 (but whatever)
        subprocess.run(["git", "add", "activity.txt"])
        subprocess.run(["git", "commit", "-m", f"Commit on {timestamp}"], env=env)

# Step 3: Push to GitHub
subprocess.run(["git", "push", "origin", "main"])
