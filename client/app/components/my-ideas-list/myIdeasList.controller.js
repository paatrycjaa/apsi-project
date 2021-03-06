angular.module('appMyIdeasListController', [])
  .controller('myIdeasListController', ['$scope', '$window', '$document','myIdeasListService', 'utils',
      function($scope, $window, $document, myIdeasListService, utils) {
        
        $scope.ideas_rest = [];
        $scope.ideas_to_edit = [];

        $scope.init = function() {
          myIdeasListService.getUserIdeas(function(response) {
            for (idea of response.data) {
              idea['dni_od_dodania'] = utils.calculateDaysSinceSubmit(idea.data_dodania);
              if (idea.status_pomyslu_id == 'Edycja') {
                $scope.ideas_to_edit.push(idea);
              } else {
                $scope.ideas_rest.push(idea);
              }
            }
          });
        }

        $scope.openIdeaOpinions = function(id) {
          $window.location.href = `/opinions/${id}/`;
        }

        $scope.editIdea = function(id) {
          $window.location.href = `/edit-idea/${id}/`;
        }
      }
])
.directive('myIdeaTable', function(){
  return {
    restrict: 'E',
    scope: {
      idea: '=',
      showAttachmentsCount: '='
    },
    templateUrl: '/app/client/app/components/utils/partials/idea-table.html'
  }
});
