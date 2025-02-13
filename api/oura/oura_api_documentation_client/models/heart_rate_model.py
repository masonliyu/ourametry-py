from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.heart_rate_source import HeartRateSource

T = TypeVar("T", bound="HeartRateModel")


@_attrs_define
class HeartRateModel:
    """
    Attributes:
        bpm (int):
        source (HeartRateSource):
        timestamp (str):
    """

    bpm: int
    source: HeartRateSource
    timestamp: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bpm = self.bpm

        source = self.source.value

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bpm": bpm,
                "source": source,
                "timestamp": timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        bpm = d.pop("bpm")

        source = HeartRateSource(d.pop("source"))

        timestamp = d.pop("timestamp")

        heart_rate_model = cls(
            bpm=bpm,
            source=source,
            timestamp=timestamp,
        )

        heart_rate_model.additional_properties = d
        return heart_rate_model

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
