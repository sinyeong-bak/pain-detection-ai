import os
import librosa
import numpy as np

# ✅ CREMA-D 데이터 경로
AUDIO_PATH = "Processed_Audio/train"
PROCESSED_AUDIO_DIR = "processed_audio"
os.makedirs(PROCESSED_AUDIO_DIR, exist_ok=True)

# ✅ 오디오 전처리 함수 (MFCC 변환)
def preprocess_audio(file_path, max_length=100):
    audio, sr = librosa.load(file_path, sr=16000)  # 샘플링 속도 16kHz
    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=40)

    #고정된 길이로 패딩
    if mfcc.shape[1] < max_length:
        pad_width = max_length - mfcc.shape[1]
        mfcc = np.pad(mfcc, pad_width=((0, 0), (0, pad_width)), mode='constant')
    else:
        mfcc = mfcc[:, :max_length]  # 길이가 길면 자름

    return mfcc

# ✅ 감정 클래스별 오디오 데이터 전처리
for emotion in os.listdir(AUDIO_PATH):
    emotion_path = os.path.join(AUDIO_PATH, emotion)
    save_path = os.path.join(PROCESSED_AUDIO_DIR, emotion)
    os.makedirs(save_path, exist_ok=True)

    for file in os.listdir(emotion_path):
        file_path = os.path.join(emotion_path, file)
        processed_audio = preprocess_audio(file_path)

        # ✅ 전처리된 오디오 저장 (넘파이 배열 형태)
        np.save(os.path.join(save_path, file.replace(".wav", ".npy")), processed_audio)

print("✅ CREMA-D 음성 데이터 전처리 완료!")
