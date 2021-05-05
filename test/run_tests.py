from app import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://leon.trieu:password@localhost/flasksql'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'

def test_createImageObject():
    testImgPath = "testPath"
    testImgDescription = "testDescription"
    image = Image(testImgPath, testImgDescription)
    assert(image.imgPath == testImgPath)
    assert(image.description == testImgDescription)

def test_addAndRemoveImage():
    addImage()
    removeImage()
    db.session.commit()

def test_validCarousel():
    queryResult = Image.query.filter_by(inCarousel=False).all()
    for result in queryResult:
        assert(result.inCarousel == False)

    queryResult = Image.query.filter_by(inCarousel=True).all()
    for result in queryResult:
        assert(result.inCarousel == True)

def addImage():
    testImgPath = "testPath"
    testImgDescription = "testDescription"
    image = Image(testImgPath, testImgDescription)

    db.session.add(image)

def removeImage():
    queryResult = Image.query.filter_by(imgPath="testPath").first()

    db.session.delete(queryResult)



    
