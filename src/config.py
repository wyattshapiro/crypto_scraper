import datetime
import os

# Set up
BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
HEADERS = {'User-Agent': 'Mozilla/5.0'}
HEADLESS = True

# Inputs
START_DATE = "20130428"
END_DATE = datetime.datetime.today().strftime('%Y%m%d')

# Outputs
OUTPUT_PATH = BASE_DIR + "/results/" + '[coin_name]' + "_" + START_DATE + "_" + END_DATE + ".csv"
