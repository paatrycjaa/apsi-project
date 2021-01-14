angular.module('appStartPageController', [])
  .controller('startPageController', ['$scope', '$interval', 'startPageService',
    function($scope, $interval, startPageService) {

      $scope.messages = [
        {
          text: 'DZIŚ DODANYCH POMYSŁÓW',
          field: 'ideasCountToday',
        },
        {
          text: 'DZIŚ DODANYCH OPINII',
          field: 'opinionsCountToday',
        },
        {
          text: 'DODANYCH POMYSŁÓW',
          field: 'ideasCount',
        },
        {
          text: 'DODANYCH OPINII',
          field: 'opinionsCount',
        },
        {
          text: 'WYDANYCH DECYZJI',
          field: 'decisionsCount',
        },
        {
          text: 'DODANYCH WĄTKÓW',
          field: 'threadsCount',
        },
        {
          text: 'DODANYCH POSTÓW',
          field: 'postsCount',
        },
      ];

      $scope.swapId = 0;
      $scope.statsInfos = [];

      $scope.init = function() {
        startPageService.getStats().then((resp) => {
          $scope.statsInfos = Object.entries(resp.data)
            .filter((e) => e[1] > 0)
            .map((entry) => ({
                message: $scope.messages.find((m) => m.field === entry[0])?.text,
                count: entry[1].toString(),
            })
          );
        });
      };

      $interval(() => {
        $scope.swapId = ($scope.swapId + 1) % $scope.statsInfos.length;
      }, 3000);
    }
  ]
);