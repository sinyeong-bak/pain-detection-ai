# pain-detection-ai
Emotion-based Pain Detection AI project

# 🎯 PainSense AI - 감정 기반 통증 감지 AI

## 📌 프로젝트 개요
- 환자의 얼굴 표정, 음성, 텍스트 데이터를 분석하여 **통증 강도 예측**
- **TensorFlow & PyTorch 기반 딥러닝 모델**을 활용하여 AI 구축
- **의료 도메인 적용**: 응급실, 중환자실, 요양병원 등에서 의사소통이 어려운 환자의 통증 감지

## 📊 데이터셋
- **UNBC-McMaster Shoulder Pain Dataset** (얼굴 표정 기반 통증 감지)
- **BioVid Heat Pain Database** (생체 신호 & 음성 기반 통증 감지)
- **Pain Audio Dataset** (음성 기반 감정 분석)

## 🔥 프로젝트 업데이트: 데이터셋 변경 및 해결책

초기 계획에서는 UNBC-McMaster 데이터셋을 사용하려 했으나, 접근 제한으로 인해 대체 데이터셋을 활용하기로 하였습니다.
- 얼굴 표정 분석 → **FER-2013** (Kaggle) 사용
- 음성 분석 → **Emotion Dataset** (Kaggle) 사용
- 텍스트 분석 → **AI 감성 챗봇 코퍼스** (AI-Hub) 사용

자세한 내용은 [문서 보기](docs/data_issue_and_solution.md).

## 🔧 기술 스택
- **Deep Learning Frameworks:** TensorFlow, PyTorch
- **Facial Expression Analysis:** CNN
- **Audio Emotion Analysis:** LSTM + MFCC
- **Text-based Sentiment Analysis:** NLP (Transformer, BERT)

## 🚀 프로젝트 진행 일정
- 📅 **Week 1:** 데이터셋 분석 및 전처리
- 📅 **Week 2:** 감정 분석 모델 구축 (표정, 음성, 텍스트)
- 📅 **Week 3:** 통합 통증 감지 모델 개발
- 📅 **Week 4:** 모델 성능 평가 및 결과 정리

## 🏥 의료 활용 가능성
- 통증을 인지하기 어려운 **노인, 어린이, 중환자**의 통증 감지 보조
- **AI 기반 의료 경고 시스템** 개발 가능

## 📂 프로젝트 구조
📁 pain-detection-ai 
├── 📁 data # 데이터셋 저장 
├── 📁 notebooks # Jupyter Notebook 코드 정리 
├── 📁 src # 메인 코드 
├── 📁 models # 학습된 모델 저장 
├── 📁 results # 결과 분석 
├── 📄 README.md # 프로젝트 설명 
├── 📄 requirements.txt # 필요 라이브러리 정리

## 📌 프로젝트 진행 과정 (업데이트)

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

📌 다음 단계: **CNN 모델 설계 & 구현**
