import datetime
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.daily_stress_summary import DailyStressSummary
from ..types import UNSET, Unset

T = TypeVar("T", bound="DailyStressModel")


@_attrs_define
class DailyStressModel:
    """Object defining daily stress.

    Attributes:
        id (str):
        day (datetime.date): Day that the daily stress belongs to.
        stress_high (Union[None, int]): Time spent in a high stress zone (top quartile of data)
        recovery_high (Union[None, int]): Time spend in a high recovery zone (bottom quartile data)
        day_summary (Union[DailyStressSummary, None, Unset]): Stress summary of full day.
    """

    id: str
    day: datetime.date
    stress_high: Union[None, int]
    recovery_high: Union[None, int]
    day_summary: Union[DailyStressSummary, None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        day = self.day.isoformat()

        stress_high: Union[None, int]
        stress_high = self.stress_high

        recovery_high: Union[None, int]
        recovery_high = self.recovery_high

        day_summary: Union[None, Unset, str]
        if isinstance(self.day_summary, Unset):
            day_summary = UNSET
        elif isinstance(self.day_summary, DailyStressSummary):
            day_summary = self.day_summary.value
        else:
            day_summary = self.day_summary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "day": day,
                "stress_high": stress_high,
                "recovery_high": recovery_high,
            }
        )
        if day_summary is not UNSET:
            field_dict["day_summary"] = day_summary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        day = isoparse(d.pop("day")).date()

        def _parse_stress_high(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        stress_high = _parse_stress_high(d.pop("stress_high"))

        def _parse_recovery_high(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        recovery_high = _parse_recovery_high(d.pop("recovery_high"))

        def _parse_day_summary(data: object) -> Union[DailyStressSummary, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                day_summary_type_0 = DailyStressSummary(data)

                return day_summary_type_0
            except:  # noqa: E722
                pass
            return cast(Union[DailyStressSummary, None, Unset], data)

        day_summary = _parse_day_summary(d.pop("day_summary", UNSET))

        daily_stress_model = cls(
            id=id,
            day=day,
            stress_high=stress_high,
            recovery_high=recovery_high,
            day_summary=day_summary,
        )

        daily_stress_model.additional_properties = d
        return daily_stress_model

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
