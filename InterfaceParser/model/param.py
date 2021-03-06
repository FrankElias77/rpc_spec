"""Parameter.

"""

from model.interface_item_base import InterfaceItemBase


class Param(InterfaceItemBase):
    """Parameter.

    :param name: item name
    :param description: list of string description elements
    :param design_description: list of string design description elements
    :param issues: list of issues
    :param todos: list of string todo elements
    :param platform: optional platform (string or None)
    :param default_value: optional default value of this parameter
    :param scope: optional scope: internal, partner or none (none by default, means public)
    :param since: string that defines the rpc spec version an element was introduced
    :param until: string that defines the rpc spec version an element was removed, deprecated, or changed
    :param deprecated: boolean that defines if an element is planned to be removed in a future release
    :param removed: boolean that defines if an element was removed from the api
    :param history: array of api element signature changes

    :param is_mandatory: boolean value indicating whether this parameter is mandatory
    :param param_type: parameter type

    """

    def __init__(self, name, param_type, description=None,
                 design_description=None, issues=None, todos=None,
                 platform=None, is_mandatory=True, default_value=None, scope=None,
                 since=None, until=None, deprecated=None, removed=None, history=None):
        super(Param, self).__init__(
            name, description=description, design_description=design_description,
            issues=issues, todos=todos, platform=platform, default_value=default_value, scope=scope,
            since=since, until=until, deprecated=deprecated, removed=removed, history=history)

        self.is_mandatory = is_mandatory
        self.param_type = param_type
