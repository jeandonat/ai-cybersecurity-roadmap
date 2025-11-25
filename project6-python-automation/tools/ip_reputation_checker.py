import requests, json, sys, os
from dotenv import load_dotenv

load_dotenv()
VT_API_KEY=os.getenv("VT_API_KEY")
VT_URL="https://www.virustotal.com/api/v3/ip_addresses/{}"

def check_ip(ip):
    headers={"x-apikey":VT_API_KEY}
    r=requests.get(VT_URL.format(ip),headers=headers)
    if r.status_code!=200:
        return {"ip":ip,"error":"API error"}
    data=r.json()
    stats=data['data']['attributes']['last_analysis_stats']
    return {"ip":ip,**stats}

if __name__=="__main__":
    with open(sys.argv[1]) as f:
        ips=[l.strip() for l in f]
    print(json.dumps([check_ip(i) for i in ips],indent=4))
