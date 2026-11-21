
from flask import Flask, request
from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms import StringField, SubmitField

app = Flask(__name__)
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
    app.run(debug=True)