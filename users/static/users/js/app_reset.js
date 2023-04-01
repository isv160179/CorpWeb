const togglePassword_new_1 = document.querySelector('#togglePassword_new_1');
const togglePassword_new_2 = document.querySelector('#togglePassword_new_2');
const password_new_1 = document.querySelector('#id_new_password1');
const password_new_2 = document.querySelector('#id_new_password2');
const eye = '/static/users/img/sprite.svg#eye';
const eye_slash = '/static/users/img/sprite.svg#eye-slash';


togglePassword_new_1.addEventListener('click', function (e) {
    const type1 = password_new_1.getAttribute('type') === 'password' ? 'text': 'password';
    const url1 = togglePassword_new_1.getAttribute('href') === eye ? eye_slash: eye;
    password_new_1.setAttribute('type', type1);
    password_new_2.setAttribute('type', type1);
    togglePassword_new_1.setAttribute('href', url1)
    togglePassword_new_2.setAttribute('href', url1)
});

togglePassword_new_2.addEventListener('click', function (e) {
    const type2 = password_new_2.getAttribute('type') === 'password' ? 'text': 'password';
    const url2 = togglePassword_new_1.getAttribute('href') === eye ? eye_slash: eye;
    password_new_1.setAttribute('type', type2);
    password_new_2.setAttribute('type', type2);
    togglePassword_new_1.setAttribute('href', url2)
    togglePassword_new_2.setAttribute('href', url2)
});