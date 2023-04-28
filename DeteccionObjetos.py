import numpy
import cv2

kernel = numpy.ones((5, 5), numpy.uint8)
cap = cv2.VideoCapture(0)

def process(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (11, 11), 0)
    (thresh, img_bw) = cv2.threshold(img_blur, 50, 255, cv2.THRESH_BINARY_INV)
    return img_bw

def contour_area(contours):
 cnt_area = []
    for i in range(0, len(contours), 1):
        cnt_area.append(cv2.contourArea(contours[i]))
    list.sort(cnt_area, reverse=True)
    return cnt_area

def draw_bounding_box(contours, img):
    draw_grid(img)
    fuente = 2
    escala = 0.8
    colorPunto = (0, 255, 0)
    colorTexto = (0, 0, 255)
    grosor = 5
    x = 0
    y = 0
    w = 640
    h = 480

    Area1 = (x, w * 1 // 4, y, h * 1 // 4)
    Area2 = (w * 1 // 4, w * 2 // 4, y, h * 1 // 4)
    Area3 = (w * 2 // 4, w * 3 // 4, y, h * 1 // 4)
    Area4 = (w * 3 // 4, w, y, h * 1 // 4)
    Area5 = (x, w * 1 // 4, h * 1 // 4, h * 2 // 4)
    Area6 = (w * 3 // 4, w, h * 1 // 4, h * 2 // 4)
    Area7 = (x, w * 1 // 4, h * 2 // 4, h * 3 // 4)
    Area8 = (w * 3 // 4, w, h * 2 // 4, h * 3 // 4)
    Area9 = (x, w * 1 // 4, h * 3 // 4, h)
    Area10 = (w * 1 // 4, w * 2 // 4, h * 3 // 4, h)
    Area11 = (w * 2 // 4, w * 3 // 4, h * 3 // 4, h)
    Area12 = (w * 3 // 4, w, h * 3 // 4, h)
    Area13 = (w * 1 // 4, w * 3 // 4, h * 1 // 4, h * 3 // 4)

    for i in range(0, len(contours), 1):
        cnt = contours[i]
        x1, y1, w1, h1 = cv2.boundingRect(cnt)
        area = w1 * h1
        if area >= 10000:
            if area <= 100000:
                cv2.rectangle(img, (x1, y1), (x1 + w1, y1 + h1), (200, 0, 200), 2)
                cx = x1 + w1 // 2
                cy = y1 + h1 // 2
                puntos = (x1, y1, cx, y1, x1 + w1, y1, x1, cy, cx, cy, x1 + w1, cy, x1, y1 + h1, cx, y1 + h1, x1 + w1, y1 + h1)

                for i in range(0, 17, 2):
                    if puntos[i] >= Area1[0] and puntos[i] <= Area1[1] and puntos[i+1] >= Area1[2] and puntos[i+1] <= Area1[3]:
                        cv2.putText(img, "1", (puntos[i], puntos[i+1]), fuente, escala, colorTexto)
                        cv2.circle(img, (puntos[i], puntos[i+1]), grosor, colorPunto, cv2.FILLED)

                    if puntos[i] >= Area2[0] and puntos[i] <= Area2[1] and puntos[i+1] >= Area2[2] and puntos[i+1] <= Area2[3]:
                        cv2.putText(img, "2", (puntos[i], puntos[i+1]), fuente, escala, colorTexto)
                        cv2.circle(img, (puntos[i], puntos[i+1]), grosor, colorPunto, cv2.FILLED)

                    if puntos[i] >= Area3[0] and puntos[i] <= Area3[1] and puntos[i+1] >= Area3[2] and puntos[i+1] <= Area3[3]:
                        cv2.putText(img, "3", (puntos[i], puntos[i+1]), fuente, escala, colorTexto)
                        cv2.circle(img, (puntos[i], puntos[i+1]), grosor, colorPunto, cv2.FILLED)

                    if puntos[i] >= Area4[0] and puntos[i] <= Area4[1] and puntos[i+1] >= Area4[2] and puntos[i+1] <= Area4[3]:
                        cv2.putText(img, "4", (puntos[i], puntos[i+1]), fuente, escala, colorTexto)
                        cv2.circle(img, (puntos[i], puntos[i+1]), grosor, colorPunto, cv2.FILLED)

                    if puntos[i] >= Area5[0] and puntos[i] <= Area5[1] and puntos[i+1] >= Area5[2] and puntos[i+1] <= Area5[3]:
                        cv2.putText(img, "5", (puntos[i], puntos[i+1]), fuente, escala, colorTexto)
                        cv2.circle(img, (puntos[i], puntos[i+1]), grosor, colorPunto, cv2.FILLED)

                    if puntos[i] >= Area6[0] and puntos[i] <= Area6[1] and puntos[i+1] >= Area6[2] and puntos[i+1] <= Area6[3]:
                        cv2.putText(img, "6", (puntos[i], puntos[i+1]), fuente, escala, colorTexto)
                        cv2.circle(img, (puntos[i], puntos[i+1]), grosor, colorPunto, cv2.FILLED)

                    if puntos[i] >= Area7[0] and puntos[i] <= Area7[1] and puntos[i+1] >= Area7[2] and puntos[i+1] <= Area7[3]:
                        cv2.putText(img, "7", (puntos[i], puntos[i+1]), fuente, escala, colorTexto)
                        cv2.circle(img, (puntos[i], puntos[i+1]), grosor, colorPunto, cv2.FILLED)

                    if puntos[i] >= Area8[0] and puntos[i] <= Area8[1] and puntos[i+1] >= Area8[2] and puntos[i+1] <= Area8[3]:
                        cv2.putText(img, "8", (puntos[i], puntos[i+1]), fuente, escala, colorTexto)
                        cv2.circle(img, (puntos[i], puntos[i+1]), grosor, colorPunto, cv2.FILLED)

                    if puntos[i] >= Area9[0] and puntos[i] <= Area9[1] and puntos[i+1] >= Area9[2] and puntos[i+1] <= Area9[3]:
                        cv2.putText(img, "9", (puntos[i], puntos[i+1]), fuente, escala, colorTexto)
                        cv2.circle(img, (puntos[i], puntos[i+1]), grosor, colorPunto, cv2.FILLED)

                    if puntos[i] >= Area10[0] and puntos[i] <= Area10[1] and puntos[i+1] >= Area10[2] and puntos[i+1] <= Area10[3]:
                        cv2.putText(img, "10", (puntos[i], puntos[i+1]), fuente, escala, colorTexto)
                        cv2.circle(img, (puntos[i], puntos[i+1]), grosor, colorPunto, cv2.FILLED)

                    if puntos[i] >= Area11[0] and puntos[i] <= Area11[1] and puntos[i+1] >= Area11[2] and puntos[i+1] <= Area11[3]:
                        cv2.putText(img, "11", (puntos[i], puntos[i+1]), fuente, escala, colorTexto)
                        cv2.circle(img, (puntos[i], puntos[i+1]), grosor, colorPunto, cv2.FILLED)

                    if puntos[i] >= Area12[0] and puntos[i] <= Area12[1] and puntos[i+1] >= Area12[2] and puntos[i+1] <= Area12[3]:
                        cv2.putText(img, "12", (puntos[i], puntos[i+1]), fuente, escala, colorTexto)
                        cv2.circle(img, (puntos[i], puntos[i+1]), grosor, colorPunto, cv2.FILLED)

                    if puntos[i] >= Area13[0] and puntos[i] <= Area13[1] and puntos[i+1] >= Area13[2] and puntos[i+1] <= Area13[3]:
                        cv2.circle(img, (puntos[i], puntos[i+1]), grosor, colorTexto, cv2.FILLED)
    return img

def draw_grid(img):
    x = 0
    y = 0
    w = 640
    h = 480
    color = (0, 125, 255)
    stroke = 2
    cv2.line(img, (x, y), (w, y), color, stroke)  # L1
    cv2.line(img, (w, y), (w, h), color, stroke)  # L2
    cv2.line(img, (w, h), (x, h), color, stroke)  # L3
    cv2.line(img, (x, y), (x, h), color, stroke)  # L4
    cv2.line(img, (w * 1//4, y), (w * 1//4, h), color, stroke)  # L5
    cv2.line(img, (w * 3//4, y), (w * 3//4, h), color, stroke)  # L6
    cv2.line(img, (x, h * 1//4), (w, h * 1//4), color, stroke)  # L7
    cv2.line(img, (x, h * 3//4), (w, h * 3//4), color, stroke)  # L8
    cv2.line(img, (w * 2//4, y), (w * 2//4, h * 1//4), color, stroke)  # L9
    cv2.line(img, (w * 2//4, h * 3//4), (w * 2//4, h), color, stroke)  # L10
    cv2.line(img, (x, h * 2//4), (w * 1//4, h * 2//4), color, stroke)  # L11
    cv2.line(img, (w * 3//4, h * 2//4), (w, h * 2//4), color, stroke)  # L12
    return img

while True:
    ret, frame = cap.read()
    img = frame
    img = cv2.resize(img, (640, 480))
    img_bw = process(img)
    contours, hierarchy = cv2.findContours(img_bw, 1, 2)
    img = draw_bounding_box(contours, img)
    cv2.imshow("imagen", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
