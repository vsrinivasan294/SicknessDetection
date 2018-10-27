#!/usr/bin/python

# Standard imports
import cv2
import numpy as np;


def detect_blood(filename):

	# Setup SimpleBlobDetector parameters.
	params = cv2.SimpleBlobDetector_Params()

	# Change thresholds
	params.minThreshold = 0
	params.maxThreshold = 200

	# Filter by Area.
	params.filterByArea = True
	params.minArea = 1
	params.maxArea = 2000

	#Filter by Circularity
	#params.filterByCircularity = True
	#params.minCircularity = 0
	#params.maxCircularity = 1

	#Filter by Color
	#params.filterByColor = True

	# Filter by Convexity
	params.filterByConvexity = True
	params.minConvexity = 0
	params.maxConvexity = 1
	    
	# Filter by Inertia
	params.filterByInertia = True
	params.minInertiaRatio = 0
	params.maxInertiaRatio = 1

	# Create a detector with the parameters
	ver = (cv2.__version__).split('.')
	if int(ver[0]) < 3 :
		detector = cv2.SimpleBlobDetector(params)
	else : 
		detector = cv2.SimpleBlobDetector_create(params)

	    
	# Read image
	im = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

	# Detect blobs.
	keypoints = detector.detect(im)

	# Draw detected blobs as red circles.
	# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
	# the size of the circle corresponds to the size of blob

	im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

	nblobs = len(keypoints)

	print("Blood Cell Detection")
	print(" ")
	print(nblobs)

	# Show blobs
	cv2.imshow("Keypoints", im_with_keypoints)
	cv2.waitKey(0)



detect_blood(FPMDEMO.png)

