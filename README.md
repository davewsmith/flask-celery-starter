# Celery Starter

A small demonstration of getting Celery 2.4.0 working with Flask 1.0.2 (with logging).

Getting Flask and Celery working together is a bit tedious to set up.
Googling for tips is liable to find parts that don't work together.


## To Build

If you have VirtualBox and Vagrant installed, `vagrant up` will get you a VM.

If you don't, see the steps in the script block at the top of `Vagrantfile`.

## To Run (on Linux/MacOS)

You'll need Redis running. If you built the VM, it'll be there.

In one shell,

    venv/bin/celery -A demo.celery --loglevel=info worker

In another shell,

    FLASK_APP=demo.py venv/bin/flask run --host='0.0.0.0'

(or use the convenient `run` script, which does the same, plus turning on `FLASK_DEBUG`)

Then browse to `http://localhost:5000/`

Behind the scenes, but visible in the logs, the handler for `/` on the Flask app side queues up a task and then waits for it to complete.
On the celery side sits a worker waiting for to process tasks.
Through the magic of the `@celery.task` annotation, they share different parts of a task subroutine.

## Next Steps

If you're using this as a starting point, note that both `celery` and `flask` start with `demo.py`.
If you need to any interesting app setup on the Flask side, you might want to make a separate `worker.py`,
which would still call `create_app()`, but can forego the extra app setup.


