# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AccessPolicy
from ._models_py3 import AccountImmutabilityPolicyProperties
from ._models_py3 import AccountSasParameters
from ._models_py3 import ActiveDirectoryProperties
from ._models_py3 import AzureEntityResource
from ._models_py3 import AzureFilesIdentityBasedAuthentication
from ._models_py3 import BlobContainer
from ._models_py3 import BlobInventoryPolicy
from ._models_py3 import BlobInventoryPolicyDefinition
from ._models_py3 import BlobInventoryPolicyFilter
from ._models_py3 import BlobInventoryPolicyRule
from ._models_py3 import BlobInventoryPolicySchema
from ._models_py3 import BlobRestoreParameters
from ._models_py3 import BlobRestoreRange
from ._models_py3 import BlobRestoreStatus
from ._models_py3 import BlobServiceItems
from ._models_py3 import BlobServiceProperties
from ._models_py3 import ChangeFeed
from ._models_py3 import CheckNameAvailabilityResult
from ._models_py3 import CloudErrorBody
from ._models_py3 import CorsRule
from ._models_py3 import CorsRules
from ._models_py3 import CustomDomain
from ._models_py3 import DateAfterCreation
from ._models_py3 import DateAfterModification
from ._models_py3 import DeleteRetentionPolicy
from ._models_py3 import DeletedAccount
from ._models_py3 import DeletedAccountListResult
from ._models_py3 import DeletedShare
from ._models_py3 import Dimension
from ._models_py3 import Encryption
from ._models_py3 import EncryptionIdentity
from ._models_py3 import EncryptionScope
from ._models_py3 import EncryptionScopeKeyVaultProperties
from ._models_py3 import EncryptionScopeListResult
from ._models_py3 import EncryptionService
from ._models_py3 import EncryptionServices
from ._models_py3 import Endpoints
from ._models_py3 import ErrorResponse
from ._models_py3 import ErrorResponseBody
from ._models_py3 import ExtendedLocation
from ._models_py3 import FileServiceItems
from ._models_py3 import FileServiceProperties
from ._models_py3 import FileShare
from ._models_py3 import FileShareItem
from ._models_py3 import FileShareItems
from ._models_py3 import GeoReplicationStats
from ._models_py3 import IPRule
from ._models_py3 import Identity
from ._models_py3 import ImmutabilityPolicy
from ._models_py3 import ImmutabilityPolicyProperties
from ._models_py3 import ImmutableStorageAccount
from ._models_py3 import ImmutableStorageWithVersioning
from ._models_py3 import KeyCreationTime
from ._models_py3 import KeyPolicy
from ._models_py3 import KeyVaultProperties
from ._models_py3 import LastAccessTimeTrackingPolicy
from ._models_py3 import LeaseContainerRequest
from ._models_py3 import LeaseContainerResponse
from ._models_py3 import LeaseShareRequest
from ._models_py3 import LeaseShareResponse
from ._models_py3 import LegalHold
from ._models_py3 import LegalHoldProperties
from ._models_py3 import ListAccountSasResponse
from ._models_py3 import ListBlobInventoryPolicy
from ._models_py3 import ListContainerItem
from ._models_py3 import ListContainerItems
from ._models_py3 import ListQueue
from ._models_py3 import ListQueueResource
from ._models_py3 import ListQueueServices
from ._models_py3 import ListServiceSasResponse
from ._models_py3 import ListTableResource
from ._models_py3 import ListTableServices
from ._models_py3 import LocalUser
from ._models_py3 import LocalUserKeys
from ._models_py3 import LocalUserRegeneratePasswordResult
from ._models_py3 import LocalUsers
from ._models_py3 import ManagementPolicy
from ._models_py3 import ManagementPolicyAction
from ._models_py3 import ManagementPolicyBaseBlob
from ._models_py3 import ManagementPolicyDefinition
from ._models_py3 import ManagementPolicyFilter
from ._models_py3 import ManagementPolicyRule
from ._models_py3 import ManagementPolicySchema
from ._models_py3 import ManagementPolicySnapShot
from ._models_py3 import ManagementPolicyVersion
from ._models_py3 import MetricSpecification
from ._models_py3 import Multichannel
from ._models_py3 import NetworkRuleSet
from ._models_py3 import ObjectReplicationPolicies
from ._models_py3 import ObjectReplicationPolicy
from ._models_py3 import ObjectReplicationPolicyFilter
from ._models_py3 import ObjectReplicationPolicyRule
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationListResult
from ._models_py3 import PermissionScope
from ._models_py3 import PrivateEndpoint
from ._models_py3 import PrivateEndpointConnection
from ._models_py3 import PrivateEndpointConnectionListResult
from ._models_py3 import PrivateLinkResource
from ._models_py3 import PrivateLinkResourceListResult
from ._models_py3 import PrivateLinkServiceConnectionState
from ._models_py3 import ProtectedAppendWritesHistory
from ._models_py3 import ProtocolSettings
from ._models_py3 import ProxyResource
from ._models_py3 import QueueServiceProperties
from ._models_py3 import Resource
from ._models_py3 import ResourceAccessRule
from ._models_py3 import RestorePolicyProperties
from ._models_py3 import Restriction
from ._models_py3 import RoutingPreference
from ._models_py3 import SKUCapability
from ._models_py3 import SasPolicy
from ._models_py3 import ServiceSasParameters
from ._models_py3 import ServiceSpecification
from ._models_py3 import SignedIdentifier
from ._models_py3 import Sku
from ._models_py3 import SkuInformation
from ._models_py3 import SmbSetting
from ._models_py3 import SshPublicKey
from ._models_py3 import StorageAccount
from ._models_py3 import StorageAccountCheckNameAvailabilityParameters
from ._models_py3 import StorageAccountCreateParameters
from ._models_py3 import StorageAccountInternetEndpoints
from ._models_py3 import StorageAccountKey
from ._models_py3 import StorageAccountListKeysResult
from ._models_py3 import StorageAccountListResult
from ._models_py3 import StorageAccountMicrosoftEndpoints
from ._models_py3 import StorageAccountRegenerateKeyParameters
from ._models_py3 import StorageAccountSkuConversionStatus
from ._models_py3 import StorageAccountUpdateParameters
from ._models_py3 import StorageQueue
from ._models_py3 import StorageSkuListResult
from ._models_py3 import SystemData
from ._models_py3 import Table
from ._models_py3 import TableAccessPolicy
from ._models_py3 import TableServiceProperties
from ._models_py3 import TableSignedIdentifier
from ._models_py3 import TagFilter
from ._models_py3 import TagProperty
from ._models_py3 import TrackedResource
from ._models_py3 import UpdateHistoryProperty
from ._models_py3 import Usage
from ._models_py3 import UsageListResult
from ._models_py3 import UsageName
from ._models_py3 import UserAssignedIdentity
from ._models_py3 import VirtualNetworkRule


from ._storage_management_client_enums import (
    AccessTier,
    AccountImmutabilityPolicyState,
    AccountStatus,
    AccountType,
    AllowedCopyScope,
    AllowedMethods,
    BlobInventoryPolicyName,
    BlobRestoreProgressStatus,
    Bypass,
    CreatedByType,
    DefaultAction,
    DefaultSharePermission,
    DirectoryServiceOptions,
    DnsEndpointType,
    EnabledProtocols,
    EncryptionScopeSource,
    EncryptionScopeState,
    ExpirationAction,
    ExtendedLocationTypes,
    Format,
    GeoReplicationStatus,
    HttpProtocol,
    IdentityType,
    ImmutabilityPolicyState,
    ImmutabilityPolicyUpdateType,
    InventoryRuleType,
    KeyPermission,
    KeySource,
    KeyType,
    Kind,
    LargeFileSharesState,
    LeaseContainerRequestEnum,
    LeaseDuration,
    LeaseShareAction,
    LeaseState,
    LeaseStatus,
    ListContainersInclude,
    ManagementPolicyName,
    MigrationState,
    MinimumTlsVersion,
    Name,
    ObjectType,
    Permissions,
    PrivateEndpointConnectionProvisioningState,
    PrivateEndpointServiceConnectionStatus,
    ProvisioningState,
    PublicAccess,
    PublicNetworkAccess,
    Reason,
    ReasonCode,
    RootSquashType,
    RoutingChoice,
    RuleType,
    Schedule,
    Services,
    ShareAccessTier,
    SignedResource,
    SignedResourceTypes,
    SkuConversionStatus,
    SkuName,
    SkuTier,
    State,
    StorageAccountExpand,
    UsageUnit,
)
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk
__all__ = [
    'AccessPolicy',
    'AccountImmutabilityPolicyProperties',
    'AccountSasParameters',
    'ActiveDirectoryProperties',
    'AzureEntityResource',
    'AzureFilesIdentityBasedAuthentication',
    'BlobContainer',
    'BlobInventoryPolicy',
    'BlobInventoryPolicyDefinition',
    'BlobInventoryPolicyFilter',
    'BlobInventoryPolicyRule',
    'BlobInventoryPolicySchema',
    'BlobRestoreParameters',
    'BlobRestoreRange',
    'BlobRestoreStatus',
    'BlobServiceItems',
    'BlobServiceProperties',
    'ChangeFeed',
    'CheckNameAvailabilityResult',
    'CloudErrorBody',
    'CorsRule',
    'CorsRules',
    'CustomDomain',
    'DateAfterCreation',
    'DateAfterModification',
    'DeleteRetentionPolicy',
    'DeletedAccount',
    'DeletedAccountListResult',
    'DeletedShare',
    'Dimension',
    'Encryption',
    'EncryptionIdentity',
    'EncryptionScope',
    'EncryptionScopeKeyVaultProperties',
    'EncryptionScopeListResult',
    'EncryptionService',
    'EncryptionServices',
    'Endpoints',
    'ErrorResponse',
    'ErrorResponseBody',
    'ExtendedLocation',
    'FileServiceItems',
    'FileServiceProperties',
    'FileShare',
    'FileShareItem',
    'FileShareItems',
    'GeoReplicationStats',
    'IPRule',
    'Identity',
    'ImmutabilityPolicy',
    'ImmutabilityPolicyProperties',
    'ImmutableStorageAccount',
    'ImmutableStorageWithVersioning',
    'KeyCreationTime',
    'KeyPolicy',
    'KeyVaultProperties',
    'LastAccessTimeTrackingPolicy',
    'LeaseContainerRequest',
    'LeaseContainerResponse',
    'LeaseShareRequest',
    'LeaseShareResponse',
    'LegalHold',
    'LegalHoldProperties',
    'ListAccountSasResponse',
    'ListBlobInventoryPolicy',
    'ListContainerItem',
    'ListContainerItems',
    'ListQueue',
    'ListQueueResource',
    'ListQueueServices',
    'ListServiceSasResponse',
    'ListTableResource',
    'ListTableServices',
    'LocalUser',
    'LocalUserKeys',
    'LocalUserRegeneratePasswordResult',
    'LocalUsers',
    'ManagementPolicy',
    'ManagementPolicyAction',
    'ManagementPolicyBaseBlob',
    'ManagementPolicyDefinition',
    'ManagementPolicyFilter',
    'ManagementPolicyRule',
    'ManagementPolicySchema',
    'ManagementPolicySnapShot',
    'ManagementPolicyVersion',
    'MetricSpecification',
    'Multichannel',
    'NetworkRuleSet',
    'ObjectReplicationPolicies',
    'ObjectReplicationPolicy',
    'ObjectReplicationPolicyFilter',
    'ObjectReplicationPolicyRule',
    'Operation',
    'OperationDisplay',
    'OperationListResult',
    'PermissionScope',
    'PrivateEndpoint',
    'PrivateEndpointConnection',
    'PrivateEndpointConnectionListResult',
    'PrivateLinkResource',
    'PrivateLinkResourceListResult',
    'PrivateLinkServiceConnectionState',
    'ProtectedAppendWritesHistory',
    'ProtocolSettings',
    'ProxyResource',
    'QueueServiceProperties',
    'Resource',
    'ResourceAccessRule',
    'RestorePolicyProperties',
    'Restriction',
    'RoutingPreference',
    'SKUCapability',
    'SasPolicy',
    'ServiceSasParameters',
    'ServiceSpecification',
    'SignedIdentifier',
    'Sku',
    'SkuInformation',
    'SmbSetting',
    'SshPublicKey',
    'StorageAccount',
    'StorageAccountCheckNameAvailabilityParameters',
    'StorageAccountCreateParameters',
    'StorageAccountInternetEndpoints',
    'StorageAccountKey',
    'StorageAccountListKeysResult',
    'StorageAccountListResult',
    'StorageAccountMicrosoftEndpoints',
    'StorageAccountRegenerateKeyParameters',
    'StorageAccountSkuConversionStatus',
    'StorageAccountUpdateParameters',
    'StorageQueue',
    'StorageSkuListResult',
    'SystemData',
    'Table',
    'TableAccessPolicy',
    'TableServiceProperties',
    'TableSignedIdentifier',
    'TagFilter',
    'TagProperty',
    'TrackedResource',
    'UpdateHistoryProperty',
    'Usage',
    'UsageListResult',
    'UsageName',
    'UserAssignedIdentity',
    'VirtualNetworkRule',
    'AccessTier',
    'AccountImmutabilityPolicyState',
    'AccountStatus',
    'AccountType',
    'AllowedCopyScope',
    'AllowedMethods',
    'BlobInventoryPolicyName',
    'BlobRestoreProgressStatus',
    'Bypass',
    'CreatedByType',
    'DefaultAction',
    'DefaultSharePermission',
    'DirectoryServiceOptions',
    'DnsEndpointType',
    'EnabledProtocols',
    'EncryptionScopeSource',
    'EncryptionScopeState',
    'ExpirationAction',
    'ExtendedLocationTypes',
    'Format',
    'GeoReplicationStatus',
    'HttpProtocol',
    'IdentityType',
    'ImmutabilityPolicyState',
    'ImmutabilityPolicyUpdateType',
    'InventoryRuleType',
    'KeyPermission',
    'KeySource',
    'KeyType',
    'Kind',
    'LargeFileSharesState',
    'LeaseContainerRequestEnum',
    'LeaseDuration',
    'LeaseShareAction',
    'LeaseState',
    'LeaseStatus',
    'ListContainersInclude',
    'ManagementPolicyName',
    'MigrationState',
    'MinimumTlsVersion',
    'Name',
    'ObjectType',
    'Permissions',
    'PrivateEndpointConnectionProvisioningState',
    'PrivateEndpointServiceConnectionStatus',
    'ProvisioningState',
    'PublicAccess',
    'PublicNetworkAccess',
    'Reason',
    'ReasonCode',
    'RootSquashType',
    'RoutingChoice',
    'RuleType',
    'Schedule',
    'Services',
    'ShareAccessTier',
    'SignedResource',
    'SignedResourceTypes',
    'SkuConversionStatus',
    'SkuName',
    'SkuTier',
    'State',
    'StorageAccountExpand',
    'UsageUnit',
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()