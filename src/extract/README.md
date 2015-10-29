# Extraction

## fr24.com

### Airlines

List of airlines.

Arguments: *None*

Returns a list of the following structure:

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

List of airports.

Arguments: *None*

Returns a list of the following structure:

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

### Airport

Provides exhaustive information on a given airport.

Arguments: four-char ICAO designator for the selected airport.

Example: `RJTT`

Returns a structure with two sections:
* `_api` holding internal information
* `result` containing two subsections:
  * `request`: see table
  * `response`: container only
    * `airlines`: container only
      * `codeshare`: see table
    * `airport`: container only
      * `pluginData`: see table

Request subsection fields:

Field|Description|Relevant|Remarks
---|---|---|---
callback|---|No|Default `null`
code|ICAO designator|Sanity check|Requested airport
format|---|No|Value: `json`
limit|---|Maybe|Default value: `25`; can be overriden
plugin|---|No|Default `[]`
plugin-setting|JSON structure|Yes|Encapsulated timestamp: ```["schedule"]["timestamp"]```

Example:
```JSON
"request":
{
	"callback":null,
	"code":"RJAA",
	"format":"json",
	"limit":25,
	"page":1,
	"plugin":[],
	"plugin-setting":
	{
		"schedule":
		{
			"mode":null,
			"timestamp":1446152700
		}
	}
}
```

Codeshare entry fields:

Field|Description|Relevant|Remarks
---|---|---|---
name|Airline name|Yes|---
code/iata|IATA designator|Yes|Two-char IATA airline designator
code/icao|ICAO designator|Yes|Three-char airline designator
