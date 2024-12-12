document.addEventListener('DOMContentLoaded', function () {
    function generateCaptcha() {
        const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
        let captcha = '';
        for (let i = 0; i < 6; i++) {
            captcha += characters.charAt(Math.floor(Math.random() * characters.length));
        }
        return captcha;
    }

    // Rick Roll
    const rickrollButton = document.getElementById('rickrollButton');
    rickrollButton.addEventListener('mouseenter', function () {
        this.style.transform = 'scale(1.05)';
        this.style.boxShadow = '0 4px 6px rgba(0,0,0,0.1)';
    });

    rickrollButton.addEventListener('mouseleave', function () {
        this.style.transform = 'scale(1)';
        this.style.boxShadow = 'none';
    });

    rickrollButton.addEventListener('click', function () {
        window.open('https://www.youtube.com/watch?v=2qBlE2-WL60', '_blank');
    });

    //404
    const cardButton = document.getElementById('cardButton');
    cardButton.addEventListener('mouseenter', function () {
        this.style.transform = 'scale(1.05)';
        this.style.boxShadow = '0 4px 6px rgba(0,0,0,0.1)';
    });

    cardButton.addEventListener('mouseleave', function () {
        this.style.transform = 'scale(1)';
        this.style.boxShadow = 'none';
    });

    cardButton.addEventListener('click', function () {
        window.open('/404', '_blank');
    });
    // Reload
    const reloadButton = document.getElementById('reloadButton');
    const loadingOverlay = document.getElementById('loadingOverlay');

    reloadButton.addEventListener('mouseenter', function () {
        this.style.transform = 'scale(1.05)';
        this.style.boxShadow = '0 4px 6px rgba(0,0,0,0.1)';
    });

    reloadButton.addEventListener('mouseleave', function () {
        this.style.transform = 'scale(1)';
        this.style.boxShadow = 'none';
    });
    reloadButton.addEventListener('click', function () {
        loadingOverlay.style.display = 'flex'
    })
    loadingOverlay.addEventListener('click', function () {
        loadingOverlay.style.display = 'none';
    });
    // Captcha
    const captchaButton = document.getElementById('captchaButton');
    const captchaDisplay = document.getElementById('captchaDisplay');
    let captchaInterval;

    captchaButton.addEventListener('mouseenter', function () {
        this.style.transform = 'scale(1.05)';
        this.style.boxShadow = '0 4px 6px rgba(0,0,0,0.1)';
    });

    captchaButton.addEventListener('mouseleave', function () {
        this.style.transform = 'scale(1)';
        this.style.boxShadow = 'none';
    });

    captchaButton.addEventListener('click', function () {
        // 避免重複
        if (captchaInterval) {
            clearInterval(captchaInterval);
            captchaInterval = null;
            captchaDisplay.textContent = '';
            return;
        }

        // 每0.05秒生成驗證碼
        captchaInterval = setInterval(() => {
            captchaDisplay.textContent = generateCaptcha();
        }, 50);
    });
});