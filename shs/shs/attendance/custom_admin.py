# custom_admin.py

from django.contrib.admin import AdminSite

class CustomAdminSite(AdminSite):
    site_header = 'Custom Admin'
    site_title = 'Custom Admin'
    index_title = 'Welcome to the Custom Admin'
