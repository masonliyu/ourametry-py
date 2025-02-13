import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.readiness_contributors import ReadinessContributors


T = TypeVar("T", bound="DailyReadinessModel")


@_attrs_define
class DailyReadinessModel:
    """
    Attributes:
        id (str):
        contributors (ReadinessContributors): Object defining readiness score contributors.
        day (datetime.date): Day that the daily readiness belongs to.
        score (Union[None, int]): Daily readiness score.
        temperature_deviation (Union[None, float]): Temperature deviation in degrees Celsius.
        temperature_trend_deviation (Union[None, float]): Temperature trend deviation in degrees Celsius.
        timestamp (str):
    """

    id: str
    contributors: "ReadinessContributors"
    day: datetime.date
    score: Union[None, int]
    temperature_deviation: Union[None, float]
    temperature_trend_deviation: Union[None, float]
    timestamp: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        contributors = self.contributors.to_dict()

        day = self.day.isoformat()

        score: Union[None, int]
        score = self.score

        temperature_deviation: Union[None, float]
        temperature_deviation = self.temperature_deviation

        temperature_trend_deviation: Union[None, float]
        temperature_trend_deviation = self.temperature_trend_deviation

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "contributors": contributors,
                "day": day,
                "score": score,
                "temperature_deviation": temperature_deviation,
                "temperature_trend_deviation": temperature_trend_deviation,
                "timestamp": timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.readiness_contributors import ReadinessContributors

        d = src_dict.copy()
        id = d.pop("id")

        contributors = ReadinessContributors.from_dict(d.pop("contributors"))

        day = isoparse(d.pop("day")).date()

        def _parse_score(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        score = _parse_score(d.pop("score"))

        def _parse_temperature_deviation(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        temperature_deviation = _parse_temperature_deviation(d.pop("temperature_deviation"))

        def _parse_temperature_trend_deviation(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        temperature_trend_deviation = _parse_temperature_trend_deviation(d.pop("temperature_trend_deviation"))

        timestamp = d.pop("timestamp")

        daily_readiness_model = cls(
            id=id,
            contributors=contributors,
            day=day,
            score=score,
            temperature_deviation=temperature_deviation,
            temperature_trend_deviation=temperature_trend_deviation,
            timestamp=timestamp,
        )

        daily_readiness_model.additional_properties = d
        return daily_readiness_model

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
