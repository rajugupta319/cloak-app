import cv2
import numpy as np
import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av

st.title("Blue Invisibility Cloak")
st.write("Step out of the frame! The app will capture the background for the first few seconds.")

class CloakProcessor:
    def __init__(self):
        self.background = None
        self.frame_count = 0

    def recv(self, frame):
        # Convert web frame to OpenCV format
        img = frame.to_ndarray(format="bgr24")
        img = np.flip(img, axis=1)

        # 1. Capture the background for the first 50 frames (~2-3 seconds)
        if self.frame_count < 50:
            self.background = img
            self.frame_count += 1
            # Show a countdown/status on the screen
            cv2.putText(img, f"Capturing Background: {self.frame_count}/50", 
                        (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            return av.VideoFrame.from_ndarray(img, format="bgr24")

        # 2. Cloak Logic (Runs after background is captured)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        
        lower_blue = np.array([90, 80, 80])
        upper_blue = np.array([130, 255, 255])
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        
        kernel = np.ones((3, 3), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)
        mask_inv = cv2.bitwise_not(mask)
        
        background_part = cv2.bitwise_and(self.background, self.background, mask=mask)
        current_part = cv2.bitwise_and(img, img, mask=mask_inv)
        final_output = cv2.addWeighted(background_part, 1, current_part, 1, 0)

        # Convert back to web frame
        return av.VideoFrame.from_ndarray(final_output, format="bgr24")

# Start the webcam stream
webrtc_streamer(key="invisibility-cloak", video_processor_factory=CloakProcessor)