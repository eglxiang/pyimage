import cv2
import glob

faceDet = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
faceDet2= cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
faceDet3= cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
faceDet4= cv2.CascadeClassifier("haarcascade_frontalface_alt_tree.xml")

emotions = ["neutral", "angle", "contempt", "disgust", "fear", "happy", "sadness", "surprise"]

def detect_faces(emotion):
	files = glob.glob("sorted_set\\%s\\*" %emotion)

	filenumber = 0
	for f in files:
		frame = cv2.imread(f)
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		# detect face using 4 different classifiers
		face = faceDet.detectMultiScale(gray, scaleFactor=1.1, minNeighbor=10, minSize=(5,5), flags=cv2.CASCADE_SCALE_IMAGE)
		face2= faceDet2.detectMultiScale(gray,scaleFactor=1.1, minNeighbor=10, minSize=(5,5), flags=cv2.CASCADE_SCALE_IMAGE)
		face3= faceDet3.detectMultiScale(gray,scaleFactor=1.1, minNeighbor=10, minSize=(5,5), flags=cv2.CASCADE_SCALE_IMAGE)
		face4= faceDet4.detectMultiScale(gray,scaleFactor=1.1, minNeighbor=10, minSize=(5,5), flags=cv2.CASCADE_SCALE_IMAGE)

		# go over detected faces, stop at first detected face, return empty if no face.
		if len(face) == 1:
			facefeatures = face
		elif len(face2) == 1:
			facefeatures = face2
		elif len(face3) == 1:
			facefeatures = face3
		elif len(face4) == 1:
			facefeatures = face4
		else:
			facefeatures = ""

		# Cut and save face
		for (x,y,w,h) in facefeatures:
			print "face found in file: %s" %f
			gray = gray[y:y+h, x:x+w]

			try:
				out = cv2.resize(gray, (350,350))
				cv2.imwrite("dataset\\%s\\%s.jpg" %(emotion, filenumber), out)
			except:
				pass # if error, pass file
			filenumber += 1 # increment image number

		for emotion in emotions:
			detect_faces(emotion)