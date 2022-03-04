# nordvpn-rotate (UA)

Якщо ви користуєтеся [NordVPN](https://nordvpn.com/ru/) - ця программа на python дозволяє автомотично оновлювати використиваний VPN сервер аби IP динамічно змінювався.

### Як завантажити

`python -m pip install -- upgrade pip`
`python -m pip install -r requirements.txt`

### Як користуватись

`python vpn_rotate.py [-h] [-t TIMEOUT] [-d DURATION] [-c COUNTRY]`

Доступні опції:
- `-t TIMEOUT`  - як часто змінювати VPN сервер у секундах (5 хвилин за замовчуванням)
- `-d DURATION` - час роботи програмити у секундах (1 година за замовчуванням)
- `-c COUNTRY`  - чи використати лише якусь конкретну страну - за відсутності, страна буде обиратися випадково із файлу **countries.txt**

*Увага: якщо треба детальніше налаштувати список країн - у файлі **countries.txt** символ '#' означає що країна не використовуватиметься.*

# nordvpn-rotate (ENG)

If you are using [NordVPN](https://nordvpn.com/ru/) - this small script allows to automatically refresh selected VPN servers.

### Installation

`python -m pip install -- upgrade pip`
`python -m pip install -r requirements.txt`

### Usage

`python vpn_rotate.py [-h] [-t TIMEOUT] [-d DURATION] [-c COUNTRY]`

Available options:
- `-t TIMEOUT`  - time interval between VPN server changes in seconds (5 mins default)
- `-d DURATION` - overall script execution duration (1 hour default)
- `-c COUNTRY`  - specific country to use - if empty, servers will be selected from random countries, specified in **countries.txt**

*Note: if you want to change list of countries in use - take a look at **countries.txt** - disabled countries are prefixed with '#' symbol.*
