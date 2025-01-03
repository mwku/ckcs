from flask import Flask, render_template, jsonify, request
from json import load, dump
import random
import string
app = Flask(__name__)


def generate_random_key(length=16):
    with open('userdata.json', 'r', encoding='utf-8') as f:
        re = load(f)
    characters = string.ascii_letters + string.digits
    while True:
        a = ''.join(random.choice(characters) for _ in range(length))
        if a not in re['tokens']:
            break
    return a


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/announcements')
def announcements():
    with open('webdata\\home\\announcements.json', 'r', encoding='utf-8') as f:
        re = load(f)
        return jsonify(re)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/log-in')
def log_in():
    return render_template('login.html')


@app.route('/login_data', methods=['POST'])
def login_data():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    with open('userdata.json', 'r', encoding='utf-8') as f:
        re = load(f)
    if username in re:
        if re[username]['password'] == password:
            a = generate_random_key()
            re[username]['token'] = a
            re['tokens'].append(a)

            with open('userdata.json', 'w', encoding='utf-8') as f:
                dump(re, f)
            return jsonify({"errdetail": "", "username": username, "token": re[username]['token']})
        else:
            return jsonify({"errdetail": "Password incorrect"})
    else:
        return jsonify({"errdetail": "Username not found"})


@app.route('/sign-up')
def sign_up():
    return render_template('signup.html')


@app.route('/signup_data', methods=['POST'])
def test():
    return jsonify({"errdetail": ""})


@app.route('/log-out', methods=['POST'])
def log_out():
    data = request.get_json()
    username = data.get('username')
    token = data.get('token')
    with open('userdata.json', 'r', encoding='utf-8') as f:
        re = load(f)
    if username in re:
        if token in re['tokens']:
            if re[username]['token'] == token:
                re[username]['token'] = ''
                re['tokens'].remove(token)
                with open('userdata.json', 'w', encoding='utf-8') as f:
                    dump(re, f, indent=4)
                return jsonify({"errdetail": ""})
            else:
                return jsonify({"errdetail": "Token incorrect"})
        else:
            return jsonify({"errdetail": "Token not found"})
    else:
        return jsonify({"errdetail": "Username not found"})


@app.route('/verify')
def verify_page():
    return render_template('verify.html')
@app.route('/template/kktix')
def t_k():
    return render_template('t_k.html')
@app.route('/template/ticketplus')
def t_tp():
    return render_template('t_tp.html')
@app.route('/template/tixcraft')
def t_ti():
    return render_template('t_ti.html')

@app.route('/verify_data', methods=['POST'])
def verify():
    # data = request.get_json()
    # mail = data.get('mail')
    # token = data.get('token')
    # with open('userdata.json', 'r', encoding='utf-8') as f:
    #     re = load(f)
    # if re['ver'][mail] == token:
    #     re[re['ver'][mail]] = {"password": re['ver'][mail]['password']}
    #     with open('userdata.json', 'w', encoding='utf-8') as f:
    #         dump(re, f, indent=4)
    #     return render_template('verified.html')
    return jsonify({"errdetail": "", 'token': generate_random_key()})


@app.route('/admin')
def admin():
    return render_template('admin.html')


@app.route('/captcha_img', methods=['POST'])
def captcha_img():
    return jsonify({"url_": f"/static/img/captcha/captcha{random.randint(10, 31)}.svg"})


@app.route('/admin_login', methods=['POST'])
def admin_login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    captcha_code = data.get('captchacode')
    user_ip = request.remote_addr
    # print(user_ip)
    with open('database/managerdata.json', 'r', encoding='utf-8') as f:
        re = load(f)
    if re['invaild_ip'].count(user_ip) > 5:
        return jsonify({"errcode": "403", "errdetail": "You are banned"})
    if username in re:
        set_captcha_code = re[username]['Captcha']
        if captcha_code != set_captcha_code:
            re['invaild_ip'].append(user_ip)
            with open('database/managerdata.json', 'w', encoding='utf-8') as f:
                dump(re, f)
            return jsonify({"errcode": "403", "errdetail": "Captcha incorrect"})
        else:
            while user_ip in re['invaild_ip']:
                re['invaild_ip'].remove(user_ip)
            with open('database/managerdata.json', 'w', encoding='utf-8') as f:
                dump(re, f)
            if re[username]['password'] == password:
                return jsonify({"errcode": "00", "errdetail": "", "token": generate_random_key()})
            else:
                re['invaild_ip'].append(user_ip)
                with open('database/managerdata.json', 'w', encoding='utf-8') as f:
                    dump(re, f)
                return jsonify({"errcode": "404", "errdetail": "Password incorrect"})
    else:
        return jsonify({"errcode": "404", "errdetail": "Username not found"})


@app.route('/practice/kktix')
def practice_k():
    if request.get_data('template'):
        return render_template('ticketplus_p.html')
    else:
        return render_template('load.html')


@app.route('/practice/ticketplus')
def practice_tp():
    if request.get_data('template'):
        return render_template('ticketplus_p.html')
    else:
        return render_template('load.html')


@app.route('/practice/tixcraft')
def practice_tx():
    if request.get_data('template'):
        return render_template('ticketplus_p.html')
    else:
        return render_template('load.html')


@app.route('/getTemplate', methods=['POST'])
def get_template():
    data = {'template': ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5']}
    return jsonify(data)


@app.route('/getTemplate_', methods=['POST'])
def get_template_():
    with open('templates\\practice\\ticketplus.html', 'r', encoding='utf-8') as f:
        re = f.read()
    data = {'TemplateHTML': re}
    return jsonify(data)


@app.route('/404')
def notfoundpage():
    return render_template('404err.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404err.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
