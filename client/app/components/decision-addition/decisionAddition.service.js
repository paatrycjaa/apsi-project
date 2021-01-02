angular.module('appDecisionAdditionService', [])
  .service('decisionAdditionService',
    function($http) {
      this.getIdeaById = function(id, callback) {
        return $http.get(`/ajax/get_idea/${id}/`).then(callback);
      }

      this.getIdeaOpinions = function(id, callback) {
        return $http.get(`/ajax/all_opinions/${id}/`).then(callback);
      }

      this.submitDecision = function( data, callback) { 
        var url = '/ajax/submit_decision/'
        console.log(data)
        console.log(JSON.stringify(data))
        console.log(url)
        return $http.post(url, JSON.stringify(data)).then(callback) }
    }
  );
