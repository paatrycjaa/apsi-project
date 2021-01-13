angular.module('appIdeasListController', [])
  .controller('ideasListController', ['$scope', '$window', '$interval', 'ideasListService',
      function($scope, $window, $interval, ideasListService) {
        
        $scope.ideas = [];

        $scope.init = function() {
          ideasListService.getIdeas(function(response) {
            $scope.ideas = response.data
          });
        }

        $scope.openIdeaOpinions = function(id) {
          $window.location.href = `/opinions/${id}/`;
        }

        $scope.blockIdea = function(id) {
          ideasListService.blockIdea(id, () => {
            $window.location.reload();
          });
        }


        $scope.ideaShown = function(idea) {
          selected=$scope.Select1
          console.log(idea,selected);
          if(selected=="wszystkie"|| selected==undefined)
          {
            return true;
          }
          else {
            return idea.status_pomyslu_id == selected;
          }
        }




      }
])
.directive('ideaTable', function(){
  return {
    restrict: 'E',
    scope: {
      idea: '=',
      showAttachmentsCount: '='
    },
    templateUrl: '/app/client/app/components/utils/partials/idea-table.html'
  }
});
