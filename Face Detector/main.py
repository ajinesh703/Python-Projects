import cv2
import numpy as np
from deepface import DeepFace

# Load the Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def analyze_emotion(face):
    try:
        # Resize the face to improve DeepFace compatibility
        resized_face = cv2.resize(face, (224, 224))
        # Use DeepFace to analyze the emotion in the detected face
        result = DeepFace.analyze(resized_face, actions=['emotion'], enforce_detection=False)
        return result['dominant_emotion']
    except Exception as e:
        print(f"Error analyzing emotion: {e}")
        return None

def main():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame.")
            break

        # Convert to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            # Draw a rectangle around the face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Extract the face for emotion analysis
            face = frame[y:y+h, x:x+w]
            emotion = analyze_emotion(face)

            # Display the detected emotion
            if emotion:
                cv2.putText(frame, emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

        # Display the resulting frame
        cv2.imshow('Face and Emotion Detection', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close the windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
