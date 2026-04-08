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
import os

import matplotlib.pyplot as plt
from taipy.gui import Gui, Markdown

# Generate a scatter plot
x = [1, 2, 3, 4, 5]  # x axis values
y = [10, 14, 12, 15, 18]  # y axis values
sizes = [100, 100, 100, 100, 100]  # Bubble sizes
colors = [30, 40, 50, 60, 70]  # Bubble color values that will be mapped to shades of colormap (cmap)

# Scatter plot
# The `c` parameter uses the `colors` list to map values to the colormap (cmap)
# The `edgecolors` parameter sets the color of the edges around the bubbles
plt.scatter(x, y, s=sizes, c=colors, cmap='Greens', edgecolors='black', linewidths=1)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Matplotlib 2D Scatter Plot')

# Adding labels next to each point
for i in range(len(x)):
    plt.text(x[i] + 0.1, y[i] - 0.1, f'Point {i+1}', fontsize=9, ha='left')

# Creating legend entries for each point
# Each entry corresponds to a point, with the color and label indicating the point's position.
# The `markerfacecolor` sets the fill color of the legend marker to match the point's color in the 'Greens' colormap.
# The `markeredgecolor` sets the edge color of the legend marker.
# The `markeredgewidth` sets the width of the edge.
handles = [
    plt.Line2D(
        [0], [0], marker='o', color='w',
        markerfacecolor=plt.cm.Greens(color / max(colors)),
        markersize=10,  # Adjust the size for visibility
        label=f'Point {i+1}',
        markeredgewidth=1,  # Thickness of the edge color
        markeredgecolor='black'  # Edge color to match the plot
    ) for i, color in enumerate(colors)
]

# Placing the legend on the left side of the chart
plt.legend(handles=handles, title="Points", loc="center left", bbox_to_anchor=(1, 0.5), frameon=True)

# Adjust the layout to ensure everything fits and nothing is clipped
plt.tight_layout(rect=[0, 0, 1, 1])

# Save the figure as a PNG image
output_dir = './images'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
content = "./images/figure.png"
plt.savefig(content)

# Define Taipy page content
page_content = Markdown("""
# Matplotlib 2D Scatter Plot
<|{content}|image|class_name=scatter-plot|>
""", style={
    ".scatter-plot": {
        "display": "block",
        "margin": "auto",
        "max-width": "100% !important",
        "width": "max-content !important",
        "height": "max-content !important"
    }
})

if __name__ == "__main__":
    Gui(page_content).run(title="Chart-Scatter-Matplotlib")
