import cv2
from picamera2 import Picamera2
import os 



# Crear carpeta para guardar fotos si no existe
carpeta = "fotos"
os.makedirs(carpeta, exist_ok=True)

def stream_video():
    contador = 1
    picam = Picamera2()
    picam.preview_configuration.main.size=(500, 500)
    picam.preview_configuration.main.format="RGB888"
    picam.preview_configuration.align()
    picam.configure("preview")
    picam.start()

    while True:
        frame = picam.capture_array()
        cv2.imshow("picam", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord('s'):
            # Crear el nombre del archivo
            nombre_foto = os.path.join(carpeta, f"foto{contador}.jpg")
            cv2.imwrite(nombre_foto, frame)
            print(f"Foto guardada como {nombre_foto}")
            contador += 1  # Incrementar el contador

        # Salir si se presiona 'q'
        if key == ord('q'):
            break
    cv2.destroyAllWindows()

if _name_ == "_main_":
    stream_video()