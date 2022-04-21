# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

from enum import Enum


class ApiVersion(str, Enum):
    V2021_04_07_preview = "2021-04-07"
    V2022_02_01_preview = "2022-02-01"


DEFAULT_VERSION = ApiVersion.V2022_02_01_preview