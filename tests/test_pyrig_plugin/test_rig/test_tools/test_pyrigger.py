"""Tests for the plugin-specific Pyrigger behavior."""

from pyrig.rig.tools.pyrigger import Pyrigger


class TestPyrigger:
    """Tests for the Pyrigger override."""

    def test_runtime_dependency(self) -> None:
        """Return pyrig as the runtime dependency."""
        assert Pyrigger.I.runtime_dependency() == "pyrig"
