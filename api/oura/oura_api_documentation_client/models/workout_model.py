import datetime
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.workout_intensity import WorkoutIntensity
from ..models.workout_source import WorkoutSource

T = TypeVar("T", bound="WorkoutModel")


@_attrs_define
class WorkoutModel:
    """
    Attributes:
        id (str):
        activity (str): Type of the workout activity.
        calories (Union[None, float]): Energy burned in kilocalories during the workout.
        day (datetime.date): Day when the workout occurred.
        distance (Union[None, float]): Distance traveled in meters during the workout.
        end_datetime (str):
        intensity (WorkoutIntensity): Possible workout intensities.
        label (Union[None, str]): User-defined label for the workout.
        source (WorkoutSource):
        start_datetime (str):
    """

    id: str
    activity: str
    calories: Union[None, float]
    day: datetime.date
    distance: Union[None, float]
    end_datetime: str
    intensity: WorkoutIntensity
    label: Union[None, str]
    source: WorkoutSource
    start_datetime: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        activity = self.activity

        calories: Union[None, float]
        calories = self.calories

        day = self.day.isoformat()

        distance: Union[None, float]
        distance = self.distance

        end_datetime = self.end_datetime

        intensity = self.intensity.value

        label: Union[None, str]
        label = self.label

        source = self.source.value

        start_datetime = self.start_datetime

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "activity": activity,
                "calories": calories,
                "day": day,
                "distance": distance,
                "end_datetime": end_datetime,
                "intensity": intensity,
                "label": label,
                "source": source,
                "start_datetime": start_datetime,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        activity = d.pop("activity")

        def _parse_calories(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        calories = _parse_calories(d.pop("calories"))

        day = isoparse(d.pop("day")).date()

        def _parse_distance(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        distance = _parse_distance(d.pop("distance"))

        end_datetime = d.pop("end_datetime")

        intensity = WorkoutIntensity(d.pop("intensity"))

        def _parse_label(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        label = _parse_label(d.pop("label"))

        source = WorkoutSource(d.pop("source"))

        start_datetime = d.pop("start_datetime")

        workout_model = cls(
            id=id,
            activity=activity,
            calories=calories,
            day=day,
            distance=distance,
            end_datetime=end_datetime,
            intensity=intensity,
            label=label,
            source=source,
            start_datetime=start_datetime,
        )

        workout_model.additional_properties = d
        return workout_model

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
