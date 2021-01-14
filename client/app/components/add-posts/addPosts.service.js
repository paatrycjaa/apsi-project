angular.module('appPostAdditionService', [])
.service('postAdditionService',  ['$http', 'utils',
    function($http, utils){
        this.submitThread = function(data, files, callback){
            const url = '/ajax/submit_post/'
            utils.sendPostRequest($http, data, files, callback, url)
        }
    }]
);