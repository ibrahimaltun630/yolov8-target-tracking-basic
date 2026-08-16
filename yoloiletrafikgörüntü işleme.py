import cv2
from ultralytics import YOLO

# YOLOv8 Nano modelini yükle (ilk çalışmada otomatik indirir)
model = YOLO("yolov8n.pt")

# Videoyu veya Kamerayı (0) başlat
cap = cv2.VideoCapture("trafik_videosu.mp4")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # Görüntüyü modele ver, sadece arabaları (classes=[2]) tespit et
    results = model(frame, classes=[2])
    
    # Sonuçların içindeki kutu koordinatlarını al
    boxes = results[0].boxes

    for box in boxes:
        # Kutunun koordinatlarını integer olarak al
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        
        # Merkez noktasını hesapla
        center_x = int((x1 + x2) / 2)
        center_y = int((y1 + y2) / 2)

for box in boxes:
        # Kutunun koordinatlarını integer olarak al
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        
        # Merkez noktasını hesapla
        center_x = int((x1 + x2) / 2)
        center_y = int((y1 + y2) / 2)

# Opsiyonel: Hedefin etrafına kutu çiz
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

        # Merkez noktasına artı (crosshair) çiz (Yeşil renk: 0, 255, 0)
        cv2.drawMarker(frame, (center_x, center_y), (0, 255, 0), 
                       markerType=cv2.MARKER_CROSS, markerSize=20, thickness=2)

    # İşlenmiş görüntüyü ekranda göster
    cv2.imshow("Hedef Kilitlenme Sistemi", frame)

    # Çıkmak için 'q' tuşuna basılmasını bekle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()