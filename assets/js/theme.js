const body = document.querySelector("body");
const theme_btn = document.querySelector("#theme_switcher_btn");

let theme_flag = false;


function switch_theme() {
    if (theme_flag) {
        localStorage.setItem("theme", "day");
        theme_flag = false;
        theme_btn.innerHTML = 'dark'
        body.className = " ";
    } else {
        localStorage.setItem("theme", "night");
        theme_flag = true;
        theme_btn.innerHTML = 'light'
        body.className = " dark-theme";
    }

}

theme_btn.addEventListener('click', switch_theme)

console.log(localStorage.getItem("theme"))
if (localStorage.getItem("theme") == "night") {
    theme_btn.innerHTML = 'light'
    theme_flag = true;
    body.className = " dark-theme";
}
