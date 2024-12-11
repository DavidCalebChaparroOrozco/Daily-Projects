# Importing necessary libraries
import cv2
import mediapipe as mp
import time

# Initialize MediaPipe Pose and Drawing utilities
mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

# Open the video file
video_path = 'video/1.mp4'
cap = cv2.VideoCapture(video_path)


# Variable to store previous time for FPS calculation
pTime = 0

# Main loop to read frames from the video
while True:
    success, img = cap.read()
    
    # Check if the frame was successfully captured
    if not success:
        print("Error: Unable to read video. Please check the file path.")
        break

    # Convert the image color from BGR to RGB for MediaPipe processing
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Process the image and get pose landmarks
    results = pose.process(imgRGB)
    
    # If pose landmarks are detected, draw them on the image
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        
        # Loop through each landmark and draw a circle on it
        for id, lm in enumerate(results.pose_landmarks.landmark):
            # Get image dimensions
            h, w, c = img.shape  
            # Calculate landmark position in pixels
            cx, cy = int(lm.x * w), int(lm.y * h)  
            # Draw circle on landmark
            cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)  

    # Calculate frames per second (FPS)
    # Current time
    cTime = time.time()  
    # Calculate FPS
    fps = 1 / (cTime - pTime)  
    # Update previous time
    pTime = cTime  

    # Display the FPS on the image
    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)

    # Show the processed image in a window named 'ImageCapture'
    cv2.imshow('ImageCapture', img)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
