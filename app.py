from flask import Flask, request

app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)

class unprotectedForm(FlaskForm):
    class Meta:
        csrf = True

    name = TextField('name')
    submit = SubmitField('submit')

@app.route('/hello')
def hello():
    name = request.args.get('name')
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run(debug=True)