import logging

import pytest

from taipy.gui import Gui


def test_handle_invalid_data_no_callback():
    result = Gui._convert_unsupported_data("invalid_data")
    assert result is None


def test_unsupported_data_converter_returns_none():
    def convert(value):
        return None  # Simulates a failed transformation

    Gui.set_unsupported_data_converter(convert)

    result = Gui._convert_unsupported_data("invalid_data")
    assert result is None

    # Reset converter
    Gui.set_unsupported_data_converter(None)


def test_unsupported_data_converter_applied():
    def convert(value):
        return "converted"  # Successful transformation

    Gui.set_unsupported_data_converter(convert)

    result = Gui._convert_unsupported_data("raw data")
    assert result == "converted"

    # Reset converter
    Gui.set_unsupported_data_converter(None)


def test_unsupported_data_converter_raises_exception(capfd, monkeypatch):
    def convert(value):
        raise ValueError("Conversion failure")  # Simulate an error

    def mock_warn(message: str):
        logging.warning(message)  # Ensure the warning goes to stderr.

    # Patch the _warn function inside the taipy.gui._warnings module.
    monkeypatch.setattr("taipy.gui._warnings._warn", mock_warn)

    Gui.set_unsupported_data_converter(convert)

    result = Gui._convert_unsupported_data("raw data")

    out, _ = capfd.readouterr()

    assert result is None  # Should return None on exception
    assert "Error transforming data: Transformation error"

    # Reset converter
    Gui.set_unsupported_data_converter(None)


@pytest.mark.parametrize("input_data", [None, 123, [], {}, set()])
def test_unsupported_data_converter_with_various_inputs(input_data):
    def convert(value):
        return "converted"  # Always returns valid data

    Gui.set_unsupported_data_converter(convert)

    result = Gui._convert_unsupported_data(input_data)
    assert result == "converted"  # Transformed correctly for all inputs

    # Reset converter
    Gui.set_unsupported_data_converter(None)
