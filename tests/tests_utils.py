# s2p (Satellite Stereo Pipeline) testing module
# Copyright (C) 2019, Julien Michel (CNES) <julien.michel@cnes.fr>

import os
import s2p


def data_path(p: str) -> str:
    """Build an absolute path to a test data file.

    The base directory can be overridden by the ``S2P_DATA_PATH``
    environment variable.  This makes it possible to run the tests on
    alternative datasets without modifying the repository structure.

    Args:
        p: path to the input test data relative to the dataset root

    Returns:
        str: absolute path to that data file
    """
    base_dir = os.environ.get("S2P_DATA_PATH")
    if base_dir is None:
        here = os.path.abspath(os.path.dirname(__file__))
        base_dir = os.path.join(here, "data")
    return os.path.join(base_dir, p)
