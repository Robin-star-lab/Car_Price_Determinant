import logging
import os
import sys

log_str = '[ %(asctime)s : %(module)s : %(levelname)s : %(message)s ]'
log_dir = 'log'
if log_dir != "":
    os.makedirs(log_dir, exist_ok=True)
log_filepath = os.path.join(log_dir,'running.logs')

logging.basicConfig(
    level=logging.INFO,
    format=log_str,
    handlers=[
        logging.FileHandler(log_filepath, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)

my_logger = logging.getLogger('Car_price_logger')