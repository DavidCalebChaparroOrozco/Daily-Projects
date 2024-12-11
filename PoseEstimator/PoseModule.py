# Importing necessary libraries
import cv2
import mediapipe as mp
import time

class PoseDetector:
    # Initialize parameters for pose detection
    def __init__(self, mode=False, upBody=False, smooth=True, detectionCon=0.5, trackCon=0.5):

        # Boolean: whether to use static image mode
        self.mode = mode  
        # Boolean: whether to detect only the upper body
        self.upBody = upBody  
        # Boolean: whether to smooth landmarks
        self.smooth = smooth  
        # Float: minimum detection confidence
        self.detectionCon = detectionCon  
        # Float: minimum tracking confidence
        self.trackCon = trackCon  

        # Initialize MediaPipe drawing and pose utilities
        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        
        # Initialize the Pose object with specified parameters
        self.pose = self.mpPose.Pose(
            static_image_mode=self.mode,
            # Complexity of the model (0: light, 1: full)
            model_complexity=1,  
            enable_segmentation=self.upBody,
            smooth_landmarks=self.smooth,
            min_detection_confidence=self.detectionCon,
            min_tracking_confidence=self.trackCon
        )

    def findPose(self, img, draw=True):
        # Convert the image from BGR to RGB for processing
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Process the image and get pose landmarks
        self.results = self.pose.process(imgRGB)
        
        # Draw landmarks on the image if they are detected and drawing is enabled
        if self.results.pose_landmarks and draw:
            self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        
        return img

    def findPosition(self, img, draw=True):
        # List to store landmark positions
        lmList = []  
        
        # Check if pose landmarks are detected
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                # Get image dimensions
                h, w, c = img.shape  
                # Calculate pixel coordinates of the landmark
                cx, cy = int(lm.x * w), int(lm.y * h)  
                # Append landmark ID and coordinates to the list
                lmList.append([id, cx, cy])  
                
                # Draw a circle on each landmark if drawing is enabled
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        
        return lmList

def main():
    # Open video file for processing
    cap = cv2.VideoCapture('video/2.mp4')
    # Previous time for FPS calculation
    pTime = 0  
    
    # Create an instance of PoseDetector
    detector = PoseDetector()  

    while True:
        # Read a frame from the video
        success, img = cap.read()  
        
        # Check if the frame was successfully captured
        if not success:
            print("Error: Unable to read video. Please check the file path.")
            break
        
        # Find and draw pose on the image
        img = detector.findPose(img) 
        # Get positions of landmarks without drawing
        lmList = detector.findPosition(img, draw=False) 
        
        # Print coordinates of a specific landmark (index 14) if it exists
        if lmList:
            # Ensure that index exists before accessing it
            print(lmList[14]) 
            
            # Draw a circle on the specified landmark (index 14)
            cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (0, 0, 255), cv2.FILLED)

        # Current time for FPS calculation
        cTime = time.time() 
        # Calculate frames per second (FPS)
        fps = 1 / (cTime - pTime) 
        # Update previous time
        pTime = cTime 

        # Display FPS on the image
        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 0), 3)

        # Show the processed image in a window named 'ImageCapture'
        cv2.imshow('ImageCapture', img)

        # Exit the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release video capture object
    cap.release()  
    # Close all OpenCV windows
    cv2.destroyAllWindows()  

if __name__ == '__main__':
    main()
