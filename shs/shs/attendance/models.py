
from django.db import models
import datetime

class Student(models.Model):
    student_id = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Class(models.Model):
    class_name = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100)
    schedule_period = models.ForeignKey(SchedulePeriod, on_delete=models.CASCADE)


    def __str__(self):
        return self.class_name

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_attended = models.ForeignKey(Class, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.BooleanField(default=True)
    tardy = models.BooleanField(default=False)
    very_tardy = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student} - {self.class_attended} - {self.date} - {self.status}"

class SchedulePeriod(models.Model):
    DAY_CHOICES = [
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
    ]
    period_number = models.PositiveIntegerField()
    day_of_week = models.CharField(max_length=3, choices=DAY_CHOICES)
    duration = models.PositiveIntegerField(help_text="Duration of the period in minutes")
    passing_period = models.PositiveIntegerField(default=5, help_text="Duration of the passing period in minutes")

    def __str__(self):
        return f"{self.get_day_of_week_display()} - Period {self.period_number}"

class TardinessThreshold(models.Model):
    class_section = models.ForeignKey(Class, on_delete=models.CASCADE)
    tardy_threshold = models.PositiveIntegerField(default=5, help_text="Tardy threshold in minutes")
    very_tardy_threshold = models.PositiveIntegerField(default=15, help_text="Very tardy threshold in minutes")

    def __str__(self):
        return f"Tardiness Threshold for {self.class_section}"
