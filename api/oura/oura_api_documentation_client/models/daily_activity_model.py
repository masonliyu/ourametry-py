import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.activity_contributors import ActivityContributors
    from ..models.sample_model import SampleModel


T = TypeVar("T", bound="DailyActivityModel")


@_attrs_define
class DailyActivityModel:
    """
    Attributes:
        id (str):
        class_5_min (Union[None, str]): 5-minute activity classification for the activity period:
            * ```0```	non wear
            * ```1``` rest
            * ```2``` inactive
            * ```3``` low activity
            * ```4``` medium activity
            * ```5``` high activity
        score (Union[None, int]): Activity score in range ```[1, 100]```
        active_calories (int): Active calories expended (in kilocalories)
        average_met_minutes (float): Average metabolic equivalent (MET) in minutes
        contributors (ActivityContributors): Object defining activity score contributors.
        equivalent_walking_distance (int): Equivalent walking distance (in meters) of energy expenditure
        high_activity_met_minutes (int): High activity metabolic equivalent (MET) in minutes
        high_activity_time (int): High activity metabolic equivalent (MET) in seconds
        inactivity_alerts (int): Number of inactivity alerts received
        low_activity_met_minutes (int): Low activity metabolic equivalent (MET) in minutes
        low_activity_time (int): Low activity metabolic equivalent (MET) in seconds
        medium_activity_met_minutes (int): Medium activity metabolic equivalent (MET) in minutes
        medium_activity_time (int): Medium activity metabolic equivalent (MET) in seconds
        met (SampleModel):
        meters_to_target (int): Remaining meters to target (from ```target_meters```
        non_wear_time (int): The time (in seconds) in which the ring was not worn
        resting_time (int): Resting time (in seconds)
        sedentary_met_minutes (int): Sedentary metabolic equivalent (MET) in minutes
        sedentary_time (int): Sedentary metabolic equivalent (MET) in seconds
        steps (int): Total number of steps taken
        target_calories (int): Daily activity target (in kilocalories)
        target_meters (int): Daily activity target (in meters)
        total_calories (int): Total calories expended (in kilocalories)
        day (datetime.date): The ```YYYY-MM-DD``` formatted local date indicating when the daily activity occurred
        timestamp (str):
    """

    id: str
    class_5_min: Union[None, str]
    score: Union[None, int]
    active_calories: int
    average_met_minutes: float
    contributors: "ActivityContributors"
    equivalent_walking_distance: int
    high_activity_met_minutes: int
    high_activity_time: int
    inactivity_alerts: int
    low_activity_met_minutes: int
    low_activity_time: int
    medium_activity_met_minutes: int
    medium_activity_time: int
    met: "SampleModel"
    meters_to_target: int
    non_wear_time: int
    resting_time: int
    sedentary_met_minutes: int
    sedentary_time: int
    steps: int
    target_calories: int
    target_meters: int
    total_calories: int
    day: datetime.date
    timestamp: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        class_5_min: Union[None, str]
        class_5_min = self.class_5_min

        score: Union[None, int]
        score = self.score

        active_calories = self.active_calories

        average_met_minutes = self.average_met_minutes

        contributors = self.contributors.to_dict()

        equivalent_walking_distance = self.equivalent_walking_distance

        high_activity_met_minutes = self.high_activity_met_minutes

        high_activity_time = self.high_activity_time

        inactivity_alerts = self.inactivity_alerts

        low_activity_met_minutes = self.low_activity_met_minutes

        low_activity_time = self.low_activity_time

        medium_activity_met_minutes = self.medium_activity_met_minutes

        medium_activity_time = self.medium_activity_time

        met = self.met.to_dict()

        meters_to_target = self.meters_to_target

        non_wear_time = self.non_wear_time

        resting_time = self.resting_time

        sedentary_met_minutes = self.sedentary_met_minutes

        sedentary_time = self.sedentary_time

        steps = self.steps

        target_calories = self.target_calories

        target_meters = self.target_meters

        total_calories = self.total_calories

        day = self.day.isoformat()

        timestamp = self.timestamp

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "class_5_min": class_5_min,
                "score": score,
                "active_calories": active_calories,
                "average_met_minutes": average_met_minutes,
                "contributors": contributors,
                "equivalent_walking_distance": equivalent_walking_distance,
                "high_activity_met_minutes": high_activity_met_minutes,
                "high_activity_time": high_activity_time,
                "inactivity_alerts": inactivity_alerts,
                "low_activity_met_minutes": low_activity_met_minutes,
                "low_activity_time": low_activity_time,
                "medium_activity_met_minutes": medium_activity_met_minutes,
                "medium_activity_time": medium_activity_time,
                "met": met,
                "meters_to_target": meters_to_target,
                "non_wear_time": non_wear_time,
                "resting_time": resting_time,
                "sedentary_met_minutes": sedentary_met_minutes,
                "sedentary_time": sedentary_time,
                "steps": steps,
                "target_calories": target_calories,
                "target_meters": target_meters,
                "total_calories": total_calories,
                "day": day,
                "timestamp": timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.activity_contributors import ActivityContributors
        from ..models.sample_model import SampleModel

        d = src_dict.copy()
        id = d.pop("id")

        def _parse_class_5_min(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        class_5_min = _parse_class_5_min(d.pop("class_5_min"))

        def _parse_score(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        score = _parse_score(d.pop("score"))

        active_calories = d.pop("active_calories")

        average_met_minutes = d.pop("average_met_minutes")

        contributors = ActivityContributors.from_dict(d.pop("contributors"))

        equivalent_walking_distance = d.pop("equivalent_walking_distance")

        high_activity_met_minutes = d.pop("high_activity_met_minutes")

        high_activity_time = d.pop("high_activity_time")

        inactivity_alerts = d.pop("inactivity_alerts")

        low_activity_met_minutes = d.pop("low_activity_met_minutes")

        low_activity_time = d.pop("low_activity_time")

        medium_activity_met_minutes = d.pop("medium_activity_met_minutes")

        medium_activity_time = d.pop("medium_activity_time")

        met = SampleModel.from_dict(d.pop("met"))

        meters_to_target = d.pop("meters_to_target")

        non_wear_time = d.pop("non_wear_time")

        resting_time = d.pop("resting_time")

        sedentary_met_minutes = d.pop("sedentary_met_minutes")

        sedentary_time = d.pop("sedentary_time")

        steps = d.pop("steps")

        target_calories = d.pop("target_calories")

        target_meters = d.pop("target_meters")

        total_calories = d.pop("total_calories")

        day = isoparse(d.pop("day")).date()

        timestamp = d.pop("timestamp")

        daily_activity_model = cls(
            id=id,
            class_5_min=class_5_min,
            score=score,
            active_calories=active_calories,
            average_met_minutes=average_met_minutes,
            contributors=contributors,
            equivalent_walking_distance=equivalent_walking_distance,
            high_activity_met_minutes=high_activity_met_minutes,
            high_activity_time=high_activity_time,
            inactivity_alerts=inactivity_alerts,
            low_activity_met_minutes=low_activity_met_minutes,
            low_activity_time=low_activity_time,
            medium_activity_met_minutes=medium_activity_met_minutes,
            medium_activity_time=medium_activity_time,
            met=met,
            meters_to_target=meters_to_target,
            non_wear_time=non_wear_time,
            resting_time=resting_time,
            sedentary_met_minutes=sedentary_met_minutes,
            sedentary_time=sedentary_time,
            steps=steps,
            target_calories=target_calories,
            target_meters=target_meters,
            total_calories=total_calories,
            day=day,
            timestamp=timestamp,
        )

        daily_activity_model.additional_properties = d
        return daily_activity_model

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
