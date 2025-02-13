from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DailySpO2AggregatedValuesModel")


@_attrs_define
class DailySpO2AggregatedValuesModel:
    """
    Attributes:
        average (float): Average oxygen saturation (SpO2) throughout the night.
    """

    average: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        average = self.average

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "average": average,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        average = d.pop("average")

        daily_sp_o2_aggregated_values_model = cls(
            average=average,
        )

        daily_sp_o2_aggregated_values_model.additional_properties = d
        return daily_sp_o2_aggregated_values_model

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
