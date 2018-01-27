from django.contrib import admin
from .models import Campaign, Organization, Donation, User

admin.site.register(Campaign)
admin.site.register(Organization)
admin.site.register(Donation)
admin.site.register(User)
