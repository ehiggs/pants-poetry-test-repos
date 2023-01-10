# Simple example of a multirepo project using pants and poetry. 

This contains a base package: `project-models` and an application: `project-app`. 

## Simple Example

Run the `project-app`
```
./pants run ::
```

This will run a web server on port 5000. Visit it at `http://localhost:5000/hello/myname`

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

How can we install dependencies from a lockfile a single time to speed up rebuilds?

cf https://stackoverflow.com/a/54763270
