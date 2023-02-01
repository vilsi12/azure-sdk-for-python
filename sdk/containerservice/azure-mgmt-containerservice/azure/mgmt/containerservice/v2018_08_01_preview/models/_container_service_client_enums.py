# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AgentPoolType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """AgentPoolType represents types of an agent pool."""

    VIRTUAL_MACHINE_SCALE_SETS = "VirtualMachineScaleSets"
    AVAILABILITY_SET = "AvailabilitySet"


class ContainerServiceStorageProfileTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Storage profile specifies what kind of storage used. Choose from StorageAccount and
    ManagedDisks. Leave it empty, we will choose for you based on the orchestrator choice.
    """

    STORAGE_ACCOUNT = "StorageAccount"
    MANAGED_DISKS = "ManagedDisks"


class ContainerServiceVMSizeTypes(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Size of agent VMs."""

    STANDARD_A1 = "Standard_A1"
    STANDARD_A10 = "Standard_A10"
    STANDARD_A11 = "Standard_A11"
    STANDARD_A1_V2 = "Standard_A1_v2"
    STANDARD_A2 = "Standard_A2"
    STANDARD_A2_V2 = "Standard_A2_v2"
    STANDARD_A2_M_V2 = "Standard_A2m_v2"
    STANDARD_A3 = "Standard_A3"
    STANDARD_A4 = "Standard_A4"
    STANDARD_A4_V2 = "Standard_A4_v2"
    STANDARD_A4_M_V2 = "Standard_A4m_v2"
    STANDARD_A5 = "Standard_A5"
    STANDARD_A6 = "Standard_A6"
    STANDARD_A7 = "Standard_A7"
    STANDARD_A8 = "Standard_A8"
    STANDARD_A8_V2 = "Standard_A8_v2"
    STANDARD_A8_M_V2 = "Standard_A8m_v2"
    STANDARD_A9 = "Standard_A9"
    STANDARD_B2_MS = "Standard_B2ms"
    STANDARD_B2_S = "Standard_B2s"
    STANDARD_B4_MS = "Standard_B4ms"
    STANDARD_B8_MS = "Standard_B8ms"
    STANDARD_D1 = "Standard_D1"
    STANDARD_D11 = "Standard_D11"
    STANDARD_D11_V2 = "Standard_D11_v2"
    STANDARD_D11_V2_PROMO = "Standard_D11_v2_Promo"
    STANDARD_D12 = "Standard_D12"
    STANDARD_D12_V2 = "Standard_D12_v2"
    STANDARD_D12_V2_PROMO = "Standard_D12_v2_Promo"
    STANDARD_D13 = "Standard_D13"
    STANDARD_D13_V2 = "Standard_D13_v2"
    STANDARD_D13_V2_PROMO = "Standard_D13_v2_Promo"
    STANDARD_D14 = "Standard_D14"
    STANDARD_D14_V2 = "Standard_D14_v2"
    STANDARD_D14_V2_PROMO = "Standard_D14_v2_Promo"
    STANDARD_D15_V2 = "Standard_D15_v2"
    STANDARD_D16_V3 = "Standard_D16_v3"
    STANDARD_D16_S_V3 = "Standard_D16s_v3"
    STANDARD_D1_V2 = "Standard_D1_v2"
    STANDARD_D2 = "Standard_D2"
    STANDARD_D2_V2 = "Standard_D2_v2"
    STANDARD_D2_V2_PROMO = "Standard_D2_v2_Promo"
    STANDARD_D2_V3 = "Standard_D2_v3"
    STANDARD_D2_S_V3 = "Standard_D2s_v3"
    STANDARD_D3 = "Standard_D3"
    STANDARD_D32_V3 = "Standard_D32_v3"
    STANDARD_D32_S_V3 = "Standard_D32s_v3"
    STANDARD_D3_V2 = "Standard_D3_v2"
    STANDARD_D3_V2_PROMO = "Standard_D3_v2_Promo"
    STANDARD_D4 = "Standard_D4"
    STANDARD_D4_V2 = "Standard_D4_v2"
    STANDARD_D4_V2_PROMO = "Standard_D4_v2_Promo"
    STANDARD_D4_V3 = "Standard_D4_v3"
    STANDARD_D4_S_V3 = "Standard_D4s_v3"
    STANDARD_D5_V2 = "Standard_D5_v2"
    STANDARD_D5_V2_PROMO = "Standard_D5_v2_Promo"
    STANDARD_D64_V3 = "Standard_D64_v3"
    STANDARD_D64_S_V3 = "Standard_D64s_v3"
    STANDARD_D8_V3 = "Standard_D8_v3"
    STANDARD_D8_S_V3 = "Standard_D8s_v3"
    STANDARD_DS1 = "Standard_DS1"
    STANDARD_DS11 = "Standard_DS11"
    STANDARD_DS11_V2 = "Standard_DS11_v2"
    STANDARD_DS11_V2_PROMO = "Standard_DS11_v2_Promo"
    STANDARD_DS12 = "Standard_DS12"
    STANDARD_DS12_V2 = "Standard_DS12_v2"
    STANDARD_DS12_V2_PROMO = "Standard_DS12_v2_Promo"
    STANDARD_DS13 = "Standard_DS13"
    STANDARD_DS13_2_V2 = "Standard_DS13-2_v2"
    STANDARD_DS13_4_V2 = "Standard_DS13-4_v2"
    STANDARD_DS13_V2 = "Standard_DS13_v2"
    STANDARD_DS13_V2_PROMO = "Standard_DS13_v2_Promo"
    STANDARD_DS14 = "Standard_DS14"
    STANDARD_DS14_4_V2 = "Standard_DS14-4_v2"
    STANDARD_DS14_8_V2 = "Standard_DS14-8_v2"
    STANDARD_DS14_V2 = "Standard_DS14_v2"
    STANDARD_DS14_V2_PROMO = "Standard_DS14_v2_Promo"
    STANDARD_DS15_V2 = "Standard_DS15_v2"
    STANDARD_DS1_V2 = "Standard_DS1_v2"
    STANDARD_DS2 = "Standard_DS2"
    STANDARD_DS2_V2 = "Standard_DS2_v2"
    STANDARD_DS2_V2_PROMO = "Standard_DS2_v2_Promo"
    STANDARD_DS3 = "Standard_DS3"
    STANDARD_DS3_V2 = "Standard_DS3_v2"
    STANDARD_DS3_V2_PROMO = "Standard_DS3_v2_Promo"
    STANDARD_DS4 = "Standard_DS4"
    STANDARD_DS4_V2 = "Standard_DS4_v2"
    STANDARD_DS4_V2_PROMO = "Standard_DS4_v2_Promo"
    STANDARD_DS5_V2 = "Standard_DS5_v2"
    STANDARD_DS5_V2_PROMO = "Standard_DS5_v2_Promo"
    STANDARD_E16_V3 = "Standard_E16_v3"
    STANDARD_E16_S_V3 = "Standard_E16s_v3"
    STANDARD_E2_V3 = "Standard_E2_v3"
    STANDARD_E2_S_V3 = "Standard_E2s_v3"
    STANDARD_E32_16_S_V3 = "Standard_E32-16s_v3"
    STANDARD_E32_8_S_V3 = "Standard_E32-8s_v3"
    STANDARD_E32_V3 = "Standard_E32_v3"
    STANDARD_E32_S_V3 = "Standard_E32s_v3"
    STANDARD_E4_V3 = "Standard_E4_v3"
    STANDARD_E4_S_V3 = "Standard_E4s_v3"
    STANDARD_E64_16_S_V3 = "Standard_E64-16s_v3"
    STANDARD_E64_32_S_V3 = "Standard_E64-32s_v3"
    STANDARD_E64_V3 = "Standard_E64_v3"
    STANDARD_E64_S_V3 = "Standard_E64s_v3"
    STANDARD_E8_V3 = "Standard_E8_v3"
    STANDARD_E8_S_V3 = "Standard_E8s_v3"
    STANDARD_F1 = "Standard_F1"
    STANDARD_F16 = "Standard_F16"
    STANDARD_F16_S = "Standard_F16s"
    STANDARD_F16_S_V2 = "Standard_F16s_v2"
    STANDARD_F1_S = "Standard_F1s"
    STANDARD_F2 = "Standard_F2"
    STANDARD_F2_S = "Standard_F2s"
    STANDARD_F2_S_V2 = "Standard_F2s_v2"
    STANDARD_F32_S_V2 = "Standard_F32s_v2"
    STANDARD_F4 = "Standard_F4"
    STANDARD_F4_S = "Standard_F4s"
    STANDARD_F4_S_V2 = "Standard_F4s_v2"
    STANDARD_F64_S_V2 = "Standard_F64s_v2"
    STANDARD_F72_S_V2 = "Standard_F72s_v2"
    STANDARD_F8 = "Standard_F8"
    STANDARD_F8_S = "Standard_F8s"
    STANDARD_F8_S_V2 = "Standard_F8s_v2"
    STANDARD_G1 = "Standard_G1"
    STANDARD_G2 = "Standard_G2"
    STANDARD_G3 = "Standard_G3"
    STANDARD_G4 = "Standard_G4"
    STANDARD_G5 = "Standard_G5"
    STANDARD_GS1 = "Standard_GS1"
    STANDARD_GS2 = "Standard_GS2"
    STANDARD_GS3 = "Standard_GS3"
    STANDARD_GS4 = "Standard_GS4"
    STANDARD_GS4_4 = "Standard_GS4-4"
    STANDARD_GS4_8 = "Standard_GS4-8"
    STANDARD_GS5 = "Standard_GS5"
    STANDARD_GS5_16 = "Standard_GS5-16"
    STANDARD_GS5_8 = "Standard_GS5-8"
    STANDARD_H16 = "Standard_H16"
    STANDARD_H16_M = "Standard_H16m"
    STANDARD_H16_MR = "Standard_H16mr"
    STANDARD_H16_R = "Standard_H16r"
    STANDARD_H8 = "Standard_H8"
    STANDARD_H8_M = "Standard_H8m"
    STANDARD_L16_S = "Standard_L16s"
    STANDARD_L32_S = "Standard_L32s"
    STANDARD_L4_S = "Standard_L4s"
    STANDARD_L8_S = "Standard_L8s"
    STANDARD_M128_32_MS = "Standard_M128-32ms"
    STANDARD_M128_64_MS = "Standard_M128-64ms"
    STANDARD_M128_MS = "Standard_M128ms"
    STANDARD_M128_S = "Standard_M128s"
    STANDARD_M64_16_MS = "Standard_M64-16ms"
    STANDARD_M64_32_MS = "Standard_M64-32ms"
    STANDARD_M64_MS = "Standard_M64ms"
    STANDARD_M64_S = "Standard_M64s"
    STANDARD_NC12 = "Standard_NC12"
    STANDARD_NC12_S_V2 = "Standard_NC12s_v2"
    STANDARD_NC12_S_V3 = "Standard_NC12s_v3"
    STANDARD_NC24 = "Standard_NC24"
    STANDARD_NC24_R = "Standard_NC24r"
    STANDARD_NC24_RS_V2 = "Standard_NC24rs_v2"
    STANDARD_NC24_RS_V3 = "Standard_NC24rs_v3"
    STANDARD_NC24_S_V2 = "Standard_NC24s_v2"
    STANDARD_NC24_S_V3 = "Standard_NC24s_v3"
    STANDARD_NC6 = "Standard_NC6"
    STANDARD_NC6_S_V2 = "Standard_NC6s_v2"
    STANDARD_NC6_S_V3 = "Standard_NC6s_v3"
    STANDARD_ND12_S = "Standard_ND12s"
    STANDARD_ND24_RS = "Standard_ND24rs"
    STANDARD_ND24_S = "Standard_ND24s"
    STANDARD_ND6_S = "Standard_ND6s"
    STANDARD_NV12 = "Standard_NV12"
    STANDARD_NV24 = "Standard_NV24"
    STANDARD_NV6 = "Standard_NV6"


class Count(int, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Number of masters (VMs) in the container service cluster. Allowed values are 1, 3, and 5. The
    default value is 1.
    """

    ONE = 1
    THREE = 3
    FIVE = 5


class NetworkPlugin(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Network plugin used for building Kubernetes network."""

    AZURE = "azure"
    KUBENET = "kubenet"


class NetworkPolicy(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Network policy used for building Kubernetes network."""

    CALICO = "calico"


class OSType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """OsType to be used to specify os type. Choose from Linux and Windows. Default to Linux."""

    LINUX = "Linux"
    WINDOWS = "Windows"
