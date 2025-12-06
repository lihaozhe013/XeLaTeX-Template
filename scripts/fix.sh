pandoc content.md -o content.tex && python fix-pandoc-format.py && mv content_fixed.tex content_fixed_no_format.tex 
pandoc -s content.md -o content.tex && python fix-pandoc-format.py && mv content_fixed.tex content_fixed_full.tex

MARGIN_CONTENT="\usepackage[margin=0.8in]{geometry}"
TARGET_FILE="content_fixed_full.tex"
TEMP_FILE=$(mktemp)
echo "$MARGIN_CONTENT" > "$TEMP_FILE"
sed -i "0r $TEMP_FILE" "$TARGET_FILE"
rm "$TEMP_FILE"

PAGE_CONTENT="\\documentclass[11pt,fleqn]{article}"
TARGET_FILE="content_fixed_full.tex"
TEMP_FILE=$(mktemp)
echo "$PAGE_CONTENT" > "$TEMP_FILE"
sed -i "0r $TEMP_FILE" "$TARGET_FILE"
rm "$TEMP_FILE"
