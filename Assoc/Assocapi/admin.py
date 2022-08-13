from django.contrib import admin
from .models import User, Association , Memberassociation , Organization

# Register your models here.
admin.site.register(User)
admin.site.register(Association)
admin.site.register(Memberassociation)
admin.site.register(Organization)