angular.module('appIdeasListService', [])
  .service('ideasListService',
    function($http) {
      this.getIdeas = function(callback) {
        return $http.get('/ajax/all_ideas/').then(callback);
      }

      this.editIdea = function(data, callback) { 
        return $http.post('/ajax/edit_idea/', JSON.stringify(data)).then(callback);
      }
      
      this.blockIdea = function(ideaId, callback) {
        return $http.post(`ajax/block_idea/${ideaId}/`).then(callback);
      }
    }
  );
