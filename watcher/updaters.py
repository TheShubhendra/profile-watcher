#!/usr/bin/python
# A python library that provides update when
# something changes in social profiles.
# Copyright (C) 2021 Shubhendra Kushwaha
# @TheShubhendra shubhendrakushwaha94@gmail.com
# This file is a part of profile-watcher <https://github.com/TheShubhendra/profile-watcher>.
#
# profile-watcher is a free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# profile-watcher is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with profile-watcher.  If not, see <http://www.gnu.org/licenses/>.


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