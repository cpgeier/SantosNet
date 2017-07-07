<img src="/sample.gif?raw=true">

# DeepGTAV_Tools
Simple tools that I used to generate and run a model with VPilot and DeepGTAV.

## Requirements
[DeepGTAV](https://github.com/ai-tor/DeepGTAV) must be installed and [VPilot](https://github.com/cpgeier/VPilot) must be in the same folder. 


- dataset.py - Uses in-game AI to drive car. Captures screen and saves driving variables in a pickle file
- drive_categorical.py - Excecutes a trained model on captured frames
- load_and_train.py - Continues training a model on a dataset
- model_xception.py - Main training program. Generates a .h5 model file that can be loaded for predictions
- pickling.py - A simple program that displays frames from a pickled file
- preprocessing.py - Loads batches of frames from a pickled file to be used in training
- sample.gif - Demonstration of the ability of a model generated using these programs

