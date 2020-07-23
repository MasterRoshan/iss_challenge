import requests
from datetime import datetime, timedelta
import argparse
from urllib.parse import urlencode
API_URL = 'http://api.open-notify.org/'

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
    'people', help='get the current crew members aboard the ISS'
)

args = parser.parse_args()

if args.command == 'loc':
    resp_json = requests.get(f'{API_URL}iss-now.json').json()

    location = resp_json.get('iss_position')

    current_time = datetime.strftime(datetime.now(), '%H:%M:%S')

    print(
        f'\nThe current location of the ISS at {current_time}'
        f" is ({location.get('latitude')}, {location.get('longitude')})\n"
    )

elif args.command == 'pass':
    query = {
        'lat': args.lat,
        'lon': args.lon
    }
    url_query = urlencode(query)
    resp_json = requests.get(f'{API_URL}iss-pass.json?{url_query}').json()

    timestamp = resp_json.get('response')[0].get('risetime')
    next_pass = datetime.fromtimestamp(timestamp)
    next_pass_time = datetime.strftime(next_pass, '%H:%M:%S')
    duration = timedelta(seconds=resp_json.get('response')[0].get('duration'))

    print(f'\nThe ISS will be overhead ({args.lat},{args.lon}) '
          f'at {next_pass_time} for {str(duration)}\n'
          )
