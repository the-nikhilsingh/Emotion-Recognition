# Emotion-Recognition
4 layers of CNN and 2 layers of dense network is used to classify the faces into the following categories: Angry, Disgust, Fear, Happy, Sad, Surprise, Neutral. With the Relu in Convolution layers and sigmoid functionin output layer, an accuracy of 64% is achived

Dataset Names:
a.	fer2013.bin (63M)
b.	test_batch.bin (7.9M)
It comprises a total of 35887 pre-cropped, 48-by-48-pixel grayscale images of faces each labeled with one of the 7 emotion classes. The faces have been automatically registered so that the face is more or less cantered and occupies about the same amount of space in each image. train.csv contains two columns, "emotion" and "pixels". The "emotion" column contains a numeric code ranging from 0 to 6, inclusive, for the emotion that is present in the image. The "pixels" column contains a string surrounded in quotes for each image. The contents of this string a space-separated pixel values in row major order. test.csv contains only the "pixels" column and your task is to predict the emotion column

Data pre-processing/ Data Cleaning Information -> The haar-cascade_frontalface_default.xml in OpenCV contains pre-trained filters and uses Ada-boost to quickly find and crop the face. The cropped face is then converted into grayscale using cv2.cvtColor and resized to 48-by-48 pixels with cv2.resize.

The confusion matrix gives the counts of emotion predictions and some insights to the performance of the multi-class classification model:
•	The model performs really well on classifying positive emotions resulting in relatively high precision scores for happy and surprised. Happy has a precision of 76.7% which could be explained by having the most examples (~7000) in the training set. Interestingly, surprise has a precision of 69.3% having the least examples in the training set. This means that there must be very strong signals in the surprise expressions. 
•	Model performance seems weaker across negative emotions on average. In particularly, the emotion sad has a low precision of only 39.7%. The model frequently misclassified angry, fear and neutral as sad. In addition, it is most confused when predicting sad and neutral faces because these two emotions are probably the least expressive (excluding crying faces).
