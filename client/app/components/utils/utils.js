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

      this.sendPostRequest = (http, data, files, callback, url) => {
        let formData = new FormData();

        data.attachments = []        
        data.attachments_size = []
        
        for (let i = 0; i < files.length; i++) {
          data.attachments.push(files[i].name)
          data.attachments_size.push(files[i].size)
          formData.append('file_' + i.toString(), files[i]);
        }

        formData.append('data', JSON.stringify(data));
        
        return http.post(url, formData, {
          headers: {'Content-Type': undefined },
          transformRequest: angular.identity
        }).then(callback)
      }

      this.checkAttachments = (files) => {
        const max_size = 10000000;  // 10 MB
        let bad_files = [];

        for (let i = 0; i < files.length; i++) {
          file = files.item(i);

          if(file.size > max_size){
            bad_files.push(file.name);
          }
        }

        if(bad_files.length > 0){
          alert('Wybrane pliki: ' + bad_files.join(' ') + ' są za duże. Maksymalny rozmiar to 10 MB.');
          return [];
        }

        return files;

      }

      this.calculateDaysSinceSubmit = (date_addition) => {
        date_created = new Date(date_addition);
        date_now = new Date();
        return Math.floor((date_now - date_created)/(1000*60*60*24));
      }
    }
);
  
  