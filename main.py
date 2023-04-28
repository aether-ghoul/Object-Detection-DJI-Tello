import cv2
import numpy

kernel = numpy.ones((5 ,5), numpy.uint8)
#print("Before URL")
cap = cv2.VideoCapture(0)
#print("After URL")


def process(img):

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (11, 11), 0)
    (thresh, img_bw) = cv2.threshold(img_blur, 80, 255, cv2.THRESH_BINARY_INV)

    opening = cv2.morphologyEx(img_bw, cv2.MORPH_OPEN, kernel)

    x, y, w, h = cv2.boundingRect(opening)

    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
    cv2.circle(frame, (x + w / 2, y + h / 2), 5, (0, 0, 255), -1)

    return img_bw


def contour_area(contours):

    cnt_area = []

    for i in range(0, len(contours), 1):
        cnt_area.append(cv2.contourArea(contours[i]))

    list.sort(cnt_area, reverse=True)

    return cnt_area


def draw_bounding_box(contours, image, number_of_boxes=1):

    cnt_area = contour_area(contours)

    for i in range(0, len(contours), 1):
        cnt = contours[i]
        if (cv2.contourArea(cnt) > cnt_area[number_of_boxes]):
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
            x = round(x+w/2)
            y = round(y+h/2)
            cv2.circle(image, (x, y), 5, (0, 0, 255), -1)

    return image



while True:

    #print('About to start the Read command')
    ret, frame = cap.read()
    img = frame
    #contours, hierarchy = cv2.findContours(process(img), 1, 2)
    #img = draw_bounding_box(contours, img)

    #print('About to show frame of Video.')
    cv2.imshow("Capturing", img)
    #print('Running..')

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()