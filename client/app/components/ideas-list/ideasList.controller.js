angular.module('appIdeasListController', [])
  .controller('ideasListController', ['$scope', '$window', '$interval', 'ideasListService',
      function($scope, $window, $interval, ideasListService) {
        
        $scope.ideas = [];

        $scope.editIdea = function(idea_id){
          window.location.href = `/edit-idea/${idea_id}/`; 
        }


        $scope.init = function() {
          ideasListService.getIdeas(function(response) {
            $scope.ideas = response.data
            console.log($scope.ideas)
          });
        }

        $scope.ideaVisible = function(idea) {
          return idea.fields.status == 'Oczekujacy'
        }

        $scope.openIdeaOpinions = function(id) {
          $window.location.href = `/opinions/${id}/`;
        }

        $scope.blockIdea = function(id) {
          callback = (response) => {            
            console.log(response);
        };
          ideasListService.editIdea({idea_id: id}, callback)
          $window.location.reload();
        }
      }
]);
