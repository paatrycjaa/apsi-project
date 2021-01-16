angular.module('appNavbarController', [])
  .controller('navbarController', ['$scope', 'navbarService',
    function($scope, navbarService) {

      $scope.init = function() {
        navbarService.getMe().then((resp) => {
          console.log(resp);
          console.log('I am normal user')
        });
      };
    }
  ]
);