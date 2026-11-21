
from flask import Flask, request
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms import StringField, SubmitField
from werkzeug.serving import WSGIRequestHandler

WSGIRequestHandler.server_version = ''
WSGIRequestHandler.sys_version = ''

app = Flask(__name__)

@app.after_request
def security_headers(response):
    response.headers['Content-Security-Policy'] = (
        "default-src 'self'; "
        "script-src 'self'; "
        "style-src 'self'; "
        "img-src 'self' data:; "
        "font-src 'self'; "
        "connect-src 'self'; "
        "object-src 'none'; "
        "base-uri 'self'; "
        "form-action 'self'; "
        "frame-ancestors 'none'"
    )

    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-Content-Type-Options'] = 'nosniff'

    return response

app.config['SECRET_KEY'] = 'clave-desarrollo-local'

csrf = CSRFProtect()
csrf.init_app(app)

class unprotectedForm(FlaskForm):
    class Meta:
        csrf = True

    name = StringField('name')
    submit = SubmitField('submit')

@app.route('/hello')
def hello():
    name = request.args.get('name')
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5005, debug=True)