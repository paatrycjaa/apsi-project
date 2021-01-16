angular.module('appOpinionsListController', [])
  .controller('opinionsListController', ['$scope', 'opinionsListService', 'utils',
  function($scope, opinionsListService, utils) {

        $scope.opinions = [];

        $scope.idea = null;

        $scope.addOpinion=function(){
          id=$scope.idea_id
          window.location.href = `/add-opinion/${id}/`;
        }

        $scope.editOpinion = function(opinion_id){
          window.location.href = `/edit-opinion/${opinion_id}/`;
        }

        $scope.canAddOpinion = function() {
          if($scope.idea === null){
             return false;
          }
          return $scope.idea.status_pomyslu_id === "Oczekujacy" &&
                 $scope.idea.ustawienia_oceniania_id !== "brak" &&
                 $scope.idea.rated === false &&
                 $scope.idea.my_idea === false;
        }

        $scope.init = function(id) {

          $scope.idea_id=id
          opinionsListService.getIdeaById($scope.idea_id, function(response) {
            $scope.idea = response.data
            $scope.idea.attachments.forEach(att => {
              att.rozmiar = utils.sizeToString(att.zalacznik__rozmar)
            });
          });

          opinionsListService.getIdeaOpinions($scope.idea_id, function(response) {
            $scope.opinions = response.data;
          })

        }
      }
])
.directive('opinionsIdeaTable', function(){
  return {
    restrict: 'E',
    scope: {
      idea: '='
    },
    templateUrl: '/app/client/app/components/utils/partials/full-idea-table.html'
  }
});
