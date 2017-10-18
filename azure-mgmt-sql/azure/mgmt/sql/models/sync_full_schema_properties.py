# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SyncFullSchemaProperties(Model):
    """Properties of the database full schema.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar tables: List of tables in the database full schema.
    :vartype tables: list[~azure.mgmt.sql.models.SyncFullSchemaTable]
    :ivar last_update_time: Last update time of the database schema.
    :vartype last_update_time: datetime
    """

    _validation = {
        'tables': {'readonly': True},
        'last_update_time': {'readonly': True},
    }

    _attribute_map = {
        'tables': {'key': 'tables', 'type': '[SyncFullSchemaTable]'},
        'last_update_time': {'key': 'lastUpdateTime', 'type': 'iso-8601'},
    }

    def __init__(self):
        self.tables = None
        self.last_update_time = None
