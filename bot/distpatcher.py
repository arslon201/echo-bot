class Dispatcher:
    def __init__(self) -> None:
        self.handlers: list = []

    def add_handler(self, handler):
        if handler not in self.handlers:
            self.handlers.append(handler)

    def process_update(self, update: dict) -> None:
        for handler in self.handlers:
            if handler.check_update(update):
                handler.handle_update(update)
                break 
