import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.moment_mood import MomentMood
from ..models.moment_type import MomentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sample_model import SampleModel


T = TypeVar("T", bound="SessionModel")


@_attrs_define
class SessionModel:
    """
    Attributes:
        id (str):
        day (datetime.date): The date when the session occurred.
        start_datetime (str):
        end_datetime (str):
        type_ (MomentType): Possible Moment types.
        heart_rate (Union['SampleModel', None, Unset]):
        heart_rate_variability (Union['SampleModel', None, Unset]):
        mood (Union[MomentMood, None, Unset]):
        motion_count (Union['SampleModel', None, Unset]):
    """

    id: str
    day: datetime.date
    start_datetime: str
    end_datetime: str
    type_: MomentType
    heart_rate: Union["SampleModel", None, Unset] = UNSET
    heart_rate_variability: Union["SampleModel", None, Unset] = UNSET
    mood: Union[MomentMood, None, Unset] = UNSET
    motion_count: Union["SampleModel", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.sample_model import SampleModel

        id = self.id

        day = self.day.isoformat()

        start_datetime = self.start_datetime

        end_datetime = self.end_datetime

        type_ = self.type_.value

        heart_rate: Union[None, Unset, dict[str, Any]]
        if isinstance(self.heart_rate, Unset):
            heart_rate = UNSET
        elif isinstance(self.heart_rate, SampleModel):
            heart_rate = self.heart_rate.to_dict()
        else:
            heart_rate = self.heart_rate

        heart_rate_variability: Union[None, Unset, dict[str, Any]]
        if isinstance(self.heart_rate_variability, Unset):
            heart_rate_variability = UNSET
        elif isinstance(self.heart_rate_variability, SampleModel):
            heart_rate_variability = self.heart_rate_variability.to_dict()
        else:
            heart_rate_variability = self.heart_rate_variability

        mood: Union[None, Unset, str]
        if isinstance(self.mood, Unset):
            mood = UNSET
        elif isinstance(self.mood, MomentMood):
            mood = self.mood.value
        else:
            mood = self.mood

        motion_count: Union[None, Unset, dict[str, Any]]
        if isinstance(self.motion_count, Unset):
            motion_count = UNSET
        elif isinstance(self.motion_count, SampleModel):
            motion_count = self.motion_count.to_dict()
        else:
            motion_count = self.motion_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "day": day,
                "start_datetime": start_datetime,
                "end_datetime": end_datetime,
                "type": type_,
            }
        )
        if heart_rate is not UNSET:
            field_dict["heart_rate"] = heart_rate
        if heart_rate_variability is not UNSET:
            field_dict["heart_rate_variability"] = heart_rate_variability
        if mood is not UNSET:
            field_dict["mood"] = mood
        if motion_count is not UNSET:
            field_dict["motion_count"] = motion_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.sample_model import SampleModel

        d = src_dict.copy()
        id = d.pop("id")

        day = isoparse(d.pop("day")).date()

        start_datetime = d.pop("start_datetime")

        end_datetime = d.pop("end_datetime")

        type_ = MomentType(d.pop("type"))

        def _parse_heart_rate(data: object) -> Union["SampleModel", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                heart_rate_type_0 = SampleModel.from_dict(data)

                return heart_rate_type_0
            except:  # noqa: E722
                pass
            return cast(Union["SampleModel", None, Unset], data)

        heart_rate = _parse_heart_rate(d.pop("heart_rate", UNSET))

        def _parse_heart_rate_variability(data: object) -> Union["SampleModel", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                heart_rate_variability_type_0 = SampleModel.from_dict(data)

                return heart_rate_variability_type_0
            except:  # noqa: E722
                pass
            return cast(Union["SampleModel", None, Unset], data)

        heart_rate_variability = _parse_heart_rate_variability(d.pop("heart_rate_variability", UNSET))

        def _parse_mood(data: object) -> Union[MomentMood, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                mood_type_0 = MomentMood(data)

                return mood_type_0
            except:  # noqa: E722
                pass
            return cast(Union[MomentMood, None, Unset], data)

        mood = _parse_mood(d.pop("mood", UNSET))

        def _parse_motion_count(data: object) -> Union["SampleModel", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                motion_count_type_0 = SampleModel.from_dict(data)

                return motion_count_type_0
            except:  # noqa: E722
                pass
            return cast(Union["SampleModel", None, Unset], data)

        motion_count = _parse_motion_count(d.pop("motion_count", UNSET))

        session_model = cls(
            id=id,
            day=day,
            start_datetime=start_datetime,
            end_datetime=end_datetime,
            type_=type_,
            heart_rate=heart_rate,
            heart_rate_variability=heart_rate_variability,
            mood=mood,
            motion_count=motion_count,
        )

        session_model.additional_properties = d
        return session_model

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
