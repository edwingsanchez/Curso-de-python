from ultralytics import YOLO
import cv2

# Cargar modelo preentrenado (se descarga automáticamente)
model = YOLO("yolov8n.pt")  # versión ligera

# Iniciar cámara
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Ejecutar detección
    results = model(frame, stream=True)

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])

            # Clase 0 = persona en COCO dataset
            if cls == 0:
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                # Dibujar caja
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f'Person {conf:.2f}', 
                            (x1, y1 - 10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 
                            0.6, (0, 255, 0), 2)

    # Mostrar
    cv2.imshow("YOLOv8 Human Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()