import requests, json, sys, os
from dotenv import load_dotenv
load_dotenv()
VT_API_KEY=os.getenv("VT_API_KEY")

def lookup(h):
    url=f"https://www.virustotal.com/api/v3/files/{h}"
    headers={"x-apikey":VT_API_KEY}
    r=requests.get(url,headers=headers)
    if r.status_code!=200:
        return {"hash":h,"error":"Not found"}
    stats=r.json()['data']['attributes']['last_analysis_stats']
    return {"hash":h,**stats}

if __name__=="__main__":
    with open(sys.argv[1]) as f:
        hashes=[l.strip() for l in f]
    print(json.dumps([lookup(h) for h in hashes],indent=4))
