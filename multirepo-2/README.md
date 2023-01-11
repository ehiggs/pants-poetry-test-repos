# Simple example of a multirepo project using pants and poetry. 

This contains a base package: `project-models` and an application: `project-app`. This runs using pants 2.14.

## Simple Example

Run the `project-app`
```
./pants run project-app:project-app-exec
```


This will run a web server on port `5000`. Visit it at `http://localhost:5000/hello/myname`

Or run the `project-app-exec`
```
./pants run project-app-async:project-app-async-exec`
```

This will run a web server on port `5001`. Visit it at `http://localhost:5001/hello/myname`

## Running tests

```
./pants test ::
```

## Docker example


Build the docker container.

```
docker build --build-arg APPLICATION=project-app -t project-app:latest .
```

Then run it:

```
docker run -p5000:5000  project-app
```

This will run a docker container with a port forward on port 5000 mapping to port 5000 of the host. You can visit using the same url as above: `http://localhost:5000/hello/myname`

## Thoughts

In `project-app-async` we import Flask even though it's not specified as a dependency there. This means teams working on different services in a monorepo system could start using libraries they haven't declared. That means team Foo could upgrade their dependencies and break team Bar's project.

