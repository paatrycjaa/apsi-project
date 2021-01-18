angular.module('appOpinionsListService', [])
  .service('opinionsListService',
    function($http) {
      this.getIdeaById = function(id, callback) {
        return $http.get(`/ajax/get_idea/${id}/`).then(callback);
      }

      this.getIdeaOpinions = function(id, callback) {
        return $http.get(`/ajax/all_opinions/${id}/`).then(callback);
      }

      this.removeOpinion = function(id, callback) {
        return $http.get(`/ajax/remove_opinion/${id}/`).then(callback);
      }
    }
  );
