<img src="/sample.gif?raw=true">

# SantosNet
Simple tools that I used to generate and run a self-driving car model with VPilot and DeepGTAV.

## Requirements
1. [DeepGTAV](https://github.com/ai-tor/DeepGTAV) must be installed and [VPilot](https://github.com/cpgeier/VPilot) must be in the same folder.

2. Keras, Tensorflow, Numpy, h5py

2. A GPU with 6 or more gigabytes of VRAM. A 980ti is barely able to simultaneously run the model and the game.

## Files

- dataset.py - Uses in-game AI to drive car. Captures screen and saves driving variables in a pickle file
- drive_categorical.py - Excecutes a trained model on captured frames
- load_and_train.py - Continues training a model on a dataset
- model_xception.py - Main training program. Generates a .h5 model file that can be loaded for predictions
- pickling.py - A simple program that displays frames from a pickled file
- preprocessing.py - Loads batches of frames from a pickled file to be used in training
- sample.gif - Demonstration of the ability of a model generated using these programs

Download a sample model [here](https://drive.google.com/file/d/1ai6qRoFwWkcAOYkNxqxzPIwiOeiuvKd-/view?usp=sharing)

## Model

The Xception V1 model is used to classify different images to different positions of the steering wheel. The steering position is collected as a float between -1 and 1, so I converted it to a positive integer between 0 and 999. This was then simply converted to a one-hot vector for input into the model. This preserves the overall structure of the Xception V1 model because the Imagenet dataset that it was designed for included 1000 classes of images. I tried to use the Xception model for regression, but did not have as good of results. During driving, the model is sent the images and returns a vector which is converted into a value between -1 and 1 to be sent to DeepGTAV for input into the game. To clarify, the model only controls the steering of the car while I control the throttle on the keyboard.

## Training

The dataset I generated was around 66 gigabytes after running for 10 hours, so I would advise having plenty of space on a hard drive to store data. Also, I training the model on an AWS p2xlarge instance for around 12 hours, during that time I was only able to go through 1 epoch of the data. However, the model still yeilded great results in running and is able to avoid obstacles and stay between road lines most of the time.

## Improvements

If you would like to contribute I have some ideas on how this model could be improved:

- Dataset balancing - Most of the steering values will be around 0, with few around -1 and 1, so balancing the dataset would probably improve performance
- Fine tune with ImageNet initilization - I initialized with random weights, but its probably best to fine tune the model with pre-trained weights
- Better preprocessing
