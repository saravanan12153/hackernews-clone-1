module.exports = function (grunt) {
    grunt.initConfig({
        watch: {
            src: {
                files: ['**/*.scss', '**/*.html', '**/*.py'],
                tasks: ['compass:dev'] 
            },
           options: {
                livereload: true,
            },
        },
        compass: {
            dev: {
                options: {
                    sassDir: 'styleproject/sass',
                    cssDir: 'hackernews/static/css',
                    imagesPath: 'img',
                    noLineComments: false,
                    outputStyle: 'compressed'
                }
            }
        },

    });
    grunt.loadNpmTasks('grunt-contrib-compass');
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-watch');


};
