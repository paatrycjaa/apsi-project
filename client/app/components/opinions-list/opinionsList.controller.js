angular.module('appOpinionsListController', [])
  .controller('opinionsListController', ['$scope', 'opinionsListService',
      function($scope, opinionsListService) {
        
        $scope.opinions = [];

        $scope.init = function() {
          $scope.$watch("idea_id", function() {
            opinionsListService.getIdeaById($scope.idea_id, function(response) {
              $scope.idea = response.data[0]
              console.log($scope.idea)
            });

            opinionsListService.getIdeaOpinions($scope.idea_id, function(response) {
              $scope.opinions = response.data;
              console.log($scope.opinions)
            })
          });
        }
      }
]);
