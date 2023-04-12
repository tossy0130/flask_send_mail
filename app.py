from flask import Flask, render_template, request, url_for, redirect
from flask_mail import Mail, Message
import os

app = Flask(__name__)


app.config['MAIL_SERVER'] = 'sv12724.xserver.jp'  # メールサーバー
app.config['MAIL_PORT'] = 587  # SSLを利用しない
app.config['MAIL_USERNAME'] = 'test_01@xs810378.xsrv.jp'
app.config['MAIL_PASSWORD'] = 'パスワード'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

# sender 設定　※ これがあるとsender設定が不要になる
app.config['MAIL_DEFAULT_SENDER'] = 'test_01@xs810378.xsrv.jp'

mail = Mail(app)

# ルーティング設定

to_mail = 'tokotoko33ok@gmail.com'
to_mail_02 = 'natsume@jimnet.co.jp'


@app.route('/')
def index():
    msg = Message('テストメール', recipients=[to_mail])
    msg.body = "Flask テストメール"
    mail.send(msg)
    return "Send OK（送信完了）"


if __name__ == '__main__':
    app.run(debug=True)
