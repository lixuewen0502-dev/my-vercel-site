import os
import requests
from datetime import datetime

def call_hermes(prompt):
    api_key = os.getenv("HERMES_API_KEY")
    if not api_key:
        raise Exception("未读取到 HERMES_API_KEY，请检查 GitHub Secrets 配置")

    url = "https://api.hermes-agent.ac.cn/v1/generate"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "赫尔墨斯-2",
        "prompt": prompt,
        "max_tokens": 1200,
        "temperature": 0.95
    }

    res = requests.post(url, headers=headers, json=payload)
    res.raise_for_status()
    return res.json()["choices"][0]["text"].strip()

# 获取当前时间信息
now = datetime.now()
update_time = now.strftime("%Y-%m-%d %H:%M:%S")
timestamp = now.timestamp()  # 关键：生成唯一时间戳，强制AI每次生成不同内容

# 给AI的指令：不限定具体功能，让它自由发挥创作全新页面
task_prompt = f"""
当前时间戳：{timestamp}
请编写一份完整独立的 HTML 页面，要求：
1. 页面标题固定为：PPnix加速
2. 内嵌 CSS，无需外部资源，浏览器可直接打开运行
3. 本次必须制作和历史版本功能、交互、视觉效果完全不同的页面
4. 可自由实现各类前端功能：动画、按钮交互、特效、时钟、表单、布局切换、色彩主题等
5. 页面底部固定一行文字：本次更新时间 {update_time}
6. 只输出完整 HTML 代码，不要解释、不要备注、不要 markdown

发挥创意，制作全新功能页面。
"""

# 调用 Hermes 生成页面代码
full_html = call_hermes(task_prompt)

# 写入并覆盖 PPnix加速.html 文件
with open("PPnix加速.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("✅ 带时间戳的全新功能页面已由 Hermes 生成并更新完成")
