# This to investigate how Celery `concurency` and `autoscale` works
Celery version:
`celery = {version = "==4.4.2", extras = ["redis"]}`

## Variations
#|Command|Result
---|---|---
1 | `celery worker -A app`| Max concurrency: 7 (number of cores - 1)
2 | `celery worker -A app --concurrency=99` | Max concurrency: 99
3 | `celery worker -A app --autoscale=19,10` | Max concurrency: 10, Max: 19, Min: 10
4 | `celery worker -A app --concurrency=99  --autoscale=19,10` | Max concurrency: 10, Max: 19, Min: 10
5 | `celery worker -A app --autoscale=19,10 --concurrency=99` | Max concurrency: 10, Max: 19, Min: 10
6 | `celery worker -A app --autoscale=1,0 --concurrency=99` | Max concurrency: 0, Max: 0, Min: 0

## Try it
run `docker compose up --build