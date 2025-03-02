# 📌 문제 및 해결 방법 정리

## 🚨 문제: 통증 감지 데이터셋의 접근 제한
본 프로젝트는 감정 기반 통증 감지 AI를 개발하는 것이 목표였습니다.  
하지만 원래 사용하려 했던 **UNBC-McMaster Shoulder Pain Dataset**이 더 이상 공개적으로 제공되지 않으며,  
다른 통증 감지 데이터셋(BioVid Heat Pain 등)도 연구 기관을 통한 요청이 필요하여 사용이 불가능했습니다.

## 🔍 해결 방법: 공개 데이터셋을 활용한 대체 전략
승인 없이 다운로드 가능한 공개 데이터셋을 찾아 기존 계획을 수정하였습니다.

### 📌 데이터셋 변경 사항

| 분석 대상  | 기존 계획 (불가능)      | 변경 후 대체 데이터셋 |
|-----------|----------------|----------------|
| 얼굴 표정 분석 | UNBC-McMaster | [FER-2013](https://www.kaggle.com/datasets/msambare/fer2013) |
| 음성 분석 | BioVid Heat Pain | [Emotion Dataset (Kaggle)](https://www.kaggle.com/datasets/seungjunlim/emotion-dataset-audio) |
| 텍스트 분석 | Pain Text Corpus | [AI 감성 챗봇 코퍼스 (AI-Hub)](https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=279) |

## ⚙ 데이터 전처리 및 활용 방법

### ✅ 얼굴 표정 데이터 (FER-2013)
- **전처리:** OpenCV를 활용한 얼굴 크롭, 정규화, 데이터 증강(Augmentation) 적용
- **활용 방식:** CNN 모델로 감정 분석 후, **"슬픔", "공포", "분노"를 통증 감지 데이터로 변환**

### ✅ 음성 데이터 (Emotion Dataset - Kaggle)
- **전처리:** MFCC 변환, 노이즈 제거
- **활용 방식:** CNN + LSTM 기반 음성 감정 모델 학습 후 **통증 관련 음성 패턴 학습**

### ✅ 텍스트 데이터 (AI 감성 챗봇 코퍼스 - AI-Hub)
- **전처리:** 한글 텍스트 정제, 토큰화(BERT Tokenizer) 적용
- **활용 방식:** Transformer 기반 감정 분석 후 **"불안", "슬픔"을 통증과 연결하여 분석**

## 📌 정리 및 업데이트
이제 새로운 데이터셋을 기반으로 모델을 설계하고, 프로젝트를 진행할 수 있습니다.

📍 추가 정보는 [README.md](../README.md)에서 확인할 수 있습니다.
