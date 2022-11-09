# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AutoScaleVCore
from ._models_py3 import AutoScaleVCoreListResult
from ._models_py3 import AutoScaleVCoreMutableProperties
from ._models_py3 import AutoScaleVCoreProperties
from ._models_py3 import AutoScaleVCoreSku
from ._models_py3 import AutoScaleVCoreUpdateParameters
from ._models_py3 import CapacitySku
from ._models_py3 import CheckCapacityNameAvailabilityParameters
from ._models_py3 import CheckCapacityNameAvailabilityResult
from ._models_py3 import DedicatedCapacities
from ._models_py3 import DedicatedCapacity
from ._models_py3 import DedicatedCapacityAdministrators
from ._models_py3 import DedicatedCapacityMutableProperties
from ._models_py3 import DedicatedCapacityProperties
from ._models_py3 import DedicatedCapacityUpdateParameters
from ._models_py3 import ErrorResponse
from ._models_py3 import ErrorResponseError
from ._models_py3 import LogSpecification
from ._models_py3 import MetricSpecification
from ._models_py3 import MetricSpecificationDimensionsItem
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationListResult
from ._models_py3 import OperationProperties
from ._models_py3 import Resource
from ._models_py3 import ServiceSpecification
from ._models_py3 import SkuDetailsForExistingResource
from ._models_py3 import SkuEnumerationForExistingResourceResult
from ._models_py3 import SkuEnumerationForNewResourceResult
from ._models_py3 import SystemData

from ._power_bi_dedicated_enums import CapacityProvisioningState
from ._power_bi_dedicated_enums import CapacitySkuTier
from ._power_bi_dedicated_enums import IdentityType
from ._power_bi_dedicated_enums import Mode
from ._power_bi_dedicated_enums import State
from ._power_bi_dedicated_enums import VCoreProvisioningState
from ._power_bi_dedicated_enums import VCoreSkuTier
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AutoScaleVCore",
    "AutoScaleVCoreListResult",
    "AutoScaleVCoreMutableProperties",
    "AutoScaleVCoreProperties",
    "AutoScaleVCoreSku",
    "AutoScaleVCoreUpdateParameters",
    "CapacitySku",
    "CheckCapacityNameAvailabilityParameters",
    "CheckCapacityNameAvailabilityResult",
    "DedicatedCapacities",
    "DedicatedCapacity",
    "DedicatedCapacityAdministrators",
    "DedicatedCapacityMutableProperties",
    "DedicatedCapacityProperties",
    "DedicatedCapacityUpdateParameters",
    "ErrorResponse",
    "ErrorResponseError",
    "LogSpecification",
    "MetricSpecification",
    "MetricSpecificationDimensionsItem",
    "Operation",
    "OperationDisplay",
    "OperationListResult",
    "OperationProperties",
    "Resource",
    "ServiceSpecification",
    "SkuDetailsForExistingResource",
    "SkuEnumerationForExistingResourceResult",
    "SkuEnumerationForNewResourceResult",
    "SystemData",
    "CapacityProvisioningState",
    "CapacitySkuTier",
    "IdentityType",
    "Mode",
    "State",
    "VCoreProvisioningState",
    "VCoreSkuTier",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
