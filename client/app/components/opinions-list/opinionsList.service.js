angular.module('appOpinionsListService', [])
  .service('opinionsListService',
    function($http) {
      this.getOpinions = function(callback) {
        return $http.get('/ajax/all_opinions/').then(callback);
      }
    }
  );
