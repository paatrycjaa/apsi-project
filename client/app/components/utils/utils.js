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
      this.sizeToString = (size) => {
        mb = 1000000
        kb = 1000
        if(size > mb){
          return (size / mb).toString() + ' MB'
        }
        if(size > kb) {
          return  (size / kb).toString() + ' kB'
        }

        return  size.toString() + ' B'
      }
    }
);
  
  