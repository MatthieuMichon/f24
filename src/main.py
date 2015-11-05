#!/usr/bin/python3

from extract.avherald import AvheraldExtract
from transform.events import AvheraldTransfrom


def main(verbose=False):
    ae = AvheraldExtract(verbose=verbose)
    avh_data = ae.data
    at = AvheraldTransfrom(extracted_data=avh_data, verbose=verbose)
    print(at.ea[0].data['reg'])

if __name__ == "__main__":
    main(verbose=True)
