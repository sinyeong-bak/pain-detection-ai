import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense, Dropout, LSTM, Bidirectional, Concatenate, BatchNormalization
from tensorflow.keras.layers import Conv1D, MaxPooling1D
from tensorflow.keras.regularizers import l2
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.optimizers.schedules import ExponentialDecay

# ✅ 최적화된 CNN + LSTM 모델 정의
def create_optimized_model():
    # ✅ 이미지 입력 (CNN 개선)
    image_input = Input(shape=(48, 48, 1), name="image_input")
    x = Conv2D(64, (3,3), activation='relu', padding='same', kernel_regularizer=l2(0.01))(image_input)
    x = BatchNormalization()(x)
    x = MaxPooling2D((2,2))(x)
    x = Conv2D(128, (3,3), activation='relu', padding='same', kernel_regularizer=l2(0.01))(x)
    x = BatchNormalization()(x)
    x = MaxPooling2D((2,2))(x)
    x = Flatten()(x)
    x = Dense(128, activation='relu')(x)
    x = Dropout(0.3)(x)  # ✅ Dropout 최적화
    image_features = x

    # ✅ 오디오 입력 (LSTM 개선)
    audio_input = Input(shape=(40, 100), name="audio_input")
    y = Conv1D(64, kernel_size=3, activation='relu', padding='same', kernel_regularizer=l2(0.01))(audio_input)
    y = MaxPooling1D(pool_size=2)(y)
    y = Bidirectional(LSTM(64, return_sequences=True))(y)
    y = Bidirectional(LSTM(64))(y)
    y = Dense(128, activation='relu')(y)
    audio_features = Dropout(0.3)(y)  # ✅ Dropout 적용

    # ✅ 이미지 + 오디오 특징 결합
    merged = Concatenate()([image_features, audio_features])
    z = Dense(128, activation='relu')(merged)
    z = Dropout(0.3)(z)
    output = Dense(4, activation='softmax')(z)

    # ✅ Learning Rate 스케줄링 적용
    lr_schedule = ExponentialDecay(
        initial_learning_rate=0.0005, decay_steps=10000, decay_rate=0.96, staircase=True
    )

    # ✅ 최종 모델 생성
    model = Model(inputs=[image_input, audio_input], outputs=output)
    model.compile(loss='categorical_crossentropy', optimizer=Adam(learning_rate=lr_schedule), metrics=['accuracy'])

    return model

# ✅ 모델 생성 및 구조 확인
if __name__ == "__main__":
    model = create_optimized_model()
    model.summary()
