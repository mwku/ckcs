document.addEventListener('DOMContentLoaded', function () {
    // document.getElementById('menu').style.display = 'none'
    // if (window.innerWidth <= 1250) {
    //     var menuButton = document.getElementById('menu-button');
    //     var menuDropdown = document.getElementById('menu');

    //     menuButton.addEventListener('click', function (event) {
    //         event.stopPropagation();
    //         if (menuDropdown.style.display === "none") {
    //             menuDropdown.style.display = "flex";
    //         } else {
    //             menuDropdown.style.display = "none";
    //         }
    //     });

    //     window.addEventListener('click', function (event) {
    //         if (!event.target.matches('#menu-button')) {
    //             menuDropdown.style.display = 'none';
    //             // menuButton.style.display = 'block';
    //         }
    //     });
    // } else {
    var username = localStorage.getItem("username");
    if (username !== null) {
        if (username.length < 7) {
            document.getElementById("account-button").innerText = username;
        } else {
            document.getElementById("account-button").innerText = username.substring(0, 6) + "...";
        }
        document.getElementById("log-out").style.display = "flex";
        document.getElementById("log-in").style.display = "none";
        document.getElementById("sign-up").style.display = "none";

        var accountButton = document.getElementById("account-button");
        var dropdownContent = document.getElementById("dropdown-content");
        var logOutButton = document.getElementById("log-out");
        if (accountButton && dropdownContent) {
            dropdownContent.style.display = "none";

            accountButton.addEventListener('click', function (event) {
                event.stopPropagation();
                if (dropdownContent.style.display === "none") {
                    dropdownContent.style.display = "flex";
                } else {
                    dropdownContent.style.display = "none";
                }
            });

            window.addEventListener('click', function () {
                if (dropdownContent.style.display === "flex") {
                    dropdownContent.style.display = "none";
                }
            });

            dropdownContent.addEventListener('click', function (event) {
                event.stopPropagation();
            });
        }
        logOutButton.addEventListener('click', function () {
            fetch("log-out", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ username: username, token: localStorage.getItem("token") }),
            }).then((response) => response.json())
                .then((data) => {
                    if (data.errdetail === "") {
                        localStorage.removeItem("username");
                        localStorage.removeItem("token");
                        document.getElementById("log-out").style.display = "none";
                        document.getElementById("log-in").style.display = "flex";
                        document.getElementById("sign-up").style.display = "flex";
                        document.getElementById("account-button").innerText = "帳號";
                    } else {
                        alert(data.errdetail);
                    }
                });
            //測試方便登出用
            // localStorage.removeItem("username");
            // localStorage.removeItem("token");
            // document.getElementById("log-out").style.display = "none";
            // document.getElementById("log-in").style.display = "flex";
            // document.getElementById("sign-up").style.display = "flex";
            // document.getElementById("account-button").innerText = "帳號";
        });
    }
    else {
        var accountButton = document.getElementById("account-button");
        var dropdownContent = document.getElementById("dropdown-content");
        document.getElementById("log-out").style.display = "none";
        if (accountButton && dropdownContent) {
            dropdownContent.style.display = "none";

            accountButton.addEventListener('click', function (event) {
                event.stopPropagation();
                if (dropdownContent.style.display === "none") {
                    dropdownContent.style.display = "flex";
                } else {
                    dropdownContent.style.display = "none";
                }
            });

            window.addEventListener('click', function () {
                if (dropdownContent.style.display === "flex") {
                    dropdownContent.style.display = "none";
                }
            });

            dropdownContent.addEventListener('click', function (event) {
                event.stopPropagation();
            });
        }
    }
    // }
});