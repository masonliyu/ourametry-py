from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.readiness_contributors import ReadinessContributors


T = TypeVar("T", bound="ReadinessSummary")


@_attrs_define
class ReadinessSummary:
    """
    Attributes:
        contributors (ReadinessContributors): Object defining readiness score contributors.
        score (Union[None, Unset, int]):
        temperature_deviation (Union[None, Unset, float]):
        temperature_trend_deviation (Union[None, Unset, float]):
    """

    contributors: "ReadinessContributors"
    score: Union[None, Unset, int] = UNSET
    temperature_deviation: Union[None, Unset, float] = UNSET
    temperature_trend_deviation: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        contributors = self.contributors.to_dict()

        score: Union[None, Unset, int]
        if isinstance(self.score, Unset):
            score = UNSET
        else:
            score = self.score

        temperature_deviation: Union[None, Unset, float]
        if isinstance(self.temperature_deviation, Unset):
            temperature_deviation = UNSET
        else:
            temperature_deviation = self.temperature_deviation

        temperature_trend_deviation: Union[None, Unset, float]
        if isinstance(self.temperature_trend_deviation, Unset):
            temperature_trend_deviation = UNSET
        else:
            temperature_trend_deviation = self.temperature_trend_deviation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contributors": contributors,
            }
        )
        if score is not UNSET:
            field_dict["score"] = score
        if temperature_deviation is not UNSET:
            field_dict["temperature_deviation"] = temperature_deviation
        if temperature_trend_deviation is not UNSET:
            field_dict["temperature_trend_deviation"] = temperature_trend_deviation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.readiness_contributors import ReadinessContributors

        d = src_dict.copy()
        contributors = ReadinessContributors.from_dict(d.pop("contributors"))

        def _parse_score(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        score = _parse_score(d.pop("score", UNSET))

        def _parse_temperature_deviation(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        temperature_deviation = _parse_temperature_deviation(d.pop("temperature_deviation", UNSET))

        def _parse_temperature_trend_deviation(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        temperature_trend_deviation = _parse_temperature_trend_deviation(d.pop("temperature_trend_deviation", UNSET))

        readiness_summary = cls(
            contributors=contributors,
            score=score,
            temperature_deviation=temperature_deviation,
            temperature_trend_deviation=temperature_trend_deviation,
        )

        readiness_summary.additional_properties = d
        return readiness_summary

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
