# celery_test

This project uses celery, celery beat, redis. Celery beat is used to perform tasks periodically.

Celery is a task queue with focus on real-time processing, while also supporting task scheduling.
Redis is a message broker. This means it handles the queue of "messages" between Django and Celery.
