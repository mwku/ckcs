document.addEventListener('DOMContentLoaded', function () {
    var signUpButton = document.getElementById('submit');
    var username_ = document.getElementById('username');
    var password_ = document.getElementById('password');
    var passwordCheck_ = document.getElementById('password-check');
    var email_ = document.getElementById('email');
    var errDetail_ = document.getElementById('errdetail');
    function clearError(input) {
        input.style.border = "1px solid #eee";
        errDetail_.innerText = "";
    }
    username_.addEventListener('input', function () {
        clearError(username_);
    });

    password_.addEventListener('input', function () {
        clearError(password_);
    });

    passwordCheck_.addEventListener('input', function () {
        clearError(passwordCheck_);
    });

    email_.addEventListener('input', function () {
        clearError(email_);
    });

    signUpButton.addEventListener('click', function () {
        var username = document.getElementById('username').value;
        if (username === "") {
            document.getElementById('username').style.border = "1px solid red";
            document.getElementById('errdetail').innerText = "請輸入帳號名稱";
            return;
        }
        var password = document.getElementById('password').value;
        if (password === "") {
            document.getElementById('password').style.border = "1px solid red";
            document.getElementById('errdetail').innerText = "請輸入密碼";
            return;
        }
        if (document.getElementById('password-check').value === "") {
            document.getElementById('password-check').style.border = "1px solid red";
            document.getElementById('errdetail').innerText = "請確認你的密碼";
            return;
        }
        if (password !== document.getElementById('password-check').value) {
            document.getElementById('password-check').style.border = "1px solid red";
            document.getElementById('errdetail').innerText = "前後密碼不一致";
            return;
        }
        var email = document.getElementById('email').value;
        if (email === "") {
            document.getElementById('email').style.border = "1px solid red";
            document.getElementById('errdetail').innerText = "請輸入電子郵件";
            return;
        }
        fetch('/signup_data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username: username,
                password: password,
                email: email
            })
        })
            .then(response => response.json())
            .then(data => {
                if (data.errdetail === "") {
                    if (confirm('請前往信箱驗證您的帳號')) {
                        window.location.href = "/";
                    }
                    // localStorage.setItem("username", username);
                    // localStorage.setItem("token", data.token);
                    // window.location.href = "/";
                } else {
                    document.getElementById("errdetail").innerText = data.errdetail;
                }
            })
            .catch(error => console.error('Error:', error));
    });
    var links = document.querySelectorAll('a');
    links.forEach(function (link) {
        link.addEventListener('click', function (event) {
            if (event.target.id !== 'log-in' && event.target.id !== 'sign-up' && event.target.id !== 'register') {
                if (!confirm('確定要離開此頁面嗎？\n 我們將不會儲存您的資料')) {
                    event.preventDefault();
                }
            }
        });
    });

});