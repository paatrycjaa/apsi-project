angular.module('appNavbarService', []).service('navbarService',
  function($http) {
    this.getUserData = function(callback) {
      return $http.get('/ajax/me/').then(callback);
    };
  }
)