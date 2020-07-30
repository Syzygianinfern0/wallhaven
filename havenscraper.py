import os

from dotenv import load_dotenv
from wallhaven import Wallhaven, Parameters
import pandas as pd

load_dotenv()

wallhaven = Wallhaven()
params = Parameters()
API_KEY = os.getenv("API_KEY")

if __name__ == '__main__':
    params.filter_by_user("RaidyHD")
    params.set_purity(True, True, True)

    latest_scrape = wallhaven.search(params)

    local_data = pd.read_csv("walls.csv")
    # print(local_data)

    for wall in latest_scrape:
        if (local_data['id'] == wall['id']).any():
            print("there")
        else:
            print("not there")
