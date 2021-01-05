angular.module('appThreadAdditionService', []).service('threadAdditionService',
        function($http){
            this.submitThread = function(data,callback){
                var url = '/ajax/submit_thread/'
                console.log(data)
                console.log(JSON.stringify(data))
                console.log(url)
                return $http.post(url,JSON.stringify(data)).then(callback)
            }
        })