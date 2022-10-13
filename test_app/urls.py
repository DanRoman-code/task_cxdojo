from django.urls import path

from test_app.views import index, upload_files

urlpatterns = [
    path("", index, name="index"),
    path("upload-files/", upload_files, name="upload"),
]

app_name = "includes"
