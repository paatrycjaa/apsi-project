angular.module('appOpinionAdditionService', [])
  .service('opinionAdditionService',
    function($http) {
      this.getOpinionById = function(id, callback) {
        return $http.get(`/ajax/get_opinion/${id}/`).then(callback);
      }
      this.submitOpinion = function( data, callback) {
         const url = '/ajax/submit_opinion/'
         return $http.post(url, JSON.stringify(data)).then(callback)
      }

      this.editOpinion = function( data, callback) {
          const url = '/ajax/edit_opinion/'
          return $http.post(url, JSON.stringify(data)).then(callback)
      }
    }
  );
