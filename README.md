# nordvpn-rotate (UA 🇺🇦)

Якщо ви користуєтеся [NordVPN](https://nordvpn.com/ru/) - ця программа на python дозволяє автомотично оновлювати використиваний VPN сервер аби IP динамічно змінювався.

### Installation

`python -m pip install -- upgrade pip`
`python -m pip install -r requirements.txt`

### Usage

`python vpn_rotate.py [-h] [-t TIMEOUT] [-d DURATION] [-c COUNTRY]`

Available options:
- `-t TIMEOUT`  - time interval between VPN server changes
- `-d DURATION` - overall script execution duration
- `-c COUNTRY`  - specific country to use - if empty, servers will be selected from random countries, specified in **countries.txt**

*Note: if you want to change list of countries in use - take a look at **countries.txt** - disabled countries are prefixed with '#' symbol .*

![IMG_5164](https://user-images.githubusercontent.com/17875017/156822065-a67c57d6-08a2-4caf-bc6b-723b5ff47880.JPG)

If you are using [NordVPN](https://nordvpn.com/ru/) - this small script allows to automatically refresh selected VPN servers.

### Installation

`python -m pip install -- upgrade pip`
`python -m pip install -r requirements.txt`

### Usage

`python vpn_rotate.py [-h] [-t TIMEOUT] [-d DURATION] [-c COUNTRY]`

Available options:
- `-t TIMEOUT`  - time interval between VPN server changes
- `-d DURATION` - overall script execution duration
- `-c COUNTRY`  - specific country to use - if empty, servers will be selected from random countries, specified in **countries.txt**

*Note: if you want to change list of countries in use - take a look at **countries.txt** - disabled countries are prefixed with '#' symbol .*
