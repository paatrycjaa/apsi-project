angular.module('appIdeasFilteredController', [])
  .controller('ideasFilteredController', ['$scope', '$window', '$interval', 'ideasFilteredService',
      function($scope, $window, $interval, ideasListService) {
        
        $scope.ideas = [];

        $scope.init = function() {
          ideasListService.getIdeas(function(response) {
            $scope.ideas = response.data
            console.log($scope.ideas)
          });
        }

        $scope.openIdeaDecision = function(id) {
          $window.location.href = `/add_decision/${id}/`;
        }
      }
]);
