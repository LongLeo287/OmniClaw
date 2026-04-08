import taipy as tp
import taipy.gui.builder as tgb
from taipy import Config, Orchestrator, Scope
from taipy.gui import Gui

json_config_node = Config.configure_json_data_node(
    id="json_node",
    default_path="./datanode_viewer_json.json",
    scope=Scope.GLOBAL,
)

with tgb.Page() as data_node_viewer:
    tgb.data_node(
        data_node="{json_data_node}"
    )

gui = Gui(page=data_node_viewer)

if __name__ == "__main__":
    Orchestrator().run()
    json_data_node = tp.create_global_data_node(json_config_node)
    gui.run(title="Datanode Viewer - json support")
