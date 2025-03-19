# VisionVault – Face Recognition Door Lock System 🚀
🔐 Secure Your Space with AI & IoT
VisionVault is a smart door lock system that uses face recognition to grant access. It integrates OpenCV, face_recognition, and Arduino via Bluetooth, providing a seamless and secure way to unlock doors.

## Features
1.Face Recognition Authentication – Detects and verifies authorized users.
2.Automatic Door Unlocking – Unlocks when an authorized face is detected.
3.Bluetooth Communication – Sends unlock/lock commands to Arduino via HC-05.
4.Security Measures – Includes a face distance threshold and cooldown period to prevent unauthorized access.
5.Real-Time Video Feed – Displays live video with face recognition results.

## Technologies Used
### Programming Language
Python (Main logic)
Arduino (C++) (For microcontroller communication)
### Libraries
1. OpenCV – Captures and processes video.
2. face_recognition – Face detection and verification.
3. NumPy – Numerical computations.
4. PySerial – Communication with Arduino.

## How It Works
1️. Capture Live Video 🎥 – The system continuously scans for faces.
2️. Detect & Verify Face 🤖 – Compares the detected face with the authorized database.
3️. Send Unlock Signal 🔓 – If the face is a match, sends an unlock command to Arduino via Bluetooth.
4️. Auto Lock Mechanism 🔒 – The door locks automatically after 5 seconds.

## Installation & Setup
1️. Clone the Repository: git clone https://github.com/yolo-co/VisionVault.git
cd VisionVault

2️. Install Dependencies:
Make sure you have Python installed, then run: pip install opencv-python face-recognition numpy pyserial

3️. Update Image Path & Bluetooth Port: authorized_image = face_recognition.load_image_file(r"C:\Users\Senguttuvan\authorized_faces\your_image.jpg")
bluetooth = serial.Serial(port='COM5', baudrate=9600, timeout=1)  # Change 'COM5' if needed

4️. Run the Project: python VisionVault.py

## Hardware Requirements
Laptop/PC with Webcam
Arduino Board (Uno/Nano)
HC-05 Bluetooth Module
Servo Motor / Electronic Door Lock
Power Supply

## Contributing
Feel free to fork this repository and submit pull requests. Let's improve VisionVault together!

## License
MIT License – Free to use and modify.

Made with by S.Yoganand
