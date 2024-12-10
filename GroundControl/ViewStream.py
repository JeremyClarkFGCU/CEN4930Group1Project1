import cv2

# Define RTSP port
streamPort = 8554 # Default RTSP Port


# The URL where the stream will be playing
rtspURL = f"rtsp://10.100.0.28:{streamPort}/stream"

# Create a video capture object in OpenCV
videoObject = cv2.VideoCapture(rtspURL)

# If camera isn't opened, exit
if not videoObject.isOpened():
    print("Error opening video stream or file")
    exit()

# loop until video is completed
while(videoObject.isOpened()):
    ret, frame = videoObject.read()
    if ret:
        cv2.imshow('RTSP Drone Stream - Press Q to exit',frame)

        # Press Q to quit
        if cv2.waitkey(25) & 0xFF == ord('q'):
            break

    else:
        break

# When everything is done, release the capture
videoObject.release()
cv2.destroyAllWindows()