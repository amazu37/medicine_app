from django.contrib import admin
from django.urls import path,include
import medicine.views as medicine

urlpatterns = [
    path('admin/', admin.site.urls),
    path('medicine/', include('medicine.urls')),
]
