from {{cookiecutter.plugin_package}}.utils import my_util
import logging
import ida_idaapi
import ida_kernwin

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("{{cookiecutter.plugin_package}}")

class {{cookiecutter.plugin_class}}(ida_idaapi.plugin_t):
    flags = ida_idaapi.PLUGIN_FIX

    # Required attributes - must be set by subclasses
    wanted_name: str = "{{cookiecutter.plugin_name}}"
    comment: str = "{{cookiecutter.plugin_name}}"
    help: str = "{{cookiecutter.plugin_name}}"

    def init(self) -> int:
        logger.info("Plugin {{cookiecutter.plugin_name}} initializing")
        addon = ida_kernwin.addon_info_t()
        addon.id = "{{cookiecutter.author_name}}.{{cookiecutter.plugin_name}}"
        addon.name = "{{cookiecutter.plugin_name}}"
        addon.producer = "{{cookiecutter.author_name}}"
        addon.url = "https://github.com/{{cookiecutter.author_name}}/{{cookiecutter.plugin_name}}"
        addon.version = "{{cookiecutter.version}}"
        ida_kernwin.register_addon(addon)
        return ida_idaapi.PLUGIN_KEEP

    def run(self, arg: int) -> None:
        logger.info("Plugin {{cookiecutter.plugin_name}} running")

    def term(self) -> None:
        logger.info("Plugin {{cookiecutter.plugin_name}} terminating")

def PLUGIN_ENTRY():
    return {{cookiecutter.plugin_class}}()
