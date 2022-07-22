from django.urls import path
# from .views import HelloView
from  . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('morning', views.morning, name='morning'),
    path('noon', views.noon, name='noon'),
    path('night', views.night, name='night'),
    path('sleep', views.sleep, name='sleep'),
    path('other', views.other, name='other'),
    path('list', views.list, name='list'),
    path('edit/<int:num>', views.edit, name='edit'),
    path('takelist', views.takeconf, name='takelist'),
    path('notice', views.notice, name='notice'),
    path('test2', views.excuse, name='test2'),
]