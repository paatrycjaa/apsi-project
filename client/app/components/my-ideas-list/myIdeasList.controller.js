angular.module('appMyIdeasListController', [])
  .controller('myIdeasListController', ['$scope', '$window', 'myIdeasListService',
      function($scope, $window, myIdeasListService) {
        
        $scope.user_ideas = [];

        $scope.init = function() {
          myIdeasListService.getUserIdeas(function(response) {
            $scope.user_ideas = response.data
            console.log($scope.user_ideas)
          });
        }

        // $scope.ideaVisible = function(idea) {
        //   return idea.fields.status == 'Oczekujacy'
        // }

        $scope.openIdeaOpinions = function(id) {
          $window.location.href = `/opinions/${id}/`;
        }
      }
]);
