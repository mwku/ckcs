function getQueryParams() {
    const params = {};
    const queryString = window.location.search.substring(1);
    const regex = /([^&=]+)=([^&]*)/g;
    let match;
    while (match = regex.exec(queryString)) {
        params[decodeURIComponent(match[1])] = decodeURIComponent(match[2]);
    }
    return params;
}
document.addEventListener('DOMContentLoaded', function () {
    const queryParams = getQueryParams();
    var submitButton = document.getElementById('submit');
    submitButton.addEventListener('click', function () {
        document.getElementById('loading').style.display = 'flex';
        submitButton.style.display = 'none';
        fetch('/verify_data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username: queryParams.username,
                token: queryParams.token
            })
        }).then(response => response.json())
            .then(data => {
                if (data.errdetail === "") {
                    document.getElementById('loading').style.display = 'none';
                    document.getElementById('finish').style.display = 'flex'
                    localStorage.setItem('username', queryParams.username);
                    localStorage.setItem('token', data.token);
                }
                else {
                    alert(data.errdetail);
                }
            });
    });
});