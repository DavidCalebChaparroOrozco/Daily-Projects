# Importing necessary libraries
import cv2
import time
import tkinter as tk
from tkinter import filedialog
from PoseModule import PoseDetector as pm
import csv

# Function to open a file dialog and select a video file
def select_video_file():
    # Initialize Tkinter root
    root = tk.Tk()
    # Hide the root window
    root.withdraw()
    # Open a file dialog to select a video file and return its path
    file_path = filedialog.askopenfilename(title="Select Video File", filetypes=[("Video files", "*.mp4;*.avi")])
    return file_path

# Function to save pose landmarks to a CSV file
def save_landmarks_to_csv(lmList, filename='landmarks.csv'):
    # Open the specified CSV file in write mode
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header row to the file
        writer.writerow(['ID', 'X', 'Y'])  
        # Write the list of landmarks to the file
        writer.writerows(lmList)

# Main function to process the video and perform pose estimation
def main():
    # Prompt the user to select a video file
    video_path = select_video_file()  
    # Open the selected video file
    cap = cv2.VideoCapture(video_path)
    # Variable to store previous time for FPS calculation
    pTime = 0
    # Create an instance of the PoseDetector class
    detector = pm()

    while True:
        # Read a frame from the video
        success, img = cap.read()
        # If the frame could not be read, print an error and exit the loop
        if not success:
            print("Error: Unable to read video. Please check the file path.")
            break
        
        # Perform pose detection on the current frame
        img = detector.findPose(img)
        # Get the positions of the landmarks
        lmList = detector.findPosition(img, draw=False)

        # If landmark positions are detected, process them
        if lmList:
            # Print the coordinates of the landmark at index 14
            print(lmList[14])  
            
            # Draw a circle on the landmark at index 14
            cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (0, 0, 255), cv2.FILLED)
            
            # Save the landmarks to a CSV file (optional)
            save_landmarks_to_csv(lmList)

        # Get the current time for FPS calculation
        cTime = time.time()
        # Calculate frames per second (FPS)
        fps = 1 / (cTime - pTime)
        # Update the previous time
        pTime = cTime
        
        # Display the FPS on the frame
        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 0), 3)

        # Show the frame in a window named 'ImageCapture'
        cv2.imshow('ImageCapture', img)

        # Exit the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object
    cap.release()
    # Close all OpenCV windows
    cv2.destroyAllWindows()

# Entry point of the script
if __name__ == '__main__':
    main()
