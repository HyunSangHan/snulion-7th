$(document).ready(() => {
    $('#hamburger').on('click', () => {
        $('#sidebar').show();
    })
    $('#sidebar').on('click', () => {
        $('#sidebar').hide();
    })
})