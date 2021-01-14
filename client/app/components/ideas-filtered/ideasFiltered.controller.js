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

        $scope.zmienstatus = function(id, new_status) {
          $scope.statusup.id=id
          $scope.statusup.status_update=new_status
          console.log($scope.statusup)
          ideasFilteredService.zmienstatuspomyslu($scope.statusup, (response) => {            
            console.log(response);
            $window.location.reload();
          });
        }

        $scope.id_to_del={
          id:''
        }
        $scope.removeIdea = function(id) {
          $scope.id_to_del.id=id
          console.log($scope.statusup)
          ideasFilteredService.removeIdea($scope.id_to_del, (response) => {
            console.log(response);
            $window.location.reload();
          });
        }      
      }
]);
