angular.module('appIdeasFilteredController', [])
  .controller('ideasFilteredController', ['$scope', '$window', '$interval', 'ideasFilteredService',
      function($scope, $window, $interval, ideasFilteredService) {
        
        $scope.ideas_rest = [];
        $scope.ideas = [];

        $scope.init = function(status) {
          $scope.status=status
          console.log($scope.status)
          ideasFilteredService.getIdeas(function(response) {
            for (idea of response.data) {
              if (idea.status_pomyslu_id == status) {
                $scope.ideas.push(idea);
              } else {
                $scope.ideas_rest.push(idea);
              }
            }
            console.log($scope.ideas)
            console.log(response.data)
          });
        }


        $scope.openIdeaDecision = function(id) {
          $window.location.href = `/add_decision/${id}/`;
        }

        $scope.reponse_received = false;
        $scope.status2 = true;

        $scope.statusup = {
          id: '',
          status_update: ''
        }

        $scope.wznow = function(id) {
          $scope.statusup.id=id
          $scope.statusup.status_update="Oczekujacy"
          console.log($scope.statusup)
          ideasFilteredService.wznowpomysl($scope.statusup, (response) => {            
            console.log(response);
            $window.location.reload();
          });
        }       
      }
]);
