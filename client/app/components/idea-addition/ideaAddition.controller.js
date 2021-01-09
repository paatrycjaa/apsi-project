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
          attachement : '',
          num_rating : true,
          text_rating : true
        }
        
        $scope.keywords = []
                
        $scope.init = function(idea_id) 
        {
          // do edycji mozna tutaj pobierac dane o pomysle
          $scope.ideaModel.idea_id = idea_id;

          console.log(idea_id)
          
          if(idea_id){
            ideaAdditionService.getIdeaById(idea_id, function(response) {
              
              data = response.data[0] 
              settings=data.ustawienia_oceniania

              $scope.ideaModel.topic= data.tematyka
              $scope.ideaModel.description = data.opis  
              $scope.ideaModel.benefits =data.planowane_korzysci
              $scope.ideaModel.costs =data.planowane_koszty
              $scope.ideaModel.attachement =data.attachement
              $scope.ideaModel.category =data.slowakluczowe_id
              $scope.ideaModel.num_rating =  settings.includes('num')
              $scope.ideaModel.text_rating =  settings.includes('text')

            })
          }

          ideaAdditionService.getKeywords(function(response){
            $scope.keywords = response.data            
          })
        }

        $scope.reponse_received = false
        $scope.status = true

        $scope.submit = function() {
          const forms = document.getElementsByClassName('needs-validation');
          if (utils.isFormValid(forms)) {

            callback = (response) => {            
              console.log(response);
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
            ideaAdditionService.editIdea($scope.ideaModel, callback);
          } else { // new opinion is added            
            ideaAdditionService.submitIdea($scope.ideaModel, callback);
          }
          }
      }
  }
]);



