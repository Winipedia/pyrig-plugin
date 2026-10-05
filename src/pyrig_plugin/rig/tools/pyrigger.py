"""Pyrigger override that declares pyrig as a runtime dependency."""

from pyrig.rig.tools.pyrigger import Pyrigger as BasePyrigger


class Pyrigger(BasePyrigger):
    """Extend Pyrig's CLI wrapper for projects that are themselves Pyrig plugins."""

    def runtime_dependencies(self) -> tuple[str, ...]:
        """Return the runtime dependencies required by the project.

        Pyrig plugins must declare Pyrig as a runtime dependency so that
        Pyrig's cross-package plugin discovery can find their implementations.

        Returns:
            The base runtime dependencies with ``pyrig`` appended.
        """
        return (*super().runtime_dependencies(), self.name())
