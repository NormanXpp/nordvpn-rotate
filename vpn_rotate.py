from nordvpn_connect import initialize_vpn, rotate_VPN, close_vpn_connection

from time import sleep
from random import choice
from os import path
from datetime import datetime
import argparse

DEFAULT_TIMEOUT = 60 * 5
INIT_TIMEOUT = 10
DEFAULT_DURATION = 60 * 60

COUNTRIES_PATH = path.join(path.dirname(__file__), "countries.txt")

with open(COUNTRIES_PATH) as countries_file:
    ALL_COUNTRIES = countries_file.read().split("\n")[:-1]
    AVAILABLE_COUNTRIES = list(filter(lambda name: name[0] != "#", ALL_COUNTRIES))

old_country = None
settings = {}


def rotate(preferred_country):
    global old_country
    global settings

    new_country = choice(AVAILABLE_COUNTRIES) if not preferred_country else preferred_country

    if old_country != new_country:
        old_country = new_country
        settings = initialize_vpn(new_country)
        sleep(INIT_TIMEOUT)

    rotate_VPN(settings)
    sleep(INIT_TIMEOUT)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Setup NordVPN with autorotation for given period of time")
    parser.add_argument("-t", "--timeout", type=int, default=DEFAULT_TIMEOUT, help="VPN session timeout - time interval between IP updates")
    parser.add_argument("-d", "--duration", type=int, default=DEFAULT_DURATION, help="Script execution duration")
    parser.add_argument("-c", "--country", type=str, help="Specific country to use as IP pool - if empty, use all based on config file")
    args = parser.parse_args()

    start_time = datetime.now()

    while (datetime.now() - start_time).seconds < args.duration:
        rotate(args.country)
        sleep(args.timeout)

    if settings:
        close_vpn_connection(settings)
