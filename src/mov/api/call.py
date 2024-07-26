def req(dt="20120101"):
    base_url == "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = "e27b3fbc58d386143693ca57ebf6cfd1"
    url = f"{base_url}?key={key}&targetDt={dt}"
    print(url)

