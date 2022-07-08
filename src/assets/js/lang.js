const lang_btn = document.querySelector("#lang_switcher_btn");

function switch_lang() {
    if (localStorage.getItem("lang") === "rus") {
        localStorage.setItem("lang", "eng")
        lang_btn.innerHTML = 'eng'
    } else {
        localStorage.setItem("lang", "rus")
        lang_btn.innerHTML = 'rus'
    }
    load_lang(lang_btn.innerHTML)
}

lang_btn.addEventListener('click', switch_lang)

function change_lang(lang) {
    console.log(lang)
    for (let key in lang) {
        try {
            document.querySelector('.' + key).innerHTML = lang[key]
        } catch (e) {
            console.error(e)
        }
    }
}

function load_lang(code) {
    const requestURLEng = `././languages/${code}.json`;

    const request = new XMLHttpRequest();
    request.open('GET', requestURLEng);
    request.send();

    request.onload = function () {
        const res = JSON.parse(request.responseText)
        change_lang(res)
    }
}

if (localStorage.getItem("lang") === "rus") {
    lang_btn.innerHTML = 'rus'
} else {
    localStorage.setItem("lang", "eng")
    lang_btn.innerHTML = 'eng'
}
load_lang(lang_btn.innerHTML)
