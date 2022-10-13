from datetime import datetime
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from test_app.forms import UploadFilesForm
from test_app.models import Document
from test_app.validation_data import working_with_files, update_files


@login_required
def index(request):
    user = get_user_model()
    users_data = working_with_files()
    for user_data in users_data:
        if not user.objects.filter(username=user_data["username"]):
            user.objects.create(
                username=user_data["username"],
                first_name=user_data["first_name"],
                last_name=user_data["last_name"],
                date_joined=datetime.fromtimestamp(int(user_data["date_joined"])),
                avatar=user_data["avatar"],
            )
            current_user = user.objects.get(username=user_data["username"])
            current_user.set_password(user_data["password"])
            current_user.save()

    context = {
        "users": user.objects.all(),
    }
    return render(request, "index.html", context=context)


def upload_files(request):
    if request.POST:
        form = UploadFilesForm(request.POST, request.FILES)
        scv_file = request.FILES["upload_csv_file"]
        xml_file = request.FILES["upload_xml_file"]

        if form.is_valid():
            if not scv_file.name.endswith(".csv"):
                messages.error(request, "File is not CSV type")
                return HttpResponseRedirect(reverse_lazy("includes:upload"))

            if not xml_file.name.endswith(".xml"):
                messages.error(request, "File is not XML type")
                return HttpResponseRedirect(reverse_lazy("includes:upload"))

            scv_file.name = "test_task.csv"
            xml_file.name = "test_task.xml"

            new_files = Document(csv_file=scv_file, xml_file=xml_file)

            update_files()

            new_files.save()

            return HttpResponseRedirect(reverse_lazy("includes:index"))
    else:
        form = UploadFilesForm()

    return render(request, "upload_files.html", context={"form": form})
