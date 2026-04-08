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

import typing as t
from pathlib import Path
from unittest.mock import Mock, patch

import pytest

from taipy import DataNode, Gui, Scope
from taipy.core.data import PickleDataNode
from taipy.core.data._data_manager_factory import _DataManagerFactory
from taipy.core.data._file_datanode_mixin import _FileDataNodeMixin
from taipy.core.reason import Reason, ReasonCollection
from taipy.gui_core._context import _GuiCoreContext

dn = PickleDataNode("dn_config_id", scope=Scope.GLOBAL, properties={"default_path": "pa/th"})


def core_get(entity_id):
    if entity_id == dn.id:
        return dn
    return None


def not_downloadable():
    return ReasonCollection()._add_reason(dn.id, Reason("foo"))


def downloadable():
    return ReasonCollection()


def not_readable(entity_id):
    return ReasonCollection()._add_reason(entity_id, Reason("foo"))


def readable(entity_id):
    return ReasonCollection()


def mock_checker(**kwargs):
    return True


def check_fails(**kwargs):
    raise Exception("Failed")


def upload_fails(a, b, editor_id, comment):
    return ReasonCollection()._add_reason(dn.id, Reason("bar"))


def download_fails(a, b, editor_id, comment):
    return ReasonCollection()._add_reason(dn.id, Reason("bar"))


class MockState:
    def __init__(self, **kwargs) -> None:
        self.assign = kwargs.get("assign")


class TestGuiCoreContext_on_file_action:
    @pytest.fixture(scope="class", autouse=True)
    def set_entities(self):
        _DataManagerFactory._build_manager()._repository._save(dn)

    def test_does_not_fail_if_wrong_args(self):
        gui_core_context = _GuiCoreContext(Mock(Gui))
        gui_core_context.on_file_action(state=Mock(), id="", payload={})
        gui_core_context.on_file_action(state=Mock(), id="", payload={"args": "wrong_args"})
        gui_core_context.on_file_action(state=Mock(), id="", payload={"args": ["wrong_args"]})

    def test_datanode_not_readable(self):
        with patch("taipy.gui_core._context.is_readable", side_effect=not_readable):
            with patch("taipy.gui_core._context.core_get", side_effect=core_get) as mock_core_get:
                with patch.object(DataNode, "write") as mock_write:
                    mockGui = Mock(Gui)
                    mockGui._get_client_id = lambda: "a_client_id"
                    gui_core_context = _GuiCoreContext(mockGui)
                    assign = Mock()
                    gui_core_context.on_file_action(
                        state=MockState(assign=assign),
                        id="",
                        payload={"args": [{"id": dn.id, "error_id": "error_var"}]},
                    )
                    mock_core_get.assert_not_called()
                    mock_write.assert_not_called()
                    assign.assert_called_once_with("error_var", "foo.")

    def test_upload_file_without_checker(self):
        with patch("taipy.gui_core._context.is_readable", side_effect=readable):
            with patch("taipy.gui_core._context.core_get", side_effect=core_get) as mock_core_get:
                with patch.object(_FileDataNodeMixin, "_upload") as mock_upload:
                    mockGui = Mock(Gui)
                    mockGui._get_client_id = lambda: "a_client_id"
                    gui_core_context = _GuiCoreContext(mockGui)
                    assign = Mock()
                    gui_core_context.on_file_action(
                        state=MockState(assign=assign),
                        id="",
                        payload={"args": [{"id": dn.id, "error_id": "error_var", "path": "pa/th"}]},
                    )
                    mock_core_get.assert_called_once_with(dn.id)
                    mock_upload.assert_called_once_with("pa/th", None, editor_id="a_client_id", comment=None)
                    assign.assert_not_called()

    def test_upload_file_with_checker(self):
        with patch("taipy.gui_core._context.is_readable", side_effect=readable):
            with patch("taipy.gui_core._context.core_get", side_effect=core_get) as mock_core_get:
                with patch.object(_FileDataNodeMixin, "_upload") as mock_upload:
                    mockGui = Mock(Gui)
                    mockGui._get_client_id = lambda: "a_client_id"
                    mockGui._get_user_function = lambda _: _
                    gui_core_context = _GuiCoreContext(mockGui)
                    assign = Mock()
                    gui_core_context.on_file_action(
                        state=MockState(assign=assign),
                        id="",
                        payload={
                            "args": [
                                {"id": dn.id, "error_id": "error_var", "path": "pa/th", "upload_check": mock_checker}
                            ]
                        },
                    )
                    mock_core_get.assert_called_once_with(dn.id)
                    mock_upload.assert_called_once_with(
                        "pa/th",
                        t.cast(t.Callable[[str, t.Any], bool], mock_checker),
                        editor_id="a_client_id",
                        comment=None,
                    )
                    assign.assert_not_called()

    def test_upload_file_with_failing_checker(self):
        with patch("taipy.gui_core._context.is_readable", side_effect=readable):
            with patch("taipy.gui_core._context.core_get", side_effect=core_get) as mock_core_get:
                with patch.object(_FileDataNodeMixin, "_upload", side_effect=upload_fails) as mock_upload:
                    mockGui = Mock(Gui)
                    mockGui._get_client_id = lambda: "a_client_id"
                    mockGui._get_user_function = lambda _: _
                    gui_core_context = _GuiCoreContext(mockGui)
                    assign = Mock()
                    gui_core_context.on_file_action(
                        state=MockState(assign=assign),
                        id="",
                        payload={
                            "args": [
                                {"id": dn.id, "error_id": "error_var", "path": "pa/th", "upload_check": check_fails}
                            ]
                        },
                    )
                    mock_core_get.assert_called_once_with(dn.id)
                    mock_upload.assert_called_once_with(
                        "pa/th",
                        t.cast(t.Callable[[str, t.Any], bool], check_fails),
                        editor_id="a_client_id",
                        comment=None,
                    )
                    assign.assert_called_once_with("error_var", "Data unavailable: bar.")

    def test_download_file_not_downloadable(self):
        with patch.object(_FileDataNodeMixin, "is_downloadable", side_effect=not_downloadable):
            with patch("taipy.gui_core._context.core_get", side_effect=core_get) as mock_core_get:
                with patch.object(_FileDataNodeMixin, "_get_downloadable_path") as mock_download:
                    mockGui = Mock(Gui)
                    mockGui._get_client_id = lambda: "a_client_id"
                    mockGui._get_user_function = lambda _: _
                    gui_core_context = _GuiCoreContext(mockGui)
                    assign = Mock()
                    gui_core_context.on_file_action(
                        state=MockState(assign=assign),
                        id="",
                        payload={"args": [{"id": dn.id, "action": "export", "error_id": "error_var"}]},
                    )
                    mock_core_get.assert_called_once_with(dn.id)
                    mock_download.assert_not_called()
                    assign.assert_called_once_with("error_var", "Data unavailable: foo.")

    def test_download(self):
        with patch.object(_FileDataNodeMixin, "is_downloadable", side_effect=downloadable):
            with patch("taipy.gui_core._context.core_get", side_effect=core_get) as mock_core_get:
                with patch.object(_FileDataNodeMixin, "_get_downloadable_path") as mock_download:
                    mockGui = Mock(Gui)
                    mockGui._get_client_id = lambda: "a_client_id"
                    mockGui._download.return_value = None
                    gui_core_context = _GuiCoreContext(mockGui)
                    assign = Mock()
                    gui_core_context.on_file_action(
                        state=MockState(assign=assign),
                        id="",
                        payload={"args": [{"id": dn.id, "action": "export", "error_id": "error_var"}]},
                    )
                    mock_core_get.assert_called_once_with(dn.id)
                    mock_download.assert_called_once()
                    mockGui._download.assert_called_once_with(Path(dn._get_downloadable_path()), dn.id)
                    assign.assert_not_called()
