document.addEventListener('DOMContentLoaded', function () {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    var template = urlParams.get('template');
    if (template === null) {
        const selectbox_ = document.createElement('div');
        selectbox_.className = 'select-area';
        selectbox_.id = 'select-box';
        const title = document.createElement('h1');
        title.textContent = '請選擇要套用的模板';
        const template_container = document.createElement('div');
        template_container.className = 'template-container';
        template_container.id = 'template-container';
        selectbox_.appendChild(title);
        selectbox_.appendChild(template_container);
        const b = document.getElementById('b')
        console.log(b)
        b.appendChild(selectbox_)
        fetch('/getTemplate', {
            method: 'post',
            json: {
                'web': 'Ticketplus'
            }
        })
            .then(response => response.json())
            .then(data => {
                template = data.template;
                addItemsToDOM(template);
            })
            .catch(error => {
                console.error('Error:', error);
            });
        function addItemsToDOM(template) {
            const container = document.getElementById('template-container');
            if (Array.isArray(template)) {
                template.forEach(item => {

                    const div = document.createElement('div');
                    const h3 = document.createElement('h3');
                    h3.textContent = item;
                    h3.style.userSelect = 'none';
                    div.className = 'item'
                    div.appendChild(h3);
                    // div.id = item;
                    div.addEventListener('click', function () {
                        window.location.href = `${window.location.href}?template=${item}`;
                    })
                    console.log(div)
                    console.log(container)
                    container.appendChild(div);
                });
            } else {
                for (const key in template) {
                    if (template.hasOwnProperty(key)) {
                        const div = document.createElement('div');
                        div.textContent = `${key}: ${template[key]}`;
                        container.appendChild(div);
                    }
                }
            }
        }
    }
    else {
        const url = new URL(window.location.href);
        const pathSegments = url.pathname.split('/');
        const webname = pathSegments[pathSegments.indexOf('practice') + 1];

        document.body.innerHTML = '';
        document.body.style.backgroundColor = 'initial';
        fetch('/getTemplate_', {
            method: 'post',
            json: {
                'web': 'Ticketplus'
            }
        })
            .then(response => response.json())
            .then(data => {
                document.body.innerHTML = data.TemplateHTML;
                loadCSS(`/static/css/practice/${webname}.css`);
            })
        function loadCSS(href) {
            const link = document.createElement('link');
            link.rel = 'stylesheet';
            link.type = 'text/css';
            link.href = href;
            document.head.appendChild(link);
        }
    }


})