angular.module('appIdeasListController', [])
  .controller('ideasListController', ['$scope', '$window', 'ideasListService', 'utils',
      function($scope, $window, ideasListService, utils) {

        $scope.ideas = [];

        $scope.init = function() {
          ideasListService.getIdeas(function(response) {
            $scope.ideas = response.data
            for (idea of $scope.ideas) {
              idea['dni_od_dodania'] = utils.calculateDaysSinceSubmit(idea.data_dodania);
            }
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
          if(selected=="wszystkie"|| selected==undefined)
          {
            return (idea.status_pomyslu_id == "Oczekujacy" ||
            idea.status_pomyslu_id == 'Odlozony' || idea.status_pomyslu_id == 'Odrzucony' ||
            idea.status_pomyslu_id == 'Zaakceptowany' )
          }
          else {
            return idea.status_pomyslu_id == selected;
          }
        }

        $scope.removeIdea = function(id) {
          ideasListService.removeIdea(id, () => {
            $window.location.reload();
          });
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
