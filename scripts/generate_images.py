import numpy as np
import cv2


width = 800
height = 600

white = np.full((height, width),255, np.uint8)

# Draw a rectangle in the middle
cv2.rectangle(white, (width//4, height//4), (width//4*3, height//4*3), (0,0,0), -1)

# Draw a circle in bottom right corner
cv2.circle(white, (width//2 + 200, height//2 +210), 50, (0,0,0), -1)
cv2.imwrite('images/white.png', white)
cv2.imshow("white", white)
cv2.waitKey(0)