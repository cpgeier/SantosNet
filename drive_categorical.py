from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from deepgtav.messages import Start, Stop, Scenario, Commands, frame2numpy
from deepgtav.client import Client
import cv2
import numpy as np

print("Loading Model...")
model = load_model('sample_model.h5') # Load trained model
print("Model Loaded. Compiling...")
model.compile(optimizer='Adadelta', loss='mean_squared_error')

if input("Continue?") == "y": # Wait until you load GTA V to continue, else can't connect to DeepGTAV
    print("Conintuing...")

# Loads into a consistent starting setting 
print("Loading Scenario...")
client = Client(ip='localhost', port=8000) # Default interface
scenario = Scenario(weather='EXTRASUNNY',vehicle='blista',time=[12,0],drivingMode=-1,location=[-2573.13916015625, 3292.256103515625, 13.241103172302246])
client.sendMessage(Start(scenario=scenario))

count = 0
print("Starting Loop...")
while True:
    try:    
        # Collect and preprocess image
        message = client.recvMessage()
        image = frame2numpy(message['frame'], (320,160))
        image = ((image/255) - .5) * 2

        # Corrects for model input shape
        model_input = []
        model_input.append(image)

        # Converts classification to float for steering input
        category_prediction = np.argmax(model.predict(np.array(model_input)))
        decimal_prediction = (category_prediction - 500) / 500
        print('Category: ' + str(category_prediction) + '     Decimal: ' + str(decimal_prediction))

        client.sendMessage(Commands(0.0,0.0,decimal_prediction * 3)) # Mutiplication scales decimal prediction for harder turning
        count += 1
    except Exception as e:
        print("Excepted as: " + str(e))
        continue

client.sendMessage(Stop()) # Stops DeepGTAV
client.close()
