angular.module('appIdeaAdditionService', [])
  .service('ideaAdditionService', ['$http', 'utils',
    function($http, utils)  {
      this.getIdeaById = function(id, callback) {
        return $http.get(`/ajax/get_idea/${id}/`).then(callback);
      }
      this.submitIdea = function(data, files, callback) {
        const url = '/ajax/submit_idea/'
        utils.sendPostRequest($http, data, files, callback, url)
      }

      this.editIdea = function(data, files, callback) {
        const url = '/ajax/edit_idea/'
        utils.sendPostRequest($http, data, files, callback, url)
      }

      this.getKeywords = function(callback) {
        return $http.get('/ajax/get_keywords').then(callback)
      }
    }]
  );
