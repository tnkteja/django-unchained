(function() {
    'use strict';

    angular
        .module('csc510ProjectApp')
        .directive('jhSocial', jhSocial);

    jhSocial.$inject = ['$filter', 'SocialService'];

    function jhSocial($filter, SocialService) {
        var directive = {
            restrict: 'E',
            scope: {
                provider: '@ngProvider'
            },
            templateUrl: 'static/app/account/social/directive/social.html',
            link: linkFunc
        };

        return directive;

        /* private helper methods */

        function linkFunc(scope) {
            
            scope.label = $filter('capitalize')(scope.provider);
            scope.providerSetting = SocialService.getProviderSetting(scope.provider);
            scope.providerURL = SocialService.getProviderURL(scope.provider);
            scope.csrf = SocialService.getCSRF();
        }

    }
})();
