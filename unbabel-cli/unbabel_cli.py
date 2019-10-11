import argparse
import logging
import utils
from moving_average import calc_moving_average

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def is_positive_int(window_size):
    """ window size needs to be positive integer and greater than 1 """
    assert window_size > 1, "window_size should be >1"

def argument_parser():
    parser = argparse.ArgumentParser(description="Unbabel_cli - a tool to compute moving average of stream")
    parser.add_argument(
        "--input_file", required=True, help="Path to the events JSON file"
    )
    parser.add_argument(
        "--window_size",
        required=True,
        type=int,
        help="Size of the moving average window",
    )

    return parser.parse_args()


def main():
    args = argument_parser()
    is_positive_int(args.window_size)

    # read json
    events_list = utils.json_file_reader(args.input_file)
    logger.info(events_list)

    # compute moving avg
    calc_moving_average(events_list)

    # write json to a file
    # utils.json_file_writer([])

if __name__ == "__main__":
    main()

