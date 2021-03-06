from from_root import from_root

PROJECT_ROOT = from_root(".")

ML_FOLDER = "StonksML"

DATASETS = PROJECT_ROOT / "datasets"
RAW_DATASETS = DATASETS / "raw"
PREPROCESSED_DATASETS = DATASETS / "preprocessed"


AUTOGLUON_PACKAGE = PROJECT_ROOT / ML_FOLDER / "sentiment_analysis"
AUTOGLUON_LOGS = AUTOGLUON_PACKAGE / "autogluon_logs"
AUTOGLUON_MODEL = AUTOGLUON_PACKAGE / "autogluon_model"
SCRAPER_LOGS = AUTOGLUON_PACKAGE / "scraper_logs"

AUTOTS_PACKAGE = PROJECT_ROOT / ML_FOLDER / "timeseries"
AUTOTS_LOGS = AUTOTS_PACKAGE / "autots_logs"
AUTOTS_MODEL_DUMPS = AUTOTS_PACKAGE / "autots_model_dumps"

STREAMLIT_PACKAGE = PROJECT_ROOT / "StonksStreamlit"

ML_UTILS = PROJECT_ROOT / ML_FOLDER / "utils"
