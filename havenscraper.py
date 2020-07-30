import os

from dotenv import load_dotenv
from wallhaven import Wallhaven, Parameters
from downloader import download_url
import csv
import numpy as np

load_dotenv()

wallhaven = Wallhaven()
params = Parameters()
API_KEY = os.getenv("API_KEY")

if __name__ == "__main__":
    params.filter_by_user("RaidyHD")
    params.set_purity(True, True, True)

    latest_scrape = wallhaven.search(params)

    with open("walls.csv", newline="") as f:
        reader = csv.reader(f)
        local_data = np.array(list(reader))

    # local_data = pd.read_csv("walls.csv")
    # print(local_data)
    new_downloads = list()

    for wall in latest_scrape[:5]:
        if wall["id"] not in local_data[1:, 0]:
            download_path = wall["path"]
            # status = download_url(download_path)
            status = True
            local_data = np.vstack((local_data,[wall["id"], status, download_path]))
            new_downloads.append([wall["id"], status, download_path])

    print(new_downloads)

    # np.savetxt("walls.csv", local_data, delimiter=",")
    with open("walls.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(local_data.tolist())