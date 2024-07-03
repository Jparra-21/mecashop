document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById('form-login');
    const email = document.getElementById('username');
    const password = document.getElementById('password');
    var valid1 = false;
    var valid2 = false;

    if (form) {
        form.addEventListener('submit', e => {
            e.preventDefault();

            validateInputs();
            if(valid1 && valid2){
                form.submit();
                window.location.href = "infouser.html";
            }
        });
    }

    const setError = (element, message) => {
        const inputControl = element.parentElement;
        const errorDisplay = inputControl.querySelector('.error');

        errorDisplay.innerText = message;
        inputControl.classList.add('error');
        inputControl.classList.remove('success');
    };

    const setSuccess = element => {
        const inputControl = element.parentElement;
        const errorDisplay = inputControl.querySelector('.error');

        errorDisplay.innerText = '';
        inputControl.classList.add('success');
        inputControl.classList.remove('error');
    };

    const isValidEmail = email => {
        const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(String(email).toLowerCase());
    };

    const validateInputs = () => {
        const emailValue = email.value.trim();
        const passwordValue = password.value.trim();

        if(emailValue === '') {
            setError(email, 'Email requerido');
        } else if (!isValidEmail(emailValue)) {
            setError(email, 'Ingrese un email valido');
        } else {
            valid1 = true;
            setSuccess(email);
        }

        if(passwordValue === '') {
            setError(password, 'Contraseña requerida');
        } else if (passwordValue.length < 8 ) {
            setError(password, 'La contraseña debe tener al menos 8 caracteres.');
        } else {
            valid2 = true;
            setSuccess(password);
        }
    };
});
