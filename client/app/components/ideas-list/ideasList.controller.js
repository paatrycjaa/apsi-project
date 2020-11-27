angular.module('appIdeasListController', [])
  .controller('ideasListController', ['$scope', '$interval', 'ideasListService',
      function($scope, $interval, ideasListService) {
        
        $scope.ideas = [];

        $scope.init = function() {
          ideasListService.getIdeas(function(response) {
            $scope.ideas = response.data
            console.log($scope.ideas)
          });
        }
      }
]);
