angular.module('appStartPageService', []).service('startPageService',
  function($http) {
    this.getStats = function(callback) {
      return $http.get('/ajax/stats/').then(callback);
    };
  }
)