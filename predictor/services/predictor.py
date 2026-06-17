import joblib
import os


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "ml",
    "models",
    "heart_model.pkl"
)

ENCODER_PATH = os.path.join(
    BASE_DIR,
    "ml",
    "models",
    "encoders.pkl"
)

model = joblib.load(
    MODEL_PATH
)

encoders = joblib.load(
    ENCODER_PATH
)


def predict_heart_disease(

    age,

    sex,

    chest_pain_type,

    resting_bp,

    cholesterol,

    fasting_bs,

    resting_ecg,

    max_hr,

    exercise_angina,

    oldpeak,

    st_slope

):

    sex = encoders["Sex"].transform(
        [sex]
    )[0]

    chest_pain_type = encoders[
        "ChestPainType"
    ].transform(
        [chest_pain_type]
    )[0]

    resting_ecg = encoders[
        "RestingECG"
    ].transform(
        [resting_ecg]
    )[0]

    exercise_angina = encoders[
        "ExerciseAngina"
    ].transform(
        [exercise_angina]
    )[0]

    st_slope = encoders[
        "ST_Slope"
    ].transform(
        [st_slope]
    )[0]

    features = [[

        age,

        sex,

        chest_pain_type,

        resting_bp,

        cholesterol,

        fasting_bs,

        resting_ecg,

        max_hr,

        exercise_angina,

        oldpeak,

        st_slope

    ]]

    prediction = model.predict(
        features
    )[0]

    probabilities = model.predict_proba(
        features
    )[0]

    confidence = round(
        max(probabilities) * 100,
        2
    )

    return {

        "prediction": int(prediction),

        "confidence": confidence

    }