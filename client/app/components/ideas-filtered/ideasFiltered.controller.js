angular.module('appIdeasFilteredController', [])
  .controller('ideasFilteredController', ['$scope', '$window', '$interval', 'ideasFilteredService',
      function($scope, $window, $interval, ideasFilteredService) {
        
        $scope.ideas = [];

        $scope.init = function(status) {
          $scope.status=status
          console.log($scope.status)
          ideasFilteredService.getIdeas(function(response) {
            $scope.ideas = response.data
            console.log($scope.ideas)
          });
        }


        $scope.openIdeaDecision = function(id) {
          $window.location.href = `/add_decision/${id}/`;
        }
      }
]);
