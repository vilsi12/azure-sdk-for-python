# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AzureBareMetalInstance
from ._models_py3 import AzureBareMetalInstancesListResult
from ._models_py3 import Disk
from ._models_py3 import Display
from ._models_py3 import ErrorDefinition
from ._models_py3 import ErrorResponse
from ._models_py3 import HardwareProfile
from ._models_py3 import IpAddress
from ._models_py3 import NetworkProfile
from ._models_py3 import OSProfile
from ._models_py3 import Operation
from ._models_py3 import OperationList
from ._models_py3 import Resource
from ._models_py3 import Result
from ._models_py3 import StorageProfile
from ._models_py3 import SystemData
from ._models_py3 import Tags
from ._models_py3 import TrackedResource

from ._bare_metal_infrastructure_client_enums import AzureBareMetalHardwareTypeNamesEnum
from ._bare_metal_infrastructure_client_enums import AzureBareMetalInstancePowerStateEnum
from ._bare_metal_infrastructure_client_enums import AzureBareMetalInstanceSizeNamesEnum
from ._bare_metal_infrastructure_client_enums import AzureBareMetalProvisioningStatesEnum
from ._bare_metal_infrastructure_client_enums import CreatedByType
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AzureBareMetalInstance",
    "AzureBareMetalInstancesListResult",
    "Disk",
    "Display",
    "ErrorDefinition",
    "ErrorResponse",
    "HardwareProfile",
    "IpAddress",
    "NetworkProfile",
    "OSProfile",
    "Operation",
    "OperationList",
    "Resource",
    "Result",
    "StorageProfile",
    "SystemData",
    "Tags",
    "TrackedResource",
    "AzureBareMetalHardwareTypeNamesEnum",
    "AzureBareMetalInstancePowerStateEnum",
    "AzureBareMetalInstanceSizeNamesEnum",
    "AzureBareMetalProvisioningStatesEnum",
    "CreatedByType",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
