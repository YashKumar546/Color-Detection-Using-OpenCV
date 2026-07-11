# pip install opencv-python pandas numpy

import argparse
import os
import cv2
import pandas as pd
import numpy as np
import sys

# ==========================================
# Command-Line Arguments
# ==========================================

parser = argparse.ArgumentParser(description='Detect and name colors from an image.')
parser.add_argument('image', nargs='?', default='pic1.jpg', help='Image file to open (pic1.jpg, pic2.jpg, pic3.jpg, etc.)')
parser.add_argument('--csv', default='colors.csv', help='CSV file containing color definitions')
args = parser.parse_args()

IMAGE_PATH = args.image
CSV_PATH = args.csv

if not os.path.exists(IMAGE_PATH):
    print(f"Error: image file not found: {IMAGE_PATH}")
    sys.exit(1)

if not os.path.exists(CSV_PATH):
    print(f"Error: CSV file not found: {CSV_PATH}")
    sys.exit(1)

# ==========================================
# Load Color Database
# ==========================================

index = ['color', 'color_name', 'hex', 'R', 'G', 'B']

try:
    df = pd.read_csv(CSV_PATH, names=index, header=None)
except FileNotFoundError:
    print("Error: colors.csv not found!")
    sys.exit()

# ==========================================
# Load Image
# ==========================================

img = cv2.imread(IMAGE_PATH)

if img is None:
    print("Error: Image not found!")
    sys.exit()

img = cv2.resize(img, (800, 600))

# ==========================================
# Global Variables
# ==========================================

clicked = False
r = g = b = 0

# ==========================================
# Function: Find Nearest Color Name
# ==========================================

def get_color_name(R, G, B):

    minimum = float("inf")
    cname = "Unknown"

    for i in range(len(df)):

        d = (
            abs(R - int(df.loc[i, 'R'])) +
            abs(G - int(df.loc[i, 'G'])) +
            abs(B - int(df.loc[i, 'B']))
        )

        if d < minimum:
            minimum = d
            cname = df.loc[i, 'color_name']

    return cname

# ==========================================
# Mouse Callback Function
# ==========================================

def mouse_callback(event, x, y, flags, param):

    global clicked, r, g, b

    if event == cv2.EVENT_LBUTTONDBLCLK:

        clicked = True

        blue, green, red = img[y, x]

        b = int(blue)
        g = int(green)
        r = int(red)

# ==========================================
# Empty Function for Trackbars
# ==========================================

def nothing(x):
    pass

# ==========================================
# Create Windows
# ==========================================

cv2.namedWindow("HSV Controls")
cv2.namedWindow("Image")

cv2.setMouseCallback("Image", mouse_callback)

# ==========================================
# HSV Trackbars
# ==========================================

cv2.createTrackbar("H Min", "HSV Controls", 0, 179, nothing)
cv2.createTrackbar("H Max", "HSV Controls", 179, 179, nothing)

cv2.createTrackbar("S Min", "HSV Controls", 0, 255, nothing)
cv2.createTrackbar("S Max", "HSV Controls", 255, 255, nothing)

cv2.createTrackbar("V Min", "HSV Controls", 0, 255, nothing)
cv2.createTrackbar("V Max", "HSV Controls", 255, 255, nothing)

# ==========================================
# Main Loop
# ==========================================

while True:

    display = img.copy()

    # Convert image to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Read Trackbar Values
    h_min = cv2.getTrackbarPos("H Min", "HSV Controls")
    h_max = cv2.getTrackbarPos("H Max", "HSV Controls")

    s_min = cv2.getTrackbarPos("S Min", "HSV Controls")
    s_max = cv2.getTrackbarPos("S Max", "HSV Controls")

    v_min = cv2.getTrackbarPos("V Min", "HSV Controls")
    v_max = cv2.getTrackbarPos("V Max", "HSV Controls")

    # Create HSV Mask
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(hsv, lower, upper)

    # Extract Selected Colors
    result = cv2.bitwise_and(img, img, mask=mask)

    # --------------------------------------

    if clicked:

        # Convert clicked pixel to HSV
        pixel = np.uint8([[[b, g, r]]])
        hsv_pixel = cv2.cvtColor(pixel, cv2.COLOR_BGR2HSV)

        h, s, v = hsv_pixel[0][0]

        color_name = get_color_name(r, g, b)

        text = (
            f"{color_name} | "
            f"RGB({r}, {g}, {b}) | "
            f"HSV({h}, {s}, {v})"
        )

        # Draw Color Banner
        cv2.rectangle(
            display,
            (20, 20),
            (display.shape[1] - 20, 70),
            (b, g, r),
            -1
        )

        # Select Text Color
        text_color = (0, 0, 0) if (r + g + b) > 600 else (255, 255, 255)

        cv2.putText(
            display,
            text,
            (30, 55),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            text_color,
            2
        )

    # --------------------------------------

    cv2.imshow("Image", display)
    cv2.imshow("Mask", mask)
    cv2.imshow("Detected Color", result)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('r'):
        clicked = False

    elif key == 27:   # ESC
        break

cv2.destroyAllWindows()