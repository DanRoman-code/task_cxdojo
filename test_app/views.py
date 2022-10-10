from datetime import datetime
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from test_app.validation_data import working_with_files


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
                password=user_data["password"],
                date_joined=datetime.fromtimestamp(int(user_data["date_joined"])),
                avatar=user_data["avatar"],
            )

    context = {
        "users": user.objects.all(),
    }
    return render(request, "index.html", context=context)
