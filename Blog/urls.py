from django.urls import path
from . import views

urlpatterns = [
    #path 自定義網址
    #分別對應網址後綴、views函數、html內容的連結
    path('', views.home, name="home"), #主頁面
    path('Navigation/Archives/', views.Archives, name="Archives"), #Navigation/Archives
    path('Navigation/Archives/Content/<int:id>/', views.Content, name="Content"), #Content/Content
    path('Navigation/About', views.About, name="About"), #Navigation/About
    path('Navigation/Tags/', views.tag, name='Tag'), #Navigation/Tags
    path('Navigation/Tags/<str:tag_name>/', views.taglist, name='Taglist'), #Content/Taglist
]