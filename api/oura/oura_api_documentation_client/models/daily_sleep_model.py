import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.sleep_contributors import SleepContributors


T = TypeVar("T", bound="DailySleepModel")


@_attrs_define
class DailySleepModel:
    """Object defining daily sleep.

    Attributes:
        id (str):
        contributors (SleepContributors): Object defining sleep score contributors.
        day (datetime.date): Day that the daily sleep belongs to.
        score (Union[None, int]): Daily sleep score.
        timestamp (str):
    """

    id: str
    contributors: "SleepContributors"
    day: datetime.date
    score: Union[None, int]
    timestamp: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        contributors = self.contributors.to_dict()

        day = self.day.isoformat()

        score: Union[None, int]
        score = self.score

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "contributors": contributors,
                "day": day,
                "score": score,
                "timestamp": timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.sleep_contributors import SleepContributors

        d = src_dict.copy()
        id = d.pop("id")

        contributors = SleepContributors.from_dict(d.pop("contributors"))

        day = isoparse(d.pop("day")).date()

        def _parse_score(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        score = _parse_score(d.pop("score"))

        timestamp = d.pop("timestamp")

        daily_sleep_model = cls(
            id=id,
            contributors=contributors,
            day=day,
            score=score,
            timestamp=timestamp,
        )

        daily_sleep_model.additional_properties = d
        return daily_sleep_model

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
