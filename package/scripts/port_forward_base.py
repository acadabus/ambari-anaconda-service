from resource_management import Execute, Script, File, Template, Directory
from resource_management.core.exceptions import ExecutionFailed
import os


class PortForwardBase(Script):

    def install_ac(self, env):
        import params
        env.set_params(params)

    def configure_ac(self, env):
        import params
        env.set_params(params)
        File("/etc/systemd/system/portforward.service",
             content=Template("portforward_service.j2", configurations=params),
             owner=params.anaconda_user,
             group=params.anaconda_group,
             mode=0o0600
             )

    def install(self, env):
        self.install_ac(self, env)