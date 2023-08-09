# views.py

from django.http import JsonResponse
from .models import Student, Attendance
import datetime
from datetime import date, time


def scan_attendance(request):
    if request.method == 'POST':
        scanned_id = request.POST.get('student_id')
        if scanned_id:
            try:
                student = Student.objects.get(student_id=scanned_id)
                class_section = get_current_class_section()
                if class_section:
                    attendance_status = calculate_attendance_status(class_section)
                    record_attendance(student, class_section, attendance_status)
                    response_data = {
                        'student_name': f"{student.first_name} {student.last_name}",
                        'tardy_status': 'Tardy' if attendance_status else 'On Time',
                    }
                    return JsonResponse(response_data)
                else:
                    return JsonResponse({'error': 'No active class found at this time.'}, status=400)
            except Student.DoesNotExist:
                return JsonResponse({'error': 'Student not found.'}, status=400)
    return JsonResponse({'error': 'Invalid request.'}, status=400)

def get_current_class_section():
    # Implement the logic to get the current class section based on the time and day of the week.
    # Return the appropriate Class object or None if no active class is found at this time.
    current_time = time(hour=12, minute=30)  # Replace this with the actual current time.
    current_day_of_week = date.today().strftime('%a')  # Get the current day of the week (e.g., Mon, Tue, ...).
    # Your logic to find the active class based on the current_time and current_day_of_week.
    return None  # Replace this with the Class object representing the active class section.

def calculate_attendance_status(class_section):
    # Implement the logic to calculate the tardy status based on the current time and class start time.
    current_time = time(hour=12, minute=30)  # Replace this with the actual current time.
    class_start_time = class_section.schedule_period.start_time
    tardy_threshold = class_section.tardiness_threshold
    return (current_time > class_start_time + tardy_threshold)

def record_attendance(student, class_section, tardy_status):
    attendance_date = date.today()
    attendance = Attendance.objects.create(
        student=student,
        class_attended=class_section,
        date=attendance_date,
        status=True,  # Assuming the student is present upon scanning the ID card.
        tardy=tardy_status,
    )
    attendance.save()
