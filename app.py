from flask import Flask, render_template, request
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

import numpy as np

app = Flask(__name__, static_folder='static')

# Define the model loading code
model = load_model('mushroom_model_v13.keras')


@app.route('/', methods=['GET'])
def home():
    return render_template("home.html")


@app.route('/check-mushroom', methods=['GET', 'POST'])
def check_mushroom():
    if request.method == 'POST':
        # Handle file upload
        imagefile = request.files['imagefile']
        image_path = "./static/images/" + imagefile.filename
        imagefile.save(image_path)

        # Preprocess the image
        img = load_img(image_path, target_size=(256, 256))
        img_array = img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Make a prediction
        prediction = model.predict(img_array)
        confidence_level = np.max(prediction)

        # Determine class
        if confidence_level > 0.7485:
            predicted_class = 'Poisonous'
        else:
            predicted_class = 'Edible'

        # Return prediction with uploaded image
        image_url = './static/images/' + imagefile.filename
        return render_template('check_mushroom.html', 
                               prediction=predicted_class, 
                               confidence=confidence_level, 
                               image_url=image_url)
    
    # Render the page for GET requests
    return render_template('check_mushroom.html', prediction=None, confidence=None)

@app.route('/funfacts', methods=['GET'])
def funfacts():
    return render_template('funfacts.html')

@app.route('/about_us', methods=['GET'])
def about_us():
    return render_template('about_us.html')

if __name__ == '__main__':
    app.run(port=3000, debug=True)
