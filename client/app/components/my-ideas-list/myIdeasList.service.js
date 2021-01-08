angular.module('appMyIdeasListService', [])
  .service('myIdeasListService',
    function($http) {
      this.getUserIdeas = function(callback) {
        return $http.get('/ajax/user_ideas/', JSON).then(callback);
      }

      // this.editIdea = function(data, callback) { 
      //   console.log(data)
      //   console.log(JSON.stringify(data))
      //   return $http.post('/ajax/edit_idea/', JSON.stringify(data)).then(callback);
      // }
    }
  );
