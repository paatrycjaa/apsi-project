angular.module('appPostAdditionService', []).service('postAdditionService',
        function($http){
            this.submitThread = function(data,callback){
                var url = '/ajax/submit_post/'
                return $http.post(url,JSON.stringify(data)).then(callback)
            }
        })