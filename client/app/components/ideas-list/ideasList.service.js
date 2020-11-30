angular.module('appIdeasListService', [])
  .service('ideasListService',
    function($http) {
      this.getIdeas = function(callback) {
        return $http.get('/ajax/all_ideas/').then(callback);
      }
    }
  );
