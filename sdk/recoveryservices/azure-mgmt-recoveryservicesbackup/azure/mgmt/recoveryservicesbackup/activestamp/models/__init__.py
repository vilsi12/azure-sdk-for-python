# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import AzureBackupGoalFeatureSupportRequest
from ._models_py3 import AzureBackupServerContainer
from ._models_py3 import AzureBackupServerEngine
from ._models_py3 import AzureFileShareBackupRequest
from ._models_py3 import AzureFileShareProtectableItem
from ._models_py3 import AzureFileShareProtectionPolicy
from ._models_py3 import AzureFileShareProvisionILRRequest
from ._models_py3 import AzureFileShareRecoveryPoint
from ._models_py3 import AzureFileShareRestoreRequest
from ._models_py3 import AzureFileshareProtectedItem
from ._models_py3 import AzureFileshareProtectedItemExtendedInfo
from ._models_py3 import AzureIaaSClassicComputeVMContainer
from ._models_py3 import AzureIaaSClassicComputeVMProtectableItem
from ._models_py3 import AzureIaaSClassicComputeVMProtectedItem
from ._models_py3 import AzureIaaSComputeVMContainer
from ._models_py3 import AzureIaaSComputeVMProtectableItem
from ._models_py3 import AzureIaaSComputeVMProtectedItem
from ._models_py3 import AzureIaaSVMErrorInfo
from ._models_py3 import AzureIaaSVMHealthDetails
from ._models_py3 import AzureIaaSVMJob
from ._models_py3 import AzureIaaSVMJobExtendedInfo
from ._models_py3 import AzureIaaSVMJobTaskDetails
from ._models_py3 import AzureIaaSVMJobV2
from ._models_py3 import AzureIaaSVMProtectedItem
from ._models_py3 import AzureIaaSVMProtectedItemExtendedInfo
from ._models_py3 import AzureIaaSVMProtectionPolicy
from ._models_py3 import AzureRecoveryServiceVaultProtectionIntent
from ._models_py3 import AzureResourceProtectionIntent
from ._models_py3 import AzureSQLAGWorkloadContainerProtectionContainer
from ._models_py3 import AzureSqlContainer
from ._models_py3 import AzureSqlProtectedItem
from ._models_py3 import AzureSqlProtectedItemExtendedInfo
from ._models_py3 import AzureSqlProtectionPolicy
from ._models_py3 import AzureStorageContainer
from ._models_py3 import AzureStorageErrorInfo
from ._models_py3 import AzureStorageJob
from ._models_py3 import AzureStorageJobExtendedInfo
from ._models_py3 import AzureStorageJobTaskDetails
from ._models_py3 import AzureStorageProtectableContainer
from ._models_py3 import AzureVMAppContainerProtectableContainer
from ._models_py3 import AzureVMAppContainerProtectionContainer
from ._models_py3 import AzureVMResourceFeatureSupportRequest
from ._models_py3 import AzureVMResourceFeatureSupportResponse
from ._models_py3 import AzureVmWorkloadItem
from ._models_py3 import AzureVmWorkloadProtectableItem
from ._models_py3 import AzureVmWorkloadProtectedItem
from ._models_py3 import AzureVmWorkloadProtectedItemExtendedInfo
from ._models_py3 import AzureVmWorkloadProtectionPolicy
from ._models_py3 import AzureVmWorkloadSAPAseDatabaseProtectedItem
from ._models_py3 import AzureVmWorkloadSAPAseDatabaseWorkloadItem
from ._models_py3 import AzureVmWorkloadSAPAseSystemProtectableItem
from ._models_py3 import AzureVmWorkloadSAPAseSystemWorkloadItem
from ._models_py3 import AzureVmWorkloadSAPHanaDBInstance
from ._models_py3 import AzureVmWorkloadSAPHanaDBInstanceProtectedItem
from ._models_py3 import AzureVmWorkloadSAPHanaDatabaseProtectableItem
from ._models_py3 import AzureVmWorkloadSAPHanaDatabaseProtectedItem
from ._models_py3 import AzureVmWorkloadSAPHanaDatabaseWorkloadItem
from ._models_py3 import AzureVmWorkloadSAPHanaHSR
from ._models_py3 import AzureVmWorkloadSAPHanaSystemProtectableItem
from ._models_py3 import AzureVmWorkloadSAPHanaSystemWorkloadItem
from ._models_py3 import AzureVmWorkloadSQLAvailabilityGroupProtectableItem
from ._models_py3 import AzureVmWorkloadSQLDatabaseProtectableItem
from ._models_py3 import AzureVmWorkloadSQLDatabaseProtectedItem
from ._models_py3 import AzureVmWorkloadSQLDatabaseWorkloadItem
from ._models_py3 import AzureVmWorkloadSQLInstanceProtectableItem
from ._models_py3 import AzureVmWorkloadSQLInstanceWorkloadItem
from ._models_py3 import AzureWorkloadAutoProtectionIntent
from ._models_py3 import AzureWorkloadBackupRequest
from ._models_py3 import AzureWorkloadContainer
from ._models_py3 import AzureWorkloadContainerAutoProtectionIntent
from ._models_py3 import AzureWorkloadContainerExtendedInfo
from ._models_py3 import AzureWorkloadErrorInfo
from ._models_py3 import AzureWorkloadJob
from ._models_py3 import AzureWorkloadJobExtendedInfo
from ._models_py3 import AzureWorkloadJobTaskDetails
from ._models_py3 import AzureWorkloadPointInTimeRecoveryPoint
from ._models_py3 import AzureWorkloadPointInTimeRestoreRequest
from ._models_py3 import AzureWorkloadRecoveryPoint
from ._models_py3 import AzureWorkloadRestoreRequest
from ._models_py3 import AzureWorkloadSAPHanaPointInTimeRecoveryPoint
from ._models_py3 import AzureWorkloadSAPHanaPointInTimeRestoreRequest
from ._models_py3 import AzureWorkloadSAPHanaPointInTimeRestoreWithRehydrateRequest
from ._models_py3 import AzureWorkloadSAPHanaRecoveryPoint
from ._models_py3 import AzureWorkloadSAPHanaRestoreRequest
from ._models_py3 import AzureWorkloadSAPHanaRestoreWithRehydrateRequest
from ._models_py3 import AzureWorkloadSQLAutoProtectionIntent
from ._models_py3 import AzureWorkloadSQLPointInTimeRecoveryPoint
from ._models_py3 import AzureWorkloadSQLPointInTimeRestoreRequest
from ._models_py3 import AzureWorkloadSQLPointInTimeRestoreWithRehydrateRequest
from ._models_py3 import AzureWorkloadSQLRecoveryPoint
from ._models_py3 import AzureWorkloadSQLRecoveryPointExtendedInfo
from ._models_py3 import AzureWorkloadSQLRestoreRequest
from ._models_py3 import AzureWorkloadSQLRestoreWithRehydrateRequest
from ._models_py3 import BEKDetails
from ._models_py3 import BMSBackupEngineQueryObject
from ._models_py3 import BMSBackupEnginesQueryObject
from ._models_py3 import BMSBackupSummariesQueryObject
from ._models_py3 import BMSContainerQueryObject
from ._models_py3 import BMSContainersInquiryQueryObject
from ._models_py3 import BMSPOQueryObject
from ._models_py3 import BMSRPQueryObject
from ._models_py3 import BMSRefreshContainersQueryObject
from ._models_py3 import BMSWorkloadItemQueryObject
from ._models_py3 import BackupEngineBase
from ._models_py3 import BackupEngineBaseResource
from ._models_py3 import BackupEngineBaseResourceList
from ._models_py3 import BackupEngineExtendedInfo
from ._models_py3 import BackupManagementUsage
from ._models_py3 import BackupManagementUsageList
from ._models_py3 import BackupRequest
from ._models_py3 import BackupRequestResource
from ._models_py3 import BackupResourceConfig
from ._models_py3 import BackupResourceConfigResource
from ._models_py3 import BackupResourceEncryptionConfig
from ._models_py3 import BackupResourceEncryptionConfigExtended
from ._models_py3 import BackupResourceEncryptionConfigExtendedResource
from ._models_py3 import BackupResourceEncryptionConfigResource
from ._models_py3 import BackupResourceVaultConfig
from ._models_py3 import BackupResourceVaultConfigResource
from ._models_py3 import BackupStatusRequest
from ._models_py3 import BackupStatusResponse
from ._models_py3 import ClientDiscoveryDisplay
from ._models_py3 import ClientDiscoveryForLogSpecification
from ._models_py3 import ClientDiscoveryForProperties
from ._models_py3 import ClientDiscoveryForServiceSpecification
from ._models_py3 import ClientDiscoveryResponse
from ._models_py3 import ClientDiscoveryValueForSingleApi
from ._models_py3 import ClientScriptForConnect
from ._models_py3 import CloudErrorBody
from ._models_py3 import ContainerIdentityInfo
from ._models_py3 import DPMContainerExtendedInfo
from ._models_py3 import DPMProtectedItem
from ._models_py3 import DPMProtectedItemExtendedInfo
from ._models_py3 import DailyRetentionFormat
from ._models_py3 import DailyRetentionSchedule
from ._models_py3 import DailySchedule
from ._models_py3 import Day
from ._models_py3 import DiskExclusionProperties
from ._models_py3 import DiskInformation
from ._models_py3 import DistributedNodesInfo
from ._models_py3 import DpmBackupEngine
from ._models_py3 import DpmContainer
from ._models_py3 import DpmErrorInfo
from ._models_py3 import DpmJob
from ._models_py3 import DpmJobExtendedInfo
from ._models_py3 import DpmJobTaskDetails
from ._models_py3 import EncryptionDetails
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ErrorDetail
from ._models_py3 import ExportJobsOperationResultInfo
from ._models_py3 import ExtendedProperties
from ._models_py3 import FeatureSupportRequest
from ._models_py3 import GenericContainer
from ._models_py3 import GenericContainerExtendedInfo
from ._models_py3 import GenericProtectedItem
from ._models_py3 import GenericProtectionPolicy
from ._models_py3 import GenericRecoveryPoint
from ._models_py3 import GetProtectedItemQueryObject
from ._models_py3 import HourlySchedule
from ._models_py3 import ILRRequest
from ._models_py3 import ILRRequestResource
from ._models_py3 import IaaSVMContainer
from ._models_py3 import IaaSVMProtectableItem
from ._models_py3 import IaasVMBackupRequest
from ._models_py3 import IaasVMILRRegistrationRequest
from ._models_py3 import IaasVMRecoveryPoint
from ._models_py3 import IaasVMRestoreRequest
from ._models_py3 import IaasVMRestoreWithRehydrationRequest
from ._models_py3 import IdentityBasedRestoreDetails
from ._models_py3 import IdentityInfo
from ._models_py3 import InquiryInfo
from ._models_py3 import InquiryValidation
from ._models_py3 import InstantItemRecoveryTarget
from ._models_py3 import InstantRPAdditionalDetails
from ._models_py3 import Job
from ._models_py3 import JobQueryObject
from ._models_py3 import JobResource
from ._models_py3 import JobResourceList
from ._models_py3 import KEKDetails
from ._models_py3 import KPIResourceHealthDetails
from ._models_py3 import KeyAndSecretDetails
from ._models_py3 import ListRecoveryPointsRecommendedForMoveRequest
from ._models_py3 import LogSchedulePolicy
from ._models_py3 import LongTermRetentionPolicy
from ._models_py3 import LongTermSchedulePolicy
from ._models_py3 import MABContainerHealthDetails
from ._models_py3 import MabContainer
from ._models_py3 import MabContainerExtendedInfo
from ._models_py3 import MabErrorInfo
from ._models_py3 import MabFileFolderProtectedItem
from ._models_py3 import MabFileFolderProtectedItemExtendedInfo
from ._models_py3 import MabJob
from ._models_py3 import MabJobExtendedInfo
from ._models_py3 import MabJobTaskDetails
from ._models_py3 import MabProtectionPolicy
from ._models_py3 import MonthlyRetentionSchedule
from ._models_py3 import MoveRPAcrossTiersRequest
from ._models_py3 import NameInfo
from ._models_py3 import NewErrorResponse
from ._models_py3 import NewErrorResponseError
from ._models_py3 import OperationResultInfo
from ._models_py3 import OperationResultInfoBase
from ._models_py3 import OperationResultInfoBaseResource
from ._models_py3 import OperationStatus
from ._models_py3 import OperationStatusError
from ._models_py3 import OperationStatusExtendedInfo
from ._models_py3 import OperationStatusJobExtendedInfo
from ._models_py3 import OperationStatusJobsExtendedInfo
from ._models_py3 import OperationStatusProvisionILRExtendedInfo
from ._models_py3 import OperationStatusValidateOperationExtendedInfo
from ._models_py3 import OperationWorkerResponse
from ._models_py3 import PointInTimeRange
from ._models_py3 import PreBackupValidation
from ._models_py3 import PreValidateEnableBackupRequest
from ._models_py3 import PreValidateEnableBackupResponse
from ._models_py3 import PrepareDataMoveRequest
from ._models_py3 import PrepareDataMoveResponse
from ._models_py3 import PrivateEndpoint
from ._models_py3 import PrivateEndpointConnection
from ._models_py3 import PrivateEndpointConnectionResource
from ._models_py3 import PrivateLinkServiceConnectionState
from ._models_py3 import ProtectableContainer
from ._models_py3 import ProtectableContainerResource
from ._models_py3 import ProtectableContainerResourceList
from ._models_py3 import ProtectedItem
from ._models_py3 import ProtectedItemQueryObject
from ._models_py3 import ProtectedItemResource
from ._models_py3 import ProtectedItemResourceList
from ._models_py3 import ProtectionContainer
from ._models_py3 import ProtectionContainerResource
from ._models_py3 import ProtectionContainerResourceList
from ._models_py3 import ProtectionIntent
from ._models_py3 import ProtectionIntentQueryObject
from ._models_py3 import ProtectionIntentResource
from ._models_py3 import ProtectionIntentResourceList
from ._models_py3 import ProtectionPolicy
from ._models_py3 import ProtectionPolicyQueryObject
from ._models_py3 import ProtectionPolicyResource
from ._models_py3 import ProtectionPolicyResourceList
from ._models_py3 import RecoveryPoint
from ._models_py3 import RecoveryPointDiskConfiguration
from ._models_py3 import RecoveryPointMoveReadinessInfo
from ._models_py3 import RecoveryPointRehydrationInfo
from ._models_py3 import RecoveryPointResource
from ._models_py3 import RecoveryPointResourceList
from ._models_py3 import RecoveryPointTierInformation
from ._models_py3 import RecoveryPointTierInformationV2
from ._models_py3 import Resource
from ._models_py3 import ResourceGuardOperationDetail
from ._models_py3 import ResourceGuardProxyBase
from ._models_py3 import ResourceGuardProxyBaseResource
from ._models_py3 import ResourceGuardProxyBaseResourceList
from ._models_py3 import ResourceHealthDetails
from ._models_py3 import ResourceList
from ._models_py3 import RestoreFileSpecs
from ._models_py3 import RestoreRequest
from ._models_py3 import RestoreRequestResource
from ._models_py3 import RetentionDuration
from ._models_py3 import RetentionPolicy
from ._models_py3 import SQLDataDirectory
from ._models_py3 import SQLDataDirectoryMapping
from ._models_py3 import SchedulePolicy
from ._models_py3 import SecurityPinBase
from ._models_py3 import Settings
from ._models_py3 import SimpleRetentionPolicy
from ._models_py3 import SimpleSchedulePolicy
from ._models_py3 import SimpleSchedulePolicyV2
from ._models_py3 import SubProtectionPolicy
from ._models_py3 import TargetAFSRestoreInfo
from ._models_py3 import TargetRestoreInfo
from ._models_py3 import TieringPolicy
from ._models_py3 import TokenInformation
from ._models_py3 import TriggerDataMoveRequest
from ._models_py3 import UnlockDeleteRequest
from ._models_py3 import UnlockDeleteResponse
from ._models_py3 import ValidateIaasVMRestoreOperationRequest
from ._models_py3 import ValidateOperationRequest
from ._models_py3 import ValidateOperationResponse
from ._models_py3 import ValidateOperationsResponse
from ._models_py3 import ValidateRestoreOperationRequest
from ._models_py3 import VaultJob
from ._models_py3 import VaultJobErrorInfo
from ._models_py3 import VaultJobExtendedInfo
from ._models_py3 import VaultStorageConfigOperationResultResponse
from ._models_py3 import WeeklyRetentionFormat
from ._models_py3 import WeeklyRetentionSchedule
from ._models_py3 import WeeklySchedule
from ._models_py3 import WorkloadInquiryDetails
from ._models_py3 import WorkloadItem
from ._models_py3 import WorkloadItemResource
from ._models_py3 import WorkloadItemResourceList
from ._models_py3 import WorkloadProtectableItem
from ._models_py3 import WorkloadProtectableItemResource
from ._models_py3 import WorkloadProtectableItemResourceList
from ._models_py3 import YearlyRetentionSchedule

from ._recovery_services_backup_client_enums import AcquireStorageAccountLock
from ._recovery_services_backup_client_enums import AzureFileShareType
from ._recovery_services_backup_client_enums import BackupEngineType
from ._recovery_services_backup_client_enums import BackupItemType
from ._recovery_services_backup_client_enums import BackupManagementType
from ._recovery_services_backup_client_enums import BackupType
from ._recovery_services_backup_client_enums import ContainerType
from ._recovery_services_backup_client_enums import CopyOptions
from ._recovery_services_backup_client_enums import CreateMode
from ._recovery_services_backup_client_enums import DataMoveLevel
from ._recovery_services_backup_client_enums import DataSourceType
from ._recovery_services_backup_client_enums import DayOfWeek
from ._recovery_services_backup_client_enums import DedupState
from ._recovery_services_backup_client_enums import EncryptionAtRestType
from ._recovery_services_backup_client_enums import EnhancedSecurityState
from ._recovery_services_backup_client_enums import FabricName
from ._recovery_services_backup_client_enums import HealthState
from ._recovery_services_backup_client_enums import HealthStatus
from ._recovery_services_backup_client_enums import HttpStatusCode
from ._recovery_services_backup_client_enums import IAASVMPolicyType
from ._recovery_services_backup_client_enums import InfrastructureEncryptionState
from ._recovery_services_backup_client_enums import InquiryStatus
from ._recovery_services_backup_client_enums import IntentItemType
from ._recovery_services_backup_client_enums import JobOperationType
from ._recovery_services_backup_client_enums import JobStatus
from ._recovery_services_backup_client_enums import JobSupportedAction
from ._recovery_services_backup_client_enums import LastBackupStatus
from ._recovery_services_backup_client_enums import LastUpdateStatus
from ._recovery_services_backup_client_enums import MabServerType
from ._recovery_services_backup_client_enums import MonthOfYear
from ._recovery_services_backup_client_enums import OperationStatusValues
from ._recovery_services_backup_client_enums import OperationType
from ._recovery_services_backup_client_enums import OverwriteOptions
from ._recovery_services_backup_client_enums import PolicyType
from ._recovery_services_backup_client_enums import PrivateEndpointConnectionStatus
from ._recovery_services_backup_client_enums import ProtectableContainerType
from ._recovery_services_backup_client_enums import ProtectedItemHealthStatus
from ._recovery_services_backup_client_enums import ProtectedItemState
from ._recovery_services_backup_client_enums import ProtectionIntentItemType
from ._recovery_services_backup_client_enums import ProtectionState
from ._recovery_services_backup_client_enums import ProtectionStatus
from ._recovery_services_backup_client_enums import ProvisioningState
from ._recovery_services_backup_client_enums import RecoveryMode
from ._recovery_services_backup_client_enums import RecoveryPointTierStatus
from ._recovery_services_backup_client_enums import RecoveryPointTierType
from ._recovery_services_backup_client_enums import RecoveryType
from ._recovery_services_backup_client_enums import RehydrationPriority
from ._recovery_services_backup_client_enums import ResourceHealthStatus
from ._recovery_services_backup_client_enums import RestorePointQueryType
from ._recovery_services_backup_client_enums import RestorePointType
from ._recovery_services_backup_client_enums import RestoreRequestType
from ._recovery_services_backup_client_enums import RetentionDurationType
from ._recovery_services_backup_client_enums import RetentionScheduleFormat
from ._recovery_services_backup_client_enums import SQLDataDirectoryType
from ._recovery_services_backup_client_enums import ScheduleRunType
from ._recovery_services_backup_client_enums import SoftDeleteFeatureState
from ._recovery_services_backup_client_enums import StorageType
from ._recovery_services_backup_client_enums import StorageTypeState
from ._recovery_services_backup_client_enums import SupportStatus
from ._recovery_services_backup_client_enums import TieringMode
from ._recovery_services_backup_client_enums import Type
from ._recovery_services_backup_client_enums import UsagesUnit
from ._recovery_services_backup_client_enums import ValidationStatus
from ._recovery_services_backup_client_enums import WeekOfMonth
from ._recovery_services_backup_client_enums import WorkloadItemType
from ._recovery_services_backup_client_enums import WorkloadType
from ._recovery_services_backup_client_enums import XcoolState
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "AzureBackupGoalFeatureSupportRequest",
    "AzureBackupServerContainer",
    "AzureBackupServerEngine",
    "AzureFileShareBackupRequest",
    "AzureFileShareProtectableItem",
    "AzureFileShareProtectionPolicy",
    "AzureFileShareProvisionILRRequest",
    "AzureFileShareRecoveryPoint",
    "AzureFileShareRestoreRequest",
    "AzureFileshareProtectedItem",
    "AzureFileshareProtectedItemExtendedInfo",
    "AzureIaaSClassicComputeVMContainer",
    "AzureIaaSClassicComputeVMProtectableItem",
    "AzureIaaSClassicComputeVMProtectedItem",
    "AzureIaaSComputeVMContainer",
    "AzureIaaSComputeVMProtectableItem",
    "AzureIaaSComputeVMProtectedItem",
    "AzureIaaSVMErrorInfo",
    "AzureIaaSVMHealthDetails",
    "AzureIaaSVMJob",
    "AzureIaaSVMJobExtendedInfo",
    "AzureIaaSVMJobTaskDetails",
    "AzureIaaSVMJobV2",
    "AzureIaaSVMProtectedItem",
    "AzureIaaSVMProtectedItemExtendedInfo",
    "AzureIaaSVMProtectionPolicy",
    "AzureRecoveryServiceVaultProtectionIntent",
    "AzureResourceProtectionIntent",
    "AzureSQLAGWorkloadContainerProtectionContainer",
    "AzureSqlContainer",
    "AzureSqlProtectedItem",
    "AzureSqlProtectedItemExtendedInfo",
    "AzureSqlProtectionPolicy",
    "AzureStorageContainer",
    "AzureStorageErrorInfo",
    "AzureStorageJob",
    "AzureStorageJobExtendedInfo",
    "AzureStorageJobTaskDetails",
    "AzureStorageProtectableContainer",
    "AzureVMAppContainerProtectableContainer",
    "AzureVMAppContainerProtectionContainer",
    "AzureVMResourceFeatureSupportRequest",
    "AzureVMResourceFeatureSupportResponse",
    "AzureVmWorkloadItem",
    "AzureVmWorkloadProtectableItem",
    "AzureVmWorkloadProtectedItem",
    "AzureVmWorkloadProtectedItemExtendedInfo",
    "AzureVmWorkloadProtectionPolicy",
    "AzureVmWorkloadSAPAseDatabaseProtectedItem",
    "AzureVmWorkloadSAPAseDatabaseWorkloadItem",
    "AzureVmWorkloadSAPAseSystemProtectableItem",
    "AzureVmWorkloadSAPAseSystemWorkloadItem",
    "AzureVmWorkloadSAPHanaDBInstance",
    "AzureVmWorkloadSAPHanaDBInstanceProtectedItem",
    "AzureVmWorkloadSAPHanaDatabaseProtectableItem",
    "AzureVmWorkloadSAPHanaDatabaseProtectedItem",
    "AzureVmWorkloadSAPHanaDatabaseWorkloadItem",
    "AzureVmWorkloadSAPHanaHSR",
    "AzureVmWorkloadSAPHanaSystemProtectableItem",
    "AzureVmWorkloadSAPHanaSystemWorkloadItem",
    "AzureVmWorkloadSQLAvailabilityGroupProtectableItem",
    "AzureVmWorkloadSQLDatabaseProtectableItem",
    "AzureVmWorkloadSQLDatabaseProtectedItem",
    "AzureVmWorkloadSQLDatabaseWorkloadItem",
    "AzureVmWorkloadSQLInstanceProtectableItem",
    "AzureVmWorkloadSQLInstanceWorkloadItem",
    "AzureWorkloadAutoProtectionIntent",
    "AzureWorkloadBackupRequest",
    "AzureWorkloadContainer",
    "AzureWorkloadContainerAutoProtectionIntent",
    "AzureWorkloadContainerExtendedInfo",
    "AzureWorkloadErrorInfo",
    "AzureWorkloadJob",
    "AzureWorkloadJobExtendedInfo",
    "AzureWorkloadJobTaskDetails",
    "AzureWorkloadPointInTimeRecoveryPoint",
    "AzureWorkloadPointInTimeRestoreRequest",
    "AzureWorkloadRecoveryPoint",
    "AzureWorkloadRestoreRequest",
    "AzureWorkloadSAPHanaPointInTimeRecoveryPoint",
    "AzureWorkloadSAPHanaPointInTimeRestoreRequest",
    "AzureWorkloadSAPHanaPointInTimeRestoreWithRehydrateRequest",
    "AzureWorkloadSAPHanaRecoveryPoint",
    "AzureWorkloadSAPHanaRestoreRequest",
    "AzureWorkloadSAPHanaRestoreWithRehydrateRequest",
    "AzureWorkloadSQLAutoProtectionIntent",
    "AzureWorkloadSQLPointInTimeRecoveryPoint",
    "AzureWorkloadSQLPointInTimeRestoreRequest",
    "AzureWorkloadSQLPointInTimeRestoreWithRehydrateRequest",
    "AzureWorkloadSQLRecoveryPoint",
    "AzureWorkloadSQLRecoveryPointExtendedInfo",
    "AzureWorkloadSQLRestoreRequest",
    "AzureWorkloadSQLRestoreWithRehydrateRequest",
    "BEKDetails",
    "BMSBackupEngineQueryObject",
    "BMSBackupEnginesQueryObject",
    "BMSBackupSummariesQueryObject",
    "BMSContainerQueryObject",
    "BMSContainersInquiryQueryObject",
    "BMSPOQueryObject",
    "BMSRPQueryObject",
    "BMSRefreshContainersQueryObject",
    "BMSWorkloadItemQueryObject",
    "BackupEngineBase",
    "BackupEngineBaseResource",
    "BackupEngineBaseResourceList",
    "BackupEngineExtendedInfo",
    "BackupManagementUsage",
    "BackupManagementUsageList",
    "BackupRequest",
    "BackupRequestResource",
    "BackupResourceConfig",
    "BackupResourceConfigResource",
    "BackupResourceEncryptionConfig",
    "BackupResourceEncryptionConfigExtended",
    "BackupResourceEncryptionConfigExtendedResource",
    "BackupResourceEncryptionConfigResource",
    "BackupResourceVaultConfig",
    "BackupResourceVaultConfigResource",
    "BackupStatusRequest",
    "BackupStatusResponse",
    "ClientDiscoveryDisplay",
    "ClientDiscoveryForLogSpecification",
    "ClientDiscoveryForProperties",
    "ClientDiscoveryForServiceSpecification",
    "ClientDiscoveryResponse",
    "ClientDiscoveryValueForSingleApi",
    "ClientScriptForConnect",
    "CloudErrorBody",
    "ContainerIdentityInfo",
    "DPMContainerExtendedInfo",
    "DPMProtectedItem",
    "DPMProtectedItemExtendedInfo",
    "DailyRetentionFormat",
    "DailyRetentionSchedule",
    "DailySchedule",
    "Day",
    "DiskExclusionProperties",
    "DiskInformation",
    "DistributedNodesInfo",
    "DpmBackupEngine",
    "DpmContainer",
    "DpmErrorInfo",
    "DpmJob",
    "DpmJobExtendedInfo",
    "DpmJobTaskDetails",
    "EncryptionDetails",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ExportJobsOperationResultInfo",
    "ExtendedProperties",
    "FeatureSupportRequest",
    "GenericContainer",
    "GenericContainerExtendedInfo",
    "GenericProtectedItem",
    "GenericProtectionPolicy",
    "GenericRecoveryPoint",
    "GetProtectedItemQueryObject",
    "HourlySchedule",
    "ILRRequest",
    "ILRRequestResource",
    "IaaSVMContainer",
    "IaaSVMProtectableItem",
    "IaasVMBackupRequest",
    "IaasVMILRRegistrationRequest",
    "IaasVMRecoveryPoint",
    "IaasVMRestoreRequest",
    "IaasVMRestoreWithRehydrationRequest",
    "IdentityBasedRestoreDetails",
    "IdentityInfo",
    "InquiryInfo",
    "InquiryValidation",
    "InstantItemRecoveryTarget",
    "InstantRPAdditionalDetails",
    "Job",
    "JobQueryObject",
    "JobResource",
    "JobResourceList",
    "KEKDetails",
    "KPIResourceHealthDetails",
    "KeyAndSecretDetails",
    "ListRecoveryPointsRecommendedForMoveRequest",
    "LogSchedulePolicy",
    "LongTermRetentionPolicy",
    "LongTermSchedulePolicy",
    "MABContainerHealthDetails",
    "MabContainer",
    "MabContainerExtendedInfo",
    "MabErrorInfo",
    "MabFileFolderProtectedItem",
    "MabFileFolderProtectedItemExtendedInfo",
    "MabJob",
    "MabJobExtendedInfo",
    "MabJobTaskDetails",
    "MabProtectionPolicy",
    "MonthlyRetentionSchedule",
    "MoveRPAcrossTiersRequest",
    "NameInfo",
    "NewErrorResponse",
    "NewErrorResponseError",
    "OperationResultInfo",
    "OperationResultInfoBase",
    "OperationResultInfoBaseResource",
    "OperationStatus",
    "OperationStatusError",
    "OperationStatusExtendedInfo",
    "OperationStatusJobExtendedInfo",
    "OperationStatusJobsExtendedInfo",
    "OperationStatusProvisionILRExtendedInfo",
    "OperationStatusValidateOperationExtendedInfo",
    "OperationWorkerResponse",
    "PointInTimeRange",
    "PreBackupValidation",
    "PreValidateEnableBackupRequest",
    "PreValidateEnableBackupResponse",
    "PrepareDataMoveRequest",
    "PrepareDataMoveResponse",
    "PrivateEndpoint",
    "PrivateEndpointConnection",
    "PrivateEndpointConnectionResource",
    "PrivateLinkServiceConnectionState",
    "ProtectableContainer",
    "ProtectableContainerResource",
    "ProtectableContainerResourceList",
    "ProtectedItem",
    "ProtectedItemQueryObject",
    "ProtectedItemResource",
    "ProtectedItemResourceList",
    "ProtectionContainer",
    "ProtectionContainerResource",
    "ProtectionContainerResourceList",
    "ProtectionIntent",
    "ProtectionIntentQueryObject",
    "ProtectionIntentResource",
    "ProtectionIntentResourceList",
    "ProtectionPolicy",
    "ProtectionPolicyQueryObject",
    "ProtectionPolicyResource",
    "ProtectionPolicyResourceList",
    "RecoveryPoint",
    "RecoveryPointDiskConfiguration",
    "RecoveryPointMoveReadinessInfo",
    "RecoveryPointRehydrationInfo",
    "RecoveryPointResource",
    "RecoveryPointResourceList",
    "RecoveryPointTierInformation",
    "RecoveryPointTierInformationV2",
    "Resource",
    "ResourceGuardOperationDetail",
    "ResourceGuardProxyBase",
    "ResourceGuardProxyBaseResource",
    "ResourceGuardProxyBaseResourceList",
    "ResourceHealthDetails",
    "ResourceList",
    "RestoreFileSpecs",
    "RestoreRequest",
    "RestoreRequestResource",
    "RetentionDuration",
    "RetentionPolicy",
    "SQLDataDirectory",
    "SQLDataDirectoryMapping",
    "SchedulePolicy",
    "SecurityPinBase",
    "Settings",
    "SimpleRetentionPolicy",
    "SimpleSchedulePolicy",
    "SimpleSchedulePolicyV2",
    "SubProtectionPolicy",
    "TargetAFSRestoreInfo",
    "TargetRestoreInfo",
    "TieringPolicy",
    "TokenInformation",
    "TriggerDataMoveRequest",
    "UnlockDeleteRequest",
    "UnlockDeleteResponse",
    "ValidateIaasVMRestoreOperationRequest",
    "ValidateOperationRequest",
    "ValidateOperationResponse",
    "ValidateOperationsResponse",
    "ValidateRestoreOperationRequest",
    "VaultJob",
    "VaultJobErrorInfo",
    "VaultJobExtendedInfo",
    "VaultStorageConfigOperationResultResponse",
    "WeeklyRetentionFormat",
    "WeeklyRetentionSchedule",
    "WeeklySchedule",
    "WorkloadInquiryDetails",
    "WorkloadItem",
    "WorkloadItemResource",
    "WorkloadItemResourceList",
    "WorkloadProtectableItem",
    "WorkloadProtectableItemResource",
    "WorkloadProtectableItemResourceList",
    "YearlyRetentionSchedule",
    "AcquireStorageAccountLock",
    "AzureFileShareType",
    "BackupEngineType",
    "BackupItemType",
    "BackupManagementType",
    "BackupType",
    "ContainerType",
    "CopyOptions",
    "CreateMode",
    "DataMoveLevel",
    "DataSourceType",
    "DayOfWeek",
    "DedupState",
    "EncryptionAtRestType",
    "EnhancedSecurityState",
    "FabricName",
    "HealthState",
    "HealthStatus",
    "HttpStatusCode",
    "IAASVMPolicyType",
    "InfrastructureEncryptionState",
    "InquiryStatus",
    "IntentItemType",
    "JobOperationType",
    "JobStatus",
    "JobSupportedAction",
    "LastBackupStatus",
    "LastUpdateStatus",
    "MabServerType",
    "MonthOfYear",
    "OperationStatusValues",
    "OperationType",
    "OverwriteOptions",
    "PolicyType",
    "PrivateEndpointConnectionStatus",
    "ProtectableContainerType",
    "ProtectedItemHealthStatus",
    "ProtectedItemState",
    "ProtectionIntentItemType",
    "ProtectionState",
    "ProtectionStatus",
    "ProvisioningState",
    "RecoveryMode",
    "RecoveryPointTierStatus",
    "RecoveryPointTierType",
    "RecoveryType",
    "RehydrationPriority",
    "ResourceHealthStatus",
    "RestorePointQueryType",
    "RestorePointType",
    "RestoreRequestType",
    "RetentionDurationType",
    "RetentionScheduleFormat",
    "SQLDataDirectoryType",
    "ScheduleRunType",
    "SoftDeleteFeatureState",
    "StorageType",
    "StorageTypeState",
    "SupportStatus",
    "TieringMode",
    "Type",
    "UsagesUnit",
    "ValidationStatus",
    "WeekOfMonth",
    "WorkloadItemType",
    "WorkloadType",
    "XcoolState",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
