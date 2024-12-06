from flask import Flask, render_template, request, send_from_directory, jsonify
import requests
import os
from json import loads
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('ticketplus.html')


@app.route('/axios/config/api/v1/getS3')
def get_s3():
    path = request.args.get('path')
    print(request.args)
    try:
        with open(f'tpdata/{path}', 'r', encoding='utf-8') as f:
            re = f.read()
        return jsonify(loads(re))
    except:
        os.makedirs(os.path.dirname(f'tpdata/{path}'), exist_ok=True)
        data = requests.get(
            f'https://apis.ticketplus.com.tw/config/api/v1/getS3?path={path}')
        with open(f'tpdata/{path}', 'wb') as f:
            f.write(data.content)
        return jsonify(data.json)


@app.route('/axios/config/api/v1/get')
def get_():
    eventid = request.args.get('eventId')
    sessionid = request.args.get('sessionId')
    path = f'event/{eventid}_{sessionid}.json'
    try:
        with open(f'tpdata/{path}', 'r', encoding='utf-8') as f:
            re = f.read()
        return jsonify(loads(re))
    except:
        os.makedirs(os.path.dirname(f'tpdata/{path}'), exist_ok=True)
        data = requests.get(
            f'https://apis.ticketplus.com.tw/config/api/v1/get?eventId={eventid}&sessionId={sessionid}&&_=1731590367000')
        with open(f'tpdata/{path}', 'wb') as f:
            f.write(data.content)
        return jsonify(data.json)


@app.route('/axios/user/api/v1/login', methods=['POST'])
def login():
    return jsonify({
        "errCode": "00",
        "errMsg": "",
        "errDetail": "",
        "userInfo": {
            "id": "fetix.1724741384379877",
            "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImZldGl4LjE3MjQ3NDEzODQzNzk4NzciLCJ1c2VyVHlwZSI6Im9vbmUiLCJtYXNrZWRNb2JpbGUiOiIwOTAyKioqMTYxIiwibWFza2VkRW1haWwiOiJrdSoqKioqKioqKioqQGdtYWlsLmNvbSIsIm1hc2tlZFVzZXJOYW1lIjoi6L6cKue3ryIsIm1hc2tlZEJpcnRoZGF5IjoiMjAwOC0wOC0qKiIsImNvdW50cnkiOiJUYWl3YW4iLCJzZHBJZCI6IjM4NDc5NzkyMDg4ODI0IiwidmVyaWZ5RW1haWwiOnRydWUsImVuY3J5cHRlZEFkZHJlc3MiOnsiaXYiOiI2ZTkxNGQxNGQzMTg0NjI4N2QyMjU5MjNiNjdhMTRlZiIsImVuY3J5cHRlZERhdGEiOiIxODQ0YzU1OTcyMGM5ZTk3YjQ4OTY1MTcyY2E3ZDk1N2MxMWE2ODNhMTcxOGRkMTI2NGNlNmZjMTNhMjhhN2MxYzE5YjIwOTdjMGZiOWEzNWJiN2RjYTg3NTIxMTdmZTRhOTFhMTZiNzgxODMwY2U3Mzk1NjhjZGI0YWI1ZGFkYyJ9LCJlbmNyeXB0ZWRVc2VyTmFtZSI6eyJpdiI6ImM5N2ZjZDMzZWM0NDRjYmUxYzQ2OGRkZTg1NWJlYzQwIiwiZW5jcnlwdGVkRGF0YSI6IjNlMGJiMWFiMzczZWFkYmFkZjc4NWM4ZmJkMjExYzYzIn0sImRpc2FiaWxpdHkiOm51bGwsImdlbmRlciI6Ik0iLCJpYXQiOjE3MzE1OTA3NTMsImV4cCI6MTczMTU5NDM1M30.WNF_Aueh9B0m1atJ92RkotEABsrAC5sUaU6QLwSLNng",
            "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImZldGl4LjE3MjQ3NDEzODQzNzk4NzciLCJ1c2VyVHlwZSI6Im9vbmUiLCJtYXNrZWRNb2JpbGUiOiIwOTAyKioqMTYxIiwibWFza2VkRW1haWwiOiJrdSoqKioqKioqKioqQGdtYWlsLmNvbSIsIm1hc2tlZFVzZXJOYW1lIjoi6L6cKue3ryIsInNkcElkIjoiMzg0Nzk3OTIwODg4MjQiLCJpYXQiOjE3MzE1OTA3NTMsImV4cCI6MTczOTM2Njc1M30.vtKlaBRFqiVe0rK3nFGs8m3AQZyiNNSmQWMCfpcqmdg",
            "access_token_expires_in": 3599,
            "verifyEmail": 'true'
        }
    })


@app.route('/axios/user/api/v1', methods=['POST'])
def token():
    token = request.data('token')
    if token:
        return jsonify({"errCode": "00", "errMsg": "", "errDetail": "", "verify": 'true'})
    rtoken = request.data('refreshToken')
    if rtoken:
        return jsonify({
            "errCode": "00",
            "errMsg": "",
            "errDetail": "",
            "userInfo": {
                "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImZldGl4LjE3MjQ3NDEzODQzNzk4NzciLCJ1c2VyVHlwZSI6Im9vbmUiLCJtYXNrZWRNb2JpbGUiOiIwOTAyKioqMTYxIiwibWFza2VkRW1haWwiOiJrdSoqKioqKioqKioqQGdtYWlsLmNvbSIsIm1hc2tlZFVzZXJOYW1lIjoi6L6cKue3ryIsIm1hc2tlZEJpcnRoZGF5IjoiMjAwOC0wOC0qKiIsImNvdW50cnkiOiJUYWl3YW4iLCJzZHBJZCI6IjM4NDc5NzkyMDg4ODI0IiwidmVyaWZ5RW1haWwiOnRydWUsImVuY3J5cHRlZEFkZHJlc3MiOnsiaXYiOiJlNzkwYzg2N2EzYzEyODNhMjc1Nzg2M2NmMmZhMGI4MyIsImVuY3J5cHRlZERhdGEiOiI3ZjE3NzEwYmYwYzZmYzVkOWNlOWZmYThkZmM3MDhjZmQ0MmNiNjdhYjQ3MmY1NTc4ZGE5MzA0NWI0Y2NhYWI5M2Q2MzY2YjY4YmRkNDgzMTVkMWZjOGFhMjdhZjY5M2E2NzYyOTU3NTJjNWIzM2E3ZWQ2OGRjZDkxYWM2ODY1OCJ9LCJlbmNyeXB0ZWRVc2VyTmFtZSI6eyJpdiI6Ijc1M2M0NWM4MmMyMWU4YTRhMzIwNzE2NGJjMTRmMGYxIiwiZW5jcnlwdGVkRGF0YSI6IjY4NzViZDQ5OTQwNWY5NWJjMmI1ZWM0MWYzNmQxOWQ0In0sImRpc2FiaWxpdHkiOm51bGwsImdlbmRlciI6Ik0iLCJpYXQiOjE3MzE1Nzc1MzcsImV4cCI6MTczMTU4MTEzN30.duaWmRDuGUSGbNCWUGf44CmgHRQpWn3NCuBrLPrUUqo",
                "access_token_expires_in": 3599,
                "verifyEmail": 'true'
            }
        })


# @app.route('/axios/config/api/v1/getS3<path:path>', methods=['GET', 'POST'])
# def proxy_s3(path):
#     print(path)
#     if 'user/api/v1/login' in path:
#         return jsonify({
#             "errCode": "00",
#             "errMsg": "",
#             "errDetail": "",
#             "userInfo": {
#                 "id": "fetix.1724741384379877",
#                 "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImZldGl4LjE3MjQ3NDEzODQzNzk4NzciLCJ1c2VyVHlwZSI6Im9vbmUiLCJtYXNrZWRNb2JpbGUiOiIwOTAyKioqMTYxIiwibWFza2VkRW1haWwiOiJrdSoqKioqKioqKioqQGdtYWlsLmNvbSIsIm1hc2tlZFVzZXJOYW1lIjoi6L6cKue3ryIsIm1hc2tlZEJpcnRoZGF5IjoiMjAwOC0wOC0qKiIsImNvdW50cnkiOiJUYWl3YW4iLCJzZHBJZCI6IjM4NDc5NzkyMDg4ODI0IiwidmVyaWZ5RW1haWwiOnRydWUsImVuY3J5cHRlZEFkZHJlc3MiOnsiaXYiOiJjMmY1NGIwMTI5ZmZhM2Y1NTg4OTgzMzE4OTMzZDMxZSIsImVuY3J5cHRlZERhdGEiOiJkZDQyNGVjOTg2MTEzYzk2NzU4N2E3NTNmYmEzYTIwYWU2ZmFkNjJjZWY5ODljOTE0NzMyZTgzNGQ5ZjIyM2JhODU4NTM5N2E4ZDg3OGNiNWYzZjMxYTkxZmU1ZWIxZGRhY2FlYTZmYWE4ZjI2ZDk0N2NhOGZmYmZlOWE2ZDdlOSJ9LCJlbmNyeXB0ZWRVc2VyTmFtZSI6eyJpdiI6ImMwNTQwYzNiMThkNWY5NmYyYzQwOWNkNGQ2N2VkYWYzIiwiZW5jcnlwdGVkRGF0YSI6ImJiZDRkNDI1NDc0YThjMTBjYTdhZjcyM2YwZmY2M2VlIn0sImRpc2FiaWxpdHkiOm51bGwsImdlbmRlciI6Ik0iLCJpYXQiOjE3MzE1Nzc2OTYsImV4cCI6MTczMTU4MTI5Nn0.gWF-iiD02TIX_7qNYkKtAMVHJQKE7zHero7JtpDnAFE",
#                 "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImZldGl4LjE3MjQ3NDEzODQzNzk4NzciLCJ1c2VyVHlwZSI6Im9vbmUiLCJtYXNrZWRNb2JpbGUiOiIwOTAyKioqMTYxIiwibWFza2VkRW1haWwiOiJrdSoqKioqKioqKioqQGdtYWlsLmNvbSIsIm1hc2tlZFVzZXJOYW1lIjoi6L6cKue3ryIsInNkcElkIjoiMzg0Nzk3OTIwODg4MjQiLCJpYXQiOjE3MzE1Nzc2OTYsImV4cCI6MTczOTM1MzY5Nn0.0T8qTbTF1ANYyLFYLwwkGOC1TgcvTSEA-icjriKepko",
#                 "access_token_expires_in": 3599,
#                 "verifyEmail": 'true'
#             }
#         })
#     elif 'user/api/v1/token' in path:
#         return jsonify({"errCode": "00", "errMsg": "", "errDetail": "", "verify": 'true'})
#     else:
#         try:
#             # 構建目標URL
#             target_url = f'https://apis.apis.ticketplus.com.tw/axios/config/api/v1/getS3{path}'

#             # 轉發請求，保留所有原始參數
#             response = requests.get(
#                 target_url,
#                 params=request.args,
#                 headers={
#                     'User-Agent': request.headers.get('User-Agent'),
#                     'Accept': request.headers.get('Accept', '*/*'),
#                     'Accept-Encoding': request.headers.get('Accept-Encoding', 'gzip, deflate, br'),
#                     'Connection': 'keep-alive'
#                 }
#             )

#             # 複製回應標頭，但排除可能造成問題的標頭
#             headers = {
#                 key: value for key, value in response.headers.items()
#                 if key.lower() not in ['content-encoding', 'transfer-encoding']
#             }

#             return response.json()  # 直接返回 JSON 數據

#         except requests.exceptions.RequestException as e:
#             return jsonify({"error": str(e)}), 500


# @app.errorhandler(404)
# def page_not_found(e):
#     path = request.path.lstrip('/')
#     url = f'https://ticketplus.com.tw/{path}'
#     response = requests.get(url)
#     if response.status_code == 200:
#         # 確保目錄存在
#         os.makedirs(os.path.dirname(path), exist_ok=True)
#         # 將內容寫入到相應的路徑
#         with open(path, 'wb') as f:
#             f.write(response.content)
#         return send_from_directory(os.path.dirname(path), os.path.basename(path))
#     else:
#         return "Resource not found on apis.ticketplus.com.tw", 404
@app.errorhandler(404)
def page_not_found(e):
    path = request.path.lstrip('/')
    url = f'https://ticketplus.com.tw/{path}'
    response = requests.get(url)
    if response.status_code == 200:
        dir_name = os.path.dirname(path)
        if dir_name:
            # 確保目錄存在
            os.makedirs(dir_name, exist_ok=True)
        # 將內容寫入到相應的路徑
        with open(path, 'wb') as f:
            f.write(response.content)
        # 傳遞正確的目錄名稱
        return send_from_directory(dir_name or '.', os.path.basename(path))
    else:
        return "Resource not found on ticketplus.com.tw", 404


if __name__ == '__main__':
    app.run(debug=True)
