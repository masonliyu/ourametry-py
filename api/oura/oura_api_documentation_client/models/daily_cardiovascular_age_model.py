import datetime
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="DailyCardiovascularAgeModel")


@_attrs_define
class DailyCardiovascularAgeModel:
    """
    Attributes:
        day (datetime.date):
        vascular_age (Union[None, int]): 'Predicted vascular age in range [18, 100].
    """

    day: datetime.date
    vascular_age: Union[None, int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        day = self.day.isoformat()

        vascular_age: Union[None, int]
        vascular_age = self.vascular_age

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "day": day,
                "vascular_age": vascular_age,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        day = isoparse(d.pop("day")).date()

        def _parse_vascular_age(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        vascular_age = _parse_vascular_age(d.pop("vascular_age"))

        daily_cardiovascular_age_model = cls(
            day=day,
            vascular_age=vascular_age,
        )

        daily_cardiovascular_age_model.additional_properties = d
        return daily_cardiovascular_age_model

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
