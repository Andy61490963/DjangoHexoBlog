from django import template

register = template.Library()

#為每個block設定不同背景大小
@register.simple_tag(takes_context=True)
def tags(context):
    #return 'small' if context.get('small_background', False) else 'big'
    # 檢查上下文中是否有 'small_background' 這個變量
    if 'small_background' in context:
        # 如果有，並且其值為 True，則返回 'small'
        if context['small_background'] == True:
            return 'small'
        # 否則返回 'big'
        else:
            return 'big'
    else:
        # 如果上下文中沒有 'small_background' 變量，也返回 'big'
        return 'big'