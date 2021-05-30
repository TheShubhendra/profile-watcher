import asyncio
from quora import User


class Quora:
    def __init__(self, username):
        self.state = None
        self.user = User(username)

    async def _update(self):
        profile = await self.user.profile()
        if self.state is None:
            self.state = profile
        elif not self.state == profile:
            print("Something changed", str(profile))
            self.state = profile

    async def start(self):
        while True:
            await self._update()
            await asyncio.sleep(5)
