# flask-notes-demo — a real Flask app for cleanroom's in-tab VM

A small, ordinary Flask notes app. Nothing here is special about cleanroom —
it is a normal repo you could run on any machine:

```bash
pip install flask
python app.py
```

Inside [cleanroom](https://amanvicky.github.io/cleanroom/) it needs neither
of those on YOUR machine: paste this repo's link, press **Set up & run**, and
the runner installs `flask` into the in-tab VM, boots the WSGI app, and serves
it through the page's own network — a server app that is usable in the browser
with no install, no account, and no process on your PC.

- the store is an in-memory dict (the VM has no database)
- the wipe erases everything — notes included — like every cleanroom session
