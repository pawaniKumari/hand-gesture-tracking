# Hand Gesture Mouse Control

A computer vision application that allows you to control your mouse cursor using hand gestures captured through your webcam. The system tracks your index finger movements to control the mouse pointer and simulates clicks when your thumb and index finger come close together.

## Features

- **Real-time Hand Tracking**: Uses MediaPipe to detect and track hand landmarks in real-time
- **Mouse Cursor Control**: Move your mouse cursor by moving your index finger
- **Gesture-based Clicking**: Click by bringing your thumb close to your index finger
- **Visual Feedback**: See hand landmarks and finger positions overlaid on the video feed

## How It Works

1. **Hand Detection**: MediaPipe detects hand landmarks from webcam feed
2. **Finger Tracking**: Tracks specific landmarks (index finger tip - ID 8, thumb tip - ID 4)
3. **Coordinate Mapping**: Converts camera coordinates to screen coordinates
4. **Mouse Control**: PyAutoGUI moves cursor and performs clicks based on finger positions
5. **Click Detection**: Measures distance between thumb and index finger to trigger clicks

## Requirements

### Hardware

- Webcam or built-in camera
- Windows, macOS, or Linux operating system

### Software Dependencies

- Python 3.7 or higher
- OpenCV (`cv2`)
- MediaPipe
- PyAutoGUI

## Installation

1. **Clone or download this repository**

   ```bash
   git clone <repository-url>
   cd hand-gesture-tracking
   ```

2. **Install required packages**
   ```bash
   pip install opencv-python mediapipe pyautogui
   ```

## Usage

1. **Run the application**

   ```bash
   python mouse_control_using_hand_gesture.py
   ```

2. **Position yourself**

   - Sit comfortably in front of your camera
   - Ensure good lighting for better hand detection
   - Keep your hand visible in the camera frame

3. **Control the mouse**
   - **Move Cursor**: Point with your index finger to move the mouse cursor
   - **Click**: Bring your thumb close to your index finger (distance < 40 pixels)
   - **Exit**: Press the `ESC` key to quit the application

## Configuration

You can adjust these parameters in the code:

- **Detection Confidence**: `min_detection_confidence=0.7` (0.0 to 1.0)
- **Tracking Confidence**: `min_tracking_confidence=0.7` (0.0 to 1.0)
- **Click Distance Threshold**: `dist<40` (adjust for sensitivity)
- **Camera Index**: `cv2.VideoCapture(0)` (change if using external camera)

## Troubleshooting

### Camera Issues

- **Error: Could not open camera**
  - Check if camera is connected and not used by another application
  - Try changing camera index (0, 1, 2, etc.)
  - Restart the application

### Performance Issues

- **Laggy cursor movement**
  - Improve lighting conditions
  - Reduce `cv2.waitKey()` delay (currently 100ms)
  - Lower detection confidence slightly

### Accuracy Issues

- **Inaccurate tracking**
  - Ensure good lighting
  - Keep hand clearly visible
  - Adjust confidence thresholds
  - Clean camera lens

## Technical Details

### Hand Landmarks

The application uses MediaPipe's 21-point hand landmark model:

- **Index Finger Tip**: Landmark ID 8
- **Thumb Tip**: Landmark ID 4

### Coordinate System

- Camera coordinates are normalized (0.0 to 1.0)
- Converted to pixel coordinates for display
- Mapped to screen resolution for mouse control

## Safety Notes

⚠️ **Important**: This application controls your mouse automatically. Use responsibly:

- Test in a safe environment first
- Keep the ESC key accessible to exit quickly
- Be aware that clicks will be performed automatically
- Consider the security implications of automated mouse control

## Acknowledgments

- **MediaPipe**: Google's framework for building perception pipelines
- **OpenCV**: Computer vision library
- **PyAutoGUI**: Cross-platform GUI automation library

---
