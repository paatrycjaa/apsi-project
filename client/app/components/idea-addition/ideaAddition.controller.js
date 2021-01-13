angular.module('appIdeaAdditionController', [])
  .controller('ideaAdditionController', ['$scope', '$timeout', 'ideaAdditionService', 'utils',
  function($scope, $timeout, ideaAdditionService, utils)
  {

        $scope.ideaModel = {
          topic : '',
          category: '',
          description : '',
          benefits : '',
          costs : '',
          num_rating : true,
          text_rating : true
        }

        $scope.attachments = []

        // used only for editing
        $scope.attachment_names = []

        $scope.keywords = []

        $scope.uploadFile = function(files){
          $scope.attachments = utils.checkAttachments(files)
          if($scope.attachments.length == 0){
            document.getElementById('attachment').value = ''
          }
        }

        $scope.init = function(idea_id)
        {
          $scope.ideaModel.idea_id = idea_id;

          ideaAdditionService.getKeywords(function(response){
            $scope.keywords = response.data
          })

          if(idea_id){
            ideaAdditionService.getIdeaById(idea_id, function(response) {

              //todo
              // display category

              data = response.data
              settings=data.ustawienia_oceniania_id

              $scope.ideaModel.topic = data.tematyka
              $scope.ideaModel.description = data.opis
              $scope.ideaModel.benefits = data.planowane_korzysci
              $scope.ideaModel.costs = data.planowane_koszty
              $scope.ideaModel.category = data.slowo_kluczowe_id
              $scope.ideaModel.num_rating =  settings.includes('num')
              $scope.ideaModel.text_rating =  settings.includes('text')

              if(data.attachments.length > 0){
                $scope.attachment_names = []
                data.attachments.forEach(att => {
                  $scope.attachment_names.push(att.zalacznik__nazwa_pliku)
                });
              }
            })
          }
        }

        $scope.reponse_received = false
        $scope.status = true

        $scope.submit = function() {
          const forms = document.getElementsByClassName('needs-validation');
          if (utils.isFormValid(forms)) {

            callback = (response) => {
              $scope.status = response.data.status;
              $scope.reponse_received = true;
              if ($scope.status === true) {
                $timeout(() => {
                  window.location.href = "/ideas";
                }, 2000);
              }
            };

                    // opinion is edited
          if($scope.ideaModel.idea_id){
            ideaAdditionService.editIdea($scope.ideaModel,  $scope.attachments, callback);
          } else { // new opinion is added
            ideaAdditionService.submitIdea($scope.ideaModel, $scope.attachments, callback);
          }
          }
      }
  }
]);
