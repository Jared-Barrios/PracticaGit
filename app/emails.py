
from flask_mail import Message
from flask import current_app, render_template
from threading import Thread
"""
def confirmacion_compra(mail, usuario, libro):
    try:
        message=Message('Confirmación de compra de libro', 
                        sender=current_app.config['MAIL_USERNAME'], 
                        recipients=['20213tn099@utez.edu.mx'])
        message.html = render_template(
            'emails/confirmacion_compra.html', 
            usuario=usuario, libro=libro)
        mail.send(message)
    except Exception as ex:
        raise Exception(ex)
"""
#Asincrono
def confirmacion_compra(app, mail, usuario, libro):
    try:
        message=Message('Confirmación de compra de libro', 
                        sender=current_app.config['MAIL_USERNAME'], 
                        recipients=['20213tn099@utez.edu.mx'])
        message.html = render_template('emails/confirmacion_compra.html', 
                                       usuario=usuario, libro=libro)
        thread = Thread(target=envio_mail_async, args=[app,mail,message])
        thread.start()
    except Exception as ex:
        raise Exception(ex)
    
def envio_mail_async(app,mail,message):
    with app.app_context():
        mail.send(message)
