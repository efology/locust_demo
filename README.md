# locust_demo

Demonstration of locust.io using docker, buildkite and gorest.co.in

## Description

[locustfile.py](https://github.com/efology/locust_demo/blob/main/locustfile.py) contains a sequence of rest calls to https://gorest.co.in api, where we list, create, modify and delete user, in that order.

The test can be run using locust.io docker container, for example:

```shell
docker run --env-file=token.env -p 8089:8089 -v $PWD:/mnt/locust locustio/locust -f /mnt/locust/locustfile.py -H https://gorest.co.in --headless --csv=/mnt/locust/results --only-summary -u 5 -r 1 -t 2m
```

[buildkite pipeline.yml](https://github.com/efology/locust_demo/blob/main/.buildkite/pipeline.yml) 

