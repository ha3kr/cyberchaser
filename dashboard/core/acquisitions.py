import requests
import re

def send_request(url):
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:82.0) Gecko/20100101 Firefox/82.0"}
    req = requests.get(url, headers=headers)
    content = req.text
    return content

# Get Company Name
def get_company_name(company, content):
    content = content
    # print(content)
    names = []
    companies = re.findall('(?:<strong class="c_identityChip-name">)(.*?)</strong>', content)
    for line in companies:
        line = line.lower()
        if company not in line:
            if line not in names:
                names.append(line)
    return(names)

# Get Company Date
def get_company_date(content):
    content = content
    dates = []
    date = re.findall('(?:<span>20)(.*?)</span>', content)
    for line in date:
        dates.append(line)
    return dates

class Acquisitions:
    def __init__(self, company):
        global acq_ulr
        self.company = company
        self.company = company.split('.')[0]
        company_cap = self.company.capitalize()
        acq_ulr = "https://index.co/company/" + company_cap +"/acquirees"
    def result(self):
        content = send_request(acq_ulr)
        name = get_company_name(self.company, content)
        date = get_company_date(content)
        if name:
            res = dict(zip(name, date))
            return res
        else:
            print("No Acquisitions Found !\n")
