angular.module('appPostAdditionController', [])
  .controller('postAdditionController', ['$scope', '$timeout', 'postAdditionService', 'utils',
  function($scope, $timeout, postAdditionService, utils) {

        $scope.postModel = {
            thread : '',
            thema : '',
            content : '',
        }

        $scope.attachments = []

        // used only for editing
        $scope.attachment_names = []

        $scope.uploadFile = function(files){
          $scope.attachments = utils.checkAttachments(files)
          if($scope.attachments.length == 0){
            document.getElementById('attachment').value = ''
          }
        }

        $scope.init = function(id) {
            $scope.$watch("thread_id", function() {
                $scope.postModel.thread=id
            });
        }

        $scope.reponse_received = false;
        $scope.status = true;

        $scope.submit = function() {
            const forms = document.getElementsByClassName('needs-validation');
        
            if (utils.isFormValid(forms)) {
                postAdditionService.submitThread($scope.postModel, $scope.attachments, (response) => {
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