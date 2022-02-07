import argparse
import glob

from azureml.core import Run

from utils import extract_features

parser = argparse.ArgumentParser()

parser.add_argument(
    "--data-folder",
    type=str,
    dest="data_folder",
    default="data",
    help="data folder mounting point",
)
parser.add_argument("--prepared-data", type=str, help="Directory for results", dest="prepared_data", help="storage geddon")

args = parser.parse_args()

data_folder = args.data_folder
save_folder = args.prepared_data

run = Run.get_context()

print("Data folder:", data_folder)