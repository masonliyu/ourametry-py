from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="SampleModel")


@_attrs_define
class SampleModel:
    """
    Attributes:
        interval (float): Interval in seconds between the sampled items.
        items (list[Union[None, float]]): Recorded sample items.
        timestamp (str):
    """

    interval: float
    items: list[Union[None, float]]
    timestamp: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interval = self.interval

        items = []
        for items_item_data in self.items:
            items_item: Union[None, float]
            items_item = items_item_data
            items.append(items_item)

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "interval": interval,
                "items": items,
                "timestamp": timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        interval = d.pop("interval")

        items = []
        _items = d.pop("items")
        for items_item_data in _items:

            def _parse_items_item(data: object) -> Union[None, float]:
                if data is None:
                    return data
                return cast(Union[None, float], data)

            items_item = _parse_items_item(items_item_data)

            items.append(items_item)

        timestamp = d.pop("timestamp")

        sample_model = cls(
            interval=interval,
            items=items,
            timestamp=timestamp,
        )

        sample_model.additional_properties = d
        return sample_model

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
