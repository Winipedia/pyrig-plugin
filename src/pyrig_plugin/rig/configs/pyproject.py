"""PyPI-specific extensions to the project's `pyproject.toml` configuration."""

from pyrig.rig.tools.pyrigger import Pyrigger
from pyrig_pypi.rig.configs.pyproject import (
    PyprojectConfigFile as BasePyprojectConfigFile,
)


class PyprojectConfigFile(BasePyprojectConfigFile):
    """Customized PyprojectConfigFile for pyrig plugins."""

    def keywords_configs(self) -> list[str]:
        """Return the list of keyword configurations.

        Adds the keyword `pyrig` to the list of keyword configurations because
        any pyrig plugin is a package depending on pyrig on PyPI.
        """
        return [*super().keywords_configs(), Pyrigger.I.name()]
