from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config.update(dict(
	DEBUG = True,

	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_TLS = False,
	MAIL_USE_SSL= True,
	MAIL_USERNAME = 'gautamamber5@gmail.com',
	MAIL_PASSWORD = 'ambergautam1998'))

mail = Mail(app)


@app.route("/")
def index():

    msg = Message("Hello",
                  sender="gautamamber5@gmail.com",
                  recipients=["ambergautam1@gmail.com"])
    msg.body = "testing"
    mail.send(msg)
    return "Sent"

if __name__ == '__main__':
	 app.run(debug=True)