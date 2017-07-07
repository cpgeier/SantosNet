<img src="/sample.gif?raw=true">

# DeepGTAV_Tools
Simple tools that I used to generate and run a model with VPilot and DeepGTAV.

## Requirements
[DeepGTAV](https://github.com/ai-tor/DeepGTAV) must be installed and [VPilot](https://github.com/cpgeier/VPilot) must be in the same folder. 

## Files

- dataset.py - Uses in-game AI to drive car. Captures screen and saves driving variables in a pickle file
- drive_categorical.py - Excecutes a trained model on captured frames
- load_and_train.py - Continues training a model on a dataset
- model_xception.py - Main training program. Generates a .h5 model file that can be loaded for predictions
- pickling.py - A simple program that displays frames from a pickled file
- preprocessing.py - Loads batches of frames from a pickled file to be used in training
- sample.gif - Demonstration of the ability of a model generated using these programs

## Model description

The Xception V1 model is used to classify different images to different positions of the steering wheel. The steering position is collected as a float between -1 and 1, so I convert it to a positive integer between 0 and 999. This was then simply converted to a one-hot vector for input into the model. This preserves the overall structure of the Xception V1 model because the Imagenet dataset that it was designed for included 1000 classes of images. I tried to use the Xception model for regression, but did not have as good of results. During driving, the model is sent the images and returns a vector which is converted into a value between -1 and 1 to be sent to DeepGTAV for input into the game.
