# Flask + Celery Starter

A small demonstration of getting Celery 2.4.0 working with Flask 1.0.2
(with logging).

Flask and Celery work well together once you work through the tedious details
of getting everything set up just right. Googling for help is liable to turn
up partial answers that don't work together, in part due to recent revisions
in Celery.
Hence this example.

## To Build

If you have VirtualBox and Vagrant installed, `vagrant up` will get you a VM.

If you don't, see the steps in the script block at the top of `Vagrantfile`.

## To Run (on Linux/MacOS)

You'll need Redis running. If you built the VM, it'll be there.

If you've built the VM, `vagrant ssh` into it twice
(or once and use `tmux` get get multiple shells).

In one shell,

    venv/bin/celery -A demo.celery --loglevel=info worker

In another shell,

    FLASK_APP=demo.py venv/bin/flask run --host='0.0.0.0'

(or use the convenient `run` script, which does the same,
plus turning on `FLASK_DEBUG`)

Then browse to `http://localhost:5000/`

Behind the scenes, but visible in the logs, the handler for `/` on the
Flask app side creates a task and then waits for it to complete.
On the celery side, a worker that's been waiting for tasks to run gets it,
processes it, and stores the answer.

You can also initiate tasks form the command line. From a third shell,

    FLASK_APP=demo.py venv/bin/flask add 40 2

will initiate a task, wait for the result, and print it. A trivial example,
but imagine instead launching a task that scrapes a web site and populates
local database tables using models and code that are shared with the Flask
app.

## Next Steps

If you're using this as a starting point, note that both `celery` and `flask`
start with `demo.py`.  If you need to any interesting app setup on the Flask
side, you might want to make a separate `worker.py`, which would still call
`create_app()`, but can forego the extra app setup.

For scheduled tasks, there are two options: The first is to use the
command-line trick above from a cron(1) job. The second is to run a separate
celery "heartbeat" worker, and configure schedules via celery. Celery has some
neat scheduling options, such as solar noon at a given latitude/longitude.
Consult the Celery docs.

If you get close to production, consider replacing Redis with RabbitMQ as
the broker.

## LICENSE

None. There's nothing novel here worth claiming.
It's also use-at-your-own-risk-ware.
It works for me (on a Raspberry Pi, no less), but YMMV.
