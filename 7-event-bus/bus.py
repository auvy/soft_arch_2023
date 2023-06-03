class EventBus:
    def __init__(self):
        self.listeners = {}

    def subscribe(self, event_name, listener):
        if event_name not in self.listeners:
            self.listeners[event_name] = []
        self.listeners[event_name].append(listener)

    def unsubscribe(self, event_name, listener):
        if event_name in self.listeners:
            print(self.listeners)
            self.listeners.pop(event_name)

    def publish(self, event_name, data=None):
        if event_name in self.listeners:
            for listener in self.listeners[event_name]:
                listener(data)

