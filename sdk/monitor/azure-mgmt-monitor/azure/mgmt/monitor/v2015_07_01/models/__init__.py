# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AlertRuleResource
from ._models_py3 import AlertRuleResourceCollection
from ._models_py3 import AlertRuleResourcePatch
from ._models_py3 import DimensionProperties
from ._models_py3 import ErrorContract
from ._models_py3 import ErrorResponse
from ._models_py3 import LocalizableString
from ._models_py3 import LocationThresholdRuleCondition
from ._models_py3 import LogSettings
from ._models_py3 import LogSpecification
from ._models_py3 import ManagementEventAggregationCondition
from ._models_py3 import ManagementEventRuleCondition
from ._models_py3 import MetricAvailability
from ._models_py3 import MetricAvailabilityLocation
from ._models_py3 import MetricDefinition
from ._models_py3 import MetricDefinitionCollection
from ._models_py3 import MetricSettings
from ._models_py3 import MetricSpecification
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationListResult
from ._models_py3 import Resource
from ._models_py3 import RetentionPolicy
from ._models_py3 import RuleAction
from ._models_py3 import RuleCondition
from ._models_py3 import RuleDataSource
from ._models_py3 import RuleEmailAction
from ._models_py3 import RuleManagementEventClaimsDataSource
from ._models_py3 import RuleManagementEventDataSource
from ._models_py3 import RuleMetricDataSource
from ._models_py3 import RuleWebhookAction
from ._models_py3 import ServiceDiagnosticSettingsResource
from ._models_py3 import ServiceSpecification
from ._models_py3 import TableInfoEntry
from ._models_py3 import ThresholdRuleCondition


from ._monitor_management_client_enums import (
    AggregationType,
    ConditionOperator,
    TimeAggregationOperator,
    Unit,
)
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk
__all__ = [
    'AlertRuleResource',
    'AlertRuleResourceCollection',
    'AlertRuleResourcePatch',
    'DimensionProperties',
    'ErrorContract',
    'ErrorResponse',
    'LocalizableString',
    'LocationThresholdRuleCondition',
    'LogSettings',
    'LogSpecification',
    'ManagementEventAggregationCondition',
    'ManagementEventRuleCondition',
    'MetricAvailability',
    'MetricAvailabilityLocation',
    'MetricDefinition',
    'MetricDefinitionCollection',
    'MetricSettings',
    'MetricSpecification',
    'Operation',
    'OperationDisplay',
    'OperationListResult',
    'Resource',
    'RetentionPolicy',
    'RuleAction',
    'RuleCondition',
    'RuleDataSource',
    'RuleEmailAction',
    'RuleManagementEventClaimsDataSource',
    'RuleManagementEventDataSource',
    'RuleMetricDataSource',
    'RuleWebhookAction',
    'ServiceDiagnosticSettingsResource',
    'ServiceSpecification',
    'TableInfoEntry',
    'ThresholdRuleCondition',
    'AggregationType',
    'ConditionOperator',
    'TimeAggregationOperator',
    'Unit',
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()