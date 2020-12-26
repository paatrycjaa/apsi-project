angular.module('appOpinionAdditionController', [])
  .controller('opinionAdditionController', ['$scope', '$timeout', 'opinionAdditionService', 'utils',
    function($scope, $timeout, opinionAdditionService, utils) {

      $scope.opinion = {
        id: '',
        description : '',
        rate : 0
      }
      
      $scope.settings = '';

      $scope.init = function(id) {
        // do edycji mozna tutaj pobierac dane o opinii
        $scope.opinion.id = id;
        $scope.settings = opinionSettings;
      }

      $scope.reponse_received = false;
      $scope.status = true;

      $scope.submit = function() {
        const forms = document.getElementsByClassName('needs-validation');
        if (utils.isFormValid(forms)) {
          opinionAdditionService.submitOpinion($scope.opinion, (response) => {            
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
