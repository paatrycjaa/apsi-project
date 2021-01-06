angular.module('appPostsListService', [])
  .service('postsListService',
    function($http) {
      this.getThreadById = function(id, callback) {
        return $http.get(`/ajax/get_thread/${id}/`).then(callback);
      }

      this.getThreadPosts = function(id, callback) {
        return $http.get(`/ajax/all_posts/${id}/`).then(callback);
      }
    }
  );