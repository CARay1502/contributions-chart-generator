# 📈 GitHub Contribution Faker

Ever wanted to light up your GitHub contributions graph? This simple Python tool helps you do exactly that — by generating backdated commits and pushing them to a public repository.

> 💡 Great for testing, demonstrations, or simply boosting your green square game.

---

## 🚀 Features

- 🔁 Generates up to N commits per day
- 📅 Fills up to 365 days of history
- ⌛ Commits are **backdated** using `GIT_AUTHOR_DATE` and `GIT_COMMITTER_DATE`
- 🛠️ Fully customizable
- ✅ Uses plain Python and Git — **no external libraries**

---

## 📦 How It Works

1. Clones your GitHub repository
2. Simulates random activity by creating a file and committing to it
3. Backs up each commit with a fake historical date
4. Pushes it all to GitHub — your graph updates within minutes

---

## 🛠️ Setup

### 1. Create a Public Repository

Go to [github.com/new](https://github.com/new) and create a **public** repo (e.g. `github-activity`).  
Do not initialize it with a README.

---

### 2. Configure the Script

Clone this repo or copy `contribute.py` into your working directory.  
Then edit the top of the script to match your info:

```python
GITHUB_REPO = "https://github.com/YOUR_USERNAME/github-activity.git"
USER_NAME = "YOUR_USERNAME"
USER_EMAIL = "your.email@example.com"
```

### 3. Run it 

Open a terminal and run:

```python
python contribute.py
```

✅ If everything is configured correctly:

A new folder (temp-repo) will be created

Commits will be made with backdated timestamps

All commits will be pushed to GitHub

🕒 Wait a few minutes, then check your GitHub profile to see the new green squares on your contributions chart!
