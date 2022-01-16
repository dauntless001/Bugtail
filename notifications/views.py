from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic.base import View
from notifications.models import Notification

# Create your views here.

class MarkNotifications(View):
    def get(self, request, *args, **kwargs):
        notifications = Notification.objects.filter(author=self.request.user, read=False).update(read=True)
        ajaxData = {}
        ajaxData['message'] = 'All Notifications marked as read'
        ajaxData['messageType'] = 'success'
        return JsonResponse(ajaxData, safe=False)