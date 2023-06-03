from flask import Flask, render_template, request
from model import predictHappyOrSad

app = Flask(__name__)

@app.route('/', methods=['POST' , 'GET'])
def upload_file_and_predict():

    if request.method == 'POST':
        file = request.files['image']
        file.save('static/upload.jpg')

        prediction = predictHappyOrSad('static/upload.jpg')
        result = 'You Are Happy :)' if prediction == 'Happy' else 'You Are Sad :('

        return render_template('index.html', result=result,)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
