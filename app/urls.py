from django.urls import path
from .views import ActivityListView, ActivityCreateView, RandomActivityView, ActivityDeleteView

urlpatterns = [
    path('', ActivityListView.as_view(), name='activity_list'),
    path('create/', ActivityCreateView.as_view(), name='activity_create'),
    path('random/', RandomActivityView.as_view(), name='random_activity'),
    path('delete/<int:pk>/', ActivityDeleteView.as_view(), name='activity_delete'),
]