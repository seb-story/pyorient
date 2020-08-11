#  Copyright 2020 Niko Usai <usai.niko@gmail.com>, http://mogui.it; Marc Auberer, https://marc-auberer.de
#
#  this file is part of pyorient
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#   limitations under the License.

__author__ = 'mogui <mogui83@gmail.com>, Marc Auberer <marc.auberer@sap.com>'

import os


def is_debug_active():
    # Check if we're in debug mode
    return 'DEBUG' in os.environ and os.environ['DEBUG'].lower() in ('1', 'true')


def dlog(msg):
    # Check for debug key because KeyErrorExceptions are not caught and if no debug key is set, the driver crashes
    # with no reason when the connection is established
    if is_debug_active():
        # Print debug log message
        print("[DEBUG]:: %s" % msg)
