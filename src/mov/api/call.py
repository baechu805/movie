import requests
import os
import pandas as pd

def echo(yaho):
    return yaho

def apply_type2df(load_dt="20120101", path="~/tmp/test_parquet"):
    df = pd.read_parquet(f'{path}/load_dt={load_dt}')
    
    num_cols = ['rnum', 'rank', 'rankInten', 'salesAmt', 'audiCnt', 'audiAcc', 'scrnCnt', 'showCnt', 'salesShare', 'salesInten', 'salesChange', 'audiInten', 'audiChange']
    
    df[num_cols] = df[num_cols].apply(pd.to_numeric)
    return df

def save2df(load_dt='20120101', url_param={}):
    """ airflow 호출지점 """
    df = list2df(load_dt, url_param)
    df['load_dt'] = load_dt
    
    print(df.head(5))
    df.to_parquet('~/tmp/test_parquet',partition_cols=['load_dt'])
    return df

def list2df(load_dt='20120101', url_param={}):
    l = req2list(load_dt)
    df = pd.DataFrame(l)
    return df

def req2list(load_dt='20120101') -> list:
    _, data = req(load_dt)
    l = data['boxOfficeResult']['dailyBoxOfficeList']
    return l

def get_key():
    key = os.getenv('MOVIE_API_KEY')
    return key

def req(load_dt="20120101"):
    url = gen_url(load_dt)
    r = requests.get(url)

    code = r.status_code
    data = r.json()
    print(data)
    return code, data

def gen_url(dt="20120101", url_param={}):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = get_key()
    url = f"{base_url}?key={key}&targetDt={dt}"
    for key, value in url_param.items():
        url = url + f"&{key}={value}"

        print("*^=" * 10)
        print(url)
        print("*^=" * 10)
        return url



