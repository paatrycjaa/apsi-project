angular.module('appThreadsListController', [])
  .controller('threadsListController', ['$scope', '$window', '$interval', 'threadsListService',
      function($scope, $window, $interval, threadsListService) {
        
        $scope.threads = [];

        $scope.init = function() {
          threadsListService.getThreads(function(response) {
            $scope.threads = response.data
            console.log($scope.threads)
          });
        }

        $scope.openThreadPosts = function(id) {
          $window.location.href = `/posts/${id}/`;
        }

        $scope.removeThread = function(id) {
          threadsListService.removeThread(id, () => {
            $window.location.reload();
          });
        }
      }
]);
