angular.module('appNavbarController', [])
  .controller('navbarController', ['$scope', 'navbarService',
    function($scope, navbarService) {

      $scope.userData = {
        firstName: '',
        lastName: '',
        role: '',
      }

      $scope.init = function() {
        navbarService.getUserData().then((resp) => {
          $scope.userData = resp.data;
        }, () => {
          $scope.userData = {
            firstName: '',
            lastName: '',
            role: '',
          }
        });
      };
    }
  ]
);