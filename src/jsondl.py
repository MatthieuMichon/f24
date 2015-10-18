#!/usr/bin/python3

import requests


class JsonDl:

    def __init__(self, url=None):
        if url is None:
            raise Exception
        self.url = url
        self.refresh()

    def refresh(self):
        try:
            data = requests.get(self.url)
        except:
            print("Failed to retrieve load balancer data.")
            return
        try:
            self.json_data = data.json()
        except:
            print("Failed to process JSON data.")
            return

    def getJson(self):
        return self.json_data

    def load(self):
        # Possible failure modes:
        # - Network connectivity issue
        # - Target file not present
        # - Unauthorized
        try:
            data = requests.get(self.DEFAULT_LB_URL)
        except:
            print("Failed to retrieve load balancer data.")
            return
        self.server_list = data.json()


def main():
    gj = JsonDl("http://www.flightradar24.com/balance.json")
    print(gj.getJson())


if __name__ == "__main__":
    main()
