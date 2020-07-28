import requests
from datetime import datetime, timedelta
import argparse
from urllib.parse import urlencode, urljoin

API_URL = 'http://api.open-notify.org/'


def current_location():
    """Response containing the current position of the ISS

    Returns
    -------
    String

    """
    path = 'iss-now.json'
    resp_json = requests.get(urljoin(API_URL, path)).json()

    location = resp_json.get('iss_position')

    current_time = datetime.strftime(datetime.now(), '%H:%M:%S')

    return(
        f'The current location of the ISS at {current_time}'
        f' is ({location.get("latitude")}, {location.get("longitude")})'
    )


def next_pass(lat: float, lon: float):
    """Response: the next time the ISS will be overhead for given coordinates

    Parameters
    ----------
    lat : float
        The latitude coordinate.
    lon : float
        The longitude coordinate.

    Returns
    -------
    String

    """
    query = {
        'lat': lat,
        'lon': lon
    }
    path = 'iss-pass.json?' + urlencode(query)
    resp_json = requests.get(urljoin(API_URL, path)).json()

    timestamp = resp_json.get('response')[0].get('risetime')
    next_pass = datetime.fromtimestamp(timestamp)
    next_pass_time = datetime.strftime(next_pass, '%H:%M:%S')
    duration = timedelta(seconds=resp_json.get('response')[0].get('duration'))

    return(f'The ISS will be overhead ({lat}, {lon}) '
           f'at {next_pass_time} for {str(duration)}'
           )


def people():
    """Response containing the names of the astronauts aboard the ISS

    Returns
    -------
    String

    """
    path = 'astros.json'
    resp_json = requests.get(urljoin(API_URL, path)).json()
    names = [x.get('name') for x in resp_json.get('people')]
    return(f'Astronauts aboard the ISS: {", ".join(names)}')


def main():
    """Parses command line arguments and calls appropriate print function

    Returns
    -------
    None

    """
    parser = argparse.ArgumentParser(
        description='Get some information about the ISS over REST'
    )
    subparsers = parser.add_subparsers(help='commands', dest='command')
    loc_parser = subparsers.add_parser(
        'loc', help='get the current location of the ISS'
    )
    pass_parser = subparsers.add_parser(
        'pass', help='pass coordinates with --lat and --lon'
    )
    pass_parser.add_argument('--lat', required=True,
                             type=float, help='latitude coordinate'
                             )
    pass_parser.add_argument('--lon', required=True, type=float,
                             help='longitude coordinate'
                             )
    pass_parser = subparsers.add_parser(
        'people', help='get the current astronauts aboard the ISS'
    )
    args = parser.parse_args()

    if args.command == 'loc':
        print(current_location())
    elif args.command == 'pass':
        print(next_pass(args.lat, args.lon))
    elif args.command == 'people':
        print(people())
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
