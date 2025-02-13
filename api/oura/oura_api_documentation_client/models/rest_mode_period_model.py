import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.rest_mode_episode import RestModeEpisode


T = TypeVar("T", bound="RestModePeriodModel")


@_attrs_define
class RestModePeriodModel:
    """Object contains information about rest mode episode.

    Attributes:
        id (str):
        episodes (list['RestModeEpisode']): Collection of episodes during rest mode, consisting of tags.
        start_day (datetime.date): Start date of rest mode.
        start_time (Union[None, str]): Timestamp when rest mode started.
        end_day (Union[None, Unset, datetime.date]): End date of rest mode.
        end_time (Union[None, Unset, str]): Timestamp when rest mode ended.
    """

    id: str
    episodes: list["RestModeEpisode"]
    start_day: datetime.date
    start_time: Union[None, str]
    end_day: Union[None, Unset, datetime.date] = UNSET
    end_time: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        episodes = []
        for episodes_item_data in self.episodes:
            episodes_item = episodes_item_data.to_dict()
            episodes.append(episodes_item)

        start_day = self.start_day.isoformat()

        start_time: Union[None, str]
        start_time = self.start_time

        end_day: Union[None, Unset, str]
        if isinstance(self.end_day, Unset):
            end_day = UNSET
        elif isinstance(self.end_day, datetime.date):
            end_day = self.end_day.isoformat()
        else:
            end_day = self.end_day

        end_time: Union[None, Unset, str]
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        else:
            end_time = self.end_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "episodes": episodes,
                "start_day": start_day,
                "start_time": start_time,
            }
        )
        if end_day is not UNSET:
            field_dict["end_day"] = end_day
        if end_time is not UNSET:
            field_dict["end_time"] = end_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.rest_mode_episode import RestModeEpisode

        d = src_dict.copy()
        id = d.pop("id")

        episodes = []
        _episodes = d.pop("episodes")
        for episodes_item_data in _episodes:
            episodes_item = RestModeEpisode.from_dict(episodes_item_data)

            episodes.append(episodes_item)

        start_day = isoparse(d.pop("start_day")).date()

        def _parse_start_time(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        start_time = _parse_start_time(d.pop("start_time"))

        def _parse_end_day(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_day_type_0 = isoparse(data).date()

                return end_day_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        end_day = _parse_end_day(d.pop("end_day", UNSET))

        def _parse_end_time(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        end_time = _parse_end_time(d.pop("end_time", UNSET))

        rest_mode_period_model = cls(
            id=id,
            episodes=episodes,
            start_day=start_day,
            start_time=start_time,
            end_day=end_day,
            end_time=end_time,
        )

        rest_mode_period_model.additional_properties = d
        return rest_mode_period_model

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
