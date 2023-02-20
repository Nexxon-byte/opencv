import requests
import io
import time
import picamera

# Öffnen der Kamera und Konfiguration der Auflösung
width = 640
height = 480

camera = picamera.PiCamera(resolution=(width, height))

# Schleife zum Lesen von Frames aus der Kamera und Senden an den Server
while True:
    # Lesen des aktuellen Frames aus der Kamera
    stream = io.BytesIO()
    camera.capture(stream, format='jpeg', use_video_port=True)
    img_bytes = stream.getvalue()

    # Definieren des API-Endpunkts des Servers und der zu sendenden Daten
    url = 'http://92.168.1.93:8000/api'
    files = {'image': ('image.jpg', img_bytes)}

    # Senden der Daten an den Server
    response = requests.post(url, files=files)

    # Drucken der Server-Antwort, falls vorhanden
    if response.content:
        print(response.content)

    # Warten auf Tastendruck zum Beenden der Schleife
    time.sleep(0.3)
