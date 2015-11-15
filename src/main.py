#!/usr/bin/python3

from extract.avherald import AvheraldExtract
from extract.fr24 import Fr24Airport
from extract.fr24 import Fr24FlightList
from extract.fr24 import Fr24FlightData

from transform.events import AvheraldTransfrom
from transform.airport import Fr24AirportTransform
from transform.flight import Fr24FlightListTransform
from transform.flight import Fr24FlightDataTransform

from load.html_out import HtmlOut
from load.chart import Chart


def airport_summary(verbose=False):
    ap_name = 'lfpg'
    pages = [-1, 1]
    ap_list = [Fr24Airport(ap_name, page) for page in pages]
    apt = Fr24AirportTransform(data=ap_list, verbose=verbose)
    print(apt.get_arrivals())


def avh_summary(verbose=False):
    ae = AvheraldExtract(verbose=verbose)
    avh_data = ae.data
    at = AvheraldTransfrom(extracted_data=avh_data, verbose=verbose)
    events_list = [event.data for event in at.ea]
    html = HtmlOut(verbose)
    html.append_dict_list(caption='avh', dict_list=events_list)
    print(html)


def arrival_charts(airport, verbose=False):
    ap_name = airport
    pages = [-1, 1]
    ap_list = [Fr24Airport(ap_name, page) for page in pages]
    apt = Fr24AirportTransform(data=ap_list, verbose=verbose)
    fl_list = apt.get_arrivals()
    id_list = []
    for flight in fl_list:
        fl = Fr24FlightList(flight_nb=flight, verbose=verbose)
        ft = Fr24FlightListTransform(data=fl.data, verbose=verbose)
        if not ft.get_id_list():
            continue
        id_list.append([ft.get_id_list()[0]])

    trail_list = []
    for id_ in id_list:
        if id_list.index(id_) > 8:
            break
        print('*** {}'.format(id_))
        fd = Fr24FlightData(flight_id=id_, verbose=verbose)
        fdt = Fr24FlightDataTransform(data=fd.data, verbose=verbose)
        trail_list.append(fdt.data['trail_raw'])

    ch = Chart(trail_list=trail_list, verbose=verbose)
    ch.crop_out_of_range(latitude=49.02, longitude=2.54,
                         distance=500, elevation=1000)
    ch.plot(longitude=2.54, latitude=49.0, distance=0.11)
    raise ValueError  # invoke pdb


def departure_charts(airport, verbose=False):
    ap_name = airport
    pages = [-1, 1]
    ap_list = [Fr24Airport(ap_name, page) for page in pages]
    apt = Fr24AirportTransform(data=ap_list, verbose=verbose)
    fl_list = apt.get_departures()
    id_list = []
    for flight in fl_list:
        fl = Fr24FlightList(flight_nb=flight, verbose=verbose)
        ft = Fr24FlightListTransform(data=fl.data, verbose=verbose)
        if not ft.get_id_list():
            continue
        id_list.append([ft.get_id_list()[0]])

    trail_list = []
    for id_ in id_list:
        if id_list.index(id_) > 8:
            break
        print('*** {}'.format(id_))
        fd = Fr24FlightData(flight_id=id_, verbose=verbose)
        fdt = Fr24FlightDataTransform(data=fd.data, verbose=verbose)
        trail_list.append(fdt.data['trail_raw'])

    ch = Chart(trail_list=trail_list, verbose=verbose)
    ch.crop_out_of_range(latitude=49.02, longitude=2.54,
                         distance=5000, elevation=1000)
    ch.plot(longitude=2.54, latitude=49.0, distance=1)
    raise ValueError  # invoke pdb


def charts_by_flight_nb(flight_nb, verbose=False):
    fl = Fr24FlightList(flight_nb=flight_nb, verbose=verbose)
    ft = Fr24FlightListTransform(data=fl.data, verbose=verbose)
    id_list = ft.get_id_list()

    trail_list = []
    for id_ in id_list:
        print('*** {}'.format(id_))
        fd = Fr24FlightData(flight_id=id_, verbose=verbose)
        fdt = Fr24FlightDataTransform(data=fd.data, verbose=verbose)
        trail_list.append(fdt.data['trail_raw'])

    ch = Chart(trail_list=trail_list, verbose=verbose)
    ch.crop_out_of_range(latitude=49.02, longitude=2.54,
                         distance=500, elevation=1000)
    ch.plot(longitude=2.54, latitude=49.0, distance=0.11)
    raise ValueError  # invoke pdb


def main(verbose=False):
    # airport_summary(verbose=verbose)
    # avh_summary(verbose=verbose)
    # charts_by_flight_nb(flight_nb='NH215', verbose=verbose)
    # arrival_charts(airport='lfpg', verbose=verbose)
    departure_charts(airport='lfpg', verbose=verbose)


if __name__ == "__main__":
    main(verbose=False)
