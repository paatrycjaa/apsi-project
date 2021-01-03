angular.module('appOpinionAdditionService', [])
  .service('opinionAdditionService',
    function($http) {
      this.getOpinionById = function(id, callback) {
        return $http.get(`/ajax/get_opinion/${id}/`).then(callback);
      }
      this.submitOpinion = function( data, callback) { 
         var url = '/ajax/submit_opinion/'
         console.log(data)
         console.log(JSON.stringify(data))
         console.log(url)
         return $http.post(url, JSON.stringify(data)).then(callback)
      }
      
      this.editOpinion = function( data, callback) { 
          var url = '/ajax/edit_opinion/'
          console.log(data)
          console.log(JSON.stringify(data))
          console.log(url)
          return $http.post(url, JSON.stringify(data)).then(callback)
      }



    }
  );
