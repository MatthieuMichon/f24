#!/usr/bin/python3

"""
f24.ap
~~~~~~

This module contains the class handling airports data
"""

import time
from data_suppliers.fr24_direct import Fr24Direct


class Airports:

    # By IATA; named fields; alt, country, name
    AP_DB_1_FILENAME = "_json/airports.php"
    # By ICAO; unnamed fields, airport web page
    AP_DB_2_FILENAME = "AirportDataService2.php"

    def __init__(self):
        self.ap_db = {}
        self.timestamp = int(time.time())
        self.ap_db["version"] = self.timestamp
        query = "version={}".format(self.timestamp)
        # Use both airport data sources
        supplier = Fr24Direct(filename=self.AP_DB_1_FILENAME)
        self.ap_db_1 = supplier.get_data()["rows"]
        supplier = Fr24Direct(filename=self.AP_DB_2_FILENAME, query=query)
        self.ap_db_2 = supplier.get_data()
        # Correlate both sources
        if len(self.ap_db_1) != len(self.ap_db_2):
            print(
                "Mismatch between databases: DB#1: {} / DB#2: {} records"
                .format(len(self.ap_db_1), len(self.ap_db_1)))
        for icao in self.ap_db_2:
            ap_data = {}
            ap_data["icao"] = icao
            for ap_db_1_entry in self.ap_db_1:
                if ap_db_1_entry["icao"] == icao:
                    ap_data.update(ap_db_1_entry)
                    break
            self.ap_db[icao] = ap_data

    def get_data(self, icao):
        """Get airport data by ICAO code

        icao: string (example LFPG)
        """
        if icao not in self.ap_db:
            return None
        return self.ap_db[icao]

    def get_pos(self, icao):
        data = self.get_data(icao)
        return (float(data["lat"]), float(data["lon"]))

    # def get_by_icao(self, icao):
    #     if icao not in self.ap_list:
    #         return None
    #     else:
    #         return self.ap_list[icao]

    # def load(self):
    #     dl = JsonDl(self.url)
    #     self.ap_list = dl.getJson()

    # def get_by_icao(self, icao):
    #     for ap in self.ap_list["rows"]:
    #         if ap["icao"] == icao:
    #             return ap
    #     return None

    # def print_version(self):
    #     print(self.ap_list["version"])

    # def print_by_icao(self, icao):
    #     print("Airport: ", icao, "; json: ", self.get_by_icao(icao))

    # def dump_json(self):
    #     print(self.ap_list)


def main():
    ap = Airports()
    print(ap.get_data("RJTT"))
    print(ap.get_pos("KLAX"))
    # ap.load()
    # ap.print_version()
    # ap.print_by_icao("LFPG")
    # ap.print_by_icao("RJOO")
    # ap.dump_json()


if __name__ == "__main__":
    main()
