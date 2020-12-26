angular.module('appUtils', [])
  .service('utils',
    function() {
      this.isFormValid = (forms) => {
        let isValid = true;
        Array.prototype.filter.call(forms, (form) => {
          if (form.checkValidity() === false) {
            isValid &= false;
          }
          form.classList.add('was-validated');
        });
        return isValid;
      }
    }
  );
  