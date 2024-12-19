from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

from orders.models import Order
from orders.service import send_notification_email
from robots.models import Robot


@receiver(post_save, sender=Robot)
def notify_customer_on_robot_creation(sender, instance: Robot, created: bool, **kwargs):
    """
    Signal to notify customers when a Robot matching their order is created.
    """
    if created:
        matching_orders = Order.objects.filter(robot_serial=instance.serial)

        for order in matching_orders:
            try:
                send_notification_email(
                    email=order.customer.email,
                    model=instance.model,
                    version=instance.version
                )
            except Exception as e:
                print(f"Error sending email for Order ID {order.id}: {str(e)}")
