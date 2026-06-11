import os
from datetime import datetime

# 模拟Hermes生成，先跳过API调用
def hermes_generate(prompt):
    return "今天也要加油！"

today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
ai_text = hermes_generate("写一句适合PPnix加速网站首页的每日更新文案，简短、正能量")

new_html = f"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PPnix加速</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background: #0F0F0F;
            color: #fff;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
        }}
        h1 {{ font-size: 2.5rem; margin-bottom: 2rem; }}
        .quote {{ font-size: 1.5rem; color: #4CAF50; }}
        .time {{ margin-top: 1rem; color: #aaa; font-size: 0.9rem; }}
    </style>
</head>
<body>
    <h1>PPnix加速 · 每日自动更新</h1>
    <p class="quote">{ai_text}</p>
    <p class="time">更新时间：{today}</p>
</body>
</html>
"""

with open("PPnix加速.html", "w", encoding="utf-8") as f:
    f.write(new_html)

print("✅ 模拟更新完成，文件已写入！")
