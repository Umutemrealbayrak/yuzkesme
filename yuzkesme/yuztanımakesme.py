import cv2
import face_recognition

resim = cv2.imread("ataturk.jpeg")

abc = face_recognition.face_locations(resim, model="cnn")

for index, faceloc in enumerate(abc):
    toplefty, bottomrightx, bottomrighty, topleftx = faceloc
    detectedface = resim[toplefty:bottomrighty, topleftx:bottomrightx]

    cv2.rectangle(resim, (topleftx, toplefty), (bottomrightx, bottomrighty), (255, 0, 0), 3)

while True:
    cv2.imshow("kesilen", detectedface)
    cv2.imshow("org", resim)

    # Eğer 'q' tuşuna basılırsa döngüyü sonlandır
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.waitKey(0)
cv2.destroyAllWindows()
