import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.sleep_time_recommendation import SleepTimeRecommendation
from ..models.sleep_time_status import SleepTimeStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sleep_time_window import SleepTimeWindow


T = TypeVar("T", bound="SleepTimeModel")


@_attrs_define
class SleepTimeModel:
    """Object contains suggested bedtime for the user.

    Attributes:
        id (str):
        day (datetime.date): Corresponding day for the sleep time.
        optimal_bedtime (Union['SleepTimeWindow', None, Unset]): Optimal bedtime.
        recommendation (Union[None, SleepTimeRecommendation, Unset]): Recommended action for bedtime.
        status (Union[None, SleepTimeStatus, Unset]): Sleep time status; used to inform sleep time recommendation.
    """

    id: str
    day: datetime.date
    optimal_bedtime: Union["SleepTimeWindow", None, Unset] = UNSET
    recommendation: Union[None, SleepTimeRecommendation, Unset] = UNSET
    status: Union[None, SleepTimeStatus, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.sleep_time_window import SleepTimeWindow

        id = self.id

        day = self.day.isoformat()

        optimal_bedtime: Union[None, Unset, dict[str, Any]]
        if isinstance(self.optimal_bedtime, Unset):
            optimal_bedtime = UNSET
        elif isinstance(self.optimal_bedtime, SleepTimeWindow):
            optimal_bedtime = self.optimal_bedtime.to_dict()
        else:
            optimal_bedtime = self.optimal_bedtime

        recommendation: Union[None, Unset, str]
        if isinstance(self.recommendation, Unset):
            recommendation = UNSET
        elif isinstance(self.recommendation, SleepTimeRecommendation):
            recommendation = self.recommendation.value
        else:
            recommendation = self.recommendation

        status: Union[None, Unset, str]
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, SleepTimeStatus):
            status = self.status.value
        else:
            status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "day": day,
            }
        )
        if optimal_bedtime is not UNSET:
            field_dict["optimal_bedtime"] = optimal_bedtime
        if recommendation is not UNSET:
            field_dict["recommendation"] = recommendation
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.sleep_time_window import SleepTimeWindow

        d = src_dict.copy()
        id = d.pop("id")

        day = isoparse(d.pop("day")).date()

        def _parse_optimal_bedtime(data: object) -> Union["SleepTimeWindow", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                optimal_bedtime_type_0 = SleepTimeWindow.from_dict(data)

                return optimal_bedtime_type_0
            except:  # noqa: E722
                pass
            return cast(Union["SleepTimeWindow", None, Unset], data)

        optimal_bedtime = _parse_optimal_bedtime(d.pop("optimal_bedtime", UNSET))

        def _parse_recommendation(data: object) -> Union[None, SleepTimeRecommendation, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                recommendation_type_0 = SleepTimeRecommendation(data)

                return recommendation_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, SleepTimeRecommendation, Unset], data)

        recommendation = _parse_recommendation(d.pop("recommendation", UNSET))

        def _parse_status(data: object) -> Union[None, SleepTimeStatus, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = SleepTimeStatus(data)

                return status_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, SleepTimeStatus, Unset], data)

        status = _parse_status(d.pop("status", UNSET))

        sleep_time_model = cls(
            id=id,
            day=day,
            optimal_bedtime=optimal_bedtime,
            recommendation=recommendation,
            status=status,
        )

        sleep_time_model.additional_properties = d
        return sleep_time_model

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
