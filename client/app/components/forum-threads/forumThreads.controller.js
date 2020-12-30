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

        //$scope.openIdeaOpinions = function(id) {
        //  $window.location.href = `/opinions/${id}/`;
        //}
      }
]);
