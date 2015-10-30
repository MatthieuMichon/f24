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
Flight|fr24.Fr24Flight|Complete data on the given flight id|Requires a valid fr24.com internal flight id
Plane|fr24.Fr24Plane|Raw plane information|Requires the aircraft reg; not trivial to transform (dynamic main key value)
Find|fr24.Fr24Find|Misc query|Requires a query string; accepts ICAO, IATA, a/c reg
