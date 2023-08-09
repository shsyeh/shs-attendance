# admin.py

from django.contrib import admin
from .models import SchedulePeriod
from .custom_admin import CustomAdminSite

class SchedulePeriodAdmin(admin.ModelAdmin):
    list_display = ('day_of_week', 'period_number', 'start_time', 'end_time')
    list_filter = ('day_of_week',)
    search_fields = ('day_of_week', 'period_number')
    ordering = ('day_of_week', 'period_number')

    def update_week_schedule_action(self, request, queryset):
        if 'start_time' in request.POST and 'end_time' in request.POST:
            new_start_time = request.POST['start_time']
            new_end_time = request.POST['end_time']
            for period in queryset:
                period.update_week_schedule(new_start_time, new_end_time)
            self.message_user(request, 'Week schedule updated successfully.')
        else:
            self.message_user(request, 'Please enter valid start and end times.', level='ERROR')

    update_week_schedule_action.short_description = 'Update Week Schedule'

# Register the custom admin site and the SchedulePeriod model
custom_admin_site = CustomAdminSite(name='custom_admin')
custom_admin_site.register(SchedulePeriod, SchedulePeriodAdmin)
