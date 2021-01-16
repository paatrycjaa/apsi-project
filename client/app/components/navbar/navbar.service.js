angular.module('appNavbarService', []).service('navbarService',
  function($http) {
    this.getMe = function(callback) {
      return $http.get('/ajax/me/').then(callback);
    };
  }
)