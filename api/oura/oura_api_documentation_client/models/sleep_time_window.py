from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SleepTimeWindow")


@_attrs_define
class SleepTimeWindow:
    """Object defining sleep time window

    Attributes:
        day_tz (int): Timezone offset in second from GMT of the day
        end_offset (int): End offset from midnight in second
        start_offset (int): Start offset from midnight in second
    """

    day_tz: int
    end_offset: int
    start_offset: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        day_tz = self.day_tz

        end_offset = self.end_offset

        start_offset = self.start_offset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "day_tz": day_tz,
                "end_offset": end_offset,
                "start_offset": start_offset,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        day_tz = d.pop("day_tz")

        end_offset = d.pop("end_offset")

        start_offset = d.pop("start_offset")

        sleep_time_window = cls(
            day_tz=day_tz,
            end_offset=end_offset,
            start_offset=start_offset,
        )

        sleep_time_window.additional_properties = d
        return sleep_time_window

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
