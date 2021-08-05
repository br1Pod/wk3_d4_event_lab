class Event:

    def __init__(self, date, title, capacity, location, description):
        self.date = date
        self.title = title
        self.capacity = capacity 
        self.location = location
        self.description = description

    def add_new_event(self, event_list, event):
        event_list.append(event)
