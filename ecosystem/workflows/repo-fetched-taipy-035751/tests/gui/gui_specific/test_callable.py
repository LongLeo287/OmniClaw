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

from taipy.gui.utils.callable import _function_name, _is_function, _is_unnamed_function


def my_function():
    pass


class my_class:
    pass


class my_callable_class:
    def __call__(self):
        pass


def test__is_unnamed_function():
    assert _is_unnamed_function(my_function) is False
    assert _is_unnamed_function(lambda x: x) is True
    assert _is_unnamed_function("a") is False


def test__is_function():
    assert _is_function(my_function) is True
    assert _is_function(lambda x: x) is True
    assert _is_function("a") is False


def test__function_name():
    assert _function_name(my_function) == "my_function"
    assert _function_name(lambda x: x) == "<lambda>"
    assert _function_name("a") == "a"
    assert _function_name(1) == "1"
    assert _function_name(1.0) == "1.0"
    assert _function_name(True) == "True"
    assert _function_name(False) == "False"
    assert _function_name(None) == "None"
    assert _function_name([]) == "[]"
    assert _function_name({}) == "{}"
    assert _function_name(set()) == "set()"
    assert _function_name(tuple()) == "()"  # noqa C408
    assert _function_name(object) == "object"
    assert _function_name(object()).startswith("<object ")
    assert _function_name(my_class) == "my_class"
    assert _function_name(my_class()).startswith("<tests.gui.gui_specific.test_callable.my_class ")
    assert _function_name(my_callable_class) == "my_callable_class"
    assert _function_name(my_callable_class()) == "<instance of my_callable_class>"
