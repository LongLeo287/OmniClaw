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
# -----------------------------------------------------------------------------------------
# To execute this script, make sure that the taipy-gui package is installed in your
# Python environment and run:
#     python <script>
# -----------------------------------------------------------------------------------------
import datetime
import re
import time
import typing as t

import requests  # type: ignore[import-untyped]

from taipy.gui import Gui, Icon, State, get_state_id, invoke_callback, invoke_long_callback

# The Wikipedia API used to generate content for a date
wiki_url = "https://en.wikipedia.org/api/rest_v1/feed/onthisday/{type}/{month}/{day}"
event_types = {
    "happen": "events",
    "passé": "events",
    "born": "births",
    "né": "births",
    "dead": "deaths",
    "mort": "deaths",
}
user_agent = "https://taipy.io/demo"

# The list of messages
messages: list[tuple[str, str, str]] = []  # (Message id, message, sender)

# The two users of this app
users = [
    ["wikipedia", Icon("https://www.wikipedia.org/static/apple-touch/wikipedia.png", "Wikipedia")],
    ["taipy", Icon("https://docs.taipy.io/en/latest/assets/images/favicon.png", "Taipy")],
]


# Initialize the user state
def on_init(state: State):
    #  Messages are for this user only
    state.messages = []


# Add the image if there is one in the Wikipedia returned data
def add_image_to_message(state: State, idx: int, text: str, image_url: str):
    msg_content: str = state.messages[idx][1]
    if (pos := msg_content.find(text)) > -1:
        msg_content = msg_content[: pos + len(text)] + f"\n\n![{text}]({image_url})" + msg_content[pos + len(text) :]
        set_message(state, msg_content, idx)


# Invoked by update_message through a thread
def update_message_with_image(gui: Gui, state_id: str, message_idx: int, text: str, image: dict):
    if src := image.get("source"):
        time.sleep(0.2) # Apply the typewriter effect
        invoke_callback(
            gui,
            state_id,
            add_image_to_message,
            [message_idx, text, src],
        )


# Invoked by query_wikipedia()
def update_message(state: State, json, event_type: str, for_date: str, idx: int):
    if isinstance(json, dict):
        # Initial response content
        set_message(state, f"{event_type} for {for_date}:\n", idx)

        for event in json.get(event_type, []):
            time.sleep(0.2) # Apply the typewriter effect
            # Update response text
            append_to_message(state, f"\n* {event.get('year', '')}: {event.get('text', '')}", idx)
            # Invoke update_message_with_image() in a separated thread
            invoke_long_callback(
                state=state,
                user_function=update_message_with_image,
                user_function_args=[
                    state.get_gui(),
                    get_state_id(state),
                    idx,
                    event.get("text", ""),
                    pages[0].get("thumbnail", {}) if (pages := event.get("pages", [])) and len(pages) else {},
                ],
            )


# Set a new message or append to an existing message.
# Return the message index in the list.
def set_message(state: State, message: str, idx: t.Optional[int] = None):
    if idx is not None and idx < len(state.messages):
        msg = state.messages[idx]
        state.messages[idx] = (msg[0], message, msg[2])
    else:
        idx = len(state.messages)
        state.messages.append((f"{len(state.messages)}", message, users[0][0]))
    state.refresh("messages")
    return idx


# Append text to an existing message
def append_to_message(state: State, message: str, idx: int):
    if idx < len(state.messages):
        msg = state.messages[idx]
        state.messages[idx] = (msg[0], f"{msg[1]}{message}", msg[2])
        state.refresh("messages")
    return idx


# Invoke the Wikipedia API. This is invoked by send_message()
def request_wikipedia(gui: Gui, state_id: str, event_type: str, month: str, day: str):
    # Let the user known that a query was sent
    idx = invoke_callback(
        gui,
        state_id,
        set_message,
        ["Fetching information from Wikipedia ..."],
    )
    request = wiki_url.format(type=event_type, month=month, day=day)
    req = requests.get(request, headers={"accept": "application/json; charset=utf-8;", "User-Agent": user_agent})
    # Handle the response
    if req.status_code == 200:
        # Display the response
        invoke_callback(
            gui,
            state_id,
            update_message,
            [req.json(), event_type, f"{day}/{month}", idx],
        )
    else:
        # Display the error
        invoke_callback(
            gui,
            state_id,
            set_message,
            [f"Wikipedia API call failed: {req.status_code}", idx],
        )


# Invoked by the 'on_action' callback of the chat control when the user presses the Send button
def send_message(state: State, id: str, payload: dict):
    args = payload.get("args", [])

    # Display the request
    state.messages.append((f"{len(state.messages)}", args[2], args[3]))
    state.refresh("messages")

    # Analyse the request
    request = args[2].lower()
    type_event = None
    for word in event_types:
        if word in request:
            type_event = event_types[word]
            break
    type_event = type_event if type_event else "events"

    month = None
    day = None
    for m in re.finditer(r"(\d\d?)", request):
        if month is None:
            month = m.group()
        elif day is None:
            day = m.group()
            break
    if month is None:
        month = f"{datetime.datetime.now().month}"
    if day is None:
        day = f"{datetime.datetime.now().day}"

    # Process the request
    invoke_long_callback(
        state=state,
        user_function=request_wikipedia,
        user_function_args=[state.get_gui(), get_state_id(state), type_event, month, day],
    )


page = """
<|{messages}|chat|users={users}|on_action=send_message|height=80vh|>
"""

if __name__ == "__main__":
    Gui(page).run(title="Chat - Ask Wikipedia")
