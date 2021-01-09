angular.module('appideasFilteredOdlozonyController', [])
  .controller('ideasFilteredOdlozonyController', ['$scope', '$window', '$interval', 'ideasFilteredOdlozonyService',
      function($scope, $window, $interval, ideasFilteredOdlozonyService) {
        
        $scope.ideas = [];

        $scope.init = function() {
          ideasFilteredOdlozonyService.getIdeas(function(response) {
            $scope.ideas = response.data
            console.log($scope.ideas)
          });
        }

        $scope.openIdeaDecision = function(id) {
          $window.location.href = `/add_decision/${id}/`;
        }
      }
]);
