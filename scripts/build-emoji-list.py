import emoji
import os

# 定义输出文件名
output_filename = "../src/latex_emoji_list.tex"

# 获取所有标准 emoji 字符
all_emojis = list(emoji.EMOJI_DATA.keys())

# 生成 LaTeX 宏定义列表
latex_lines = []
skipped_count = 0

for emo in all_emojis:
    # 过滤掉多字符序列（包含变体选择器、零宽连接符、国旗等）
    # newunicodechar 只能处理单个 Unicode 字符
    
    # 检查是否包含零宽连接符 (ZWJ)
    if '\u200D' in emo:
        skipped_count += 1
        continue
    
    # 检查是否包含变体选择器
    if '\uFE0F' in emo or '\uFE0E' in emo:
        skipped_count += 1
        continue
    
    # 检查字符长度（某些emoji由多个码点组成，如国旗）
    # 只保留单个码点的emoji
    if len(emo) > 1:
        # 进一步检查：某些单个"字符"实际上由多个码点组成
        # 例如国旗由两个区域指示符字母组成
        codepoints = [ord(c) for c in emo]
        # 如果有多个码点，跳过
        if len(codepoints) > 1:
            skipped_count += 1
            continue
    
    # 使用原始 emoji 字符作为参数
    line = f"\\newunicodechar{{{emo}}}{{\\emoji{{{emo}}}}}"
    latex_lines.append(line)

# 写入文件
try:
    with open(output_filename, "w", encoding="utf8") as f:
        f.write("\n".join(latex_lines))
    print(f"✅ 成功生成文件: **{output_filename}**")
    print(f"共包含 {len(latex_lines)} 个 emoji 宏定义。")
    print(f"跳过了 {skipped_count} 个复杂组合 emoji。")
except Exception as e:
    print(f"❌ 写入文件时发生错误: {e}")
