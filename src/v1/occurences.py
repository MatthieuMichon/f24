#!/usr/bin/python3

"""
f24.occurences
~~~~~~~~~~~~~~

This module contains the class handling air transport occurences.
"""

from data_suppliers.avherald import Avherald
from flight_list import FlightList


class Occurences:

    def __init__(self):
        avh = Avherald()
        occurence = {}
        occurence = avh.get_latest()
        print(occurence)
        fl = FlightList(occurence['reg'])
        fl.print_past_flights()


def main():
    Occurences()

if __name__ == "__main__":
    main()
