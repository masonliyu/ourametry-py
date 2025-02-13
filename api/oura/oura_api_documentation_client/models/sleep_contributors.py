from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SleepContributors")


@_attrs_define
class SleepContributors:
    """Object defining sleep score contributors.

    Attributes:
        deep_sleep (Union[None, Unset, int]): Contribution of deep sleep in range [1, 100].
        efficiency (Union[None, Unset, int]): Contribution of sleep efficiency in range [1, 100].
        latency (Union[None, Unset, int]): Contribution of sleep latency in range [1, 100].
        rem_sleep (Union[None, Unset, int]): Contribution of REM sleep in range [1, 100].
        restfulness (Union[None, Unset, int]): Contribution of sleep restfulness in range [1, 100].
        timing (Union[None, Unset, int]): Contribution of sleep timing in range [1, 100].
        total_sleep (Union[None, Unset, int]): Contribution of total sleep in range [1, 100].
    """

    deep_sleep: Union[None, Unset, int] = UNSET
    efficiency: Union[None, Unset, int] = UNSET
    latency: Union[None, Unset, int] = UNSET
    rem_sleep: Union[None, Unset, int] = UNSET
    restfulness: Union[None, Unset, int] = UNSET
    timing: Union[None, Unset, int] = UNSET
    total_sleep: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deep_sleep: Union[None, Unset, int]
        if isinstance(self.deep_sleep, Unset):
            deep_sleep = UNSET
        else:
            deep_sleep = self.deep_sleep

        efficiency: Union[None, Unset, int]
        if isinstance(self.efficiency, Unset):
            efficiency = UNSET
        else:
            efficiency = self.efficiency

        latency: Union[None, Unset, int]
        if isinstance(self.latency, Unset):
            latency = UNSET
        else:
            latency = self.latency

        rem_sleep: Union[None, Unset, int]
        if isinstance(self.rem_sleep, Unset):
            rem_sleep = UNSET
        else:
            rem_sleep = self.rem_sleep

        restfulness: Union[None, Unset, int]
        if isinstance(self.restfulness, Unset):
            restfulness = UNSET
        else:
            restfulness = self.restfulness

        timing: Union[None, Unset, int]
        if isinstance(self.timing, Unset):
            timing = UNSET
        else:
            timing = self.timing

        total_sleep: Union[None, Unset, int]
        if isinstance(self.total_sleep, Unset):
            total_sleep = UNSET
        else:
            total_sleep = self.total_sleep

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deep_sleep is not UNSET:
            field_dict["deep_sleep"] = deep_sleep
        if efficiency is not UNSET:
            field_dict["efficiency"] = efficiency
        if latency is not UNSET:
            field_dict["latency"] = latency
        if rem_sleep is not UNSET:
            field_dict["rem_sleep"] = rem_sleep
        if restfulness is not UNSET:
            field_dict["restfulness"] = restfulness
        if timing is not UNSET:
            field_dict["timing"] = timing
        if total_sleep is not UNSET:
            field_dict["total_sleep"] = total_sleep

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_deep_sleep(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        deep_sleep = _parse_deep_sleep(d.pop("deep_sleep", UNSET))

        def _parse_efficiency(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        efficiency = _parse_efficiency(d.pop("efficiency", UNSET))

        def _parse_latency(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        latency = _parse_latency(d.pop("latency", UNSET))

        def _parse_rem_sleep(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        rem_sleep = _parse_rem_sleep(d.pop("rem_sleep", UNSET))

        def _parse_restfulness(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        restfulness = _parse_restfulness(d.pop("restfulness", UNSET))

        def _parse_timing(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        timing = _parse_timing(d.pop("timing", UNSET))

        def _parse_total_sleep(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        total_sleep = _parse_total_sleep(d.pop("total_sleep", UNSET))

        sleep_contributors = cls(
            deep_sleep=deep_sleep,
            efficiency=efficiency,
            latency=latency,
            rem_sleep=rem_sleep,
            restfulness=restfulness,
            timing=timing,
            total_sleep=total_sleep,
        )

        sleep_contributors.additional_properties = d
        return sleep_contributors

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
