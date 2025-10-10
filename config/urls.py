from django.contrib import admin
from django.urls import include, path  # добавляем include
from django.shortcuts import redirect

def root_redirect(request): return redirect('/accounts/login/')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", root_redirect),
    path("diary/", include("diary.urls", namespace="diary")),
    path("users/", include("users.urls", namespace="users")),
    path("accounts/", include("django.contrib.auth.urls")),
]
