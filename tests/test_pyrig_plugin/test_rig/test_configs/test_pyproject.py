"""Test module."""

from pyrig_pypi.rig.configs.pyproject import PyprojectConfigFile


class TestPyprojectConfigFile:
    """Test class."""

    def test_keywords_configs(self) -> None:
        """Test method."""
        assert PyprojectConfigFile.I.keywords_configs() == ["pyrig"]
