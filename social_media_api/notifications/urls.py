from django.urls import path
from .views import NotificationListView, mark_notification_as_read

urlpatterns = [
    path('', NotificationListView.as_view(), name='notifications_list'),
    path('<int:notification_id>/read/', mark_notification_as_read, name='mark_notification_as_read'),

]
