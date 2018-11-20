"""Imports."""
import os
from flask import Flask, request, url_for
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired

# Initialize web app, mail and serializer, load config. 
app = Flask(__name__)
app.config.from_pyfile('config.cfg')
sender = app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME','Error')
app.config['MAIL_PASSWORD']=os.getenv('MAIL_PASSWORD','Error')
mail = Mail(app)
serializer = URLSafeTimedSerializer('this should be a secret')
salt = 'spaghetti'
max_age_seconds = 30
#print(app.config)


@app.route('/', methods=['GET', 'POST'])
def home():
    """Create Token Route."""
    if request.method == 'GET':
        return '<form action="/" method = "POST"><input name = "email"><input type = "submit"></form>'

    email = request.form['email']
    token = serializer.dumps(email, salt=salt)

    link = url_for('confirm_email',token=token, external=True)

    full_link = 'http://localhost:5000' + link

    message = Message('Confirm your email.',sender=sender,recipients=[email])

    message.body = 'Click the following link to activate your account. {}'.format(full_link)

    mail.send(message)

    return 'The email entered is {}. The token is {}.'.format(request.form['email'], token)


@app.route('/confirm_email/<token>')
def confirm_email(token):
    """Confirm Token Route."""
    try:
        email = serializer.loads(token, salt=salt, max_age=max_age_seconds)
        return 'The token works'

    except SignatureExpired:
        return 'The token is expired'


if '__main__'==__name__:
    app.run(debug=True)
