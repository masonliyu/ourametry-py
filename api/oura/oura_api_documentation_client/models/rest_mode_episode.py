from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RestModeEpisode")


@_attrs_define
class RestModeEpisode:
    """Object defining a Rest Mode episode.

    Attributes:
        tags (list[str]): Tags selected for the episode.
        timestamp (str): ISO 8601 date-time that requires timezone and milliseconds
    """

    tags: list[str]
    timestamp: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tags = self.tags

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tags": tags,
                "timestamp": timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        tags = cast(list[str], d.pop("tags"))

        timestamp = d.pop("timestamp")

        rest_mode_episode = cls(
            tags=tags,
            timestamp=timestamp,
        )

        rest_mode_episode.additional_properties = d
        return rest_mode_episode

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
