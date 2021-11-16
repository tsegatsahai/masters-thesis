# masters-thesis
Monitoring seniors in their homes using CNN 

## Folders (in the order they appear)

- **dataset**: contains the raw videos downloaded from the internet (the videos before they get converted to images)

- **falling**: raw falling images before they're convered to stick figures 

- **images**: contains two raw and two stick-figure images that show how the stick-figure images would look if the person saw sideways or turned around

- **papers**: contains some papers about fall detection

- **sitting**: raw sitting images before they're converted to stick figures

- **src_code**: contains all the source code and data used for this research 
  - **actions copy**: original images used to train and test model 1 (still had 4 classes instead of 3)
  - **actions**: images used to train and test model 4
  - **actionsModel2**: images used to train and test model 2
  - **actionsModel3**: images used to train and test model 3
  - **actionsRaw**: images used to train and test the model with raw images 
  - **actionsKFold**: images used to train/test the 10-fold cross validation
  - **binaryActions**: images used to train and test the model that classified the images as fall/no_fall
  - **fallOut**: stick figure images of falling
  - **fallOut1**: stick figure images of falling
  - **images**: images of graphs/accuracies from jupyter-notebook
  - **kfoldModels**: the 10 models that were produced by the 10-fold cross validation
  - **sitOut**: stick figure images of sitting 
  - **standOut**: stick figure images of standing
  - **testing**: stick figure images used for testing the model 
  - **testingRaw**: images used to test the raw-image model 
  - **walkOut**: stick figure images of walking
  - **walkOut1**: stick figure images of walking
  - *actionRecognition.ipynb*: the notebook where the models are trained and tested
  - *classification.csv*: a csv file that was created for the 10-fold cross validation
  - *classification.txt*: a txt file that was created for the 10-fold cross validation
  - *image_label.ipynb*: used to manually classify/label the images as walking, standing, falling...
  - *kfoldCrossVal2.ipynb*: the 10-fold cross validation code 
  - *sensitivity_specificty.ipynb*: code for calculating the sensitivity and specificity of the model 
  - *stickFigure.ipynb*: code to convert raw image into stick figures 
  - *vid_to_img.ipynb*: code to capture images from the raw videos 

- **standing**: raw standing images before they're converted to stick figures 

- **training_images**: images captured from the data1 video folder (in dataset folder) -- cam8

- **training_images23**:images captured from the data23 video folder (in dataset folder) -- cam8

- **training_images4**: images captured from the data4 video folder (in dataset folder) -- cam8

- **training_images9**: images captured from the data9 video folder (in dataset folder) -- cam8

- **walkOut**: stick figure images of walking 

- **walking**: raw walking images before they're converted to stick figures 
