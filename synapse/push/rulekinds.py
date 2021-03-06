# Copyright 2015 OpenMarket Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

PRIORITY_CLASS_MAP = {
    'underride': 1,
    'sender': 2,
    'room': 3,
    'content': 4,
    'override': 5,
}
PRIORITY_CLASS_INVERSE_MAP = {v: k for k, v in PRIORITY_CLASS_MAP.items()}
