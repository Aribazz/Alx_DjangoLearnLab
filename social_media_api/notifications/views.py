from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework.decorators import api_view


class NotificationListView(generics.ListAPIView):
    """Retrieve notifications for the authenticated user."""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user)


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
def mark_notification_as_read(request, notification_id):
    """Marks a notification as read."""
    notification = get_object_or_404(Notification, id=notification_id, recipient=request.user)
    notification.is_read = True
    notification.save()
    return Response({"message": "Notification marked as read"}, status=status.HTTP_200_OK)