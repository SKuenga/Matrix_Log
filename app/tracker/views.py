from django.shortcuts import render, redirect
from .models import SessionLog, Student
from .forms import SessionLogForm
from django.db.models import Sum, F

def calculate_earnings(request):
    completed_session = SessionLog.objects.filter(status = "COMPLETED")
    total_earning = completed_session.annotate(earned = F('duration')*F('hourly_rate')).aggregate(total=Sum("earned"))['total'] or 0
    #annotate is used to add a temporary virtual field to each individual objects. For the above, we named the temporary column as earned
    #Then we use .aggregrate method that return a python dictionary with the aggregrate type(For now it results as "total": sum of the total).
    #Then to access the value of the key named "total", we use [total].
    #If no session exist with completed status, it throws 0 as the answer.
    students = Student.objects.all()
    if request.method == "POST":
        form = SessionLogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("calculate_earnings")
    else:
        form = SessionLogForm()
    context = {
        "students": students,
        "total_earning": total_earning,
        "form": form,
    }
    return render(request, "index.html", context)
