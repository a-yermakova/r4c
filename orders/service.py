from django.core.mail import send_mail

from R4C import settings


def send_notification_email(email: str, model: str, version: str) -> None:
    """
    Sends an email notification to the customer about robot availability.

    Args:
        email (str): The email address of the customer.
        model (str): The model of the robot.
        version (str): The version of the robot.

    Returns:
        None
    """
    subject = "Ваш робот теперь в наличии"
    message = (
        f"Добрый день!\n\n"
        f"Недавно вы интересовались нашим роботом модели {model}, версии {version}.\n"
        f"Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами."
    )
    from_email = settings.EMAIL_HOST_USER
    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=[email],
        fail_silently=False,
    )
