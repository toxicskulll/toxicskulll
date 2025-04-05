import requests

quote = requests.get("https://your-api-url/quote").json().get("quote", "Stay coding.")
with open("README.template.md", "r") as f:
    template = f.read()

with open("README.md", "w") as f:
    f.write(template.replace("{{QUOTE}}", quote))
