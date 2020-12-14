angular.module('appOpinionsListController', [])
  .controller('opinionsListController', ['$scope', '$interval', 'opinionsListService',
      function($scope, $interval, opinionsListService) {
        
        $scope.opinions = [];
        $scope.ideas = [];

        // $scope.init = function() {
        //   opinionsListService.getOpinions(function(response) {
        //     $scope.opinions = response.data
        //     console.log($scope.opinions)
        //   });

          // opinionsListService.getIdeas(function(response) {
          //   $scope.ideas = response.data
          //   console.log($scope.ideas)
          // });
        }
      }
]);
