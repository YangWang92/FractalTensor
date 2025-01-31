# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------

from __future__ import absolute_import, division, print_function

import sys

from kaleido.frontend import operations
from kaleido.frontend.fractal_tensor import *
from kaleido.frontend.tensor import Parameter, Tensor
from kaleido.frontend.types import *
from kaleido.parser import *

del absolute_import
del division
del print_function

# FIXME(Ying): please manually create the soft link of the build dynamic library
# in the build directory.
# It needs a standarded way to distribute the package and import
# bindings in future.
# import _core

# _core.init_glog(sys.argv[0])
