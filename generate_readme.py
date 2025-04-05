import requests
from datetime import datetime

def fetch_quote():
    try:
        res = requests.get("https://your-fastapi-url.com/quote")
        if res.status_code == 200:
            return res.json().get("quote", "Keep coding like a beast.")
    except:
        return "Keep coding like a beast."
    
quote = fetch_quote()

template = f"""\
# 🔥 Aadishesh aka toxicskulll

_Last updated: **{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC**_

> 💬 Quote of the day: _"{quote}"_

<!-- Your whole README content here -->
...
"""

with open("README.md", "w") as f:
    f.write(template)
