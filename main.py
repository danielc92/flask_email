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
max_age_seconds = 300
#print(app.config)


@app.route('/', methods=['GET', 'POST'])
def home():
    """Create Token Route."""
    if request.method == 'GET':
        return '<h1>Enter Email: </h1><form action="/" method = "POST"><input name = "email"><br><input style = "padding:8px; margin-top:5px" type = "submit"></form>'

    email = request.form['email']
    token = serializer.dumps(email, salt=salt)

    link = url_for('confirm_email',token=token, external=True)

    full_link = 'http://localhost:5000' + link

    message = Message('Confirm your email.',sender=sender,recipients=[email])

    message.html = '<h1>Welcome to flask-email app.</h1><code>this token will expire in 5 miutes</code><p>Click the following <a href={}>link</a> to activate your account. Thank you for joining us.</p>'.format(full_link)

    mail.send(message)

    return '<h1>Success!</h1><p>The email is <strong>{}</strong>. The token is <strong>{}</strong>.<p>'.format(request.form['email'], token)


@app.route('/confirm_email/<token>')
def confirm_email(token):
    """Confirm Token Route."""
    try:
        email = serializer.loads(token, salt=salt, max_age=max_age_seconds)
        return '<h1>The token is valid.</h1>'

    except SignatureExpired:
        return '<h1>The token has expired.</h1>'


if '__main__'==__name__:
    app.run(debug=True)
