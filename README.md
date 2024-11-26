# Hand Distance Measurement with OpenCV and Mediapipe

This project is a Python-based application that measures the distance between two points (thumb and index fingertip) on a hand using a webcam. It includes a simple interactive game where the user matches a target distance for scoring points.

---

## Features

1. **Real-time Hand Detection**:
   - Utilizes Mediapipe's `Hands` module to track and detect hand landmarks.
   - Calculates the distance between the thumb tip and the index fingertip.

2. **Game Mechanics**:
   - A random target distance is generated, and the user attempts to match it by adjusting their hand posture.
   - Scores are awarded for matching the target distance within ±10 pixels.
   - The game runs for a predefined time (30 seconds by default).

3. **User Feedback**:
   - Displays the calculated distance, target distance, score, and remaining time directly on the webcam feed.

4. **Interactive Visualization**:
   - Draws landmarks, points, and connecting lines on the detected hand in real time.

---

## Requirements

Before running the program, ensure the following dependencies are installed:

1. **Python 3.7 or higher**
2. **Libraries**:
   - Mediapipe: For hand landmark detection.
   - OpenCV: For video capture and rendering.

Install dependencies using pip:
```bash
pip install mediapipe opencv-python
```

---

## How It Works

### Hand Detection
The Mediapipe Hands module identifies key landmarks on the hand. The program extracts two specific points:
- **Thumb Tip** (`THUMB_TIP`)
- **Index Finger Tip** (`INDEX_FINGER_TIP`)

### Distance Calculation
The Euclidean distance between the two points is calculated using the formula:
\[
\text{distance} = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
\]

### Game Logic
1. A random **target distance** is generated (50–200 pixels).
2. The user adjusts their thumb and index finger to match this target.
3. The score increases by 1 if the calculated distance is within 10 pixels of the target distance.
4. The game lasts for 30 seconds, displaying:
   - Current distance
   - Target distance
   - Score
   - Time remaining

---

## Code Structure

### Imports
```python
import cv2
import mediapipe as mp
import numpy as np
import random
```

### Functions
- **`calculate_distance(p1, p2)`**: Computes the Euclidean distance between two points.
  ```python
  def calculate_distance(p1, p2):
      return int(np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2))
  ```

### Mediapipe Initialization
```python
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils
```

### Game Variables
```python
target_distance = random.randint(50, 200)  # Random target distance
score = 0  # Initial score
game_time = 30  # Game duration in seconds
```

### Webcam Capture Loop
1. Captures video frames using OpenCV.
2. Processes each frame with Mediapipe to detect hand landmarks.
3. Calculates and displays:
   - Current distance
   - Target distance
   - Game score
   - Time remaining

---

## Usage

1. Run the script:
   ```bash
   python hand_distance_game.py
   ```

2. Allow access to your webcam.

3. Adjust the position of your thumb and index finger to match the target distance displayed on the screen.

4. Try to score as many points as possible before the time runs out.

5. Press **`q`** to exit at any time.

---

## Output

- **Webcam Feed**:
  - Displays:
    - Real-time hand landmarks with connecting lines.
    - Distance between thumb and index fingertip.
    - Target distance, score, and remaining time.

- **Game End**:
  - A "Game Over!" message is displayed when the timer expires.

---

## Example Output

### Game Interface:
- The webcam feed shows:
  - Hand landmarks with thumb and index fingertip highlighted.
  - A line connecting the two points.
  - Distance metrics and game information.

### End of Game:
- The program displays "Game Over!" and freezes the last frame for 3 seconds.

---

## Customization

1. **Game Duration**:
   Modify the `game_time` variable:
   ```python
   game_time = 60  # Set game duration to 60 seconds
   ```

2. **Target Distance Range**:
   Adjust the range for random target distances:
   ```python
   target_distance = random.randint(30, 150)
   ```

3. **Tolerance**:
   Change the tolerance for distance matching:
   ```python
   if abs(distance - target_distance) < 5:  # More challenging
   ```

---

## Limitations

1. Accuracy depends on proper lighting and the webcam's resolution.
2. Distance is calculated in pixels, not in real-world units (e.g., centimeters).

---

## Future Enhancements

1. Convert pixel distances to real-world units using camera calibration.
2. Add difficulty levels (e.g., smaller tolerances or moving targets).
3. Integrate sound effects or visual animations for improved user experience.

---

## Troubleshooting

1. **No Hand Detected**:
   - Ensure proper lighting.
   - Keep the hand within the webcam frame.

2. **Low Performance**:
   - Reduce frame resolution for smoother processing.
     ```python
     cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
     cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
     ```

---

## Conclusion

This project demonstrates real-time hand distance measurement and gamification using OpenCV and Mediapipe. It’s a fun and interactive way to learn computer vision concepts!
