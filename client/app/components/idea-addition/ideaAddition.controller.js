angular.module('appIdeaAdditionController', [])
  .controller('ideaAdditionController', ['$scope', '$timeout', 'ideaAdditionService', 'utils',
  function($scope, $timeout, ideaAdditionService, utils) {

        $scope.ideaModel = {
          topic : '',
          description : '',
          benefits : '',
          costs : '',
          attachement : '',
          num_rating : true,
          text_rating : true
        }        
                
        $scope.init = function() {
          // do edycji mozna tutaj pobierac dane o pomysle
        }

        $scope.reponse_received = false
        $scope.status = true

        $scope.submit = function() {
          const forms = document.getElementsByClassName('needs-validation');
          if (utils.isFormValid(forms)) {
            ideaAdditionService.submitIdea($scope.ideaModel,(response) => {            
              console.log(response)
              $scope.status = response.data.status
              $scope.reponse_received = true
  
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
