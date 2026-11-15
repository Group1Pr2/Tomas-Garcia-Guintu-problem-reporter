import cv2

def test_camera():
    print("Attempting to open webcam (index 0)...")
    # Try opening the default video device
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        print("Diagnostic Note: If you see a device index error here, it confirms your Linux container")
        print("still lacks the host video driver module (/dev/video0) required by Chromebook Crostini.")
        return

    print("Success! Webcam opened. Press 'q' in the video window to close it.")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to grab video frame.")
            break
        
        # Display the live frame in a window
        cv2.imshow("Chromebook Webcam Test", frame)
        
        # Press 'q' to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Clean up resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    test_camera()