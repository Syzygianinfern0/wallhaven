import os

import requests


def download_url(url, folder="downloads"):
    print("downloading: ", url)

    file_name_start_pos = url.rfind("/") + 1
    file_name = url[file_name_start_pos:]

    try:
        r = requests.get(url, stream=True)
        if r.status_code == requests.codes.ok:
            with open(os.path.join(folder, file_name), "wb") as f:
                for data in r:
                    f.write(data)
        return True
    except ConnectionError:
        print("Invalid URL")
        return False
