const lang_btn = document.querySelector("#lang_switcher_btn");

function switch_lang() {
    if (localStorage.getItem("lang") === "ru") {
        localStorage.setItem("lang", "eng")
        lang_btn.innerHTML = 'eng'
    } else{
        localStorage.setItem("lang", "ru")
        lang_btn.innerHTML = 'ru'
    }
    change_lang(lang_btn.innerHTML)

}

lang_btn.addEventListener('click', switch_lang)

function change_lang(lang_code) {
    const requestURLEng = `languages/${lang_code}.json`;

    const request = new XMLHttpRequest();
    request.open('GET', requestURLEng);
    request.send();

    request.onload = function () {
        const res = JSON.parse(request.responseText);
        lang = res
    }

    for (let key in lang) {
        try {
            console.log(lang[key])
            document.querySelector('.' + key).innerHTML = lang[key]
        } catch (e){
            console.error(e)
        }
    }
}


change_lang(lang_btn.innerHTML)
