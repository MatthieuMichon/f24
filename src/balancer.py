#!/usr/bin/python3

import sys

from jsondl import JsonDl


class LoadBalance:

    DEFAULT_LB_URL = "http://www.flightradar24.com/balance.json"

    def __init__(self, url=None):
        if url is None:
            self.url = self.DEFAULT_LB_URL
            self.server_list = {}
            self.best_server = (None, sys.maxsize)

    def load(self):

        # Possible failure modes:
        # - Network connectivity issue
        # - Target file not present
        # - Unauthorized

        dl = JsonDl(self.DEFAULT_LB_URL)
        self.server_list = dl.getJson()

    def get_server(self):
        for server in self.server_list:
            if int(self.server_list[server]) < self.best_server[1]:
                self.best_server = (server, self.server_list[server])

    def dump_json(self):
        print(self.server_list)
        for param in self.server_list:
            print(param, self.server_list[param])

    def get_best_server(self):
        print(self.best_server[0])


def main():
    lb = LoadBalance()
    lb.load()
    lb.dump_json()
    lb.get_server()
    lb.get_best_server()


if __name__ == "__main__":
    main()
