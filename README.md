# 🏥 Pain Detection AI
**Emotion-based Pain Detection AI using CNN & LSTM**

# 감정 기반 통증 감지 AI

## 프로젝트 개요
이 프로젝트는 최근 대한민국은 의료 인력 부족, 파업, 응급 대기 시간 증가 등으로 인해 **의료 서비스 접근성에 심각한 위기(의료 대란)**를 겪고 있습니다.
이러한 상황에서 한 명의 의료진이 더 많은 환자를 동시에 진료해야 하는 현실은 빠른 판단, 정확한 분류, 반복적 업무의 자동화를 필수적으로 요구합니다.

이 프로젝트는 AI가 환자의 통증을 먼저 감지해 정량화된 정보로 제공함으로써,
의료진이 보다 우선순위 높은 환자에게 집중할 수 있도록 돕고,
궁극적으로 진료 효율성과 환자 만족도를 동시에 향상시키기 위한 목적으로 기획되었습니다. 

## 📂 프로젝트 구조
 ```bash
pain-detection-ai/
│── models/                 # 다양한 모델 구조 저장
│    ├── baseline_model.py 
│    ├── cnn_lstm_model.py 
│    ├── optimized_model.py
│── data/                   # 데이터셋 (Git 업로드 X)
│   ├── README.md           # 데이터 다운로드 경로 설명
│── scripts/                # 학습 및 평가 관련 코드
│   ├── preprocessing/      # ✅ 데이터 전처리 관련 코드
│       ├── image_preprocessing.py  # 이미지 데이터 전처리
│       ├── audio_preprocessing.py  # 오디오 데이터 전처리
│── README.md               # 프로젝트 개요 설명
│── requirements.txt        # 필요한 패키지 정리
````


## 사용 데이터셋
- **[FER-2013](https://www.kaggle.com/datasets/msambare/fer2013)**
  - 감정이 포함된 얼굴 이미지 데이터셋 (Angry, Fear, Neutral, Sad)
- **[CREMA-D](https://github.com/CheyneyComputerScience/CREMA-D)**
  - 다양한 감정이 표현된 음성 데이터셋 (Angry, Fear, Neutral, Sad)

## ⚙️ 사용 기술
- **이미지 감정 분석:** CNN (Convolutional Neural Network)
- **음성 감정 분석:** LSTM + MFCC (Mel-Frequency Cepstral Coefficients)
- **멀티모달 통합:** CNN + LSTM 모델 결합
- **데이터 전처리:** OpenCV, Librosa, NumPy, Pandas
- **모델 학습:** TensorFlow, PyTorch

## 🛠 프로젝트 진행 과정
### ✅ 데이터 전처리 완료
- FER-2013 데이터셋에서 **4개 감정만 필터링 (Angry, Fear, Neutral, Sad)**
- CREMA-D 데이터셋에서 **텍스트 제외, 음성 데이터 전처리 (MFCC 변환)**
- CREMA-D 데이터셋의 **음성 데이터 증강 완료 (피치 변환, 속도 변화, 노이즈 추가)**
- FER-2013 및 CREMA-D의 **Train/Test 데이터 균형 조정 완료**

### 다음 목표: CNN + LSTM 모델 설계
- CNN을 활용하여 **얼굴 표정에서 감정 특징 추출**
- LSTM을 활용하여 **음성 데이터의 감정 특징 분석**
- **멀티모달 모델로 이미지와 음성을 함께 학습하는 방식 구현**

## 🔧 기술 스택
- **Deep Learning Frameworks:** TensorFlow, PyTorch
- **Facial Expression Analysis:** CNN
- **Audio Emotion Analysis:** LSTM + MFCC
- **Text-based Sentiment Analysis:** NLP (Transformer, BERT)

## 프로젝트 진행 일정
- 📅 **Week 1:** 데이터셋 분석 및 전처리
- 📅 **Week 2:** 감정 분석 모델 구축 (표정, 음성)
- 📅 **Week 3:** 통합 통증 감지 모델 개발
- 📅 **Week 4:** 모델 성능 평가 및 결과 정리

## 🏥 의료 활용 가능성
- 통증을 인지하기 어려운 **노인, 어린이, 중환자**의 통증 감지 보조
- **AI 기반 의료 경고 시스템** 개발 가능

## 프로젝트 진행 과정 (업데이트) 

### ✅ 1. 데이터 정리
- `FER-2013` 데이터셋을 활용하여 얼굴 표정 분석 기반 감정 인식 프로젝트 진행
- **불필요한 감정 클래스 제거**: `disgust`, `happy, surprise`
- **데이터 증강(Augmentation) 수행**: `surprise` 클래스 (3171개 → 4000개 이상)

### ✅ 2. 데이터 전처리
- **이미지 크기 조정**: 모든 이미지를 `48x48`로 변환
- **정규화(Normalization)**: 픽셀 값을 `[0,1]` 범위로 변환 (`/255.0`)
- **레이블 원-핫 인코딩**: `angry, fear, neutral, sad` (총 4개 클래스)
- **훈련(train), 테스트(test) 데이터 분리** (8:2 비율)

### ✅ 3. 현재 상태
✔ **훈련 데이터:** `(17509, 48, 48, 1)`  
✔ **검증 데이터:** `(2189, 48, 48, 1)`  
✔ **테스트 데이터:** `(2189, 48, 48, 1)`

다음 단계: **CNN 모델 설계 & 구현**
---
## 프로젝트 진행 과정 (업데이트) 

## 📊 모델 성능 결과 (Train & Test Performance)

| Model Version       | Train Accuracy | Test Accuracy | F1-score | 주요 변경 사항 |
|--------------------|---------------|--------------|----------|--------------|
| **CNN + LSTM 통합 모델** | 98.55% | 28.88% | 0.1304 | 얼굴 표정 + 음성 데이터 통합 |

✅ **Train Accuracy가 높지만 Test Accuracy가 낮아 Overfitting이 발생함.**  
✅ **현재 Regularization, Data Augmentation 등의 최적화 작업을 진행 중.**

---


### **이번 프로젝트를 통해 배운 점**

- 데이터 품질과 양이 모델 성능에 미치는 영향이 크다는 점을 깨달음
- 멀티모달 모델을 개발할 때, 서로 다른 데이터(이미지 & 오디오)를 병합할 때의 통일성이 중요함
- Overfitting을 해결하기 위한 다양한 기법(Regularization, Dropout, Data Augmentation 등)의 필요성을 체감함

---

## ✅ **다음 목표 (향후 계획)**

- Overfitting 해결을 위한 최적화 진행 (Regularization, Learning Rate Tuning 등 적용 예정)
- 실제 의료 환경에서 적용 가능성을 고려한 평가 방법 검토

## 📦 환경 설정
```bash
# 패키지 설치
pip install -r requirements.txt

