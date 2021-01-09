angular.module('appMyIdeasListService', [])
  .service('myIdeasListService',
    function($http) {
      this.getUserIdeas = function(callback) {
        return $http.get('/ajax/user_ideas/', JSON).then(callback);
      }
    }
  );
