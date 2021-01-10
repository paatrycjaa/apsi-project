angular.module('appIdeaAdditionService', [])
  .service('ideaAdditionService',
    function($http) {
      this.getIdeaById = function(id, callback) {
        return $http.get(`/ajax/get_idea/${id}/`).then(callback);
      }
      this.submitIdea = function(data, file, callback) { 
        var formData = new FormData();

        data.attachment = file.name

        formData.append('data', JSON.stringify(data));
        formData.append('file', file);

        return $http.post('/ajax/submit_idea/', formData, {
          headers: {'Content-Type': undefined },
          transformRequest: angular.identity
      })
      }

      this.editIdea = function( data, callback) { 
        var url = '/ajax/edit_idea/'
        return $http.post(url, JSON.stringify(data)).then(callback)
      }
      this.getKeywords = function(callback) {
        return $http.get('/ajax/get_keywords').then(callback)
      }
    }
  );
