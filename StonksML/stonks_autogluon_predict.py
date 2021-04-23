import logging
import pandas as pd
from pathlib import Path
from autogluon.text import TextPredictor

logging.basicConfig(
    level=logging.INFO,
    filename="./StonksML/autogluon_logs/autogluon_prediction.log",
    filemode="w",
    format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger()
model_save_path = Path(__file__).resolve().parent / "autogluon_model"
predictor = TextPredictor.load(model_save_path)

test_data = pd.read_csv(Path(__file__).resolve().parent / "test_data.csv").iloc[
    :5000, 1:
]
test_data.columns = ["sentences", "label"]

test_sentences = test_data["sentences"].tolist()
labels = test_data["label"].tolist()
predictions = predictor.predict({"sentence": test_sentences})

num_corrects = 0


def determine_score(prediction, label):
    global num_corrects
    score_calculation = prediction - label
    if score_calculation == 0:
        num_corrects += 1
        return "🤩ok"
    elif score_calculation == -1:
        return "💩FP"
    return "💀FN"


for prediction, label, sentence in zip(predictions, labels, test_sentences):
    score = determine_score(prediction, label)
    output = f"{score} {sentence}"
    logger.info(output)

total_trials = len(test_sentences)
percentage_correct = num_corrects / total_trials * 100

logger.info(f"Score: {num_corrects}/{total_trials} ({percentage_correct}%)")
logger.info("\n\n\n")

sentences = test_sentences + [
    "it's a charming and often affecting journey.",
    "It's slow, very, very, very slow.",
    "happy",
    "sad",
    "oh no",
    ":O",
    "omg",
    "diamond hands",
    "paper hands",
    "lit stocks",
    "to the moon",
    "gamestop",
    "losses",
    "roaring kitty",
    "yolo",
    "bagholder",
    "tendies",
]
predictions = predictor.predict({"sentence": sentences[-50:]})

[
    logger.info(f'{"🤩" if not not prediction else "😭/😐"} {sentences[idx]}')
    for idx, prediction in enumerate(predictions)
]

predictions_proba = predictor.predict_proba({"sentence": sentences})

# [
#     logger.info(
#         f'"Sentence": {sentences[idx]}      "Predicted Sentiment Probability": {(prediction - 0.5) * 2}'
#         # '"Sentence":',
#         # sentences[idx],
#         # '"Predicted Sentiment Probability":',
#         # (prediction - 0.5) * 2,
#     )
#     for idx, prediction in enumerate(predictions_proba.iloc[:, 1])
# ]