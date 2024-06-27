document.addEventListener('DOMContentLoaded', function () {
  const forms = document.querySelectorAll('.auth-form');


  forms.forEach(form => {
    form.addEventListener('submit', function (event) {
      const inputs = form.querySelectorAll('input[type="text"], input[type="password"]');
      let valid = true;

      inputs.forEach(input => {
        if (input.value.trim() === '') {
          input.style.border = '2px solid red';
          valid = false;
        } else {
          input.style.border = 'none';
        }
      });

      if (!valid) {
        event.preventDefault();
        alert('Please fill in all fields.');
      }
    });

    form.addEventListener('focusin', function (event) {
      const input = event.target;
      input.style.border = '2px solid #6a11cb';
    });

    form.addEventListener('focusout', function (event) {
      const input = event.target;
      if (input.value.trim() === '') {
        input.style.border = '2px solid red';
      } else {
        input.style.border = 'none';
      }
    });
  });
});


