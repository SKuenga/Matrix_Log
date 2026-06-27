from django.shortcuts import render, redirect
from .models import SessionLog, Student
def active_and_earning(request):
    if request.method == "GET":
        earning_data = SessionLog.objects.values_list("duration", "hourly_rate", "status")
        total_expected_earning = sum(i[0]*i[1] for i in earning_data if i[2] == "ON_GOING")
    context = {
        "total_expected_earning": total_expected_earning
    }
    return render(request, "index.html", context)


