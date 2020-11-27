angular.module('appIdeaAdditionService', [])
  .service('ideaAdditionService',
    function($http) {
      this.submitIdea = function(data, callback) { 
        console.log(data)
        console.log(JSON.stringify(data))
        return $http.post('/ajax/submit_idea/', JSON.stringify(data)).then(callback) }
    }
  );
