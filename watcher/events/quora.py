#!/usr/bin/python
# A python library that provides update when
# something changes in social profiles.
# Copyright (C) 2021 Shubhendra Kushwaha
# @TheShubhendra shubhendrakushwaha94@gmail.com
# This file is a part of profile-watcher
# <https://github.com/TheShubhendra/profile-watcher>.
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

import json
from .event import WatcherEvent


class QuoraEvent(WatcherEvent):
    def json(self):
        event = self.__dict__.copy()
        event.pop("user")
        event.pop("profile")
        data = dict()
        data["plateform"] = "quora"
        data["type"] = self.__class__.__name__
        data["event"] = event
        data["username"] = self.user.username
        return json.dumps(data)


class FollowingCountChange(QuoraEvent):
    def __init__(self, user, profile, oldCount, newCount, data_dict={}):
        self.user = user
        self.profile = profile
        self.oldCount = oldCount
        self.newCount = newCount
        self.countChange = newCount - oldCount
        self.data_dict = data_dict


class FollowerCountChange(QuoraEvent):
    def __init__(self, user, profile, oldCount, newCount, data_dict={}):
        self.user = user
        self.profile = profile
        self.oldCount = oldCount
        self.newCount = newCount
        self.countChange = newCount - oldCount
        self.data_dict = data_dict


class AnswerCountChange(QuoraEvent):
    def __init__(self, user, profile, oldCount, newCount, data_dict={}):
        self.user = user
        self.profile = profile
        self.oldCount = oldCount
        self.newCount = newCount
        self.countChange = newCount - oldCount
        self.data_dict = data_dict
