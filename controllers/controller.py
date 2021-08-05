from flask import render_template, request
from app import app
from models.event import *
from models.event_list import events

@app.route("/events")
def index():
    return render_template("index.html", title="home", events = events)

@app.route("/events", methods = ["POST"])
def add_event():
    event_title = request.form["title"]
    event_description = request.form["description"]
    new_event = Event("21th Aug",  event_title, 250, "The Stand", event_description)
    new_event.add_new_event(events, new_event)
    return render_template("index.html", title="home", events = events)


@app.route("/events/new")
def new_event():
    return render_template("new.html", title="new event")


