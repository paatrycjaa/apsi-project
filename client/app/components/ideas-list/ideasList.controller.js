angular.module('appIdeasListController', [])
  .controller('ideasListController', ['$scope', '$window', '$interval', 'ideasListService',
      function($scope, $window, $interval, ideasListService) {
        
        $scope.ideas = [];

        $scope.init = function() {
          ideasListService.getIdeas(function(response) {
            $scope.ideas = response.data
          });
        }

        $scope.ideaVisible = function(idea) {
          return idea.fields.status == 'Oczekujacy'
        }

        $scope.openIdeaOpinions = function(id) {
          $window.location.href = `/opinions/${id}/`;
        }

        $scope.blockIdea = function(id) {
          ideasListService.blockIdea(id, () => {
            $window.location.reload();
          });
        }
      }
]);
