# ckcs
# Python模組
flask 如果沒有安裝過請在終端機輸入 pip install flask
# 執行view.py
執行view.py後前往終端輸出的連結
 * Serving Flask app 'main'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on https://127.0.0.1:5000     # 這裡
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 130-870-665
# 路由
/ : 主頁
/about : 關於我們
/log-in : 登入
/sign-up : 註冊
/verify : 註冊後驗證帳號的路由 #未完成
/admin : 後台 #目前只有登入
/practice/<webname> : 搶票練習 #預計不會做
/captcha/<webname> : 驗證碼練習 #預計不會做
# 待完成
提供 /practice 範本
