"""Tests for the plugin-specific Pyrigger behavior."""

from pyrig.rig.tools.pyrigger import Pyrigger


class TestPyrigger:
    """Tests for the Pyrigger override."""

    def test_runtime_dependencies(self) -> None:
        """Include pyrig alongside the inherited pyrig-runtime dependency."""
        assert Pyrigger.I.runtime_dependencies() == ("pyrig-runtime", "pyrig")
