const easyMDE = new EasyMDE({
    autoDownloadFontAwesome: false,
    autosave: {
        enabled: true,
        delay: 1000,
        uniqueId: 'article_content_input'
    },
    element: document.getElementById('article_content_input'),
    initialValue: '## Заголовок \nMarkDown редактор статьи!'
});

function check_article_form(){
    document.getElementById('article_form').submit();
}
