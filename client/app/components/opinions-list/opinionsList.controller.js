angular.module('appOpinionsListController', [])
  .controller('opinionsListController', ['$scope', '$interval', 'opinionsListService',
      function($scope, $interval, opinionsListService) {
        
        $scope.opinions = [];

        $scope.init = function() {
          opinionsListService.getOpinions(function(response) {
            $scope.opinions = response.data
            console.log($scope.opinions)
            // $scope.idea = {'tematyka': 'komputery', 'opis': '123', 'planowane_korzysci': "123", 'planowane_koszty': "123", "ocena_wazona": 6};
            // $scope.opinions = [{'data': "2020", "ocena_liczbowa": 6, 'opis': 'Very good'}];
          });
        }
      }
]);
