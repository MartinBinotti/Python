import cv2

# Inicializar la cámara
camera = cv2.VideoCapture(0)

# Cargar el detector de rostros (Haar Cascade)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Cargar el detector de ojos (Haar Cascade)
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

while True:
    # Capturar un marco de la cámara
    ret, frame = camera.read()

    # Convertir el marco a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar rostros en el marco
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Dibujar un rectángulo alrededor de los rostros detectados
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Obtener la región de interés (ROI) del rostro
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Detectar ojos en la ROI
        eyes = eye_cascade.detectMultiScale(roi_gray)

        # Dibujar un rectángulo alrededor de los ojos detectados
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
