angular.module('appIdeasFilteredService', [])
  .service('ideasFilteredService',
    function($http) {
      this.getIdeas = function(callback) {
        return $http.get('/ajax/filtered_ideas/').then(callback);
      }

      this.zmienstatuspomyslu = function( data, callback) { 
        var url = '/ajax/change_status/'
        console.log(data)
        console.log(JSON.stringify(data))
        console.log(url)
        return $http.post(url, JSON.stringify(data)).then(callback);
      }

      this.removeIdea = function(data, callback) {
        console.log(data)
        console.log(JSON.stringify(data))
        return $http.post('/ajax/delete_idea/', JSON.stringify(data)).then(callback);
      }

    }
  );
