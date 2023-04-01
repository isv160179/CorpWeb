const togglePassword = document.querySelector('#togglePassword');
const password = document.querySelector('#id_password');
const eye = '/static/users/img/sprite.svg#eye';
const eye_slash = '/static/users/img/sprite.svg#eye-slash';

togglePassword.addEventListener('click', function (e) {
    const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
    const url = togglePassword.getAttribute('href') === eye ? eye_slash : eye;
    password.setAttribute('type', type);
    togglePassword.setAttribute('href', url)
});