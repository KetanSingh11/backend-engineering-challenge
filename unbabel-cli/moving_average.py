""" Computes a moving agerage over a window """
from collections import deque
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)

def calc_moving_average(event_list):
    min_datetime = event_list[0]["timestamp"]
    max_datetime = event_list[-1]["timestamp"] + timedelta(minutes=1)  # Add 1 minute otherwise the last minute is ignored

    logger.info(min_datetime)
    logger.info(max_datetime)