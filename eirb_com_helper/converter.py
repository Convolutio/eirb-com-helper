from telegramify_markdown import customize, markdownify as telegramify
import re


customize.strict_markdown = True  # If you want to use __underline__ as underline, set it to False, or it will be converted to bold.
customize.cite_expandable = True  # If you want to enable expandable citation, set it to True.

def markdownToMarkdownV2(standardMarkdown):
    """
    Take a string in true markdown (openmark) and convert it into markdown v2
    that Telegram support
    """
    return telegramify(standardMarkdown, max_line_length=None, normalize_whitespace=False)


def htmlToSulgukHtml(htmlContent):
    toSulgukSpoilers = lambda s: s.replace("<span class=\"spoiler\">", "<span class=\"tg-spoiler\">")
    return toSulgukSpoilers(htmlContent)

def htmlToMarkdown(htmlContent):
    return lib_htmlToMarkdown(htmlContent, heading_style="ATX")
