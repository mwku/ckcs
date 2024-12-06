document.addEventListener('DOMContentLoaded', function () {
    fetch(
        "/captcha_img",
        {
            method: 'post',
            headers: {
                'Content-Type': 'application/json'
            },
            json: {
                'type': 'admin'
            }
        }
    )
        .then(response => response.json())
        .then(data => {
            document.getElementById('captcha').src = data.url_;
        })
    var submitButton = document.getElementById('submit');
    submitButton.addEventListener('click', function () {
        var username = document.getElementById('account').value;
        var password = document.getElementById('password').value;
        var captchacode = document.getElementById('captchacode').value;
        fetch('/admin_login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username: username,
                password: password,
                captchacode: captchacode
            })
        }).then(response => response.json())
            .then(data => {
                if (data.errcode === '00') {
                    localStorage.setItem("manager", username);
                    localStorage.setItem("manage_token", data.token);
                    window.location.href = '/admin_home';
                }
                else {
                    alert(data.errdetail);
                }
            })
    })
})