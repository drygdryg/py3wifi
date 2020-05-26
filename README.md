# Python wrapper for [3WiFi Wireless Database](https://3wifi.stascorp.com/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/py3wifi.svg)](https://pypi.python.org/pypi/py3wifi/)
[![PyPI license](https://img.shields.io/pypi/l/py3wifi.svg)](https://pypi.python.org/pypi/py3wifi/)
[![PyPI version shields.io](https://img.shields.io/pypi/v/py3wifi.svg)](https://pypi.python.org/pypi/py3wifi/)
![PyPI - Downloads](https://img.shields.io/pypi/dm/py3wifi)
## Install
```
pip install py3wifi
```
Or you can install from source with:
```
https://github.com/drygdryg/py3wifi.git
cd py3wifi
python setup.py install
```
## API usage
### Authorization
```python
import py3wifi

api_session = py3wifi.Api(login='mylogin', password='mypassword')
api_session.auth()
```
Or with read API key:
```python
api_session = py3wifi.Api(read_key='abcdefghijklmnopqrstuvwxyz123456')
```
### Calling methods
```python
>>> api_session.method('apiquery', params={'bssid': '4C:F2:BF:30:81:A4'})
{'4C:F2:BF:30:81:A4': [{'time': '2017-07-27 10:39:43', 'bssid': '4C:F2:BF:30:81:A4', 'essid': 'IDNet-41', 'sec': 'WPA2', 'key': '87059894216', 'wps': '12345678', 'lat': 54.89953995, 'lon': 69.14550781}]}
```
Or:
```python
>>> api = api_session.get_api()
>>> api.apiquery(bssid='4C:F2:BF:30:81:A4')
{'4C:F2:BF:30:81:A4': [{'time': '2017-07-27 10:39:43', 'bssid': '4C:F2:BF:30:81:A4', 'essid': 'IDNet-41', 'sec': 'WPA2', 'key': '87059894216', 'wps': '12345678', 'lat': 54.89953995, 'lon': 69.14550781}]}
```
See https://3wifi.stascorp.com/apidoc for detailed API guide.
## Usage of 3WiFi AJAX interface
```python
import py3wifi

client = py3wifi.Client(login='mylogin', password='mypassword')
client.auth()
```
```python
>>> client.request('find', {'bssid': '04:95:E6:6C:36:*', 'essid': 'Tenda_◯', 'wps': '□□□□□□□□'})
{'result': True, 'data': [{'id': 93806549, 'time': '2019-12-08 17:30:55', 'comment': 'Router Scan', 'range': '192.168.0.0/16', 'nowifi': False, 'hidden': False, 'bssid': '04:95:E6:6C:36:50', 'essid': 'Tenda_6C3650', 'sec': 'None', 'key': '<empty>', 'wps': '21847080', 'lat': 44.52231216, 'lon': 33.59743881, 'fav': False}], 'found': 1, 'page': {'current': 1, 'count': 1}, 'time': 0.013512849807739}
```