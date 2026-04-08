# Copyright 2021-2025 Avaiga Private Limited
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

from taipy.gui import Gui, Icon

msgs = [
    ["1", "msg 1", "Alice", None],
    ["2", "msg From Another unknown User", "Charles", None],
    ["3", "This from the sender User", "taipy", None],
    ["4", "And from another known one", "Alice", None],
]
users = [
    ["Alice", Icon("./alice-avatar.png", "Alice avatar")],
    ["Charles", Icon("./charles-avatar.png", "Charles avatar")],
    ["taipy", Icon("./beatrix-avatar.png", "Beatrix avatar")],
]


def on_action(state, var_name: str, payload: dict):
    (reason, varName, text, senderId, imageData) = payload.get("args", [])
    msgs.append([f"{len(msgs) +1 }", text, senderId, imageData])
    state.msgs = msgs


page="""
<|1 1 1|layout|
<|{msgs}|chat|users={users}|show_sender={True}|>

<|part|>

<|{msgs}|chat|users={users}|show_sender={True}|not with_input|>
|>

"""

if __name__ == "__main__":
    Gui(page).run(title="Chat - Simple")
