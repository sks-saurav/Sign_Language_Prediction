## Sign Language Prediction
#### this project detects sign language symbol from 0 to 9. and can be easily extended to detect all alphabets.

![screen_cap](https://github.com/sks-saurav/Sign_Language_Prediction/blob/main/screen_capture.gif)

### CNN Model Training
For prediction of symbol I have used Convolution Neural Network, I have taken [MobileNet](https://github.com/Zehaos/MobileNet) CNN architecture and fined tuned it for prediction for 10 classes of symbol.

then trained on decent amount of data. DataSet can be found [here](https://drive.google.com/drive/folders/1IcyxjNSwJ5OWHHLmyZutLfMSIuFuk-h_?usp=sharing). 
during training accuracy of model was good (aprox 99%). 

### Prediction
OpenCv is used input and output of image data. 

It capture a image frame from webCamera, the captured image is send for preprocessing and then given to model for prediction.

model predicts its belonging to one class out of 10 possible classes. 

the predicted optput is printed on output image.
