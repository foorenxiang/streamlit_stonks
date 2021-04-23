from stonks_autots import StonksAutoTS
from cli_read_results import generate_results

import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


if __name__ == "__main__":
    StonksAutoTS.train_stonks()
    generate_results()