# Extraction

## fr24.com

### Airlines

List of airlines with the following data:

|Field|Description|Remarks
|---|---|---|
|Name|Airline name|---|
|Code|IATA designator|Two-char IATA airline designator|
|ICAO|ICAO designator|Three-char airline designator|

Example:
```JSON
{
  "Code":"A3",
  "Name":"Aegean Airlines",
  "ICAO":"AEE"
}
```

### Airports

List of airports with the following data:

|Field|Description|Remarks
|---|---|---|
|name|Airport name|---|
|iata|IATA designator|Three-char IATA airport designator|
|ICAO|ICAO designator|Four-char airline designator|
|lat|Airport latitude|In degrees plus decimal fractions|
|lon|Airport longitude|In degrees plus decimal fractions|
|country|Country in which is located the airport|---|
|alt|Airport altitude|Altitude in feet|

Example:
```JSON
{
  "name":"Atlantic City International Airport",
  "iata":"ACY",
  "icao":"KACY",
  "lat":"39.457581",
  "lon":"-74.577103",
  "country":"United States",
  "alt":"74"
}
```
