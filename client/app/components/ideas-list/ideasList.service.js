angular.module('appIdeasListService', [])
  .service('ideasListService',
    function($http) {
      this.getIdeas = function(callback) {
        return $http.get('/ajax/all_ideas/').then(callback);
      }

      this.blockIdea = function(ideaId, callback) {
        return $http.post(`ajax/block_idea/${ideaId}/`).then(callback);
      }
    }
  );
