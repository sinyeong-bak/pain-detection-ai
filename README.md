# 🏥 Pain Detection AI
**Emotion-based Pain Detection AI using CNN & LSTM**

# 감정 기반 통증 감지 AI (PainSense AI)

## 프로젝트 개요
이 프로젝트는 **환자의 얼굴 표정과 음성 데이터를 분석하여 통증을 자동 감지하는 AI 모델**을 개발하는 프로젝트입니다.  
CNN과 LSTM을 결합하여 멀티모달 데이터를 처리하며, 모델 최적화를 통해 성능을 개선하는 과정을 거쳤습니다.  
## 📂 프로젝트 구조
 ```bash
pain-detection-ai/
│── models/                 # 다양한 모델 구조 저장
│── data/                   # 데이터셋 (Git 업로드 X)
│   ├── README.md           # 데이터 다운로드 경로 설명
│── scripts/                # 학습 및 평가 관련 코드
│   ├── train.py            # 모델 학습 코드
│   ├── evaluate.py         # 모델 평가 코드
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

## 실행 방법
1. **데이터 다운로드 및 전처리**
   ```bash
   python preprocess.py

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
- **불필요한 감정 클래스 제거**: `disgust`, `happy`
- **데이터 증강(Augmentation) 수행**: `surprise` 클래스 (3171개 → 4000개 이상)

### ✅ 2. 데이터 전처리
- **이미지 크기 조정**: 모든 이미지를 `48x48`로 변환
- **정규화(Normalization)**: 픽셀 값을 `[0,1]` 범위로 변환 (`/255.0`)
- **레이블 원-핫 인코딩**: `angry, fear, neutral, sad, surprise` (총 5개 클래스)
- **훈련(train), 검증(validation), 테스트(test) 데이터 분리** (8:1:1 비율)

### ✅ 3. 현재 상태
✔ **훈련 데이터:** `(17509, 48, 48, 1)`  
✔ **검증 데이터:** `(2189, 48, 48, 1)`  
✔ **테스트 데이터:** `(2189, 48, 48, 1)`

다음 단계: **CNN 모델 설계 & 구현**
---
## 프로젝트 진행 과정 (업데이트) 

## 모델 구조 실험 과정
### 🔹 1️⃣ **Baseline Model (기본 모델)**
- `models/baseline_model.py`
- 초기 CNN 모델을 사용하여 얼굴 표정 데이터만 분석
- `Accuracy: 0.65, F1-score: 0.58`

### 🔹 2️⃣ **CNN + LSTM 통합 모델**
- `models/cnn_lstm_model.py`
- 얼굴 표정 + 음성 데이터를 함께 분석하는 멀티모달 모델
- `Accuracy: 0.74, F1-score: 0.68`

### 🔹 3️⃣ **최적화된 모델**
- `models/optimized_model.py`
- Softmax/Sigmoid 전환, L2 정규화, Dropout 최적화
- `Accuracy: 0.85, F1-score: 0.79`

---

## 📊 실험 결과 및 분석
| Model Version       | Accuracy | F1-score | 주요 변경 사항 |
|--------------------|----------|----------|--------------|
| Baseline Model    | 0.65     | 0.58     | CNN만 사용 |
| CNN + LSTM        | 0.74     | 0.68     | 얼굴 표정 + 음성 데이터 통합 |
| Optimized Model   | 0.85     | 0.79     | Regularization, Hyperparameter Tuning |

---

## 📦 환경 설정
```bash
# 패키지 설치
pip install -r requirements.txt

