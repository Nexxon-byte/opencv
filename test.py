import requests
import pygame.camera
import pygame.image
import time
import io
from PIL import Image

# Define URL for API endpoint
url = "http://127.0.0.1:8000/api"

# Initialize pygame camera
pygame.camera.init()

# Initialize camera capture
cam = pygame.camera.Camera("/dev/video0", (640, 480))
cam.start()

while True:
    # Capture an image
    img = cam.get_image()

    # Wait for a short time before capturing another image
    time.sleep(0.3)

    # Convert image to JPEG format
    img_str = pygame.image.tostring(img, "RGB")
    img_jpg = Image.frombytes("RGB", (640, 480), img_str).convert("RGB")
    img_bytes = io.BytesIO()
    img_jpg.save(img_bytes, format='JPEG')
    img_bytes = img_bytes.getvalue()

    # Send image to API
    files = {'file': ('image.jpg', img_bytes)}
    r = requests.post(url, files=files)

    # Display response from API
    print(r.text)

# Clean up
cam.stop()
pygame.camera.quit()
