import requests
import time
import json

with open("login_info", 'r') as f:
  login = json.loads(f.read())

print(login)
username = login.get('id')
password = login.get('pw')

st_date = "2019-01-01"
ed_date = "2020-01-01"

with requests.Session() as s:
    req = s.get('https://www.kidsa-z.com')
    status = req.status_code
    cookie_BIGip = req.cookies['BIGipServerlaz_prod_kidsa-z']
    headers = {
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      'Accept-Encoding': 'gzip, deflate, br',
      'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
      'Cache-Control': 'max-age=0',
      'Connection': 'keep-alive',
      'Content-Length': '49',
      'Content-Type': 'application/x-www-form-urlencoded',
      'Cookie': 'BIGipServerlaz_prod_kidsa-z={}'.format(cookie_BIGip),
      'Host': 'www.kidsa-z.com',
      'Origin': 'https://www.kidsa-z.com',
      'Referer': 'https://www.kidsa-z.com/main/Login',
      'Sec-Fetch-Mode': 'navigate',
      'Sec-Fetch-Site': 'same-origin',
      'Sec-Fetch-User': '?1',
      'Upgrade-Insecure-Requests': '1',
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
    url = "https://www.kidsa-z.com/main/Authorize"
    payload = "username={}&password={}&submit=".format(username, password)
    req2 = s.request("POST", url, headers=headers, data = payload)
    url = "https://www.kidsa-z.com/api/reports/activities/class?end_time={}&start_time={}".format(ed_date, st_date)
    response = s.request("GET", url)


print("Request Completed!===========")

result = response.json()
# print(result_json)

result_array = []
for key in result.keys():
    student = result[key]
    stu_act = student['activity_rollups_by_subject']
    try:
        stu_Dict = { 
            "full_name": student['full_name'],
            "level": student['level'],
            "star_earned": stu_act['overview']['stars_earned'],
            "logins": stu_act['overview']['logins'],
            "listen": stu_act['reading']['listen'],
            "read": stu_act['reading']['read'],
            "worksheet": stu_act['reading']['worksheet'],
            "quiz": stu_act['reading']['quiz'],
            "passed_quiz_count": stu_act['reading']['passed_quiz_count'],
            "practice_recording": stu_act['reading']['practice_recording']
        }
    except:
        continue
    print(stu_Dict)
    result_array.append(stu_Dict)