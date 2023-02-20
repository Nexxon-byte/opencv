import requests
import cv2

# Öffnen der Kamera und Konfiguration der Auflösung
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Schleife zum Lesen von Frames aus der Kamera und Senden an den Server
while True:
    # Lesen des aktuellen Frames aus der Kamera
    ret, frame = cap.read()

    # Konvertieren des Frames in ein Byte-Array
    ret, buffer = cv2.imencode('.jpg', frame)
    jpg_as_text = buffer.tobytes()

    # Definieren des API-Endpunkts des Servers und der zu sendenden Daten
    url = 'http://localhost:8000/api'
    files = {'image': ('image.jpg', jpg_as_text)}

    # Senden der Daten an den Server und Warten auf die Antwort
    response = None
    while not response:
        response = requests.post(url, files=files)

    # Drucken der Server-Antwort
    print(response.text)

    # Warten auf Tastendruck zum Beenden der Schleife
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Freigabe der Kamera und Schließen des Skripts
cap.release()
cv2.destroyAllWindows()
