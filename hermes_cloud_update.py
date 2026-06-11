from datetime import datetime

now = datetime.now()
update_time = now.strftime("%Y-%m-%d %H:%M:%S")

# 模拟生成不同内容，不调用API
html_content = f"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PPnix加速</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: sans-serif;
            background-color: #0b0b0b;
            color: #f5f5f5;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }}
        h1 {{ color: #60d378; margin-bottom: 2rem; }}
        .time-info {{ color: #888; margin-top: 1rem; }}
    </style>
</head>
<body>
    <h1>PPnix加速 · 测试页面</h1>
    <p>当前更新时间：{update_time}</p>
</body>
</html>
"""

with open("PPnix加速.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("✅ 模拟更新完成")
