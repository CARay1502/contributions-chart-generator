# 📈 GitHub Contribution Graph Filler

![Github Contributions Screenshot](https://github.com/CARay1502/contributions-chart-generator/blob/main/Screenshot%202025-05-26%20111042.png)

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
GITHUB_REPO = "https://github.com/YOUR_USERNAME/github-activity.git"  # change this to repo url
LOCAL_REPO = "temp-repo" #leave or change to any name you want
USER_NAME = "YOUR_USERNAME"  # change this 
USER_EMAIL = "your.email@example.com"  # change this
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

### Troubleshooting

If you get an error first make sure that your github username and email are configured correctly on your local machine: 

Use git config command to configure email and name. 
```bash
git config --global user.name "Your name"
git config --global user.email "your.email@example.com" #replace with github profile email
```

If this does not work, consult ChatGPT like I did. Good luck! 
