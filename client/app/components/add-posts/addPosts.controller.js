angular.module('appPostAdditionController', [])
  .controller('postAdditionController', ['$scope', '$timeout', 'postAdditionService', 'utils',
  function($scope, $timeout, postAdditionService, utils) {

        $scope.postModel = {
            thread : '',
            thema : '',
            content : '',
            attachement : ''
        }

        $scope.init = function(id) {
            $scope.$watch("thread_id", function() {
            
                $scope.postModel.thread=id
                console.log(id, $scope.postModel.thread)
            });
        }

        $scope.reponse_received = false;
        $scope.status = true;

        $scope.submit = function() {
            const forms = document.getElementsByClassName('needs-validation');
            console.log(forms)
        
            if (utils.isFormValid(forms)) {
                postAdditionService.submitThread($scope.postModel, (response) => {            
                    console.log(response);
                    $scope.status = response.data.status;
                    $scope.reponse_received = true;

                    if ($scope.status == true) {
                    $timeout(() => { 
                      window.location.href = "/posts/" + $scope.postModel.thread;
                    }, 2000);
                  }
                });
            }
        }
    }
]);