angular.module('appOpinionsListController', [])
  .controller('opinionsListController', ['$scope', 'opinionsListService',
      
  
  
  
  function($scope, opinionsListService) {
        
        $scope.opinions = [];

        $scope.addOpinion=function(){
          id=$scope.idea_id
          window.location.href = `/add-opinion/${id}/`; 
        }


        $scope.init = function(id) {
          // $scope.$watch("idea_id", function() {
            
            $scope.idea_id=id
            // console.log(id)
            // opinionsListService.getIdeaById($scope.idea_id, function(response) {
            //   $scope.idea = response.data[0]
            //   console.log($scope.idea)
            // });



            // opinionsListService.getIdeaOpinions($scope.idea_id, function(response) {
            //   $scope.opinions = response.data;
            //   console.log($scope.opinions)
            // })
          // });
        }
      }
]);
