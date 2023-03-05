from flask import Flask, request, jsonify
from flask import Flask, render_template, request,redirect
import requests
# import numpy as np
from flask_swagger_ui import get_swaggerui_blueprint
app = Flask(__name__)


SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')

API_URL = '/static/documentation.json' 
API_ENDPOINT = 'http://your-api-endpoint.com/predict_gender'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
)

app.register_blueprint(swaggerui_blueprint)

# basepath="C:\Users\91932\Desktop\COC\lattes-master"
# model1 = load_model((os.path.join(basepath,'realFake.h5')))
# model1.make_predict_function()
# model2 = load_model(os.path.join(basepath,'weights.best.inc.male.hdf5'))
# model2.make_predict_function()


@app.route('/', methods=['POST', 'GET'])




def index():
    # if request.method == 'POST':
    # # # Get the image URL from the request
    #     image_url = request.args.get('urll')
    #     url=image_url
    #     print(url)
        
    #     # Load the image from the URL and preprocess it
    #     # image = Image.open(requests.get(image_url, stream=True).raw)
    #     # image = image.resize((224, 224))  # resize to match VGG-16 input size
    #     # image = np.array(image)
    #     # image = preprocess_input(image)
    #     # image = np.expand_dims(image, axis=0)  # add batch dimension
        
    #     # # Use the model to predict the gender of the person in the image
    #     # prediction = model2.predict(image)
        
    #     if prediction > 0.5:
    #         gender = 'female'
    #     else:
    #         gender = 'male'
        
    #     # Return the prediction as a JSON response
    #     return render_template('index.html', gender=gender)
    
    return render_template('index.html')





if __name__ == '__main__':
    app.run(debug=True)

