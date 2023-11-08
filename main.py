import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

colors = {
    "lightBlue":(210,228),
    "Red": (0, 15),
    "Orange": (16, 30),
    "Yellow": (31, 45),
    "Green": (46, 75),
    "Blue": (76, 130),
    "Purple": (131, 160),
    "Pink": (161, 175),
    "Red": (176, 179),
}

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape
    cx = int(width / 2)
    cy = int(height / 2)

    hue, sat, value = hsv_frame[cy, cx]
    color = "Undefined"

    for name, (lower, upper) in colors.items():
        if lower <= hue <= upper:
            color = name
            break

    if sat < 40:
        color = "Gray"
    if value < 40:
        color = "Black"
    if value > 200:
        color = "White"

    cv2.putText(frame, color, (200, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2)
    cv2.circle(frame, (cx, cy), 5, (255, 0, 0), 3)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
