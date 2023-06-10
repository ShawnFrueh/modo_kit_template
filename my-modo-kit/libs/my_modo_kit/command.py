from operator import ior
from functools import reduce

from lx.symbol import fCMDARG_OPTIONAL, fCMDARG_QUERY
from lxu.command import BasicCommand


class KitCommand(BasicCommand):
    """Command wrapper to add an index return when adding an argument."""
    arg_index = 0

    def add_arg(self, name: str, arg_type: str, optional: bool = True, query: bool = False) -> int:
        """Adds an argument to the command and returns its index.

        Args:
            name (str): The name of the argument.
            arg_type (str): The string type of the argument.
            optional (bool): If the argument is optional.
            query (bool): If the argument is queryable.

        Returns:
            current_index (int): The index of the newly added argument.
        """
        self.dyna_Add(name, arg_type)
        current_index = self.arg_index

        flags = list()
        if optional:
            flags.append(fCMDARG_OPTIONAL)
        if query:
            flags.append(fCMDARG_QUERY)

        # Add flags to argument. reduce with ior == flag | flag | ...
        self.dyna_SetFlags(current_index, reduce(ior, flags))
        self.arg_index += 1

        return current_index
