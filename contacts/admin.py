from django.contrib import admin
from .models import SendMailContacts, SendContacts


admin.site.register(SendMailContacts)
admin.site.register(SendContacts)
