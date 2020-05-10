import os
from typing import Union


def path() -> Union[str, bytes]:
    return os.path.dirname(__file__)
