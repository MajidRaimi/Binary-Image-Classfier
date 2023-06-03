from flask import Flask, render_template, request
from model import predictHappyOrSad
import base64

app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_file_and_predict():
    if request.method == 'POST':
        file = request.files['image']
        file.save('static/upload.jpg')

        prediction = predictHappyOrSad('static/upload.jpg')

        result = 'You Are Happy :)' if prediction == 'Happy' else 'You Are Sad :('

        with open('static/upload.jpg', "rb") as image_file:
            encoded_string = base64.b64encode(
                image_file.read()).decode('utf-8')

        return render_template('index.html', result=result, image='data:image/png;base64,{}'.format(encoded_string))


if __name__ == '__main__':
    app.run(debug=True)
