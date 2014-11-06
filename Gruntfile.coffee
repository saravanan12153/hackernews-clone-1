module.exports = (grunt) ->
  paths = 
		compass:
			files: 'staticproject/sass/**/*.scss'
			src: 'staticproject/sass/'
			dest: 'hackernews/static/css'
		coffee:
			cwd: 'staticproject/coffee'
			src: '**/*.coffee'
			dest: 'hackernews/static/js'
      
  # configuration
  grunt.initConfig 
    # grunt sass

    compass: 
      dev: 
        options: 
          sassDir: paths.compass.src
          cssDir: paths.compass.dest
          imagesPath: 'hackernews/static/img'
          noLineComments: false
          outputStyle: 'compressed'               
            
 
    # grunt coffee
    coffee:
      compile:
        expand: true
        cwd: paths.coffee.cwd
        src: paths.coffee.src
        dest: paths.coffee.dest 
        ext: '.js' 
        options:
          bare: true
          preserve_dirs: true
 
    # grunt watch (or simply grunt)
    watch:
      compass: 
        files: paths.compass.files
        tasks: ['compass:dev']          
      html:
        files: ['**/*.html']
      coffee:
        files: paths.coffee.cwd+'/'+paths.coffee.src
        tasks: ['coffee']
      options:
        livereload: true
 
  # load plugins

  grunt.loadNpmTasks 'grunt-contrib-coffee'
  grunt.loadNpmTasks 'grunt-contrib-watch'
  grunt.loadNpmTasks 'grunt-contrib-compass'
  # tasks
  grunt.registerTask 'default', ['coffee', 'watch']
