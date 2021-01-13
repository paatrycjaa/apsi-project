angular.module('appStartPageController', [])
  .controller('startPageController', ['$scope', '$interval',
  function($scope, $interval) {

    $scope.numbers = [13, 53, 2137, 1410, 71];
    $scope.messages = [
      'DZIŚ DODANYCH POMYSŁÓW',
      'DZIŚ DODANYCH OPINII',
      'DODANYCH POMYSŁÓW',
      'DODANYCH OPINII',
      'WYDANYCH DECYZJI',
    ]

    $scope.id = 0;
    $interval(function() {
      $scope.id = ($scope.id + 1) % $scope.numbers.length;
    }, 3000);


  }
]);