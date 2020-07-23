# ISS Challenge

## Details

There is an API (http://api.open-notify.org/) that provides information on the International Space Station. Documentation is provided via the website, along with sample request/response.



## Task

Implement a Python script that will accept the following command line arguments, along with any required information, and print the expected results

**loc**

print the current location of the ISS

Example: “The ISS current location at {time} is {LAT, LONG}”

**pass**

print the passing details of the ISS for a given location

Example: “The ISS will be overhead {LAT, LONG} at {time} for {duration}”

**people**

for each craft print the details of those people that are currently in space
## Dependencies

This script depends on requests
```pip install requests``` or ```pip install -r requirements.txt```

## Usage
```
usage: iss_io.py [-h] {loc,pass,people} ...

Get some information about the ISS over REST

positional arguments:
  {loc,pass,people}  commands
    loc              get the current location of the ISS
    pass             pass coordinates with --lat and --lon
    people           get the current astronauts aboard the ISS

optional arguments:
  -h, --help         show this help message and exit
```

## Testing
```
python tests.py
```
