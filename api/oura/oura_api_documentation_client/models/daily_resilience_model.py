import datetime
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.long_term_resilience_level import LongTermResilienceLevel

if TYPE_CHECKING:
    from ..models.resilience_contributors import ResilienceContributors


T = TypeVar("T", bound="DailyResilienceModel")


@_attrs_define
class DailyResilienceModel:
    """
    Attributes:
        id (str):
        day (datetime.date): Day when the resilience record was recorded.
        contributors (ResilienceContributors):
        level (LongTermResilienceLevel): Possible long term resilience level values.
    """

    id: str
    day: datetime.date
    contributors: "ResilienceContributors"
    level: LongTermResilienceLevel
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        day = self.day.isoformat()

        contributors = self.contributors.to_dict()

        level = self.level.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "day": day,
                "contributors": contributors,
                "level": level,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.resilience_contributors import ResilienceContributors

        d = src_dict.copy()
        id = d.pop("id")

        day = isoparse(d.pop("day")).date()

        contributors = ResilienceContributors.from_dict(d.pop("contributors"))

        level = LongTermResilienceLevel(d.pop("level"))

        daily_resilience_model = cls(
            id=id,
            day=day,
            contributors=contributors,
            level=level,
        )

        daily_resilience_model.additional_properties = d
        return daily_resilience_model

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
