#thanks to blog.sahildiwan.com/posts/flask-and-postgresql-app-deployed-on-heroku/
from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/comparables'
db = SQLAlchemy(app)

#Create our database model
class ReducedLog(db.Model):
    __tablename__ = "reduced_logs"
    id = db.Column(db.Integer, primary_key=True)
    hash_id = db.Column(db.String(200), unique=True)

    def __init__(self, hash_id):
        self.hash_id = hash_id

    def __repr__(self):
        return '<hash_id %r>' % self.hash_id

# Set "homepage" to index.html
@app.route('/')
def index():
    return render_template('index.html')

# Save hash_id to database and send to success page
@app.route('/prereg', methods=['POST'])
def prereg():
    hash_id = None
    if request.method == 'POST':
        hash_id = request.form['hash_id']
        # Check that hash_id does not already exists
        if not db.session.query(ReducedLog).filter(ReducedLog.hash_id == hash_id).count():
            reg = ReducedLog(hash_id)
            db.session.add(reg)
            db.session.commit()
            return render_template('success.html')
        return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
