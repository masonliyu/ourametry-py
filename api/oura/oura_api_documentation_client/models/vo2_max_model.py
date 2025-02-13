import datetime
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="VO2MaxModel")


@_attrs_define
class VO2MaxModel:
    """
    Attributes:
        id (str):
        day (datetime.date): Day that the estimate belongs to.
        timestamp (str):
        vo2_max (Union[None, float]): VO2 max value.
    """

    id: str
    day: datetime.date
    timestamp: str
    vo2_max: Union[None, float]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        day = self.day.isoformat()

        timestamp = self.timestamp

        vo2_max: Union[None, float]
        vo2_max = self.vo2_max

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "day": day,
                "timestamp": timestamp,
                "vo2_max": vo2_max,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        day = isoparse(d.pop("day")).date()

        timestamp = d.pop("timestamp")

        def _parse_vo2_max(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        vo2_max = _parse_vo2_max(d.pop("vo2_max"))

        vo2_max_model = cls(
            id=id,
            day=day,
            timestamp=timestamp,
            vo2_max=vo2_max,
        )

        vo2_max_model.additional_properties = d
        return vo2_max_model

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
