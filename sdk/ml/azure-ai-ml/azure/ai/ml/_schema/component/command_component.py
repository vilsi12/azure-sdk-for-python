# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

# pylint: disable=unused-argument,no-self-use,protected-access

from copy import deepcopy

import yaml
from marshmallow import INCLUDE, fields, post_load

from azure.ai.ml._schema.core.fields import ArmVersionedStr, NestedField, StringTransformedEnum, UnionField
from azure.ai.ml._schema.assets.asset import AnonymousAssetSchema
from azure.ai.ml._schema.assets.environment import AnonymousEnvironmentSchema
from azure.ai.ml._schema.component.component import ComponentSchema
from azure.ai.ml._schema.component.resource import ComponentResourceSchema
from azure.ai.ml._schema.core.fields import FileRefField, GitStr, LocalPathField, RegistryStr, SerializeValidatedUrl
from azure.ai.ml._schema.job.distribution import (
    MPIDistributionSchema,
    PyTorchDistributionSchema,
    TensorFlowDistributionSchema,
)
from azure.ai.ml.constants import BASE_PATH_CONTEXT_KEY, AzureMLResourceType, ComponentSource, NodeType


class CommandComponentSchema(ComponentSchema):
    type = StringTransformedEnum(allowed_values=[NodeType.COMMAND])
    command = fields.Str(metadata={"description": "String to be executed. Can set variables using ${{ }}"})
    code = UnionField(
        [
            SerializeValidatedUrl(),
            LocalPathField(),
            RegistryStr(azureml_type=AzureMLResourceType.CODE),
            # Accept str to support git paths
            GitStr(),
            # put arm versioned string at last order as it can deserialize any string into "azureml:<origin>"
            ArmVersionedStr(azureml_type=AzureMLResourceType.CODE),
        ],
        metadata={"description": "A local path or http:, https:, azureml: url pointing to a remote location."},
    )
    environment = UnionField(
        [
            NestedField(AnonymousEnvironmentSchema),
            RegistryStr(azureml_type=AzureMLResourceType.ENVIRONMENT),
            ArmVersionedStr(azureml_type=AzureMLResourceType.ENVIRONMENT, allow_default_version=True),
        ],
        required=True,
    )
    resources = NestedField(ComponentResourceSchema, unknown=INCLUDE)
    distribution = UnionField(
        [
            NestedField(MPIDistributionSchema, unknown=INCLUDE),
            NestedField(TensorFlowDistributionSchema, unknown=INCLUDE),
            NestedField(PyTorchDistributionSchema, unknown=INCLUDE),
        ],
        metadata={"description": "Provides the configuration for a distributed run."},
    )


class RestCommandComponentSchema(CommandComponentSchema):
    """When component load from rest, won't validate on name since there might
    be existing component with invalid name."""

    name = fields.Str(required=True)


class AnonymousCommandComponentSchema(AnonymousAssetSchema, CommandComponentSchema):
    """Anonymous command component schema.

    Note inheritance follows order: AnonymousAssetSchema,
    CommandComponentSchema because we need name and version to be
    dump_only(marshmallow collects fields follows method resolution
    order).
    """

    @post_load
    def make(self, data, **kwargs):
        from azure.ai.ml.entities import CommandComponent

        # Inline component will have source=YAML.JOB
        # As we only regard full separate component file as YAML.COMPONENT
        return CommandComponent(
            base_path=self.context[BASE_PATH_CONTEXT_KEY],
            _source=ComponentSource.YAML_JOB,
            **data,
        )


class ComponentFileRefField(FileRefField):
    def _deserialize(self, value, attr, data, **kwargs):
        # Get component info from component yaml file.
        data = super()._deserialize(value, attr, data, **kwargs)
        component_dict = yaml.safe_load(data)
        source_path = self.context[BASE_PATH_CONTEXT_KEY] / value

        # Update base_path to parent path of component file.
        component_schema_context = deepcopy(self.context)
        component_schema_context[BASE_PATH_CONTEXT_KEY] = source_path.parent
        component = AnonymousCommandComponentSchema(context=component_schema_context).load(
            component_dict, unknown=INCLUDE
        )
        component._source_path = source_path
        component._source = ComponentSource.YAML_COMPONENT
        return component
