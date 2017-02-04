import cv2
import dlib

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def get_landmarks(image):
	detections = detector(image, 1)
	for k,d in enumerate(detections):
		shape = predictor(image, d)
		xlist = []
		ylist = []
		for i in range(1,68):
			xlist.append(float(shape.part(i).x))
			ylist.append(float(shape.part(i).y))

		xmean = np.mean(xlist)
		ymean = np.mean(ylist)
		xcentral = [(x-xmean) for x in xlist]
		ycentral = [(y-ymean) for y in ylist]

		if xlist[26] == xlist[29]:
			anglenose = 0
		else:
			anglenose = int(math.atan((ylist[26] - ylist[29])/(xlist[26]-xlist[29]))*180/math.pi)

		if anglenose < 0:
			anglenose += 90
		else:
			anglenose -= 90

		landmarks_vectorized = []

		for x,y,w,z in zip(xcentral, ycentral, xlist, ylist):
			landmarks_vectorized.append(x)
			landmarks_vectorized.append(y)

			meannp = np.asarray((ymean,xmean))
			coornp = np.asarray((z,w))
			dist = np.linalg.norm(coornp-meannp)
			landmarks_vectorized.append(dist)

			anglerelative = (math.atan((z-ymean)/(w-xmean))*180/math.pi) - anglenose
			landmarks_vectorized.append(anglerelative)

	if len(detections) < 1:
		landmarks_vectorized = "error"

	return landmarks_vectorized