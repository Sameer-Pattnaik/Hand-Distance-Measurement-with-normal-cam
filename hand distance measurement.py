import cv2
import mediapipe as mp
import numpy as np
import random

# Initialize Mediapipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Define a function to calculate Euclidean distance
def calculate_distance(p1, p2):
    return int(np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2))

# Initialize the game variables
target_distance = random.randint(50, 200)
score = 0
game_time = 30  # seconds

# Start capturing from webcam
cap = cv2.VideoCapture(0)
start_time = cv2.getTickCount()

while True:
    success, frame = cap.read()
    if not success:
        print("Failed to capture frame. Exiting...")
        break

    # Flip the frame for a mirror effect
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame to detect hands
    results = hands.process(rgb_frame)

    # Draw landmarks and calculate distances
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Extract the coordinates of the index fingertip and thumb tip
            index_finger = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]

            # Convert normalized coordinates to pixel values
            index_point = (int(index_finger.x * w), int(index_finger.y * h))
            thumb_point = (int(thumb_tip.x * w), int(thumb_tip.y * h))

            # Draw points and the line between them
            cv2.circle(frame, index_point, 10, (255, 0, 0), -1)
            cv2.circle(frame, thumb_point, 10, (0, 255, 0), -1)
            cv2.line(frame, index_point, thumb_point, (0, 255, 255), 3)

            # Calculate the distance
            distance = calculate_distance(index_point, thumb_point)

            # Display the distance
            cv2.putText(frame, f"Distance: {distance}px", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Check if the distance matches the target distance
            if abs(distance - target_distance) < 10:
                score += 1
                target_distance = random.randint(50, 200)  # Generate a new target distance

    # Display the target distance and score
    cv2.putText(frame, f"Target: {target_distance}px", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    cv2.putText(frame, f"Score: {score}", (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Calculate the remaining time
    elapsed_time = (cv2.getTickCount() - start_time) / cv2.getTickFrequency()
    remaining_time = max(0, int(game_time - elapsed_time))
    cv2.putText(frame, f"Time: {remaining_time}s", (10, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # End the game if time is up
    if remaining_time == 0:
        cv2.putText(frame, "Game Over!", (w // 2 - 100, h // 2), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
        cv2.imshow("Hand Distance Measurement Game", frame)
        cv2.waitKey(3000)  # Display "Game Over" for 3 seconds
        break

    # Display the frame
    cv2.imshow("Hand Distance Measurement Game", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
hands.close()
