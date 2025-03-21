import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense, Dropout, LSTM, Bidirectional, Concatenate
from tensorflow.keras.layers import Conv1D, MaxPooling1D
from tensorflow.keras.optimizers import Adam

# ✅ CNN + LSTM 모델 정의
def create_cnn_lstm_model():
    # ✅ 이미지 입력 (CNN)
    image_input = Input(shape=(48, 48, 1), name="image_input")
    x = Conv2D(32, (3,3), activation='relu', padding='same')(image_input)
    x = MaxPooling2D((2,2))(x)
    x = Conv2D(64, (3,3), activation='relu', padding='same')(x)
    x = MaxPooling2D((2,2))(x)
    x = Flatten()(x)
    x = Dense(128, activation='relu')(x)
    x = Dropout(0.5)(x)
    image_features = x

    # ✅ 오디오 입력 (LSTM)
    audio_input = Input(shape=(40, 100), name="audio_input")
    y = Conv1D(64, kernel_size=3, activation='relu', padding='same')(audio_input)
    y = MaxPooling1D(pool_size=2)(y)
    y = Bidirectional(LSTM(64, return_sequences=True))(y)
    y = Bidirectional(LSTM(64))(y)
    audio_features = Dense(128, activation='relu')(y)

    # ✅ 이미지 + 오디오 특징 결합
    merged = Concatenate()([image_features, audio_features])
    z = Dense(128, activation='relu')(merged)
    z = Dropout(0.5)(z)
    output = Dense(4, activation='softmax')(z)

    # ✅ 최종 모델 생성
    model = Model(inputs=[image_input, audio_input], outputs=output)
    model.compile(loss='categorical_crossentropy', optimizer=Adam(learning_rate=0.0005), metrics=['accuracy'])

    return model

# ✅ 모델 생성 및 구조 확인
if __name__ == "__main__":
    model = create_cnn_lstm_model()
    model.summary()
