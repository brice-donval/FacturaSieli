from datetime import datetime

from django.shortcuts import get_object_or_404

from ..models import Notification, Company

@staticmethod
def send_notification(notification_type:str, service_title:str,company_sender_id:int, company_receiver_id:int):
    company_sender = get_object_or_404(Company, pk=company_sender_id)
    company_receiver = get_object_or_404(Company, pk=company_receiver_id)
   
    notification = Notification()
    notification.send_at = datetime.now()
    notification.type=notification_type
    notification.service_title = service_title
    notification.company_sender = company_sender
    notification.company_receiver = company_receiver
    notification.save()