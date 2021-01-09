angular.module('appIdeasFilteredOdlozonyService', [])
  .service('ideasFilteredOdlozonyService',
    function($http) {
      this.getIdeas = function(callback) {
        return $http.get('/ajax/filtered_ideas/').then(callback);
      }
    }
  );
