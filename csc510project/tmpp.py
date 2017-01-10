from os import walk
from htmlmin import minify

CACHE_FUNC_TEMPLATE =\
"""
angular.module('%s').run(['$templateCache',function($templateCache){
    $templateCache.put('%s','%s');\n}]);
)
"""


for root, directories, files in walk("static/app/"):
    for file in files:
        if file.endswith(".html"):
            with open(root+'/'+file,"r") as fr, open("template.js","a") as fw:
                print >> fw, CACHE_FUNC_TEMPLATE%("csc510ProjectApp", root+'/'+file, minify(unicode(fr.read())))
