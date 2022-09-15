from django.contrib import admin
from .models import LoginForm, VerifyDocument, feedback 
from django.contrib.auth.models import User, Group

# Register your models here.

admin.site.register(LoginForm)
admin.site.register(VerifyDocument)
admin.site.register(feedback)
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.site_title = "Document Verification"
admin.site.site_header = "Document Verification Administration"
admin.site.index_title = "Admin Panel"