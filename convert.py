import sys

from dotenv_vault import load_dotenv
load_dotenv()

from eirb_com_helper.converter import markdownToMarkdownV2

if __name__ == "__main__":
    markdown_text = sys.stdin.read()
    sys.stdout.write(markdownToMarkdownV2(markdown_text))
