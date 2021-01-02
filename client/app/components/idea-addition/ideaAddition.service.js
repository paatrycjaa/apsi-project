angular.module('appIdeaAdditionService', [])
  .service('ideaAdditionService',
    function($http) {
      this.getIdeaById = function(id, callback) {
        return $http.get(`/ajax/get_idea/${id}/`).then(callback);
      }
      this.submitIdea = function(data, callback) { 
        console.log(data)
        console.log(JSON.stringify(data))
        return $http.post('/ajax/submit_idea/', JSON.stringify(data)).then(callback) }

      this.editIdea = function( data, callback) { 
        var url = '/ajax/edit_idea/'
        console.log(data)
        console.log(JSON.stringify(data))
        console.log(url)
        return $http.post(url, JSON.stringify(data)).then(callback)
      }
    }
  );
