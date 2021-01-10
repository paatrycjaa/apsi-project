angular.module('appPostAdditionService', []).service('postAdditionService',
        function($http){
            this.submitThread = function(data, file, callback){

                var formData = new FormData();

                data.attachment = file.name
                data.attachment_size = file.size

                formData.append('data', JSON.stringify(data));
                formData.append('file', file);

                const url = '/ajax/submit_post/'

                return $http.post(url, formData, {
                    headers: {'Content-Type': undefined },
                    transformRequest: angular.identity
                  }).then(callback)
            }
        })