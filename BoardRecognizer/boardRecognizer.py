import numpy as np
import cv2


class BoardRecognizer:

    def __init__(self):
        # Mask for filtering the board edges
        self.mask = dict()

    def getmask(self):
        return self.mask

    def setmask(self, mask):
        self.mask = mask

    def processframe(self, frame):
        # Smoothing
        frame = cv2.bilateralFilter(frame, 12, 50, 50)

        # Color space conversions
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Color filtering
        # was approximately 50 50 50
        lower_green = np.array([self.mask['H'] - 10, self.mask['S'] - 20, self.mask['V'] - 20])
        upper_green = np.array([self.mask['H'] + 10, 255, 255])

        mask = cv2.inRange(hsv, lower_green, upper_green)

        # copy the mask because findContours destroys the image
        thresh = mask.copy()
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Board vertexes
        points = []

        # Contour filter
        for contour in contours:
            area = cv2.contourArea(contour)
            # Make sure the area is of significant size (and not some random group of pixels)
            if area > 500:
                m = cv2.moments(contour)

                # FIXME We have no clue what this actually does..
                cx = int(m['m10']/m['m00'])
                cy = int(m['m01']/m['m00'])

                points.append((cx, cy))

        # If the board is found we can try and recognize the pieces
        if len(points) == 4:
            # FIXME make this more clear
            # Pick channel 1 (rGb, Green channel)
            gray = frame[:, :, 1]


            # FIXME Make this more efficient than sorting it thrice
            # Sort on x coordinate
            points.sort(key=lambda tup: tup[0])
            # Pick first 2
            lower = points[:2]

            # Sort on y coordinate
            lower.sort(key=lambda tup: tup[1])
            upper = points[2:]
            upper.sort(key=lambda tup: tup[1])
            points = lower + upper

            # Convert to numpy array
            points1 = np.float32(points)
            points2 = np.float32([[0, 0], [0, 400], [400, 0], [400, 400]])
            m = cv2.getPerspectiveTransform(points1, points2)

            board = cv2.warpPerspective(gray, m, (400, 400))

            return True, board
        else:
            # FIXME why must we pass 0 as second argument?
            return False, 0
