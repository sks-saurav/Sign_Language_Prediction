import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet import preprocess_input


def prepare_image(image):
	resized_image = cv2.resize(image, (224,224))
	expanded_image = np.expand_dims(resized_image, axis=0)
	return preprocess_input(expanded_image)
	
def predict_image(camera_captured):
	prepared_image = prepare_image(camera_captured)
	prediction = model.predict(prepared_image)
	max_prob = 0
	dig = 0
	arr = prediction[0]
	for i in range(10):
		if arr[i] > max_prob:
			max_prob = arr[i]
			dig = i;
	return dig_list[dig]
	
	

dig_list = ['Zero','One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
	
model = load_model('model_training/trained_model1.h5')
video = cv2.VideoCapture(0)


ans = "taking imput from Camera"
counter = 0
while True:
	counter += 1
	check, cam_img = video.read()
	if counter == 40:
		ans = predict_image(cam_img)
		print(ans)
		counter = 0
	
	output_img = cv2.putText(cam_img, ans, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3)
	cv2.imshow("Output", output_img)
	
	key = cv2.waitKey(10)
	if key == ord('q'):
		break


video.release()
cv2.destroyAllWindows
