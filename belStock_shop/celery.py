import os
from celery import Celery

# Set the enviroment variable, witch contain name settins file
# your project
#
#
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'belStock_shop.settings')
#  create an application copy(instance)
app = Celery('belStock_shop')
# Download configurations witch settings your project, call method config_form_object
app.config_from_object('django.conf:settings', namespace='CELERY')
# Search and download asynchronous tasks in your project
app.autodiscover_tasks()

