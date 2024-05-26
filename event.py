import cv2
import numpy as np
import random

# Load background image (replace with your desired image path)
bg_image = cv2.imread('tape.png')

# Load scissors image (replace with your desired image path)
scissors_image = cv2.imread('tape.png', cv2.IMREAD_UNCHANGED)  # Load with alpha channel

# Resize scissors image if needed
scissors_image = cv2.resize(scissors_image, (0, 0), fx=0.5, fy=0.5)  # Adjust resize factors as needed

# Create a red ribbon (adjust width and height as desired)
ribbon_width = 300
ribbon_height = 20
ribbon_color = (0, 0, 255)  # Red color
ribbon = np.zeros((ribbon_height, ribbon_width, 3), dtype=np.uint8)
cv2.rectangle(ribbon, (0, 0), (ribbon_width, ribbon_height), ribbon_color, -1)

# Randomly place the ribbon on the bottom of the background image
ribbon_y = bg_image.shape[0] - ribbon_height
ribbon_x = random.randint(0, bg_image.shape[1] - ribbon_width)

# Place the ribbon onto the background
bg_image[ribbon_y:ribbon_y + ribbon_height, ribbon_x:ribbon_x + ribbon_width] = ribbon

# Function to simulate cutting the ribbon (replace with your cutting animation logic)
def cut_ribbon(frame, scissors_image, ribbon_x, ribbon_y):
    # Simulate cutting animation (e.g., gradually remove ribbon pixels, move scissors)
    num_cuts = 20  # Adjust number of cuts for animation smoothness
    for i in range(num_cuts):
        cut_width = int(ribbon_width * (i / (num_cuts - 1)))
        bg_image[ribbon_y:ribbon_y + ribbon_height, ribbon_x:ribbon_x + cut_width] = (0, 0, 0)  # Simulate cutting by setting pixels to black
        # Optionally, move scissors image for a cutting animation effect

    # Place the scissors image on top of the cut ribbon
    mask = scissors_image[:, :, 3]  # Extract alpha channel from scissors image
    bg_image[ribbon_y:ribbon_y + scissors_image.shape[0], ribbon_x:ribbon_x + scissors_image.shape[1]] = \
        cv2.addWeighted(bg_image[ribbon_y:ribbon_y + scissors_image.shape[0], ribbon_x:ribbon_x + scissors_image.shape[1]], 1, scissors_image[:, :, :3], 1, 0, mask=mask)

# Display the initial scene with the uncut ribbon
cv2.imshow("Virtual Tape Cutting", bg_image)

# Press 'c' key to simulate the cutting ceremony
key = cv2.waitKey(0)
if key == ord('c'):
    cut_ribbon(bg_image.copy(), scissors_image.copy(), ribbon_x, ribbon_y)
    cv2.imshow("Virtual Tape Cutting (Cut)", bg_image)
    cv2.waitKey(0)

cv2.destroyAllWindows()
