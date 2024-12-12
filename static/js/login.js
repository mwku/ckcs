document.addEventListener('DOMContentLoaded', function () {
    if (localStorage.getItem("username") === null) {
        document.getElementById('submit').addEventListener('click', function () {
            var username = document.getElementById("username").value;
            var password = document.getElementById("password").value;
            if (username === "" || password === "") {
                if (username === "") {
                    document.getElementById("username").style.border = "1px solid red";
                    document.getElementById("errdetail").innerText = "請輸入帳號名稱";
                } else {
                    document.getElementById("password").style.border = "1px solid red";
                    document.getElementById("errdetail").innerText = "請輸入密碼";
                }
                return;
            }
            fetch('/login_data', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    username: username,
                    password: password
                })
            })
                .then(response => response.json())
                .then(data => {
                    if (data.errdetail === "") {
                        // 登入成功，儲存用戶名和 token
                        localStorage.setItem("username", username);
                        // 假設伺服器返回一個 token
                        localStorage.setItem("token", data.token);
                        if (window.location.href.includes('next')) {
                            window.location.href = window.location.href.split('next=')[1];
                        } else {
                            window.location.href = '/';
                        }
                    } else {
                        document.getElementById("errdetail").innerText = data.errdetail;
                    }
                })
                .catch(error => {
                    console.error('Error during login:', error);
                    document.getElementById("errdetail").innerText = '登入失敗，請稍後再試。';
                });
        });
    } else {
        document.getElementById('submit').style.backgroundColor = "gray";
        document.getElementById('submit').style.borderColor = "gray";
        document.getElementById('submit').style.cursor = "default";
        document.getElementById('submit').innerText = "你已經成功登入了";

    }
    var links = document.querySelectorAll('a');
    links.forEach(function (link) {
        link.addEventListener('click', function (event) {
            if (event.target.id !== 'log-in' && event.target.id !== 'sign-up' && event.target.id !== 'register' && event.target.id !== 'forget') {
                if (!confirm('確定要離開此頁面嗎？\n 我們將不會儲存您的資料')) {
                    event.preventDefault();
                }
            }
        });
    });
    if (localStorage.getItem('username') !== null) {
        if (localStorage.getItem('username').length < 7) {
            var UsernameText = localStorage.getItem('username')
        }
        else {
            var UsernameText = localStorage.getItem('username').substring(0, 6) + '...';
        }
        document.getElementById('account-button').innerText = UsernameText;
    }

});