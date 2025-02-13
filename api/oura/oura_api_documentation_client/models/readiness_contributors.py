from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ReadinessContributors")


@_attrs_define
class ReadinessContributors:
    """Object defining readiness score contributors.

    Attributes:
        activity_balance (Union[None, int]): Contribution of cumulative activity balance in range [1, 100].
        body_temperature (Union[None, int]): Contribution of body temperature in range [1, 100].
        hrv_balance (Union[None, int]): Contribution of heart rate variability balance in range [1, 100].
        previous_day_activity (Union[None, int]): Contribution of previous day's activity in range [1, 100].
        previous_night (Union[None, int]): Contribution of previous night's sleep in range [1, 100].
        recovery_index (Union[None, int]): Contribution of recovery index in range [1, 100].
        resting_heart_rate (Union[None, int]): Contribution of resting heart rate in range [1, 100].
        sleep_balance (Union[None, int]): Contribution of sleep balance in range [1, 100].
    """

    activity_balance: Union[None, int]
    body_temperature: Union[None, int]
    hrv_balance: Union[None, int]
    previous_day_activity: Union[None, int]
    previous_night: Union[None, int]
    recovery_index: Union[None, int]
    resting_heart_rate: Union[None, int]
    sleep_balance: Union[None, int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activity_balance: Union[None, int]
        activity_balance = self.activity_balance

        body_temperature: Union[None, int]
        body_temperature = self.body_temperature

        hrv_balance: Union[None, int]
        hrv_balance = self.hrv_balance

        previous_day_activity: Union[None, int]
        previous_day_activity = self.previous_day_activity

        previous_night: Union[None, int]
        previous_night = self.previous_night

        recovery_index: Union[None, int]
        recovery_index = self.recovery_index

        resting_heart_rate: Union[None, int]
        resting_heart_rate = self.resting_heart_rate

        sleep_balance: Union[None, int]
        sleep_balance = self.sleep_balance

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "activity_balance": activity_balance,
                "body_temperature": body_temperature,
                "hrv_balance": hrv_balance,
                "previous_day_activity": previous_day_activity,
                "previous_night": previous_night,
                "recovery_index": recovery_index,
                "resting_heart_rate": resting_heart_rate,
                "sleep_balance": sleep_balance,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_activity_balance(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        activity_balance = _parse_activity_balance(d.pop("activity_balance"))

        def _parse_body_temperature(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        body_temperature = _parse_body_temperature(d.pop("body_temperature"))

        def _parse_hrv_balance(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        hrv_balance = _parse_hrv_balance(d.pop("hrv_balance"))

        def _parse_previous_day_activity(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        previous_day_activity = _parse_previous_day_activity(d.pop("previous_day_activity"))

        def _parse_previous_night(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        previous_night = _parse_previous_night(d.pop("previous_night"))

        def _parse_recovery_index(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        recovery_index = _parse_recovery_index(d.pop("recovery_index"))

        def _parse_resting_heart_rate(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        resting_heart_rate = _parse_resting_heart_rate(d.pop("resting_heart_rate"))

        def _parse_sleep_balance(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        sleep_balance = _parse_sleep_balance(d.pop("sleep_balance"))

        readiness_contributors = cls(
            activity_balance=activity_balance,
            body_temperature=body_temperature,
            hrv_balance=hrv_balance,
            previous_day_activity=previous_day_activity,
            previous_night=previous_night,
            recovery_index=recovery_index,
            resting_heart_rate=resting_heart_rate,
            sleep_balance=sleep_balance,
        )

        readiness_contributors.additional_properties = d
        return readiness_contributors

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
