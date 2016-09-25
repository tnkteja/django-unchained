(function() {
    'use strict';

    angular
        .module('csc510ProjectApp')
        .config(stateConfig);

    stateConfig.$inject = ['$stateProvider'];

    function stateConfig($stateProvider) {
        $stateProvider.state('home', {
            parent: 'app',
            url: '/',
            data: {
                authorities: []
            },
            views: {
                'content@': {
                    templateUrl: 'static/app/entities/movie/movies.html',
                    controller: 'MovieController',
                    controllerAs: 'vm'
                }
            },
            resolve: {

            }
        });
    }
})();
