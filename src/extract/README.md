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
AutoCompleteAirplanes|fr24.Fr24AutoCompAirplanes|Returns airplane 24-bit ICAO hex reg|Requires airplane reg

## avherald.com

Handled in file `avherald.py`.

Instantiating the `AvheraldExtract` performs the following actions:
* Request the top-level page
* Scrape the HTML for articles IDs
* For each ID, request the matching article page

The following datasets are exposed:

Dataset|Path|Class|Description|Remarks
---|---|---|---|---
Top-level|`data['main']`|avherald.AvheraldMain|HTML data |Enclosed in CSS ID `#ad1cell`
Events|`data['events']`|avherald.AvheraldArticle|Pair of HTML data|CSS selectors `#ad1cell > p` and `#ad1cell > table`
