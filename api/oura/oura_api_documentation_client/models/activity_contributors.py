from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityContributors")


@_attrs_define
class ActivityContributors:
    """Object defining activity score contributors.

    Attributes:
        meet_daily_targets (Union[None, Unset, int]): Contribution of meeting previous 7-day daily activity targets in
            range [1, 100].
        move_every_hour (Union[None, Unset, int]): Contribution of previous 24-hour inactivity alerts in range [1, 100].
        recovery_time (Union[None, Unset, int]): Contribution of previous 7-day recovery time in range [1, 100].
        stay_active (Union[None, Unset, int]): Contribution of previous 24-hour activity in range [1, 100].
        training_frequency (Union[None, Unset, int]): Contribution of previous 7-day exercise frequency in range [1,
            100].
        training_volume (Union[None, Unset, int]): Contribution of previous 7-day exercise volume in range [1, 100].
    """

    meet_daily_targets: Union[None, Unset, int] = UNSET
    move_every_hour: Union[None, Unset, int] = UNSET
    recovery_time: Union[None, Unset, int] = UNSET
    stay_active: Union[None, Unset, int] = UNSET
    training_frequency: Union[None, Unset, int] = UNSET
    training_volume: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        meet_daily_targets: Union[None, Unset, int]
        if isinstance(self.meet_daily_targets, Unset):
            meet_daily_targets = UNSET
        else:
            meet_daily_targets = self.meet_daily_targets

        move_every_hour: Union[None, Unset, int]
        if isinstance(self.move_every_hour, Unset):
            move_every_hour = UNSET
        else:
            move_every_hour = self.move_every_hour

        recovery_time: Union[None, Unset, int]
        if isinstance(self.recovery_time, Unset):
            recovery_time = UNSET
        else:
            recovery_time = self.recovery_time

        stay_active: Union[None, Unset, int]
        if isinstance(self.stay_active, Unset):
            stay_active = UNSET
        else:
            stay_active = self.stay_active

        training_frequency: Union[None, Unset, int]
        if isinstance(self.training_frequency, Unset):
            training_frequency = UNSET
        else:
            training_frequency = self.training_frequency

        training_volume: Union[None, Unset, int]
        if isinstance(self.training_volume, Unset):
            training_volume = UNSET
        else:
            training_volume = self.training_volume

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if meet_daily_targets is not UNSET:
            field_dict["meet_daily_targets"] = meet_daily_targets
        if move_every_hour is not UNSET:
            field_dict["move_every_hour"] = move_every_hour
        if recovery_time is not UNSET:
            field_dict["recovery_time"] = recovery_time
        if stay_active is not UNSET:
            field_dict["stay_active"] = stay_active
        if training_frequency is not UNSET:
            field_dict["training_frequency"] = training_frequency
        if training_volume is not UNSET:
            field_dict["training_volume"] = training_volume

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_meet_daily_targets(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        meet_daily_targets = _parse_meet_daily_targets(d.pop("meet_daily_targets", UNSET))

        def _parse_move_every_hour(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        move_every_hour = _parse_move_every_hour(d.pop("move_every_hour", UNSET))

        def _parse_recovery_time(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        recovery_time = _parse_recovery_time(d.pop("recovery_time", UNSET))

        def _parse_stay_active(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        stay_active = _parse_stay_active(d.pop("stay_active", UNSET))

        def _parse_training_frequency(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        training_frequency = _parse_training_frequency(d.pop("training_frequency", UNSET))

        def _parse_training_volume(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        training_volume = _parse_training_volume(d.pop("training_volume", UNSET))

        activity_contributors = cls(
            meet_daily_targets=meet_daily_targets,
            move_every_hour=move_every_hour,
            recovery_time=recovery_time,
            stay_active=stay_active,
            training_frequency=training_frequency,
            training_volume=training_volume,
        )

        activity_contributors.additional_properties = d
        return activity_contributors

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
