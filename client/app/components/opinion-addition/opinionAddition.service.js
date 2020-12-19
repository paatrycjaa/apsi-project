angular.module('appOpinionAdditionService', [])
  .service('opinionAdditionService',
    function($http) {
       this.submitOpinion = function(data, callback) { 
         console.log(data)
         console.log(JSON.stringify(data))
         return $http.post('/ajax/submit_opinion/', JSON.stringify(data)).then(callback) }
    }
  );
