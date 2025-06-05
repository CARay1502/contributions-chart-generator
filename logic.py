# this is the logic.py file that runs the logic with GUI.py
# The exact same process as 'contribute.py' but instead passes the info to the GUI 
# 'Contribute.py' is easier to read with comments if you want to understand logic

import os
import subprocess
from datetime import datetime, timedelta
import random

def run_commit_script(repo_url, local_repo, username, email, days_back, max_commits, branch, status_callback):
    try:
        # Step 1: Clone repo if not exists
        if not os.path.exists(local_repo):
            status_callback(f"Cloning into {local_repo}...")
            subprocess.run(["git", "clone", "-b", branch, repo_url, local_repo], check=True)
        else:
            status_callback(f"Using existing repo: {local_repo}")

        os.chdir(local_repo)

        subprocess.run(["git", "config", "user.name", username], check=True)
        subprocess.run(["git", "config", "user.email", email], check=True)

        start_date = datetime.now() - timedelta(days=int(days_back))
        status_callback(f"Generating commits over last {days_back} days...")

        for day in range(int(days_back)):
            commit_date = start_date + timedelta(days=day)
            commits_today = random.randint(0, int(max_commits))

            for _ in range(commits_today):
                timestamp = commit_date.strftime("%Y-%m-%dT%H:%M:%S")
                env = os.environ.copy()
                env["GIT_AUTHOR_DATE"] = timestamp
                env["GIT_COMMITTER_DATE"] = timestamp

                with open("activity.txt", "a") as f:
                    f.write(f"Commit on {timestamp}\n")

                subprocess.run(["git", "add", "activity.txt"], check=True)
                subprocess.run(["git", "commit", "-m", f"Commit on {timestamp}"], env=env, check=True)

        status_callback("Pushing commits...")
        subprocess.run(["git", "push", "origin", branch], check=True)
        status_callback("🎉 Push complete!")

    except subprocess.CalledProcessError as e:
        status_callback(f"[ERROR] Git command failed: {e}")
    except Exception as e:
        status_callback(f"[ERROR] Unexpected: {e}")
