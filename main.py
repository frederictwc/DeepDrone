import cv2
import easytello

# Initialize some variables
drone = easytello.Tello()
drone.streamon()
print("Battery at: " + str(drone.get_battery()) + "%")
process_this_frame = True
print("Connecting...")
video_capture = cv2.VideoCapture("udp://@0.0.0.0:11111")
print("Success!")

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()
    if ret:
        # Display the resulting image
        cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        drone.streamoff()
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()

