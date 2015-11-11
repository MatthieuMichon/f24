#!/usr/bin/python3

from extract.avherald import AvheraldExtract
from extract.fr24 import Fr24Airport

from transform.events import AvheraldTransfrom
from transform.airport import Fr24AirportTransform


from load.html_out import HtmlOut


def airport_summary(verbose=False):
    ap_name = 'lfpg'
    pages = [-1, 1]
    ap_list = [Fr24Airport(ap_name, page) for page in pages]
    Fr24AirportTransform(data=ap_list, verbose=verbose)
    # print([ap.data for ap in ap_list])


def avh_summary(verbose=False):
    ae = AvheraldExtract(verbose=verbose)
    avh_data = ae.data
    at = AvheraldTransfrom(extracted_data=avh_data, verbose=verbose)
    events_list = [event.data for event in at.ea]
    html = HtmlOut(verbose)
    html.append_dict_list('avh', events_list)
    print(html)


def main(verbose=False):
    airport_summary(verbose=verbose)
    #avh_summary(verbose=verbose)


if __name__ == "__main__":
    main(verbose=False)
