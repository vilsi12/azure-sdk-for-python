# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import ApiError
from ._models_py3 import AuthenticationKeys
from ._models_py3 import AvailableServiceSku
from ._models_py3 import AvailableServiceSkuCapacity
from ._models_py3 import AvailableServiceSkuSku
from ._models_py3 import AzureActiveDirectoryApp
from ._models_py3 import AzureBlob
from ._models_py3 import BackupConfiguration
from ._models_py3 import BackupFileInfo
from ._models_py3 import BackupSetInfo
from ._models_py3 import BlobShare
from ._models_py3 import CheckOCIDriverTaskInput
from ._models_py3 import CheckOCIDriverTaskOutput
from ._models_py3 import CheckOCIDriverTaskProperties
from ._models_py3 import CommandProperties
from ._models_py3 import ConnectToMongoDbTaskProperties
from ._models_py3 import ConnectToSourceMySqlTaskInput
from ._models_py3 import ConnectToSourceMySqlTaskProperties
from ._models_py3 import ConnectToSourceNonSqlTaskOutput
from ._models_py3 import ConnectToSourceOracleSyncTaskInput
from ._models_py3 import ConnectToSourceOracleSyncTaskOutput
from ._models_py3 import ConnectToSourceOracleSyncTaskProperties
from ._models_py3 import ConnectToSourcePostgreSqlSyncTaskInput
from ._models_py3 import ConnectToSourcePostgreSqlSyncTaskOutput
from ._models_py3 import ConnectToSourcePostgreSqlSyncTaskProperties
from ._models_py3 import ConnectToSourceSqlServerSyncTaskProperties
from ._models_py3 import ConnectToSourceSqlServerTaskInput
from ._models_py3 import ConnectToSourceSqlServerTaskOutput
from ._models_py3 import ConnectToSourceSqlServerTaskOutputAgentJobLevel
from ._models_py3 import ConnectToSourceSqlServerTaskOutputDatabaseLevel
from ._models_py3 import ConnectToSourceSqlServerTaskOutputLoginLevel
from ._models_py3 import ConnectToSourceSqlServerTaskOutputTaskLevel
from ._models_py3 import ConnectToSourceSqlServerTaskProperties
from ._models_py3 import ConnectToTargetAzureDbForMySqlTaskInput
from ._models_py3 import ConnectToTargetAzureDbForMySqlTaskOutput
from ._models_py3 import ConnectToTargetAzureDbForMySqlTaskProperties
from ._models_py3 import ConnectToTargetAzureDbForPostgreSqlSyncTaskInput
from ._models_py3 import ConnectToTargetAzureDbForPostgreSqlSyncTaskOutput
from ._models_py3 import ConnectToTargetAzureDbForPostgreSqlSyncTaskProperties
from ._models_py3 import ConnectToTargetOracleAzureDbForPostgreSqlSyncTaskInput
from ._models_py3 import ConnectToTargetOracleAzureDbForPostgreSqlSyncTaskOutput
from ._models_py3 import ConnectToTargetOracleAzureDbForPostgreSqlSyncTaskOutputDatabaseSchemaMapItem
from ._models_py3 import ConnectToTargetOracleAzureDbForPostgreSqlSyncTaskProperties
from ._models_py3 import ConnectToTargetSqlDbSyncTaskInput
from ._models_py3 import ConnectToTargetSqlDbSyncTaskProperties
from ._models_py3 import ConnectToTargetSqlDbTaskInput
from ._models_py3 import ConnectToTargetSqlDbTaskOutput
from ._models_py3 import ConnectToTargetSqlDbTaskProperties
from ._models_py3 import ConnectToTargetSqlMISyncTaskInput
from ._models_py3 import ConnectToTargetSqlMISyncTaskOutput
from ._models_py3 import ConnectToTargetSqlMISyncTaskProperties
from ._models_py3 import ConnectToTargetSqlMITaskInput
from ._models_py3 import ConnectToTargetSqlMITaskOutput
from ._models_py3 import ConnectToTargetSqlMITaskProperties
from ._models_py3 import ConnectionInfo
from ._models_py3 import CopyProgressDetails
from ._models_py3 import DataIntegrityValidationResult
from ._models_py3 import DataItemMigrationSummaryResult
from ._models_py3 import DataMigrationError
from ._models_py3 import DataMigrationProjectMetadata
from ._models_py3 import DataMigrationService
from ._models_py3 import DataMigrationServiceList
from ._models_py3 import DataMigrationServiceStatusResponse
from ._models_py3 import Database
from ._models_py3 import DatabaseBackupInfo
from ._models_py3 import DatabaseFileInfo
from ._models_py3 import DatabaseFileInput
from ._models_py3 import DatabaseInfo
from ._models_py3 import DatabaseMigration
from ._models_py3 import DatabaseMigrationListResult
from ._models_py3 import DatabaseMigrationProperties
from ._models_py3 import DatabaseMigrationPropertiesSqlDb
from ._models_py3 import DatabaseMigrationPropertiesSqlMi
from ._models_py3 import DatabaseMigrationPropertiesSqlVm
from ._models_py3 import DatabaseMigrationSqlDb
from ._models_py3 import DatabaseMigrationSqlMi
from ._models_py3 import DatabaseMigrationSqlVm
from ._models_py3 import DatabaseObjectName
from ._models_py3 import DatabaseSummaryResult
from ._models_py3 import DatabaseTable
from ._models_py3 import DeleteNode
from ._models_py3 import ErrorInfo
from ._models_py3 import ExecutionStatistics
from ._models_py3 import FileList
from ._models_py3 import FileShare
from ._models_py3 import FileStorageInfo
from ._models_py3 import GetProjectDetailsNonSqlTaskInput
from ._models_py3 import GetTdeCertificatesSqlTaskInput
from ._models_py3 import GetTdeCertificatesSqlTaskOutput
from ._models_py3 import GetTdeCertificatesSqlTaskProperties
from ._models_py3 import GetUserTablesMySqlTaskInput
from ._models_py3 import GetUserTablesMySqlTaskOutput
from ._models_py3 import GetUserTablesMySqlTaskProperties
from ._models_py3 import GetUserTablesOracleTaskInput
from ._models_py3 import GetUserTablesOracleTaskOutput
from ._models_py3 import GetUserTablesOracleTaskProperties
from ._models_py3 import GetUserTablesPostgreSqlTaskInput
from ._models_py3 import GetUserTablesPostgreSqlTaskOutput
from ._models_py3 import GetUserTablesPostgreSqlTaskProperties
from ._models_py3 import GetUserTablesSqlSyncTaskInput
from ._models_py3 import GetUserTablesSqlSyncTaskOutput
from ._models_py3 import GetUserTablesSqlSyncTaskProperties
from ._models_py3 import GetUserTablesSqlTaskInput
from ._models_py3 import GetUserTablesSqlTaskOutput
from ._models_py3 import GetUserTablesSqlTaskProperties
from ._models_py3 import InstallOCIDriverTaskInput
from ._models_py3 import InstallOCIDriverTaskOutput
from ._models_py3 import InstallOCIDriverTaskProperties
from ._models_py3 import IntegrationRuntimeMonitoringData
from ._models_py3 import MiSqlConnectionInfo
from ._models_py3 import MigrateMISyncCompleteCommandInput
from ._models_py3 import MigrateMISyncCompleteCommandOutput
from ._models_py3 import MigrateMISyncCompleteCommandProperties
from ._models_py3 import MigrateMongoDbTaskProperties
from ._models_py3 import MigrateMySqlAzureDbForMySqlOfflineDatabaseInput
from ._models_py3 import MigrateMySqlAzureDbForMySqlOfflineTaskInput
from ._models_py3 import MigrateMySqlAzureDbForMySqlOfflineTaskOutput
from ._models_py3 import MigrateMySqlAzureDbForMySqlOfflineTaskOutputDatabaseLevel
from ._models_py3 import MigrateMySqlAzureDbForMySqlOfflineTaskOutputError
from ._models_py3 import MigrateMySqlAzureDbForMySqlOfflineTaskOutputMigrationLevel
from ._models_py3 import MigrateMySqlAzureDbForMySqlOfflineTaskOutputTableLevel
from ._models_py3 import MigrateMySqlAzureDbForMySqlOfflineTaskProperties
from ._models_py3 import MigrateMySqlAzureDbForMySqlSyncDatabaseInput
from ._models_py3 import MigrateMySqlAzureDbForMySqlSyncTaskInput
from ._models_py3 import MigrateMySqlAzureDbForMySqlSyncTaskOutput
from ._models_py3 import MigrateMySqlAzureDbForMySqlSyncTaskOutputDatabaseError
from ._models_py3 import MigrateMySqlAzureDbForMySqlSyncTaskOutputDatabaseLevel
from ._models_py3 import MigrateMySqlAzureDbForMySqlSyncTaskOutputError
from ._models_py3 import MigrateMySqlAzureDbForMySqlSyncTaskOutputMigrationLevel
from ._models_py3 import MigrateMySqlAzureDbForMySqlSyncTaskOutputTableLevel
from ._models_py3 import MigrateMySqlAzureDbForMySqlSyncTaskProperties
from ._models_py3 import MigrateOracleAzureDbForPostgreSqlSyncTaskProperties
from ._models_py3 import MigrateOracleAzureDbPostgreSqlSyncDatabaseInput
from ._models_py3 import MigrateOracleAzureDbPostgreSqlSyncTaskInput
from ._models_py3 import MigrateOracleAzureDbPostgreSqlSyncTaskOutput
from ._models_py3 import MigrateOracleAzureDbPostgreSqlSyncTaskOutputDatabaseError
from ._models_py3 import MigrateOracleAzureDbPostgreSqlSyncTaskOutputDatabaseLevel
from ._models_py3 import MigrateOracleAzureDbPostgreSqlSyncTaskOutputError
from ._models_py3 import MigrateOracleAzureDbPostgreSqlSyncTaskOutputMigrationLevel
from ._models_py3 import MigrateOracleAzureDbPostgreSqlSyncTaskOutputTableLevel
from ._models_py3 import MigratePostgreSqlAzureDbForPostgreSqlSyncDatabaseInput
from ._models_py3 import MigratePostgreSqlAzureDbForPostgreSqlSyncDatabaseTableInput
from ._models_py3 import MigratePostgreSqlAzureDbForPostgreSqlSyncTaskInput
from ._models_py3 import MigratePostgreSqlAzureDbForPostgreSqlSyncTaskOutput
from ._models_py3 import MigratePostgreSqlAzureDbForPostgreSqlSyncTaskOutputDatabaseError
from ._models_py3 import MigratePostgreSqlAzureDbForPostgreSqlSyncTaskOutputDatabaseLevel
from ._models_py3 import MigratePostgreSqlAzureDbForPostgreSqlSyncTaskOutputError
from ._models_py3 import MigratePostgreSqlAzureDbForPostgreSqlSyncTaskOutputMigrationLevel
from ._models_py3 import MigratePostgreSqlAzureDbForPostgreSqlSyncTaskOutputTableLevel
from ._models_py3 import MigratePostgreSqlAzureDbForPostgreSqlSyncTaskProperties
from ._models_py3 import MigrateSchemaSqlServerSqlDbDatabaseInput
from ._models_py3 import MigrateSchemaSqlServerSqlDbTaskInput
from ._models_py3 import MigrateSchemaSqlServerSqlDbTaskOutput
from ._models_py3 import MigrateSchemaSqlServerSqlDbTaskOutputDatabaseLevel
from ._models_py3 import MigrateSchemaSqlServerSqlDbTaskOutputError
from ._models_py3 import MigrateSchemaSqlServerSqlDbTaskOutputMigrationLevel
from ._models_py3 import MigrateSchemaSqlServerSqlDbTaskProperties
from ._models_py3 import MigrateSchemaSqlTaskOutputError
from ._models_py3 import MigrateSqlServerDatabaseInput
from ._models_py3 import MigrateSqlServerSqlDbDatabaseInput
from ._models_py3 import MigrateSqlServerSqlDbSyncDatabaseInput
from ._models_py3 import MigrateSqlServerSqlDbSyncTaskInput
from ._models_py3 import MigrateSqlServerSqlDbSyncTaskOutput
from ._models_py3 import MigrateSqlServerSqlDbSyncTaskOutputDatabaseError
from ._models_py3 import MigrateSqlServerSqlDbSyncTaskOutputDatabaseLevel
from ._models_py3 import MigrateSqlServerSqlDbSyncTaskOutputError
from ._models_py3 import MigrateSqlServerSqlDbSyncTaskOutputMigrationLevel
from ._models_py3 import MigrateSqlServerSqlDbSyncTaskOutputTableLevel
from ._models_py3 import MigrateSqlServerSqlDbSyncTaskProperties
from ._models_py3 import MigrateSqlServerSqlDbTaskInput
from ._models_py3 import MigrateSqlServerSqlDbTaskOutput
from ._models_py3 import MigrateSqlServerSqlDbTaskOutputDatabaseLevel
from ._models_py3 import MigrateSqlServerSqlDbTaskOutputDatabaseLevelValidationResult
from ._models_py3 import MigrateSqlServerSqlDbTaskOutputError
from ._models_py3 import MigrateSqlServerSqlDbTaskOutputMigrationLevel
from ._models_py3 import MigrateSqlServerSqlDbTaskOutputTableLevel
from ._models_py3 import MigrateSqlServerSqlDbTaskOutputValidationResult
from ._models_py3 import MigrateSqlServerSqlDbTaskProperties
from ._models_py3 import MigrateSqlServerSqlMIDatabaseInput
from ._models_py3 import MigrateSqlServerSqlMISyncTaskInput
from ._models_py3 import MigrateSqlServerSqlMISyncTaskOutput
from ._models_py3 import MigrateSqlServerSqlMISyncTaskOutputDatabaseLevel
from ._models_py3 import MigrateSqlServerSqlMISyncTaskOutputError
from ._models_py3 import MigrateSqlServerSqlMISyncTaskOutputMigrationLevel
from ._models_py3 import MigrateSqlServerSqlMISyncTaskProperties
from ._models_py3 import MigrateSqlServerSqlMITaskInput
from ._models_py3 import MigrateSqlServerSqlMITaskOutput
from ._models_py3 import MigrateSqlServerSqlMITaskOutputAgentJobLevel
from ._models_py3 import MigrateSqlServerSqlMITaskOutputDatabaseLevel
from ._models_py3 import MigrateSqlServerSqlMITaskOutputError
from ._models_py3 import MigrateSqlServerSqlMITaskOutputLoginLevel
from ._models_py3 import MigrateSqlServerSqlMITaskOutputMigrationLevel
from ._models_py3 import MigrateSqlServerSqlMITaskProperties
from ._models_py3 import MigrateSsisTaskInput
from ._models_py3 import MigrateSsisTaskOutput
from ._models_py3 import MigrateSsisTaskOutputMigrationLevel
from ._models_py3 import MigrateSsisTaskOutputProjectLevel
from ._models_py3 import MigrateSsisTaskProperties
from ._models_py3 import MigrateSyncCompleteCommandInput
from ._models_py3 import MigrateSyncCompleteCommandOutput
from ._models_py3 import MigrateSyncCompleteCommandProperties
from ._models_py3 import MigrationEligibilityInfo
from ._models_py3 import MigrationOperationInput
from ._models_py3 import MigrationReportResult
from ._models_py3 import MigrationStatusDetails
from ._models_py3 import MigrationTableMetadata
from ._models_py3 import MigrationValidationDatabaseLevelResult
from ._models_py3 import MigrationValidationDatabaseSummaryResult
from ._models_py3 import MigrationValidationOptions
from ._models_py3 import MigrationValidationResult
from ._models_py3 import MongoDbCancelCommand
from ._models_py3 import MongoDbClusterInfo
from ._models_py3 import MongoDbCollectionInfo
from ._models_py3 import MongoDbCollectionProgress
from ._models_py3 import MongoDbCollectionSettings
from ._models_py3 import MongoDbCommandInput
from ._models_py3 import MongoDbConnectionInfo
from ._models_py3 import MongoDbDatabaseInfo
from ._models_py3 import MongoDbDatabaseProgress
from ._models_py3 import MongoDbDatabaseSettings
from ._models_py3 import MongoDbError
from ._models_py3 import MongoDbFinishCommand
from ._models_py3 import MongoDbFinishCommandInput
from ._models_py3 import MongoDbMigrationProgress
from ._models_py3 import MongoDbMigrationSettings
from ._models_py3 import MongoDbObjectInfo
from ._models_py3 import MongoDbProgress
from ._models_py3 import MongoDbRestartCommand
from ._models_py3 import MongoDbShardKeyField
from ._models_py3 import MongoDbShardKeyInfo
from ._models_py3 import MongoDbShardKeySetting
from ._models_py3 import MongoDbThrottlingSettings
from ._models_py3 import MySqlConnectionInfo
from ._models_py3 import NameAvailabilityRequest
from ._models_py3 import NameAvailabilityResponse
from ._models_py3 import NodeMonitoringData
from ._models_py3 import NonSqlDataMigrationTable
from ._models_py3 import NonSqlDataMigrationTableResult
from ._models_py3 import NonSqlMigrationTaskInput
from ._models_py3 import NonSqlMigrationTaskOutput
from ._models_py3 import ODataError
from ._models_py3 import OfflineConfiguration
from ._models_py3 import OperationListResult
from ._models_py3 import OperationsDefinition
from ._models_py3 import OperationsDisplayDefinition
from ._models_py3 import OracleConnectionInfo
from ._models_py3 import OracleOCIDriverInfo
from ._models_py3 import OrphanedUserInfo
from ._models_py3 import PostgreSqlConnectionInfo
from ._models_py3 import Project
from ._models_py3 import ProjectFile
from ._models_py3 import ProjectFileProperties
from ._models_py3 import ProjectList
from ._models_py3 import ProjectTask
from ._models_py3 import ProjectTaskProperties
from ._models_py3 import ProxyResource
from ._models_py3 import QueryAnalysisValidationResult
from ._models_py3 import QueryExecutionResult
from ._models_py3 import Quota
from ._models_py3 import QuotaList
from ._models_py3 import QuotaName
from ._models_py3 import RegenAuthKeys
from ._models_py3 import ReportableException
from ._models_py3 import Resource
from ._models_py3 import ResourceSku
from ._models_py3 import ResourceSkuCapabilities
from ._models_py3 import ResourceSkuCapacity
from ._models_py3 import ResourceSkuCosts
from ._models_py3 import ResourceSkuRestrictions
from ._models_py3 import ResourceSkusResult
from ._models_py3 import SchemaComparisonValidationResult
from ._models_py3 import SchemaComparisonValidationResultType
from ._models_py3 import SchemaMigrationSetting
from ._models_py3 import SelectedCertificateInput
from ._models_py3 import ServerProperties
from ._models_py3 import ServiceOperation
from ._models_py3 import ServiceOperationDisplay
from ._models_py3 import ServiceOperationList
from ._models_py3 import ServiceSku
from ._models_py3 import ServiceSkuList
from ._models_py3 import SourceLocation
from ._models_py3 import SqlBackupFileInfo
from ._models_py3 import SqlBackupSetInfo
from ._models_py3 import SqlConnectionInfo
from ._models_py3 import SqlConnectionInformation
from ._models_py3 import SqlDbMigrationStatusDetails
from ._models_py3 import SqlDbOfflineConfiguration
from ._models_py3 import SqlFileShare
from ._models_py3 import SqlMigrationListResult
from ._models_py3 import SqlMigrationService
from ._models_py3 import SqlMigrationServiceUpdate
from ._models_py3 import SqlMigrationTaskInput
from ._models_py3 import SqlServerSqlMISyncTaskInput
from ._models_py3 import SsisMigrationInfo
from ._models_py3 import StartMigrationScenarioServerRoleResult
from ._models_py3 import SyncMigrationDatabaseErrorEvent
from ._models_py3 import SystemData
from ._models_py3 import TargetLocation
from ._models_py3 import TaskList
from ._models_py3 import TrackedResource
from ._models_py3 import UploadOCIDriverTaskInput
from ._models_py3 import UploadOCIDriverTaskOutput
from ._models_py3 import UploadOCIDriverTaskProperties
from ._models_py3 import ValidateMigrationInputSqlServerSqlDbSyncTaskProperties
from ._models_py3 import ValidateMigrationInputSqlServerSqlMISyncTaskInput
from ._models_py3 import ValidateMigrationInputSqlServerSqlMISyncTaskOutput
from ._models_py3 import ValidateMigrationInputSqlServerSqlMISyncTaskProperties
from ._models_py3 import ValidateMigrationInputSqlServerSqlMITaskInput
from ._models_py3 import ValidateMigrationInputSqlServerSqlMITaskOutput
from ._models_py3 import ValidateMigrationInputSqlServerSqlMITaskProperties
from ._models_py3 import ValidateMongoDbTaskProperties
from ._models_py3 import ValidateOracleAzureDbForPostgreSqlSyncTaskProperties
from ._models_py3 import ValidateOracleAzureDbPostgreSqlSyncTaskOutput
from ._models_py3 import ValidateSyncMigrationInputSqlServerTaskInput
from ._models_py3 import ValidateSyncMigrationInputSqlServerTaskOutput
from ._models_py3 import ValidationError
from ._models_py3 import WaitStatistics

from ._data_migration_management_client_enums import AuthenticationType
from ._data_migration_management_client_enums import BackupFileStatus
from ._data_migration_management_client_enums import BackupMode
from ._data_migration_management_client_enums import BackupType
from ._data_migration_management_client_enums import CommandState
from ._data_migration_management_client_enums import CommandType
from ._data_migration_management_client_enums import CreatedByType
from ._data_migration_management_client_enums import DataMigrationResultCode
from ._data_migration_management_client_enums import DatabaseCompatLevel
from ._data_migration_management_client_enums import DatabaseFileType
from ._data_migration_management_client_enums import DatabaseMigrationStage
from ._data_migration_management_client_enums import DatabaseMigrationState
from ._data_migration_management_client_enums import DatabaseState
from ._data_migration_management_client_enums import ErrorType
from ._data_migration_management_client_enums import LoginMigrationStage
from ._data_migration_management_client_enums import LoginType
from ._data_migration_management_client_enums import MigrationState
from ._data_migration_management_client_enums import MigrationStatus
from ._data_migration_management_client_enums import MongoDbClusterType
from ._data_migration_management_client_enums import MongoDbErrorType
from ._data_migration_management_client_enums import MongoDbMigrationState
from ._data_migration_management_client_enums import MongoDbProgressResultType
from ._data_migration_management_client_enums import MongoDbReplication
from ._data_migration_management_client_enums import MongoDbShardKeyOrder
from ._data_migration_management_client_enums import MySqlTargetPlatformType
from ._data_migration_management_client_enums import NameCheckFailureReason
from ._data_migration_management_client_enums import ObjectType
from ._data_migration_management_client_enums import OperationOrigin
from ._data_migration_management_client_enums import ProjectProvisioningState
from ._data_migration_management_client_enums import ProjectSourcePlatform
from ._data_migration_management_client_enums import ProjectTargetPlatform
from ._data_migration_management_client_enums import ReplicateMigrationState
from ._data_migration_management_client_enums import ResourceSkuCapacityScaleType
from ._data_migration_management_client_enums import ResourceSkuRestrictionsReasonCode
from ._data_migration_management_client_enums import ResourceSkuRestrictionsType
from ._data_migration_management_client_enums import ResourceType
from ._data_migration_management_client_enums import ScenarioSource
from ._data_migration_management_client_enums import ScenarioTarget
from ._data_migration_management_client_enums import SchemaMigrationOption
from ._data_migration_management_client_enums import SchemaMigrationStage
from ._data_migration_management_client_enums import ServerLevelPermissionsGroup
from ._data_migration_management_client_enums import ServiceProvisioningState
from ._data_migration_management_client_enums import ServiceScalability
from ._data_migration_management_client_enums import Severity
from ._data_migration_management_client_enums import SqlSourcePlatform
from ._data_migration_management_client_enums import SsisMigrationOverwriteOption
from ._data_migration_management_client_enums import SsisMigrationStage
from ._data_migration_management_client_enums import SsisStoreType
from ._data_migration_management_client_enums import SyncDatabaseMigrationReportingState
from ._data_migration_management_client_enums import SyncTableMigrationState
from ._data_migration_management_client_enums import TaskState
from ._data_migration_management_client_enums import TaskType
from ._data_migration_management_client_enums import UpdateActionType
from ._data_migration_management_client_enums import ValidationStatus
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ApiError",
    "AuthenticationKeys",
    "AvailableServiceSku",
    "AvailableServiceSkuCapacity",
    "AvailableServiceSkuSku",
    "AzureActiveDirectoryApp",
    "AzureBlob",
    "BackupConfiguration",
    "BackupFileInfo",
    "BackupSetInfo",
    "BlobShare",
    "CheckOCIDriverTaskInput",
    "CheckOCIDriverTaskOutput",
    "CheckOCIDriverTaskProperties",
    "CommandProperties",
    "ConnectToMongoDbTaskProperties",
    "ConnectToSourceMySqlTaskInput",
    "ConnectToSourceMySqlTaskProperties",
    "ConnectToSourceNonSqlTaskOutput",
    "ConnectToSourceOracleSyncTaskInput",
    "ConnectToSourceOracleSyncTaskOutput",
    "ConnectToSourceOracleSyncTaskProperties",
    "ConnectToSourcePostgreSqlSyncTaskInput",
    "ConnectToSourcePostgreSqlSyncTaskOutput",
    "ConnectToSourcePostgreSqlSyncTaskProperties",
    "ConnectToSourceSqlServerSyncTaskProperties",
    "ConnectToSourceSqlServerTaskInput",
    "ConnectToSourceSqlServerTaskOutput",
    "ConnectToSourceSqlServerTaskOutputAgentJobLevel",
    "ConnectToSourceSqlServerTaskOutputDatabaseLevel",
    "ConnectToSourceSqlServerTaskOutputLoginLevel",
    "ConnectToSourceSqlServerTaskOutputTaskLevel",
    "ConnectToSourceSqlServerTaskProperties",
    "ConnectToTargetAzureDbForMySqlTaskInput",
    "ConnectToTargetAzureDbForMySqlTaskOutput",
    "ConnectToTargetAzureDbForMySqlTaskProperties",
    "ConnectToTargetAzureDbForPostgreSqlSyncTaskInput",
    "ConnectToTargetAzureDbForPostgreSqlSyncTaskOutput",
    "ConnectToTargetAzureDbForPostgreSqlSyncTaskProperties",
    "ConnectToTargetOracleAzureDbForPostgreSqlSyncTaskInput",
    "ConnectToTargetOracleAzureDbForPostgreSqlSyncTaskOutput",
    "ConnectToTargetOracleAzureDbForPostgreSqlSyncTaskOutputDatabaseSchemaMapItem",
    "ConnectToTargetOracleAzureDbForPostgreSqlSyncTaskProperties",
    "ConnectToTargetSqlDbSyncTaskInput",
    "ConnectToTargetSqlDbSyncTaskProperties",
    "ConnectToTargetSqlDbTaskInput",
    "ConnectToTargetSqlDbTaskOutput",
    "ConnectToTargetSqlDbTaskProperties",
    "ConnectToTargetSqlMISyncTaskInput",
    "ConnectToTargetSqlMISyncTaskOutput",
    "ConnectToTargetSqlMISyncTaskProperties",
    "ConnectToTargetSqlMITaskInput",
    "ConnectToTargetSqlMITaskOutput",
    "ConnectToTargetSqlMITaskProperties",
    "ConnectionInfo",
    "CopyProgressDetails",
    "DataIntegrityValidationResult",
    "DataItemMigrationSummaryResult",
    "DataMigrationError",
    "DataMigrationProjectMetadata",
    "DataMigrationService",
    "DataMigrationServiceList",
    "DataMigrationServiceStatusResponse",
    "Database",
    "DatabaseBackupInfo",
    "DatabaseFileInfo",
    "DatabaseFileInput",
    "DatabaseInfo",
    "DatabaseMigration",
    "DatabaseMigrationListResult",
    "DatabaseMigrationProperties",
    "DatabaseMigrationPropertiesSqlDb",
    "DatabaseMigrationPropertiesSqlMi",
    "DatabaseMigrationPropertiesSqlVm",
    "DatabaseMigrationSqlDb",
    "DatabaseMigrationSqlMi",
    "DatabaseMigrationSqlVm",
    "DatabaseObjectName",
    "DatabaseSummaryResult",
    "DatabaseTable",
    "DeleteNode",
    "ErrorInfo",
    "ExecutionStatistics",
    "FileList",
    "FileShare",
    "FileStorageInfo",
    "GetProjectDetailsNonSqlTaskInput",
    "GetTdeCertificatesSqlTaskInput",
    "GetTdeCertificatesSqlTaskOutput",
    "GetTdeCertificatesSqlTaskProperties",
    "GetUserTablesMySqlTaskInput",
    "GetUserTablesMySqlTaskOutput",
    "GetUserTablesMySqlTaskProperties",
    "GetUserTablesOracleTaskInput",
    "GetUserTablesOracleTaskOutput",
    "GetUserTablesOracleTaskProperties",
    "GetUserTablesPostgreSqlTaskInput",
    "GetUserTablesPostgreSqlTaskOutput",
    "GetUserTablesPostgreSqlTaskProperties",
    "GetUserTablesSqlSyncTaskInput",
    "GetUserTablesSqlSyncTaskOutput",
    "GetUserTablesSqlSyncTaskProperties",
    "GetUserTablesSqlTaskInput",
    "GetUserTablesSqlTaskOutput",
    "GetUserTablesSqlTaskProperties",
    "InstallOCIDriverTaskInput",
    "InstallOCIDriverTaskOutput",
    "InstallOCIDriverTaskProperties",
    "IntegrationRuntimeMonitoringData",
    "MiSqlConnectionInfo",
    "MigrateMISyncCompleteCommandInput",
    "MigrateMISyncCompleteCommandOutput",
    "MigrateMISyncCompleteCommandProperties",
    "MigrateMongoDbTaskProperties",
    "MigrateMySqlAzureDbForMySqlOfflineDatabaseInput",
    "MigrateMySqlAzureDbForMySqlOfflineTaskInput",
    "MigrateMySqlAzureDbForMySqlOfflineTaskOutput",
    "MigrateMySqlAzureDbForMySqlOfflineTaskOutputDatabaseLevel",
    "MigrateMySqlAzureDbForMySqlOfflineTaskOutputError",
    "MigrateMySqlAzureDbForMySqlOfflineTaskOutputMigrationLevel",
    "MigrateMySqlAzureDbForMySqlOfflineTaskOutputTableLevel",
    "MigrateMySqlAzureDbForMySqlOfflineTaskProperties",
    "MigrateMySqlAzureDbForMySqlSyncDatabaseInput",
    "MigrateMySqlAzureDbForMySqlSyncTaskInput",
    "MigrateMySqlAzureDbForMySqlSyncTaskOutput",
    "MigrateMySqlAzureDbForMySqlSyncTaskOutputDatabaseError",
    "MigrateMySqlAzureDbForMySqlSyncTaskOutputDatabaseLevel",
    "MigrateMySqlAzureDbForMySqlSyncTaskOutputError",
    "MigrateMySqlAzureDbForMySqlSyncTaskOutputMigrationLevel",
    "MigrateMySqlAzureDbForMySqlSyncTaskOutputTableLevel",
    "MigrateMySqlAzureDbForMySqlSyncTaskProperties",
    "MigrateOracleAzureDbForPostgreSqlSyncTaskProperties",
    "MigrateOracleAzureDbPostgreSqlSyncDatabaseInput",
    "MigrateOracleAzureDbPostgreSqlSyncTaskInput",
    "MigrateOracleAzureDbPostgreSqlSyncTaskOutput",
    "MigrateOracleAzureDbPostgreSqlSyncTaskOutputDatabaseError",
    "MigrateOracleAzureDbPostgreSqlSyncTaskOutputDatabaseLevel",
    "MigrateOracleAzureDbPostgreSqlSyncTaskOutputError",
    "MigrateOracleAzureDbPostgreSqlSyncTaskOutputMigrationLevel",
    "MigrateOracleAzureDbPostgreSqlSyncTaskOutputTableLevel",
    "MigratePostgreSqlAzureDbForPostgreSqlSyncDatabaseInput",
    "MigratePostgreSqlAzureDbForPostgreSqlSyncDatabaseTableInput",
    "MigratePostgreSqlAzureDbForPostgreSqlSyncTaskInput",
    "MigratePostgreSqlAzureDbForPostgreSqlSyncTaskOutput",
    "MigratePostgreSqlAzureDbForPostgreSqlSyncTaskOutputDatabaseError",
    "MigratePostgreSqlAzureDbForPostgreSqlSyncTaskOutputDatabaseLevel",
    "MigratePostgreSqlAzureDbForPostgreSqlSyncTaskOutputError",
    "MigratePostgreSqlAzureDbForPostgreSqlSyncTaskOutputMigrationLevel",
    "MigratePostgreSqlAzureDbForPostgreSqlSyncTaskOutputTableLevel",
    "MigratePostgreSqlAzureDbForPostgreSqlSyncTaskProperties",
    "MigrateSchemaSqlServerSqlDbDatabaseInput",
    "MigrateSchemaSqlServerSqlDbTaskInput",
    "MigrateSchemaSqlServerSqlDbTaskOutput",
    "MigrateSchemaSqlServerSqlDbTaskOutputDatabaseLevel",
    "MigrateSchemaSqlServerSqlDbTaskOutputError",
    "MigrateSchemaSqlServerSqlDbTaskOutputMigrationLevel",
    "MigrateSchemaSqlServerSqlDbTaskProperties",
    "MigrateSchemaSqlTaskOutputError",
    "MigrateSqlServerDatabaseInput",
    "MigrateSqlServerSqlDbDatabaseInput",
    "MigrateSqlServerSqlDbSyncDatabaseInput",
    "MigrateSqlServerSqlDbSyncTaskInput",
    "MigrateSqlServerSqlDbSyncTaskOutput",
    "MigrateSqlServerSqlDbSyncTaskOutputDatabaseError",
    "MigrateSqlServerSqlDbSyncTaskOutputDatabaseLevel",
    "MigrateSqlServerSqlDbSyncTaskOutputError",
    "MigrateSqlServerSqlDbSyncTaskOutputMigrationLevel",
    "MigrateSqlServerSqlDbSyncTaskOutputTableLevel",
    "MigrateSqlServerSqlDbSyncTaskProperties",
    "MigrateSqlServerSqlDbTaskInput",
    "MigrateSqlServerSqlDbTaskOutput",
    "MigrateSqlServerSqlDbTaskOutputDatabaseLevel",
    "MigrateSqlServerSqlDbTaskOutputDatabaseLevelValidationResult",
    "MigrateSqlServerSqlDbTaskOutputError",
    "MigrateSqlServerSqlDbTaskOutputMigrationLevel",
    "MigrateSqlServerSqlDbTaskOutputTableLevel",
    "MigrateSqlServerSqlDbTaskOutputValidationResult",
    "MigrateSqlServerSqlDbTaskProperties",
    "MigrateSqlServerSqlMIDatabaseInput",
    "MigrateSqlServerSqlMISyncTaskInput",
    "MigrateSqlServerSqlMISyncTaskOutput",
    "MigrateSqlServerSqlMISyncTaskOutputDatabaseLevel",
    "MigrateSqlServerSqlMISyncTaskOutputError",
    "MigrateSqlServerSqlMISyncTaskOutputMigrationLevel",
    "MigrateSqlServerSqlMISyncTaskProperties",
    "MigrateSqlServerSqlMITaskInput",
    "MigrateSqlServerSqlMITaskOutput",
    "MigrateSqlServerSqlMITaskOutputAgentJobLevel",
    "MigrateSqlServerSqlMITaskOutputDatabaseLevel",
    "MigrateSqlServerSqlMITaskOutputError",
    "MigrateSqlServerSqlMITaskOutputLoginLevel",
    "MigrateSqlServerSqlMITaskOutputMigrationLevel",
    "MigrateSqlServerSqlMITaskProperties",
    "MigrateSsisTaskInput",
    "MigrateSsisTaskOutput",
    "MigrateSsisTaskOutputMigrationLevel",
    "MigrateSsisTaskOutputProjectLevel",
    "MigrateSsisTaskProperties",
    "MigrateSyncCompleteCommandInput",
    "MigrateSyncCompleteCommandOutput",
    "MigrateSyncCompleteCommandProperties",
    "MigrationEligibilityInfo",
    "MigrationOperationInput",
    "MigrationReportResult",
    "MigrationStatusDetails",
    "MigrationTableMetadata",
    "MigrationValidationDatabaseLevelResult",
    "MigrationValidationDatabaseSummaryResult",
    "MigrationValidationOptions",
    "MigrationValidationResult",
    "MongoDbCancelCommand",
    "MongoDbClusterInfo",
    "MongoDbCollectionInfo",
    "MongoDbCollectionProgress",
    "MongoDbCollectionSettings",
    "MongoDbCommandInput",
    "MongoDbConnectionInfo",
    "MongoDbDatabaseInfo",
    "MongoDbDatabaseProgress",
    "MongoDbDatabaseSettings",
    "MongoDbError",
    "MongoDbFinishCommand",
    "MongoDbFinishCommandInput",
    "MongoDbMigrationProgress",
    "MongoDbMigrationSettings",
    "MongoDbObjectInfo",
    "MongoDbProgress",
    "MongoDbRestartCommand",
    "MongoDbShardKeyField",
    "MongoDbShardKeyInfo",
    "MongoDbShardKeySetting",
    "MongoDbThrottlingSettings",
    "MySqlConnectionInfo",
    "NameAvailabilityRequest",
    "NameAvailabilityResponse",
    "NodeMonitoringData",
    "NonSqlDataMigrationTable",
    "NonSqlDataMigrationTableResult",
    "NonSqlMigrationTaskInput",
    "NonSqlMigrationTaskOutput",
    "ODataError",
    "OfflineConfiguration",
    "OperationListResult",
    "OperationsDefinition",
    "OperationsDisplayDefinition",
    "OracleConnectionInfo",
    "OracleOCIDriverInfo",
    "OrphanedUserInfo",
    "PostgreSqlConnectionInfo",
    "Project",
    "ProjectFile",
    "ProjectFileProperties",
    "ProjectList",
    "ProjectTask",
    "ProjectTaskProperties",
    "ProxyResource",
    "QueryAnalysisValidationResult",
    "QueryExecutionResult",
    "Quota",
    "QuotaList",
    "QuotaName",
    "RegenAuthKeys",
    "ReportableException",
    "Resource",
    "ResourceSku",
    "ResourceSkuCapabilities",
    "ResourceSkuCapacity",
    "ResourceSkuCosts",
    "ResourceSkuRestrictions",
    "ResourceSkusResult",
    "SchemaComparisonValidationResult",
    "SchemaComparisonValidationResultType",
    "SchemaMigrationSetting",
    "SelectedCertificateInput",
    "ServerProperties",
    "ServiceOperation",
    "ServiceOperationDisplay",
    "ServiceOperationList",
    "ServiceSku",
    "ServiceSkuList",
    "SourceLocation",
    "SqlBackupFileInfo",
    "SqlBackupSetInfo",
    "SqlConnectionInfo",
    "SqlConnectionInformation",
    "SqlDbMigrationStatusDetails",
    "SqlDbOfflineConfiguration",
    "SqlFileShare",
    "SqlMigrationListResult",
    "SqlMigrationService",
    "SqlMigrationServiceUpdate",
    "SqlMigrationTaskInput",
    "SqlServerSqlMISyncTaskInput",
    "SsisMigrationInfo",
    "StartMigrationScenarioServerRoleResult",
    "SyncMigrationDatabaseErrorEvent",
    "SystemData",
    "TargetLocation",
    "TaskList",
    "TrackedResource",
    "UploadOCIDriverTaskInput",
    "UploadOCIDriverTaskOutput",
    "UploadOCIDriverTaskProperties",
    "ValidateMigrationInputSqlServerSqlDbSyncTaskProperties",
    "ValidateMigrationInputSqlServerSqlMISyncTaskInput",
    "ValidateMigrationInputSqlServerSqlMISyncTaskOutput",
    "ValidateMigrationInputSqlServerSqlMISyncTaskProperties",
    "ValidateMigrationInputSqlServerSqlMITaskInput",
    "ValidateMigrationInputSqlServerSqlMITaskOutput",
    "ValidateMigrationInputSqlServerSqlMITaskProperties",
    "ValidateMongoDbTaskProperties",
    "ValidateOracleAzureDbForPostgreSqlSyncTaskProperties",
    "ValidateOracleAzureDbPostgreSqlSyncTaskOutput",
    "ValidateSyncMigrationInputSqlServerTaskInput",
    "ValidateSyncMigrationInputSqlServerTaskOutput",
    "ValidationError",
    "WaitStatistics",
    "AuthenticationType",
    "BackupFileStatus",
    "BackupMode",
    "BackupType",
    "CommandState",
    "CommandType",
    "CreatedByType",
    "DataMigrationResultCode",
    "DatabaseCompatLevel",
    "DatabaseFileType",
    "DatabaseMigrationStage",
    "DatabaseMigrationState",
    "DatabaseState",
    "ErrorType",
    "LoginMigrationStage",
    "LoginType",
    "MigrationState",
    "MigrationStatus",
    "MongoDbClusterType",
    "MongoDbErrorType",
    "MongoDbMigrationState",
    "MongoDbProgressResultType",
    "MongoDbReplication",
    "MongoDbShardKeyOrder",
    "MySqlTargetPlatformType",
    "NameCheckFailureReason",
    "ObjectType",
    "OperationOrigin",
    "ProjectProvisioningState",
    "ProjectSourcePlatform",
    "ProjectTargetPlatform",
    "ReplicateMigrationState",
    "ResourceSkuCapacityScaleType",
    "ResourceSkuRestrictionsReasonCode",
    "ResourceSkuRestrictionsType",
    "ResourceType",
    "ScenarioSource",
    "ScenarioTarget",
    "SchemaMigrationOption",
    "SchemaMigrationStage",
    "ServerLevelPermissionsGroup",
    "ServiceProvisioningState",
    "ServiceScalability",
    "Severity",
    "SqlSourcePlatform",
    "SsisMigrationOverwriteOption",
    "SsisMigrationStage",
    "SsisStoreType",
    "SyncDatabaseMigrationReportingState",
    "SyncTableMigrationState",
    "TaskState",
    "TaskType",
    "UpdateActionType",
    "ValidationStatus",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
