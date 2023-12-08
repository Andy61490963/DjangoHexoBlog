from django.urls import path
from . import views

urlpatterns = [
    #path 自定義網址
    #分別對應網址後綴、views函數、html內容的連結
    path('', views.home, name="home"), #主頁面
]