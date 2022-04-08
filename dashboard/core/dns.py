import requests

class PortScanning:
    def __init__(self, domain):
        self.domain = domain
    def ScanIP(self):
        res = requests.get(f"https://internetdb.shodan.io/{self.domain}")
        get_info = res.json()
        get_hostnames = get_info['hostnames']
        get_ports = get_info['ports']
        return get_info
