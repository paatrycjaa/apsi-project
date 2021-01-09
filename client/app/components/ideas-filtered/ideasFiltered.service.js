angular.module('appIdeasFilteredService', [])
  .service('ideasFilteredService',
    function($http) {
      this.getIdeas = function(callback) {
        return $http.get('/ajax/filtered_ideas/').then(callback);
      }
    }
  );
