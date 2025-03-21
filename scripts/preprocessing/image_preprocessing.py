import os
import cv2
import numpy as np

# ✅ FER-2013 데이터셋 경로
FER_PATH = "fer2013"

# ✅ 전처리된 데이터 저장 폴더
PROCESSED_IMG_DIR = "processed_images"
os.makedirs(PROCESSED_IMG_DIR, exist_ok=True)

# ✅ 이미지 전처리 함수
def preprocess_image(img_path):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (48, 48))  # FER-2013은 48x48 픽셀
    img = img / 255.0  # 정규화
    return img

# ✅ 감정 클래스별 이미지 전처리
for folder in ["train", "test"]:
    input_folder = os.path.join(FER_PATH, folder)
    output_folder = os.path.join(PROCESSED_IMG_DIR, folder)
    os.makedirs(output_folder, exist_ok=True)

    for emotion in os.listdir(input_folder):
        emotion_path = os.path.join(input_folder, emotion)
        save_path = os.path.join(output_folder, emotion)
        os.makedirs(save_path, exist_ok=True)

        for img_file in os.listdir(emotion_path):
            img_path = os.path.join(emotion_path, img_file)
            processed_img = preprocess_image(img_path)

            # ✅ 전처리된 이미지 저장 (넘파이 배열 형태)
            np.save(os.path.join(save_path, img_file.replace(".jpg", ".npy")), processed_img)

print("✅ FER-2013 이미지 데이터 전처리 완료!")

