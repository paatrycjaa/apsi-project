angular.module('appIdeasFilteredService', [])
  .service('ideasFilteredService',
    function($http) {
      this.getIdeas = function(callback) {
        return $http.get('/ajax/filtered_ideas/').then(callback);
      }

      this.wznowpomysl = function( data, callback) { 
        var url = '/ajax/change_status/'
        console.log(data)
        console.log(JSON.stringify(data))
        console.log(url)
        return $http.post(url, JSON.stringify(data)).then(callback) }
    }
  );
