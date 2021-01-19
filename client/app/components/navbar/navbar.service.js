angular.module('appNavbarService', []).service('navbarService',
  function($http) {
    this.getUserData = function(success, fail) {
      return $http.get('/ajax/me/').then(success, fail);
    };
  }
)