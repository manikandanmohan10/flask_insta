import os
from flask_mail import Message
from src.celery_woker import celery
from src.mail import mail
# from flask import current_app

@celery.task(name='src.tasks.send_celery_email')
def send_celery_email(message_data=None):
    # app = current_app._get_current_object()
    # message = Message(subject=message_data['subject'],
    #                 recipients=[message_data['recipients']],
    #                 body=message_data['body'],
    #                 sender=app.config['MAIL_DEFAULT_SENDER'])

    message = Message(
        subject='Hello',
        sender=os.getenv('MAIL_USERNAME'),
        recipients=message_data.get('recipients'),
        body=message_data.get('body')
    )
    
    mail.send(message)