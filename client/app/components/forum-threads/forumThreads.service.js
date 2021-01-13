angular.module('appThreadsListService', [])
  .service('threadsListService',
    function($http) {
      this.getThreads = function(callback) {
        return $http.get('/ajax/all_threads/').then(callback);
      }

      this.removeThread = function(threadId, callback) {
        return $http.post(`ajax/remove_thread/${threadId}/`).then(callback);
      }
    }
  );
