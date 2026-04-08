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
# This script needs to run in a Python environment where the Matplotlib library is
# installed.
# -----------------------------------------------------------------------------------------
# Matplotlib example
import numpy as np

import matplotlib.pyplot as plt
import taipy.gui.builder as tgb
from taipy.gui import Gui

fig = plt.figure(figsize=(5, 4))
xx = np.arange(0, 2 * np.pi, 0.01)
plot = fig.subplots(1, 1)
plot.fill(xx, np.sin(xx), facecolor="none", edgecolor="purple", linewidth=2)

with tgb.Page(
    style={
        ".matplotlib_example": {
            "display": "inline-flex", "width": "520px", "height": "420px"
            }
        }
) as page:
    tgb.html("h1", "Taipy Example for Matplotlib Integration")
    tgb.part(content="{fig}", class_name = "matplotlib_example")


# Run the Taipy Application:
if __name__ == "__main__":
    Gui(page).run(title="Matplotlib Example")
