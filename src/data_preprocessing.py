import os
import numpy as np
import cv2
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split

# 데이터셋 경로 설정
data_dir = "data/train"

# 사용할 감정 클래스
classes = ["angry", "fear", "neutral", "sad", "surprise"]
num_classes = len(classes)

# 데이터 저장 리스트
X, y = [], []

# 데이터 로드 및 전처리
for label, class_name in enumerate(classes):
    class_path = os.path.join(data_dir, class_name)
    
    for img_name in os.listdir(class_path):
        img_path = os.path.join(class_path, img_name)
        
        # 이미지 로드 (Grayscale, 48x48 변환)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (48, 48))  # 크기 조정
        img = img / 255.0  # 정규화
        
        X.append(img)
        y.append(label)

# NumPy 배열 변환
X = np.array(X).reshape(-1, 48, 48, 1)  # CNN 입력 형태 (N, 48, 48, 1)
y = np.array(y)

# 원-핫 인코딩 적용
y = to_categorical(y, num_classes=num_classes)

# 훈련/검증/테스트 세트 분리
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42, stratify=y_temp)

# 데이터 크기 확인
print(f"✅ 훈련 데이터: {X_train.shape}, 레이블: {y_train.shape}")
print(f"✅ 검증 데이터: {X_val.shape}, 레이블: {y_val.shape}")
print(f"✅ 테스트 데이터: {X_test.shape}, 레이블: {y_test.shape}")
