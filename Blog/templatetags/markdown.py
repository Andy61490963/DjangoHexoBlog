import markdown

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def convert_markdown(value):
    # 启用大量的 Markdown 扩展
    extensions = [
        "markdown.extensions.extra",
        "markdown.extensions.admonition",
        "markdown.extensions.codehilite",
        "markdown.extensions.legacy_attrs",
        "markdown.extensions.legacy_em",
        "markdown.extensions.meta",
        "markdown.extensions.nl2br",
        "markdown.extensions.sane_lists",
        "markdown.extensions.smarty",
        "markdown.extensions.toc",
        "markdown.extensions.wikilinks",
    ]

    # 转换 Markdown 到 HTML
    html = markdown.markdown(value, extensions=extensions)

    return html
