nuget
==================

Nuget library wrapper for Node.js.

This library uses [Vinyl](https://github.com/wearefractal/vinyl) files for flexibility and Gulp compatibility.

# Raw usage

```
nuget = require 'nuget'

nuget.pack 'package.nuspec', (err, nupkg_file) ->
  throw err if err

  nuget.push nupkg_file, (err) ->
    throw err if err

    console.log "Successfully pushed #{nupkg_file.path}"
```

# Gulp usage

```
gulp = require 'gulp'
gutil = require 'gulp-util'
es = require 'event-stream'
nuget = require 'nuget'

nugetGulp = -> es.map (file, callback) ->
  nuget.pack file, (err, nupkg_file) ->
    return callback(err) if err
    nuget.push nupkg_file, (err) -> if err then gutil.log(err) else callback()

gulp.src('*.nuspec')
  .pipe(nugetGulp())
```

Configuring Nuget
-------------

Add the 'nuget.org' source to your Nuget config file

$ mono nuget.exe sources add -name "nuget.org" -source "https://www.nuget.org/api/v2/package"

Add the credentials for your source

$ mono nuget.exe setApiKey {YOUR_API_KEY} -source nuget.org
