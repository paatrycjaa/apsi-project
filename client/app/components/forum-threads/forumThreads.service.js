angular.module('appThreadsListService', [])
  .service('threadsListService',
    function($http) {
      this.getThreads = function(callback) {
        return $http.get('/ajax/all_threads/').then(callback);
      }
    }
  );
