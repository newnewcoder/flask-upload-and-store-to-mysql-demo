import base64

from flask import render_template, Flask, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import FileField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'the secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:abc123@localhost/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy()
db.init_app(app)


@app.teardown_request
def teardown_request(exception):
    if exception:
        db.session.rollback()
    db.session.remove()


class UploadDemo(db.Model):
    """
    upload demo model
    """
    __tablename__ = 'upload_demo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    file = db.Column(db.LargeBinary)


class UploadDemoForm(FlaskForm):
    file = FileField('upload', validators=[FileAllowed(['jpg', 'png', 'gif'], 'only allow jpg、png or gif')])


@app.route('/', methods=['GET', 'POST'])
def index():
    form = UploadDemoForm()
    upload_demo = UploadDemo.query.first()  # for demo. it's always delete insert.
    if form.validate_on_submit():
        if upload_demo:
            db.session.delete(upload_demo)
            db.session.commit()
        upload_demo = UploadDemo(
            file=request.files[form.file.name].read() if form.file.name else None
        )
        db.session.add(upload_demo)
        db.session.commit()
        return redirect(url_for('.index'))
    img_base64 = None
    if upload_demo and upload_demo.file:
        img_base64 = base64.b64encode(upload_demo.file).decode('UTF-8')

    return render_template('index.html', form=form, img_base64=img_base64)


if __name__ == '__main__':
    app.run()