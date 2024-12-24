from django.contrib import admin
from .models import City, State, ServiceCategory, Worker, ServiceRequest, Response, Feedback, UserProfile

# Register models to the admin panel
admin.site.register(City)
admin.site.register(State)
admin.site.register(ServiceCategory)
admin.site.register(Worker)
admin.site.register(ServiceRequest)
admin.site.register(Response)
admin.site.register(Feedback)
admin.site.register(UserProfile)
