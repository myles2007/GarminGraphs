import os

from Graphs import app
import flask
import werkzeug

@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if flask.request.method == 'POST':
        import pudb; pudb.set_trace()
        file_ = flask.request.files['file']
        if file_ and allowed_file(file_.filename):
            filename = werkzeug.secure_filename(file_.filename)
            file_.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return flask.make_response('<div> Success! </div>', 201)
    return '<div> ??? </div'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']
