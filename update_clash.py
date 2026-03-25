import os
import glob
import re

workspace = r"c:\Users\User\Documents\project\clash2"

# 1. Update AI.list and create ChatGPT.list
ai_list_path = os.path.join(workspace, "list", "AI.list")
chatgpt_list_path = os.path.join(workspace, "list", "ChatGPT.list")

with open(ai_list_path, 'r', encoding='utf-8') as f:
    ai_lines = f.readlines()

new_ai_lines = []
chatgpt_lines = [
    "# 内容：ChatGPT / OpenAI 专属规则\n",
    "# 域名关键字匹配\n",
    "DOMAIN-KEYWORD,openai\n\n",
    "# OpenAI / ChatGPT\n"
]

in_chatgpt_block = False
for line in ai_lines:
    if "DOMAIN-KEYWORD,openai" in line:
        continue # Moved
    if line.startswith("# OpenAI / ChatGPT"):
        in_chatgpt_block = True
    elif in_chatgpt_block and line.startswith("# "):
        in_chatgpt_block = False
        
    if in_chatgpt_block and line.strip() != "# OpenAI / ChatGPT":
        if line.strip():
            chatgpt_lines.append(line)
    elif not in_chatgpt_block:
        new_ai_lines.append(line)

with open(ai_list_path, 'w', encoding='utf-8') as f:
    f.writelines(new_ai_lines)

with open(chatgpt_list_path, 'w', encoding='utf-8') as f:
    f.writelines(chatgpt_lines)

print("Created ChatGPT.list and updated AI.list")

# 2. Update all .ini files
ini_files = glob.glob(os.path.join(workspace, "*.ini"))

for ini_file in ini_files:
    with open(ini_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add ruleset
    ruleset_ai = r"ruleset=🤖 AI,https://gh-proxy.com/raw.githubusercontent.com/missgogo/clash2/refs/heads/main/list/AI.list"
    ruleset_chatgpt = "ruleset=🤖 ChatGPT,https://gh-proxy.com/raw.githubusercontent.com/missgogo/clash2/refs/heads/main/list/ChatGPT.list\n"
    if "ruleset=🤖 ChatGPT" not in content and ruleset_ai in content:
        content = content.replace(ruleset_ai, ruleset_chatgpt + ruleset_ai)

    # Add ChatGPT proxy groups
    # Look for custom_proxy_group=🤖 AI
    group_ai = r"custom_proxy_group=🤖 AI`select`"
    
    group_chatgpt = """custom_proxy_group=🤖 ChatGPT`select`[]ChatGPT-自动`[]美国-自动`[]BESTVPN-US-自动`[]牛逼-美国-自动`[]所有-手动`[]REJECT
custom_proxy_group=ChatGPT-自动`url-test`(美国|US|us|美|BESTVPN.*美国|BESTVPN.*US|牛逼.*美国|牛逼.*US)`https://chat.openai.com/favicon.ico`180,5,100
"""
    if "custom_proxy_group=🤖 ChatGPT" not in content:
        # We need to insert it right before custom_proxy_group=🤖 AI
        # Let's find the AI line
        lines = content.splitlines()
        new_lines = []
        for i, line in enumerate(lines):
            if line.startswith("custom_proxy_group=🤖 AI`select"):
                # Insert comment and chatgpt groups
                new_lines.append("; ChatGPT - 独立专属节点与测速")
                new_lines.extend(group_chatgpt.splitlines())
            new_lines.append(line)
        content = "\n".join(new_lines) + "\n"

    # Add 牛逼-美国-自动
    # Look for custom_proxy_group=美国-自动
    group_usa = r"custom_proxy_group=美国-自动`url-test`("
    group_niubi = "custom_proxy_group=牛逼-美国-自动`url-test`(牛逼.*美国|牛逼.*US|牛逼.*us|牛逼.*美)`https://generativelanguage.googleapis.com/generate_204`180,5,100"
    
    if "custom_proxy_group=牛逼-美国-自动" not in content:
        lines = content.splitlines()
        new_lines = []
        for line in lines:
            new_lines.append(line)
            if line.startswith("custom_proxy_group=美国-自动`"):
                new_lines.append(group_niubi)
        content = "\n".join(new_lines) + "\n"
        
    with open(ini_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated {os.path.basename(ini_file)}")

print("Done updates.")
