"""Pyrigger override that declares pyrig as a runtime dependency."""

from pyrig.rig.tools.pyrigger import Pyrigger as BasePyrigger


class Pyrigger(BasePyrigger):
    """Extend Pyrig's CLI wrapper for projects that are themselves Pyrig plugins."""

    def runtime_dependency(self) -> str:
        """Return pyrig as the runtime dependency.

        Pyrig plugins must declare Pyrig as a runtime dependency so that
        Pyrig's cross-package plugin discovery can find their implementations.

        This overrides the base implementation, which returns `pyrig-runtime`
        for non-plugin projects. Because `pyrig` itself depends on
        `pyrig-runtime`, plugin projects only need to declare `pyrig`.

        Returns:
            The name of the runtime dependency, which is `pyrig`.
        """
        return self.name()
