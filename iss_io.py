import requests
import time
import argparse

API_URL = 'http://api.open-notify.org/'

parser = argparse.ArgumentParser(
    description='Get some information about the ISS over REST'
)
subparsers = parser.add_subparsers(help='commands', dest='command')
loc_parser = subparsers.add_parser(
    'loc', help='get the current location of the ISS'
)
pass_parser = subparsers.add_parser(
    'pass', help='pass coordinates with --lat and --long'
)
pass_parser.add_argument('--lat', required=True,
                         type=float, help='latitude coordinate'
                         )
pass_parser.add_argument('--long', required=True, type=float,
                         help='longitude coordinate'
                         )
pass_parser = subparsers.add_parser(
    'people', help='get the current crew members aboard the ISS'
)

args = parser.parse_args()

if args.command == 'loc':
    resp_json = requests.get(f'{API_URL}iss-now.json').json()

    location = resp_json.get('iss_position')

    current_time = time.strftime('%H:%M:%S', time.localtime())

    print(
        f"\nThe current location of the ISS at {current_time}\n"
        f"latitute: {location.get('latitude')}\n"
        f"longitude: {location.get('longitude')}\n"
    )

elif args.command == 'pass':
    pass
