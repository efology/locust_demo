# locust_demo

Demonstration of locust.io using docker, buildkite and gorest.co.in

## Description

[locustfile.py](https://github.com/efology/locust_demo/blob/main/locustfile.py) contains a sequence of rest calls to https://gorest.co.in api, where we list, create, modify and delete user, in that order.

The test can be run using locust.io docker container, for example:

```shell
docker run --env-file=token.env -p 8089:8089 -v $PWD:/mnt/locust locustio/locust -f /mnt/locust/locustfile.py -H https://gorest.co.in --headless --csv=/mnt/locust/results --only-summary -u 5 -r 1 -t 2m
```

So far so good, next step was creating a CI pipeline, in this case I opted for buildkite, as it seemed as more elegant option compared to Jenkins/BlueOcean. The rationale was that it was easier to install buildkite agent, than to set up Jenkins/BlueOcean with all the plugins etc.

I tried using two different docker images for the pipeline, "locustio/locust" and a regular "python:3".
In both cases I ran into same problem, the buildkite agent would not properly mount the directory where the code was checked out to containers WORKDIR.
WORKDIR was simply empty, and locust could not find any locustfile.py to run.

[buildkite pipeline.yml](https://github.com/efology/locust_demo/blob/main/.buildkite/pipeline.yml) 

After few hours of troubleshooting and googling error messages and so forth, I decided that maybe I should have run with Jenkins after all :)
