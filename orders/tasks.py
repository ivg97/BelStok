from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def order_created(order_id):
    '''Task post email-notification if order registration successfully'''

    order = Order.objects.get(id=order_id)
    subject = 'Order nr.{}'.format(order.id)
    messages = 'Dear {}, \n\nYou have successfully placed an order.' \
               'Your order id is {}.'.format(order.first_name, order.id)
    mail_sent = send_mail(subject,
                          messages,
                          'admin@belStock_shop.com',
                          [order.email])
    return mail_sent