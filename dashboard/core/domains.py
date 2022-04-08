import requests
import urllib.parse
import re
import whois

class Domains:
    def __init__(self, domain):
        self.domain = domain
    def get_domains(self):
        all_domains = set()
        org = whois.query(self.domain)
        org_encoded = urllib.parse.quote(org.registrant)
        res = requests.get(f"https://crt.sh/?O={org_encoded}&output=json", headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36"})
        content = res.json()
        for item in content:
            for i in re.finditer('(\.[\w-]+){2}$', item['common_name']):
                all_domains.add(i.group(0).split('.', 1)[1])
        return all_domains, org.registrant