# Instagram Bot (Basic Selenium Script)

This is a basic Instagram automation bot written in Python using Selenium.

## ⚙️ Features

- Follow a user
- Like a post
- Comment on a post

## 🚀 How to Use

1. Install [Firefox GeckoDriver](https://github.com/mozilla/geckodriver/releases)
2. Make sure you have `selenium` installed:
   ```bash
   pip install selenium
   ```
3. Replace placeholders in the code:
   - `gecko driver path` → your geckodriver location
   - `username area xpath`, `password area xpath`, etc. → actual Instagram XPaths
   - `<Username>` and `<Password>` → your login credentials

4. Run the script:
   ```bash
   python instagram_bot.py
   ```

5. Select one of the options:
   - `1` → Follow a user
   - `2` → Like a post
   - `3` → Comment on a post

## ⚠️ Warning

This script is for **educational purposes only**.  
Use responsibly. Instagram may block your account if you use automation.
