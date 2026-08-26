"""
QUESTION: class EventBus() — an Observer/pub-sub system with subscribe(event,
handler), unsubscribe(event, handler), and publish(event, payload) that calls
every subscribed handler. Used by pro-4-analytics-engine to react to inventory
events (e.g. "low_stock") without tight coupling between modules.

Input:  bus.subscribe("low_stock", handler); bus.publish("low_stock", {"sku": "A1"})
Output: handler({"sku": "A1"}) is called
"""


class EventBus:
    def __init__(self):
        # TODO
        pass

    def subscribe(self, event_name, handler):
        # TODO
        pass

    def unsubscribe(self, event_name, handler):
        # TODO
        pass

    def publish(self, event_name, payload):
        # TODO
        pass


# --- TEST ---
# bus = EventBus()
# bus.subscribe("low_stock", lambda p: print(f"ALERT: {p['sku']}"))
# bus.publish("low_stock", {"sku": "A1"})  # expected: prints "ALERT: A1"
