import asyncio


class Dispatcher:
    def __init__(self, eventQueue, logger):
        self.handlers = set()
        self.eventQueue = eventQueue
        self.logger = logger

    def add_handler(self, event, callback):
        self.logger.info(
            f"Adding event handler {callback.__name__} for {event.__name__}"
        )
        self.handlers.add((event, callback))

    def remove_handler(self, event, callback):
        self.handlers.remove((event, callback))

    def on(self, event):
        def decorator(func):
            self.add_handler(event, func)
            return func

        return decorator

    async def listen(self):
        self.logger.info("Starting dispatcher")
        while True:
            self.logger.debug("Dispatcher is running")
            if not self.eventQueue.empty():
                self.logger.info("Got an update")
                event = await self.eventQueue.get()
                for _event, callback in self.handlers:
                    if isinstance(event, _event):
                        await callback(event)

            await asyncio.sleep(5)
