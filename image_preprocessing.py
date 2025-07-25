import cv2
import numpy as np
import os

# 이미지 폴더 경로
img_dir = r"C:\Users\양세진\OneDrive\바탕 화면\화재 데이터셋\train\images"
output_dir = "preprocessed_samples"
os.makedirs(output_dir, exist_ok=True)

# 처리할 이미지 수
max_samples = 5
processed_count = 0

for filename in os.listdir(img_dir):
    if not filename.endswith(".jpg"):
        continue

    path = os.path.join(img_dir, filename)
    img = cv2.imread(path)

    if img is None:
        continue

    # 1. HSV 변환 후 빨간색 필터
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([179, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 + mask2

    # 🔍 컨투어 기반 객체 크기 확인
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if all(cv2.contourArea(c) < 500 for c in contours):
        continue  # 너무 작으면 건너뜀

    # 2. Grayscale + 밝기 검사
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if np.mean(gray) < 40:
        continue  # 너무 어두우면 건너뜀

    # 3. 크기 조정 (224x224)
    img_resized = cv2.resize(img, (224, 224))

    # 4. Grayscale 변환 + Normalize
    gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
    normalized = gray / 255.0

    # 5. 노이즈 제거
    blurred = cv2.GaussianBlur(normalized, (5, 5), 0)

    # 6. 데이터 증강: 좌우 반전, 회전, 색상 변화
    flipped = cv2.flip(img_resized, 1)  # 좌우 반전
    rotated = cv2.rotate(img_resized, cv2.ROTATE_90_CLOCKWISE)

    # 저장
    save_path = os.path.join(output_dir, f"processed_{processed_count}.jpg")
    cv2.imwrite(save_path, img_resized)
    processed_count += 1

    if processed_count >= max_samples:
        break

print(f"총 {processed_count}장 전처리 이미지 저장 완료 ✅")
