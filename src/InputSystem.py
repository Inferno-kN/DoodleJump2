class InputSystem:

    def __init__(self):
        self.subscriptions = {}

    def handle_events(self, events):
        for event in events:

            for key_code in self.subscriptions.keys():
                if event.type == key_code:
                    callback = self.subscriptions[key_code]
                    callback(event)

    def sub(self, key_code, callback):
        self.subscriptions[key_code] = callback
