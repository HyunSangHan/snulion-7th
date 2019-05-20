$(document).ready(() => {
    $('#hamburger').on('click', () => {
        $('#sidebar').fadeIn();
    })
    $('#sidebar').on('click', () => {
        $('#sidebar').fadeOut();
    })
})