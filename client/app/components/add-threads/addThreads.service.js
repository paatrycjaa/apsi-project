angular.module('appThreadAdditionService', []).service('threadAdditionService',
        function($http){
            this.submitThread = function(data,callback){
                var url = '/ajax/submit_thread/'
                return $http.post(url,JSON.stringify(data)).then(callback)
            }
        })