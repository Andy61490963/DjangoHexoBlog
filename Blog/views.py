from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.utils.html import format_html
from django.core.paginator import Paginator

#Import Database
from .models import homepost

def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    post = homepost.objects.all()  # .order_by('-name')
    name = "Sentimental1"

    #以ownerid分類、設定分幾頁
    p = homepost.objects.all().order_by('ownerid')
    paginator = Paginator(p, 1)

    #使用者從請求中獲取的頁面參數（通常從 GET 請求中獲取）來獲取特定的頁面，page會傳給home.html作為切分資料{% for post in page %}
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    #頁數賦予到字串
    #pages = "a" * page.paginator.num_pages

    # time
    now = datetime.now()
    time = now.strftime("%Y-%m-%d, %H:%M")
    return render(request,
                  'home.html', {
                      "post": post,
                      "name": name,
                      "year": year,
                      "month": month,
                      "time": time,
                      "page": page,
                      #"pages": pages,
                  })