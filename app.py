"""A real Flask notes app — small enough to read, real enough to use.

The store is an in-memory dict: this demo runs inside cleanroom's in-tab
VM, where a process has no sockets and no database — the page itself is
the app's network. The code is an ordinary Flask app otherwise.
"""
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
NOTES = []
_next_id = [1]


@app.route("/")
def index():
    return render_template("index.html", notes=NOTES)


@app.route("/add", methods=["POST"])
def add():
    text = (request.form.get("text") or "").strip()
    if text:
        NOTES.append({"id": _next_id[0], "text": text})
        _next_id[0] += 1
    return redirect(url_for("index"))


@app.route("/delete/<int:note_id>", methods=["POST"])
def delete(note_id):
    NOTES[:] = [n for n in NOTES if n["id"] != note_id]
    return redirect(url_for("index"))


if __name__ == "__main__":
    print("this app is meant to run inside cleanroom's in-tab VM —")
    print("type: set up & run   (or: run app.py)")
    app.run(debug=True)
