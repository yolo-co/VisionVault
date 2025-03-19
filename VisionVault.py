import cv2
import serial
import time
import face_recognition
import numpy as np

bluetooth = serial.Serial(port='COM5', baudrate=9600, timeout=1)  # Change 'COM5' to match your HC-05 module
time.sleep(2)  # Give time to establish connection


authorized_image = face_recognition.load_image_file(r"C:\authorized_faces\yoga.jpg")  # Update with correct path
authorized_encoding = face_recognition.face_encodings(authorized_image)[0]


cap = cv2.VideoCapture(0)  # 0 = Default Webcam


door_unlocked = False
last_unlock_time = 0
FACE_MATCH_THRESHOLD = 0.5  # Set strict face match threshold (Lower = more strict)

def unlock_door():
    """Sends command to Arduino to unlock the door and turn on LED."""
    global door_unlocked
    bluetooth.write(b'o')  # Send 'o' to unlock door
    bluetooth.write(b'l')  # Send 'l' to turn LED on
    print("🔓 Door Unlocked! LED ON")
    door_unlocked = True
    time.sleep(5)  # Keep unlocked for 5 sec
    lock_door()

def lock_door():
    """Sends command to Arduino to lock the door and turn off LED."""
    global door_unlocked
    bluetooth.write(b'c')  # Send 'c' to lock door
    bluetooth.write(b'x')  # Send 'x' to turn LED off
    print("🔒 Door Locked! LED OFF")
    door_unlocked = False

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Camera Error! Check webcam.")
        break

    # Convert frame to RGB (required for face recognition)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect faces and get encodings
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Compare detected face with authorized face
        face_distance = face_recognition.face_distance([authorized_encoding], face_encoding)[0]
        is_match = face_distance < FACE_MATCH_THRESHOLD  # Check if distance is below threshold

        if is_match:
            # Draw a rectangle around the authorized face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, "✅ Authorized", (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            # Unlock door if not already unlocked
            current_time = time.time()
            if not door_unlocked and current_time - last_unlock_time > 10:  # 10-sec cooldown
                unlock_door()
                last_unlock_time = current_time
        else:
            # Draw rectangle for unauthorized face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.putText(frame, "❌ Unauthorized", (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    # Display video
    cv2.imshow('Face Recognition Lock System', frame)

    # Quit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
bluetooth.close()
cv2.destroyAllWindows()
