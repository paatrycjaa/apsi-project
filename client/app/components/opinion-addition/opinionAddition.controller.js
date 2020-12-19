angular.module('appOpinionAdditionController', [])
  .controller('opinionAdditionController', ['$scope', '$timeout', 'opinionAdditionService',
      function($scope, $timeout, opinionAdditionService) {

         $scope.opinion = {
           description : '',
           rate : 0
         }
        //   description : '',
        //   benefits : '',
        //   costs : '',
        //   attachement : '',
        //   num_rating : true,
        //   text_rating : true
        // }        
                
        $scope.init = function() {
          // do edycji mozna tutaj pobierac dane o opinii
        }

         $scope.reponse_received = false
         $scope.status = true

         $scope.submit = function() {
           opinionAdditionService.submitOpinion($scope.opinion, function(response) {            
             console.log(response)
             $scope.status = response.data.status
             $scope.reponse_received = true
             if ($scope.status === true) {
               $timeout(function() { 
                 window.location.href = redirect_url;
               }, 2000);
             }
           });
         }

         window.addEventListener('load', function() {
             // Fetch all the forms we want to apply custom Bootstrap validation styles to
             var forms = document.getElementsByClassName('needs-validation');
             // Loop over them and prevent submission
             var validation = Array.prototype.filter.call(forms, function(form) {
               form.addEventListener('submit', function(event) {
                 if (form.checkValidity() === false) {
                   event.preventDefault();
                   event.stopPropagation();
                 }
                 form.classList.add('was-validated');
               }, false);
             });
           }, false);        
      }
]);
