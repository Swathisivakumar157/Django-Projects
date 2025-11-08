from django.urls import path
from . import views

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),

    path('mark/<int:pk>/',views.mark,name='mark'), #mark as done
    path('unmark/<int:pk>/',views.unmark,name='unmark'),#mark ans undone
    
    #Edit feature
    path('edit/<int:pk>/',views.edit,name='edit'),

    #delete feature
    path('dele/<int:pk>/', views.dele, name='dele'),
]