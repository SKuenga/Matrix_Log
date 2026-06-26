from django.db import models


class Student(models.Model):
    class Course(models.TextChoices):
        ENGLISH = "ENGLISH", "English"
        MATHEMATICS = "MATHEMATICS", "Mathematics"
        SCIENCE = "SCIENCE", "Science"
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    course = models.CharField(max_length = 50, choices = Course.choices)

class SessionLog(models.Model):
    class Status(models.TextChoices):
        COMPLETED = "COMPLETED", "Completed"
        ON_GOING = "ON_GOING", "On_going"
        CANCELLED = "CANCELLED", "Cancelled"
        PAUSED = "PAUSED", "Paused"
        UNKNOWN = "UNKNOWN", "Unknown"
    base_status = Status.UNKNOWN
    student = models.ForeignKey(Student, on_delete = models.CASCADE, related_name="student")
    date = models.DateTimeField()
    duration = models.DurationField()
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=6)
    status = models.CharField(max_length=55, choices= Status.choices, default = base_status)