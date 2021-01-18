angular.module('appOpinionAdditionController', [])
  .controller('opinionAdditionController', ['$scope', '$timeout', 'opinionAdditionService', 'utils',
    function($scope, $timeout, opinionAdditionService, utils) {

      $scope.opinion = {
        idea_id: '',
        opinion_id: '',
        description : '',
        rate : 0
      }

      $scope.settings = '';

      $scope.init = function(idea_id) {
        // do edycji mozna tutaj pobierac dane o opinii
        $scope.opinion.idea_id = idea_id;
        $scope.opinion.opinion_id = opinionId;
        $scope.settings = opinionSettings;

        console.log(idea_id, opinionId, opinionSettings)

        if(opinionId){
          opinionAdditionService.getOpinionById(opinionId, function(response) {
            data = response.data[0]
            $scope.opinion.description = data.opis
            $scope.opinion.rate = data.ocena_liczbowa

          })
        }
      }

      $scope.reponse_received = false;
      $scope.status = true;

      $scope.submit = function() {
        const forms = document.getElementsByClassName('needs-validation');
        if (utils.isFormValid(forms)) {

          callback = (response) => {
            console.log(response);
            $scope.status = response.data.status;
            $scope.reponse_received = true;
            if ($scope.status === true) {
              $timeout(() => {
                window.location.href = "/opinions/" + $scope.opinion.idea_id;
              }, 2000);
            }
         };

          // opinion is edited
          if($scope.opinion.opinion_id){
            opinionAdditionService.editOpinion($scope.opinion, callback);
          } else { // new opinion is added
            opinionAdditionService.submitOpinion($scope.opinion, callback);
          }
        }
      }
    }
]);
