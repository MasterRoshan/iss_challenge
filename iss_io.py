import requests
from datetime import datetime, timedelta
import argparse
from urllib.parse import urlencode, urljoin

API_URL = 'http://api.open-notify.org/'


def print_current_location():
    """Prints out the current coordinates of the ISS

    Returns
    -------
    None

    """
    path = 'iss-now.json'
    resp_json = requests.get(urljoin(API_URL, path)).json()

    location = resp_json.get('iss_position')

    current_time = datetime.strftime(datetime.now(), '%H:%M:%S')

    print(
        f'\nThe current location of the ISS at {current_time}'
        f' is ({location.get("latitude")}, {location.get("longitude")})\n'
    )


def print_next_pass(lat: float, lon: float):
    """Prints when the next time the ISS will be overhead for given coordinates

    Parameters
    ----------
    lat : float
        Description of parameter `lat`.
    lon : float
        Description of parameter `lon`.

    Returns
    -------
    None

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

    print(f'\nThe ISS will be overhead ({lat}, {lon}) '
          f'at {next_pass_time} for {str(duration)}\n'
          )


def print_people():
    """Prints the names of the astronauts aboard the ISS

    Returns
    -------
    None

    """
    path = 'astros.json'
    resp_json = requests.get(urljoin(API_URL, path)).json()
    names = [x.get('name') for x in resp_json.get('people')]
    print(f'\nAstronauts aboard the ISS: {", ".join(names)}\n')


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
        print_current_location()
    elif args.command == 'pass':
        print_next_pass(args.lat, args.lon)
    elif args.command == 'people':
        print_people()


if __name__ == "__main__":
    main()
