from django.shortcuts import render, get_object_or_404
from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.utils.html import format_html
from django.core.paginator import Paginator
from django.db.models import Count

#Import Database
from .models import homepost
from .models import archives
from .models import content
from .models import Tag

# Gobel background control
context = {'small_background': True}

def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    post = homepost.objects.all()

    #以ownerid分類、設定分幾頁
    p = homepost.objects.all().order_by('ownerid')
    paginator = Paginator(p, 1)

    #使用者從請求中獲取的頁面參數（通常從 GET 請求中獲取）來獲取特定的頁面，page會傳給home.html作為切分資料{% for post in page %}
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    now = datetime.now()
    time = now.strftime("%Y-%m-%d, %H:%M")
    return render(request,
                  'home.html', {
                      "post": post,
                      "year": year,
                      "month": month,
                      "time": time,
                      "page": page,
                  })

def Archives(request):
    post = archives.objects.all()
    #為每個block設定不同背景大小
    return render(request,
                  'Navigation/Archives.html',{
                      "post": post,
                      **context,
                  })

#views可以用來分成不同連結，藉由id
def Content(request ,id):
    #Content要顯示的話，必須抓取model中，archives下的content的內容id=id的部分是每篇文章的連結
    article = get_object_or_404(archives, id=id)

    # 以ownerid分類、設定分幾頁
    p = content.objects.all().order_by('ownerid')
    paginator = Paginator(p, 1)

    # 使用者從請求中獲取的頁面參數（通常從 GET 請求中獲取）來獲取特定的頁面，page會傳給home.html作為切分資料{% for post in page %}
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    return render(request,
                  'Content/Content.html', {
                      "article": article,
                      "page": page,
                      **context,
                  })


def tag(request):
    tags = Tag.objects.annotate(num_articles=Count('content'))
    for tag in tags:
        # 确保字体大小在合理范围内
        tag.font_size = min(max(12 + tag.num_articles, 12), 30)  # 例如，字体大小限制在 12px 到 30px 之间
    return render(request,
                  'Navigation/Tag.html',  {
                      'tags': tags,
                      **context,
                  })


def taglist(request, tag_name):
    tag = Tag.objects.get(name=tag_name)
    content_articles = tag.content_set.all()
    archives_content = []
    for content_article in content_articles:
        if hasattr(content_article, 'archives'):
        #if content_article.archives:
            archives_content.append(content_article.archives)

    return render(request, 'Content/Taglist.html', {
        'articles': archives_content,
        'tag': tag,
        **context,
    })


def About(request):
    #為每個block設定不同背景大小
    return render(request, 'Navigation/About.html',context)