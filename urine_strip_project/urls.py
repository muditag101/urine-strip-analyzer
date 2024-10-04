from django.contrib import admin
from django.urls import path
from api.views import index, upload_image

urlpatterns = [
    path("admin/", admin.site.urls),
    path("upload/", upload_image, name="upload_image"),
    path("", index, name="index"),
]
