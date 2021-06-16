import numpy as np
import cv2

cap = cv2.VideoCapture(0)

rect = None

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    qrCodeDetector = cv2.QRCodeDetector()
    decodedText, points, _ = qrCodeDetector.detectAndDecode(frame)

    if decodedText:
        rect = (tuple(points[0][1]), tuple(points[0][3]))
        print(decodedText, rect)
        
    if rect is not None:
        cv2.rectangle(frame, rect[0], rect[1], (0,255,0), 3)

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
