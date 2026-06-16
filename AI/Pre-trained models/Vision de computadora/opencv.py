import cv2

# Abrir la cámara (0 = cámara principal)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("No se pudo abrir la cámara")
    exit()

while True:
    # Leer frame
    ret, frame = cap.read()
    if not ret:
        print("No se pudo recibir el frame")
        break

    # Convertir a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar bordes con Canny
    edges = cv2.Canny(gray, 100, 200)

    # Mostrar resultados
    cv2.imshow('Video original', frame)
    cv2.imshow('Bordes', edges)

    # Salir con tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()