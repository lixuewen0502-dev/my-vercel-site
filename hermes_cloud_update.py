import os
import requests
from datetime import datetime

HERMES_API_KEY = os.getenv("HERMES_API_KEY")
if not HERMES_API_KEY:
    raise ValueError("❌ HERMES_API_KEY 未配置，请检查 GitHub Secrets")

def hermes_generate(prompt):
    url = "https://api.hermes-agent.ac.cn/v1/generate"
    headers = {
        "Authorization": f"Bearer {HERMES_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "hermes-4",
        "prompt": prompt,
        "max_tokens": 150
    }
    res = requests.post(url, headers=headers, json=data)
    res.raise_for_status()
    return res.json().get("text", "今天也要加油！")

today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
ai_text = hermes_generate("写一句适合PPnix加速网站首页的每日更新文案，简短、正能量")

new_html = f"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PPnix加速</title>
</head>
<body>
    <h1>PPnix加速 · 每日自动更新</h1>
    <p>更新时间：{today}</p>
    <p>AI文案：{ai_text}</p>
</body>
</html>
"""

with open("PPnix加速.html", "w", encoding="utf-8") as f:
    f.write(new_html)

print("✅ Hermes 已更新 PPnix加速.html")
