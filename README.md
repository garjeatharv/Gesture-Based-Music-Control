# Gesture-Based Music Control using Hand Tracking

This project allows users to control music playback using hand gestures detected by a webcam. By performing specific hand gestures, users can control various functions such as adjusting volume, skipping tracks, pausing and playing music, and muting the audio.

## Installation

To run the Gesture-Based Music Control project, follow these steps:

1. **Clone the Repository:**
   Clone the project repository to your local machine using the following command:
   ```
   git clone <repository_url>
   ```

2. **Install Dependencies:**
   Navigate to the project directory and install the required dependencies using the following command:
   ```
   pip install -r requirements.txt
   ```

3. **Run the Application:**
   Run the main Python script to start the gesture-based music control application:
   ```
   python gesture_music_control.py
   ```

## Requirements

- Python 3.x
- OpenCV
- cvzone (HandTrackingModule)
- NumPy
- PyAutoGUI

## Usage

1. **Camera Setup:**
   Ensure that your webcam is properly connected to your computer and positioned to capture hand gestures effectively.

2. **Run the Application:**
   Execute the main Python script (`gesture_music_control.py`) to start the application.

3. **Perform Hand Gestures:**
   Use your hand gestures in front of the webcam to control various music playback functions:
   - Right: Skip to the next song
   - Left: Go back to the previous song
   - Up: Increase the volume
   - Down: Decrease the volume
   - All Fingers: Pause or play the music
   - Thumb and Index Finger Extended: Skip to the next song
   - Thumb and Little Finger Extended: Go back to the previous song
   - Index, Middle, and Ring Fingers Extended: Mute the audio

4. **Exit the Application:**
   Press the 'q' key on your keyboard to exit the application and stop music playback control.

## Troubleshooting

- If the hand gestures are not being detected accurately, try adjusting the lighting conditions in the environment or the camera angle.
- Ensure that the dependencies are properly installed and up-to-date.
- Check the console for any error messages or warnings that may indicate issues with the application.

## Contribution

Contributions to improve the project are welcome! Please feel free to fork the repository, make your changes, and submit a pull request with your enhancements.
