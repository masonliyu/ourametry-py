from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ResilienceContributors")


@_attrs_define
class ResilienceContributors:
    """
    Attributes:
        sleep_recovery (float): Sleep recovery contributor to the resilience score. Range: [0, 100]
        daytime_recovery (float): Daytime recovery contributor to the resilience score. Range: [0, 100]
        stress (float): Stress contributor to the resilience score. Range: [0, 100]
    """

    sleep_recovery: float
    daytime_recovery: float
    stress: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sleep_recovery = self.sleep_recovery

        daytime_recovery = self.daytime_recovery

        stress = self.stress

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sleep_recovery": sleep_recovery,
                "daytime_recovery": daytime_recovery,
                "stress": stress,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        sleep_recovery = d.pop("sleep_recovery")

        daytime_recovery = d.pop("daytime_recovery")

        stress = d.pop("stress")

        resilience_contributors = cls(
            sleep_recovery=sleep_recovery,
            daytime_recovery=daytime_recovery,
            stress=stress,
        )

        resilience_contributors.additional_properties = d
        return resilience_contributors

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
