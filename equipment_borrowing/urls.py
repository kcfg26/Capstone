from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('borrow_system.urls')),  # Include the borrow_system URLs
]
