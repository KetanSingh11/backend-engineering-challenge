# some utility functions
import os
import sys
import json
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

HERE = os.path.abspath(os.path.dirname(__file__))
INPUT_TIME_FORMAT = "%Y-%m-%d %H:%M:%S.%f"
OUTPUT_TIME_FORMAT = "%Y-%m-%d %H:%M:00"


def is_valid_json_file(filepath):
    if not filepath_validator(filepath):
        logger.error("Input file is not a valid file.")
        return False

    if filepath.lower().endswith("json"):
        return True
    else:
        logger.error("Invalid file extension: '{}'. Must end with *.json".format(filepath))
        return False

def filepath_validator(filepath):
    """ Check the file exists and is a file """
    if os.path.isfile(filepath):
        return True
    else:
        return False


def json_file_reader(filepath):
    """
    Reads lines from JSON and returns a list of events
    converts timestamps to datetimes.
    :param filepath: absolute path to a file containing events
    """

    events_list = []        #Assumption: json rows are in ascending order always
    events_objs = None      #Todo: make list of Event objects
    try:
        logger.info("Reading JSON file: %s", filepath)
        if is_valid_json_file:
            with open(filepath, "r") as file:
                # Todo: if file is huge?! then we should read it part by part
                for i, line in enumerate(file.readlines(), start=1):
                    event_obj = _validate(i, line.strip(), filepath, change_to_datetime=True)
                    events_list.append(event_obj)
        else:
            logger.error("File '{}' is not a valid path. Please check again.".format(filepath))
            raise FileNotFoundError

    except Exception as e:
        logger.exception(e)
        return

    return events_list

def _validate(i, line, filepath, change_to_datetime=True):
    """Asserts that each line from the input file is in the correct format.
    :param i (int):
    :param line (str):
    :param filepath (str):
    :param change_to_datetime (bool):
    """

    # assert event is JSON-readable
    event = json.loads(line)

    # # assert event is not missing mandatory keys
    # for key in EXPECTED_KEYS:
    #     if key not in event.keys():
    #         raise UnknownFormatError(
    #             filepath,
    #             reason="line {} is missing expected events key '{}'".format(i, key),
    #         )

    # assert event timestamp is in correct format, then convert it also
    try:
        if change_to_datetime:
            event["timestamp"] = datetime.strptime(event["timestamp"], INPUT_TIME_FORMAT)
    except ValueError:
        logger.error("line {} contains a timestamp which is not in the format {}".format(i, INPUT_TIME_FORMAT))
        logger.critical("Aborting...")
        sys.exit(1)

    return event


# def _read_json(filepath: Text) -> List[Dict[Text, Any]]:
#     """Reads lines from JSON and converts timestamps to datetimes."""
#     events = []
#
#     with open(filepath, "r") as f:
#         for i, line in enumerate(f.readlines()):
#             event = _validate(i, line, filepath)
#             events.append(event)
#
#     return events

def get_date_and_duration(data):
    try:
        assert int(data['duration']) >= 0   # Checks whether duration is not negative

        return (datetime.fromisoformat(data['timestamp']),
                int(data['duration']))  # Attempt to convert input format to a valid datetime
    except (AssertionError, TypeError, ValueError) as err:
        logger.error(err, exc_info=True)
        return (None, None)

def json_file_writer(ma_list):
    """
    Writed a list of moving averages to a local file
    :param ma_list: list of moving averages

    {"date": "2018-12-26 18:11:00", "average_delivery_time": 0}
    {"date": "2018-12-26 18:12:00", "average_delivery_time": 20}
    {"date": "2018-12-26 18:13:00", "average_delivery_time": 20}
    {"date": "2018-12-26 18:14:00", "average_delivery_time": 20}
    {"date": "2018-12-26 18:15:00", "average_delivery_time": 20}
    {"date": "2018-12-26 18:16:00", "average_delivery_time": 25.5}
    {"date": "2018-12-26 18:17:00", "average_delivery_time": 25.5}
    """
    with open("output.json", "w") as file:
        file.writelines(ma_list)
