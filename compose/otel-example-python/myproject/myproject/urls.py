from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]


# シンプルなビュー関数を定義
def hello_world(request):
    return HttpResponse("Hello, World!")


# URLルーティング
urlpatterns = [
    path("", hello_world),  # ルートURLにアクセスすると "Hello, World!" を表示
]
