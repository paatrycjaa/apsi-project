angular.module('appIdeaAdditionService', [])
  .service('ideaAdditionService',
    function($http) {
      this.getIdeaById = function(id, callback) {
        return $http.get(`/ajax/get_idea/${id}/`).then(callback);
      }
      this.submitIdea = function(data, callback) { 
        return $http.post('/ajax/submit_idea/', JSON.stringify(data)).then(callback) }

      this.editIdea = function( data, callback) { 
        var url = '/ajax/edit_idea/'
        return $http.post(url, JSON.stringify(data)).then(callback)
      }
      this.getKeywords = function(callback) {
        return $http.get('/ajax/get_keywords').then(callback)
      }
    }
  );
