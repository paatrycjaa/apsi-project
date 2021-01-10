angular.module('appMyIdeasListController', [])
  .controller('myIdeasListController', ['$scope', '$window', '$document','myIdeasListService',
      function($scope, $window, $document, myIdeasListService) {
        
        $scope.ideas_rest = [];
        $scope.ideas_to_edit = [];

        $scope.init = function() {
          myIdeasListService.getUserIdeas(function(response) {
            for (idea of response.data) {
              if (idea.fields.status == 'Edycja') {
                $scope.ideas_to_edit.push(idea);
              } else {
                $scope.ideas_rest.push(idea);
              }
            }
            console.log('Ideas to edit');
            console.log($scope.ideas_to_edit);
            console.log('Rest of ideas');
            console.log($scope.ideas_rest);
          });

          
        }

        $scope.openIdeaOpinions = function(id) {
          $window.location.href = `/opinions/${id}/`;
        }

        $scope.editIdea = function(id) {
          // $window.location.href = `//${id}/`;
          console.log('Redirect to idea edit');
        }
      }
]);
