import sys
from eirb_com_helper.converter import toMarkdownV2

if __name__ == "__main__":
    markdown_text = sys.stdin.read()
    sys.stdout.write(toMarkdownV2(markdown_text))
