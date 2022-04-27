from celery import shared_task

@shared_task(bind=True)
def test_func(self):
    print('hello')
    for i in range(10):
        print(i)
    return "Done"

@shared_task(bind=True)
def test_hello_func(self):
    print("hello for test")
    return "done dona done"

@shared_task(bind=True)
def test_another_func(self):
    print ("new task")
    return "new task done"

