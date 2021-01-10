angular.module('appOpinionsListController', [])
  .controller('opinionsListController', ['$scope', 'opinionsListService',
  function($scope, opinionsListService) {
        
        $scope.opinions = [];

        $scope.addOpinion=function(){
          id=$scope.idea_id
          window.location.href = `/add-opinion/${id}/`; 
        }

        $scope.editOpinion = function(opinion_id){
          window.location.href = `/edit-opinion/${opinion_id}/`; 
        }

        $scope.init = function(id) {
            
          $scope.idea_id=id            
          opinionsListService.getIdeaById($scope.idea_id, function(response) {
            $scope.idea = response.data
            console.log(response.data)
            $scope.idea.attachments.forEach(att => {
              mb = 1000000
              kb = 1000
              if(att.zalacznik__rozmar > mb){
                att.rozmiar = (att.zalacznik__rozmar / mb).toString() + ' MB'
              } else if(att.zalacznik__rozmar > kb) {
                att.rozmiar = (att.zalacznik__rozmar / kb).toString() + ' kB'
              } else {
                att.rozmiar = att.zalacznik__rozmar.toString() + ' B'
              }

              
            });
          });

          opinionsListService.getIdeaOpinions($scope.idea_id, function(response) {
            $scope.opinions = response.data;              
          })
        
        }
      }
]);

