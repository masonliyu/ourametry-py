from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ring_color import RingColor
from ..models.ring_design import RingDesign
from ..models.ring_hardware_type import RingHardwareType
from ..types import UNSET, Unset

T = TypeVar("T", bound="RingConfigurationModel")


@_attrs_define
class RingConfigurationModel:
    """
    Attributes:
        id (str):
        color (Union[None, RingColor, Unset]): Color of the ring.
        design (Union[None, RingDesign, Unset]): Design of the ring.
        firmware_version (Union[None, Unset, str]): Firmware version of the ring.
        hardware_type (Union[None, RingHardwareType, Unset]): Hardware type of the ring.
        set_up_at (Union[None, Unset, str]): UTC timestamp indicating when the ring was set up.
        size (Union[None, Unset, int]): US size of the ring.
    """

    id: str
    color: Union[None, RingColor, Unset] = UNSET
    design: Union[None, RingDesign, Unset] = UNSET
    firmware_version: Union[None, Unset, str] = UNSET
    hardware_type: Union[None, RingHardwareType, Unset] = UNSET
    set_up_at: Union[None, Unset, str] = UNSET
    size: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        color: Union[None, Unset, str]
        if isinstance(self.color, Unset):
            color = UNSET
        elif isinstance(self.color, RingColor):
            color = self.color.value
        else:
            color = self.color

        design: Union[None, Unset, str]
        if isinstance(self.design, Unset):
            design = UNSET
        elif isinstance(self.design, RingDesign):
            design = self.design.value
        else:
            design = self.design

        firmware_version: Union[None, Unset, str]
        if isinstance(self.firmware_version, Unset):
            firmware_version = UNSET
        else:
            firmware_version = self.firmware_version

        hardware_type: Union[None, Unset, str]
        if isinstance(self.hardware_type, Unset):
            hardware_type = UNSET
        elif isinstance(self.hardware_type, RingHardwareType):
            hardware_type = self.hardware_type.value
        else:
            hardware_type = self.hardware_type

        set_up_at: Union[None, Unset, str]
        if isinstance(self.set_up_at, Unset):
            set_up_at = UNSET
        else:
            set_up_at = self.set_up_at

        size: Union[None, Unset, int]
        if isinstance(self.size, Unset):
            size = UNSET
        else:
            size = self.size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if color is not UNSET:
            field_dict["color"] = color
        if design is not UNSET:
            field_dict["design"] = design
        if firmware_version is not UNSET:
            field_dict["firmware_version"] = firmware_version
        if hardware_type is not UNSET:
            field_dict["hardware_type"] = hardware_type
        if set_up_at is not UNSET:
            field_dict["set_up_at"] = set_up_at
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        def _parse_color(data: object) -> Union[None, RingColor, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                color_type_0 = RingColor(data)

                return color_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, RingColor, Unset], data)

        color = _parse_color(d.pop("color", UNSET))

        def _parse_design(data: object) -> Union[None, RingDesign, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                design_type_0 = RingDesign(data)

                return design_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, RingDesign, Unset], data)

        design = _parse_design(d.pop("design", UNSET))

        def _parse_firmware_version(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        firmware_version = _parse_firmware_version(d.pop("firmware_version", UNSET))

        def _parse_hardware_type(data: object) -> Union[None, RingHardwareType, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                hardware_type_type_0 = RingHardwareType(data)

                return hardware_type_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, RingHardwareType, Unset], data)

        hardware_type = _parse_hardware_type(d.pop("hardware_type", UNSET))

        def _parse_set_up_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        set_up_at = _parse_set_up_at(d.pop("set_up_at", UNSET))

        def _parse_size(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        size = _parse_size(d.pop("size", UNSET))

        ring_configuration_model = cls(
            id=id,
            color=color,
            design=design,
            firmware_version=firmware_version,
            hardware_type=hardware_type,
            set_up_at=set_up_at,
            size=size,
        )

        ring_configuration_model.additional_properties = d
        return ring_configuration_model

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
