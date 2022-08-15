# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ConfigurationDataType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Data type of the configuration.
    """

    BOOLEAN = "Boolean"
    NUMERIC = "Numeric"
    INTEGER = "Integer"
    ENUMERATION = "Enumeration"

class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource.
    """

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"

class CreateMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The mode to create a new PostgreSQL server.
    """

    DEFAULT = "Default"
    CREATE = "Create"
    UPDATE = "Update"
    POINT_IN_TIME_RESTORE = "PointInTimeRestore"

class CreateModeForUpdate(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The mode to update a new PostgreSQL server.
    """

    DEFAULT = "Default"
    UPDATE = "Update"

class FailoverMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Failover mode.
    """

    PLANNED_FAILOVER = "PlannedFailover"
    FORCED_FAILOVER = "ForcedFailover"
    PLANNED_SWITCHOVER = "PlannedSwitchover"
    FORCED_SWITCHOVER = "ForcedSwitchover"

class GeoRedundantBackupEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """A value indicating whether Geo-Redundant backup is enabled on the server.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class HighAvailabilityMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The HA mode for the server.
    """

    DISABLED = "Disabled"
    ZONE_REDUNDANT = "ZoneRedundant"
    SAME_ZONE = "SameZone"

class OperationOrigin(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The intended executor of the operation.
    """

    NOT_SPECIFIED = "NotSpecified"
    USER = "user"
    SYSTEM = "system"

class Reason(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The name availability reason.
    """

    INVALID = "Invalid"
    ALREADY_EXISTS = "AlreadyExists"

class ServerHAState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """A state of a HA server that is visible to user.
    """

    NOT_ENABLED = "NotEnabled"
    CREATING_STANDBY = "CreatingStandby"
    REPLICATING_DATA = "ReplicatingData"
    FAILING_OVER = "FailingOver"
    HEALTHY = "Healthy"
    REMOVING_STANDBY = "RemovingStandby"

class ServerPublicNetworkAccessState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """public network access is enabled or not
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class ServerState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """A state of a server that is visible to user.
    """

    READY = "Ready"
    DROPPING = "Dropping"
    DISABLED = "Disabled"
    STARTING = "Starting"
    STOPPING = "Stopping"
    STOPPED = "Stopped"
    UPDATING = "Updating"

class ServerVersion(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The version of a server.
    """

    FOURTEEN = "14"
    THIRTEEN = "13"
    TWELVE = "12"
    ELEVEN = "11"

class SkuTier(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The tier of the particular SKU, e.g. Burstable.
    """

    BURSTABLE = "Burstable"
    GENERAL_PURPOSE = "GeneralPurpose"
    MEMORY_OPTIMIZED = "MemoryOptimized"
