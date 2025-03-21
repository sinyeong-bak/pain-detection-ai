# 📂 Data Folder

이 폴더는 **모델 학습에 필요한 데이터셋을 저장하는 곳**입니다.  
**GitHub 저장소에는 데이터셋을 직접 업로드하지 않습니다.**  

---

## 📥 데이터 다운로드 방법

이 프로젝트에서는 **FER-2013 (얼굴 이미지 데이터셋)**과 **CREMA-D (음성 데이터셋)**을 사용합니다.  
아래 링크를 통해 데이터셋을 다운로드한 후, `data/` 폴더에 정리해주세요.

---

### 1️⃣ **FER-2013 - 감정이 포함된 얼굴 이미지 데이터셋**
🔗 [데이터셋 다운로드](https://www.kaggle.com/datasets/msambare/fer2013)  

📌 **데이터셋 설명:**  
FER-2013은 다양한 감정을 담고 있는 **48x48 픽셀 흑백 얼굴 이미지 데이터셋**입니다.  
이 프로젝트에서는 `Angry`, `Fear`, `Neutral`, `Sad` 감정만을 사용합니다.  

📥 **데이터 정리 방법**  
1. Kaggle에서 `fer2013.csv` 파일을 다운로드  
2. `data/fer2013/` 폴더를 만들고 CSV 파일을 저장  
```bash
mkdir -p data/fer2013
mv fer2013.csv data/fer2013/
```

### 2️⃣ **CREMA-D - 감정이 표현된 음성 데이터셋**
🔗 [데이터셋 다운로드](https://github.com/CheyneyComputerScience/CREMA-D)

📌 **데이터셋 설명:**  
CREMA-D는 배우들이 다양한 감정을 표현하며 읽은 **음성 데이터셋**입니다.  
이 프로젝트에서는 **`Angry`, `Fear`, `Neutral`, `Sad`** 감정만을 사용합니다.

---

📥 **데이터 정리 방법**
1. **CREMA-D GitHub 페이지**에서 `AudioWAV.zip` 파일을 다운로드합니다.
2. 압축을 풀고 `data/crema-d/` 폴더를 생성하여 음성 파일을 저장합니다.

```bash
mkdir -p data/crema-d
mv AudioWAV/* data/crema-d/
