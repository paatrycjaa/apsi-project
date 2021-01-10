angular.module('appPostAdditionController', [])
  .controller('postAdditionController', ['$scope', '$timeout', 'postAdditionService', 'utils',
  function($scope, $timeout, postAdditionService, utils) {

        $scope.postModel = {
            thread : '',
            thema : '',
            content : '',
            attachment : '',
            attachment_size : ''
        }

        $scope.attachement = ''

        const max_size = 10000000  // 10 MB

        $scope.uploadFile = function(files){
          $scope.attachement = files[0] 
          if($scope.attachement.size > max_size){
            alert('Wybrany plik jest za duży. Maksymalny rozmiar to 10 MB.');            
            $scope.attachement = ''
            document.getElementById('attachment').value = ''
          }          
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
                postAdditionService.submitThread($scope.postModel, $scope.attachement, (response) => {                  
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