var theme = true;

function theme_switch() {
    console.log(theme)
    let link_css_theme = document.getElementsByClassName('link_css_theme');
    if (theme) {

        link_css_theme.setAttribute('href', 'assets/index_light_color.css');
    } else {
        link_css_theme.setAttribute('href', 'assets/index_dark_color.css');
    }

    theme = !theme;
}