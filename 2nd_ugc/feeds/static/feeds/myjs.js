$(document).ready(() => {
    $('#hamburger').on('click', () => {
        $('#sidebar').fadeIn();
    })
    $('#sidebar').on('click', () => {
        $('#sidebar').fadeOut();
    })
    var str = $('#textarea').val();
    str = str.replace(/(?:\r\n|\r|\n)/g, '<br/>');
    $('#textarea').val(str);
})