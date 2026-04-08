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
from example_library import ExampleLibrary

from taipy.gui import Gui

set1 = {
    "x": [1, 2, 3, 4, 4, 4, 8, 9, 10],
    "type": "box",
    "name": "Set 1"
}

set2 = {
    "x": [2, 3, 3, 3, 3, 5, 6, 6, 7],
    "type": "box",
    "name": "Set 2"
}

data = [set1, set2]

layout = {
    "title": {
        "text": "Horizontal Box Plot"
    }
}

page = """
<|{data}|dashboard|layout={layout}|>
"""

if __name__ == "__main__":
    Gui(page, libraries=[ExampleLibrary()]).run(title="Horizontal Box Plot")
