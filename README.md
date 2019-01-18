# Flask Emailing
Sending emails using a flask web application. For this project I followed one of pretty printed's tutorials quite closely.

# Before you get started
- SMTP Servers
- Flask applications basics

# Setup
**How to obtain this repository:**
```sh
git clone https://github.com/danielc92/flask_email.git
```
**Modules/dependencies:**
- `flask_mail`
- `flask`
- `itsdangerous`

Install the following dependences:
```sh
pip install flask itsdangerous flask_mail
```

Running locally:
```sh
python3 main.py
```

# Tests
- Tested accessing `gmail`'s SMTP server successfully through `python`
- Tested sending mail via the SMTP server
- Tested authenticating links sent via the SMTP server (confirmation links)

# Contributors
- Daniel Corcoran

# Sources
- ['Pretty Printed's Website - For flask tutorials](https://prettyprinted.com/)