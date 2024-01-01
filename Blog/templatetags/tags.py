from django import template
import os
from urllib.parse import unquote

register = template.Library()

# 為每個頁面設定不同背景大小
@register.simple_tag(takes_context=True)
def tags(context):
    # 檢查views中是否有 'small_background' 這個變量
    if 'small_background' in context:
        # 如果有，並且其值為 True，則返回 'small'
        if context['small_background'] == True:
            return 'small'
        # 否則返回 'default'
        else:
            return 'default'
    else:
        # 如果Views沒有引入 'small_background' 變量 --> **context，也返回 'default'
        return 'default'

@register.filter
def filename(value):
    decoded_url = unquote(value)
    return os.path.basename(decoded_url)