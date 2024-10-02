from telegramify_markdown import customize, markdownify as telegramify

import sys

customize.strict_markdown = True  # If you want to use __underline__ as underline, set it to False, or it will be converted to bold.
customize.cite_expandable = True  # If you want to enable expandable citation, set it to True.

def toMarkdownV2(standardMarkdown):
    """
    Take a string in true markdown (openmark) and convert it into markdown v2
    that Telegram support
    """
    return telegramify(standardMarkdown, max_line_length=None, normalize_whitespace=False)

if __name__ == "__main__":
    markdown_text = sys.stdin.read()
    sys.stdout.write(toMarkdownV2(markdown_text))

