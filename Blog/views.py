from django.shortcuts import render, get_object_or_404
from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.utils.html import format_html
from django.core.paginator import Paginator

#Import Database
from .models import homepost
from .models import archives
from .models import content

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
    context = {'small_background': True}
    return render(request,
                  'Navigation/Archives.html',{
                      "post": post,
                      **context,
                  })


def About(request):
    #為每個block設定不同背景大小
    context = {'small_background': True}
    return render(request, 'Navigation/About.html',context)


def Content(request ,id):
    #Content要顯示的話，必須抓取model中，archives下的content的內容id=id的部分是每篇文章的連結
    article = get_object_or_404(archives, id=id)
    context = {'small_background': True}

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