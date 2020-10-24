from celery import Celery
import os

app = Celery('tasks', broker='amqp://myuser:mypassword@localhost:5672/myvhost')

@app.task
def benchop(prob):
    execute = 'octave Table.m ' + prob
    os.system(execute)
    return 'done'