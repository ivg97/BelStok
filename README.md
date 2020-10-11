# BelStok
# Internet shop

#### Install project:

##### Loading project:
> git clone https://github.com/ivg97/BelStok

##### Install all library:
> pip3 install -r requirements.txt

##### Run:
> python3 manage.py runserver

#### Project connection ty celery
For celery==4.1.0 install kombu==4.1.0 and billiard==3.5.0.2, alse kombu>=4.2.0 rename 'async' in 'asynchronous'

### Run selery:
> celery -A belStock_shop worker -l info

####  Run monitoring from  on help celery
> celery -A belStock_shop flower

In  browser : http://localhost:5555/dashboard/
