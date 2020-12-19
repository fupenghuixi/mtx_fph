
import time
from http.cookiejar import Cookie

import requests


def sleep(n_secs):
    time.sleep(n_secs)

def redirect_location():
    url="http://121.42.15.146:9090/mtx/index.php?s=/index/order/pay/id/7613.html"
    params={
        Cookie:"PHPSESSID=a2onofmff78bkknf1ti4v5a1b6"
    }
    resp=requests.get(url,params=params)
    s=resp.json().get("location")
    return s

if __name__ == '__main__':
    print(redirect_location())
