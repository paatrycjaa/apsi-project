angular.module('appDecisionAdditionController', [])
  .controller('decisionAdditionController', ['$scope', 'decisionAdditionService', '$timeout', 'utils',


  function($scope, decisionAdditionService, $timeout, utils) {

        $scope.opinions = [];

        $scope.decision = {
          id: '',
          werdykt : '',
          description : ''
        }


        $scope.init = function(id) {
           $scope.decision.id=id;
           $scope.$watch("idea_id", function() {

            $scope.idea_id=id
            console.log(id)
            decisionAdditionService.getIdeaById($scope.idea_id, function(response) {
              $scope.idea = response.data[0]
              console.log($scope.idea)
            });



            decisionAdditionService.getIdeaOpinions($scope.idea_id, function(response) {
              $scope.opinions = response.data;
              console.log($scope.opinions)
            })
          });
        }

        

        $scope.settings = '';
        $scope.reponse_received = false;
        $scope.status = true;

        $scope.submit = function() {
          const forms = document.getElementsByClassName('form-decision');
          if (utils.isFormValid(forms)) {
            decisionAdditionService.submitDecision($scope.decision, (response) => {            
              console.log(response);
              $scope.status = response.data.status;
              $scope.reponse_received = true;
              if ($scope.status === true) {
                $timeout(() => { 
                  window.location.href = redirect_url;
                }, 2000);
              }
            });
          }
        }       


      }
]);
