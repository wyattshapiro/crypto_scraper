import datetime
import os

# Set up
BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
HEADERS = {'User-Agent': 'Mozilla/5.0'}

# Inputs
COIN = "ripple"  # could also be "ripple", "bitcoin", etc
START_DATE = "20170428"
END_DATE = datetime.datetime.today().strftime('%Y%m%d')

# Outputs
OUTPUT_PATH = BASE_DIR + "/results/" + COIN + "_" + START_DATE + "_" + END_DATE + ".csv"
