angular.module('appPostsListController', [])
  .controller('postsListController', ['$scope', 'postsListService',
      
  
  
  
  function($scope, postsListService) {
        
        $scope.posts = [];

        $scope.addPost=function(){
          id=$scope.thread_id
          window.location.href = `/add-post/${id}/`; 
        }


        $scope.init = function(id) {
           $scope.$watch("thread_id", function() {
            
            $scope.thread_id=id
            console.log(id)
            postsListService.getThreadById($scope.thread_id, function(response) {
              $scope.thread = response.data[0]
              console.log($scope.thread)
            });



            postsListService.getThreadPosts($scope.thread_id, function(response) {
              $scope.posts = response.data;
              console.log($scope.posts)
            })
          });
        }
      }
]);