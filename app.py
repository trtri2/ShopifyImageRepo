from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://leon.trieu:password@localhost/flasksql'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'

db = SQLAlchemy(app)

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    imgPath = db.Column(db.String(160), nullable=False)
    description = db.Column(db.String(160))
    inCarousel = db.Column(db.Boolean)

    def __init__(self, imgPath, description):
        self.imgPath = imgPath
        self.description = description
        self.inCarousel = False


@app.route('/')
def home():
    queryResult = Image.query.all()   

    return render_template("index.html", images=queryResult)

@app.route('/upload')
def upload():
    return render_template("upload.html")

@app.route('/addImage', methods=['POST'])
def addImage():
    imgPath = request.form["imgPath"]
    description = request.form["description"]
    entry = Image(imgPath,description)

    try:
        db.session.add(entry)
        db.session.commit()
    except Exception as err:
        return render_template("response.html", message="A problem occured: " + str(err))

    return render_template("upload.html", message="Successfully added image to repository.")

@app.route('/delete/<image_id>')
def deleteImage(image_id, methods=['DELETE']):
    queryResult = Image.query.get(image_id)
    if not queryResult:
        return render_template("response.html", message="Image no longer exists.")
    
    try:
        db.session.delete(queryResult)
        db.session.commit()
    except Exception as err:
        return render_template("response.html", message="A problem occured: " + str(err))

    return redirect('/')


######## CAROUSEL ENDPOINTS ########

@app.route('/carousel')
def carousel():
    queryResult = Image.query.filter_by(inCarousel=True).all()
    return render_template("carousel.html", images=queryResult)

@app.route('/carousel/add/<image_id>')
def addToCarousel(image_id):
    queryResult = Image.query.get(image_id)
    queryResult.inCarousel = True

    try:
        db.session.commit()
    except Exception as err:
        return render_template("response.html", message=("exception occured: " + str(err)))

    return redirect('/')

@app.route('/carousel/delete/<image_id>')
def deleteFromCarousel(image_id):
    queryResult = Image.query.get(image_id)
    queryResult.inCarousel = False

    try:
        db.session.commit()
    except Exception as err:
        return render_template("response.html", message="A problem occured: " + str(err))

    return redirect('/')

@app.route('/carousel/reset/')
def resetCarousel():
    queryResult = Image.query.filter_by(inCarousel=True).all()

    for res in queryResult:
        res.inCarousel = False

    try:
        db.session.commit()
    except Exception as err:
        return render_template("response.html", message="A problem occured: " + str(err))

    return redirect('/')

######## END OF CAROUSEL ENDPOINTS ########



if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

