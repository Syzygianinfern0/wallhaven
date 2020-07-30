import os

from dotenv import load_dotenv
from wallhaven import Wallhaven, Parameters

load_dotenv()

wallhaven = Wallhaven()
params = Parameters()
API_KEY = os.getenv("API_KEY")

if __name__ == '__main__':
    params.filter_by_user("RaidyHD")

    data = wallhaven.search(params)
    print(data)
