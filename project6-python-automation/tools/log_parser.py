import re, json, sys
SSH_FAIL=r"Failed password.* from (\d+\.\d+\.\d+\.\d+)"

def parse(file):
    ips=[]
    for line in open(file):
        m=re.search(SSH_FAIL,line)
        if m: ips.append(m.group(1))
    return {"failed_ssh_ips":ips,"total_failures":len(ips)}

if __name__=="__main__":
    print(json.dumps(parse(sys.argv[1]),indent=4))
