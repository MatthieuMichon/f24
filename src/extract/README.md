# Extraction

## fr24.com

Handled in file `fr24.py`.

Supported datasets:

Dataset|Class|Description|Remarks
---|---|---|---
Airlines|fr24.Fr24Airlines|Active airline list|Mostly static
Airports|fr24.Fr24Airports|Active airport list|Mostly static
Planes|fr24.Fr24Planes|Active plane list|Dynamically updated
Airport|fr24.Fr24Airport|Exhaustive data on a given airport|Requires the airport ICAO designator
