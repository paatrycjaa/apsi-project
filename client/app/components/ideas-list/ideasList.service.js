angular.module('appIdeasListService', [])
  .service('ideasListService',
    function($http) {
      this.getIdeas = function(callback) {
        return $http.get('/ajax/all_ideas/').then(callback);
      }

      this.editIdea = function(data, callback) { 
        console.log(data)
        console.log(JSON.stringify(data))
        return $http.post('/ajax/edit_idea/', JSON.stringify(data)).then(callback);
      }
    }
  );
