angular.module('appThreadAdditionController', [])
  .controller('threadAdditionController', ['$scope', '$timeout', 'threadAdditionService', 'utils',
  function($scope, $timeout, threadAdditionService, utils) {
      $scope.init = function() {
        }

      $scope.threadModel = {
          thema : '',
          content : '',
          attachement : ''
      }

      $scope.reponse_received = false;
      $scope.status = true;

      $scope.submit = function() {
          const forms = document.getElementsByClassName('needs-validation');
          console.log(forms)
        
          if (utils.isFormValid(forms)) {
              threadAdditionService.submitThread($scope.threadModel, (response) => {            
                  console.log(response);
                  $scope.status = response.data.status;
                  $scope.reponse_received = true;

                  if ($scope.status == true) {
                    $timeout(() => { 
                      window.location.href = "/threads";
                    }, 2000);
                  }
                });
            }
        }
    }
]);