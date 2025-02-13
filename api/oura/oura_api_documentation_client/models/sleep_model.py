import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.sleep_algorithm_version import SleepAlgorithmVersion
from ..models.sleep_type import SleepType

if TYPE_CHECKING:
    from ..models.readiness_summary import ReadinessSummary
    from ..models.sample_model import SampleModel


T = TypeVar("T", bound="SleepModel")


@_attrs_define
class SleepModel:
    """
    Attributes:
        id (str):
        average_breath (Union[None, float]): Average breathing rate during sleep as breaths/second.
        average_heart_rate (Union[None, float]): Average heart rate during sleep as beats/minute.
        average_hrv (Union[None, int]): Average heart rate variability during sleep.
        awake_time (Union[None, int]): Duration spent awake in seconds.
        bedtime_end (str):
        bedtime_start (str):
        day (datetime.date): Day that the sleep belongs to.
        deep_sleep_duration (Union[None, int]): Duration spent in deep sleep in seconds.
        efficiency (Union[None, int]): Sleep efficiency rating in range [1, 100].
        heart_rate (Union['SampleModel', None]): Object containing heart rate samples.
        hrv (Union['SampleModel', None]):
        latency (Union[None, int]): Sleep latency in seconds. This is the time it took for the user to fall asleep after
            going to bed.
        light_sleep_duration (Union[None, int]): Duration spent in light sleep in seconds.
        low_battery_alert (bool): Flag indicating if a low battery alert occurred.
        lowest_heart_rate (Union[None, int]): Lowest heart rate during sleep.
        movement_30_sec (Union[None, str]):
                    30-second movement classification for the period where every character corresponds to:
                    '1' = no motion,
                    '2' = restless,
                    '3' = tossing and turning
                    '4' = active

        period (int): ECore sleep period identifier.
        readiness (Union['ReadinessSummary', None]): Object containing the readiness details for this sleep. As opposed
            to the daily readiness object which represents the readiness for the entire day.
        readiness_score_delta (Union[None, int]): Effect on readiness score caused by this sleep period.
        rem_sleep_duration (Union[None, int]): Duration spent in REM sleep in seconds.
        restless_periods (Union[None, int]): Number of restless periods during sleep.
        sleep_phase_5_min (Union[None, str]):
                    5-minute sleep phase classification for the period where every character corresponds to:
                    '1' = deep sleep,
                    '2' = light sleep,
                    '3' = REM sleep
                    '4' = awake.

        sleep_score_delta (Union[None, int]): Effect on sleep score caused by this sleep period.
        sleep_algorithm_version (Union[None, SleepAlgorithmVersion]): Version of the sleep algorithm used to calculate
            the sleep data.
        time_in_bed (int): Duration spent in bed in seconds.
        total_sleep_duration (Union[None, int]): Total sleep duration in seconds.
        type_ (SleepType): Possible sleep period types.
            'deleted' = deleted sleep by user.
            'sleep' = user confirmed sleep / nap, min 15 minutes, max 3 hours, contributes to daily scores
            'late_nap' = user confirmed sleep / nap, min 15 minutes, ended after sleep day change (6 pm), contributes to
            next days daily scores
            'long_sleep' = sleep that is long enough (>3h) to automatically contribute to daily scores
            'rest' = Falsely detected sleep / nap, rejected in confirm prompt by user
    """

    id: str
    average_breath: Union[None, float]
    average_heart_rate: Union[None, float]
    average_hrv: Union[None, int]
    awake_time: Union[None, int]
    bedtime_end: str
    bedtime_start: str
    day: datetime.date
    deep_sleep_duration: Union[None, int]
    efficiency: Union[None, int]
    heart_rate: Union["SampleModel", None]
    hrv: Union["SampleModel", None]
    latency: Union[None, int]
    light_sleep_duration: Union[None, int]
    low_battery_alert: bool
    lowest_heart_rate: Union[None, int]
    movement_30_sec: Union[None, str]
    period: int
    readiness: Union["ReadinessSummary", None]
    readiness_score_delta: Union[None, int]
    rem_sleep_duration: Union[None, int]
    restless_periods: Union[None, int]
    sleep_phase_5_min: Union[None, str]
    sleep_score_delta: Union[None, int]
    sleep_algorithm_version: Union[None, SleepAlgorithmVersion]
    time_in_bed: int
    total_sleep_duration: Union[None, int]
    type_: SleepType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.readiness_summary import ReadinessSummary
        from ..models.sample_model import SampleModel

        id = self.id

        average_breath: Union[None, float]
        average_breath = self.average_breath

        average_heart_rate: Union[None, float]
        average_heart_rate = self.average_heart_rate

        average_hrv: Union[None, int]
        average_hrv = self.average_hrv

        awake_time: Union[None, int]
        awake_time = self.awake_time

        bedtime_end = self.bedtime_end

        bedtime_start = self.bedtime_start

        day = self.day.isoformat()

        deep_sleep_duration: Union[None, int]
        deep_sleep_duration = self.deep_sleep_duration

        efficiency: Union[None, int]
        efficiency = self.efficiency

        heart_rate: Union[None, dict[str, Any]]
        if isinstance(self.heart_rate, SampleModel):
            heart_rate = self.heart_rate.to_dict()
        else:
            heart_rate = self.heart_rate

        hrv: Union[None, dict[str, Any]]
        if isinstance(self.hrv, SampleModel):
            hrv = self.hrv.to_dict()
        else:
            hrv = self.hrv

        latency: Union[None, int]
        latency = self.latency

        light_sleep_duration: Union[None, int]
        light_sleep_duration = self.light_sleep_duration

        low_battery_alert = self.low_battery_alert

        lowest_heart_rate: Union[None, int]
        lowest_heart_rate = self.lowest_heart_rate

        movement_30_sec: Union[None, str]
        movement_30_sec = self.movement_30_sec

        period = self.period

        readiness: Union[None, dict[str, Any]]
        if isinstance(self.readiness, ReadinessSummary):
            readiness = self.readiness.to_dict()
        else:
            readiness = self.readiness

        readiness_score_delta: Union[None, int]
        readiness_score_delta = self.readiness_score_delta

        rem_sleep_duration: Union[None, int]
        rem_sleep_duration = self.rem_sleep_duration

        restless_periods: Union[None, int]
        restless_periods = self.restless_periods

        sleep_phase_5_min: Union[None, str]
        sleep_phase_5_min = self.sleep_phase_5_min

        sleep_score_delta: Union[None, int]
        sleep_score_delta = self.sleep_score_delta

        sleep_algorithm_version: Union[None, str]
        if isinstance(self.sleep_algorithm_version, SleepAlgorithmVersion):
            sleep_algorithm_version = self.sleep_algorithm_version.value
        else:
            sleep_algorithm_version = self.sleep_algorithm_version

        time_in_bed = self.time_in_bed

        total_sleep_duration: Union[None, int]
        total_sleep_duration = self.total_sleep_duration

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "average_breath": average_breath,
                "average_heart_rate": average_heart_rate,
                "average_hrv": average_hrv,
                "awake_time": awake_time,
                "bedtime_end": bedtime_end,
                "bedtime_start": bedtime_start,
                "day": day,
                "deep_sleep_duration": deep_sleep_duration,
                "efficiency": efficiency,
                "heart_rate": heart_rate,
                "hrv": hrv,
                "latency": latency,
                "light_sleep_duration": light_sleep_duration,
                "low_battery_alert": low_battery_alert,
                "lowest_heart_rate": lowest_heart_rate,
                "movement_30_sec": movement_30_sec,
                "period": period,
                "readiness": readiness,
                "readiness_score_delta": readiness_score_delta,
                "rem_sleep_duration": rem_sleep_duration,
                "restless_periods": restless_periods,
                "sleep_phase_5_min": sleep_phase_5_min,
                "sleep_score_delta": sleep_score_delta,
                "sleep_algorithm_version": sleep_algorithm_version,
                "time_in_bed": time_in_bed,
                "total_sleep_duration": total_sleep_duration,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.readiness_summary import ReadinessSummary
        from ..models.sample_model import SampleModel

        d = src_dict.copy()
        id = d.pop("id")

        def _parse_average_breath(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        average_breath = _parse_average_breath(d.pop("average_breath"))

        def _parse_average_heart_rate(data: object) -> Union[None, float]:
            if data is None:
                return data
            return cast(Union[None, float], data)

        average_heart_rate = _parse_average_heart_rate(d.pop("average_heart_rate"))

        def _parse_average_hrv(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        average_hrv = _parse_average_hrv(d.pop("average_hrv"))

        def _parse_awake_time(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        awake_time = _parse_awake_time(d.pop("awake_time"))

        bedtime_end = d.pop("bedtime_end")

        bedtime_start = d.pop("bedtime_start")

        day = isoparse(d.pop("day")).date()

        def _parse_deep_sleep_duration(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        deep_sleep_duration = _parse_deep_sleep_duration(d.pop("deep_sleep_duration"))

        def _parse_efficiency(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        efficiency = _parse_efficiency(d.pop("efficiency"))

        def _parse_heart_rate(data: object) -> Union["SampleModel", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                heart_rate_type_0 = SampleModel.from_dict(data)

                return heart_rate_type_0
            except:  # noqa: E722
                pass
            return cast(Union["SampleModel", None], data)

        heart_rate = _parse_heart_rate(d.pop("heart_rate"))

        def _parse_hrv(data: object) -> Union["SampleModel", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                hrv_type_0 = SampleModel.from_dict(data)

                return hrv_type_0
            except:  # noqa: E722
                pass
            return cast(Union["SampleModel", None], data)

        hrv = _parse_hrv(d.pop("hrv"))

        def _parse_latency(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        latency = _parse_latency(d.pop("latency"))

        def _parse_light_sleep_duration(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        light_sleep_duration = _parse_light_sleep_duration(d.pop("light_sleep_duration"))

        low_battery_alert = d.pop("low_battery_alert")

        def _parse_lowest_heart_rate(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        lowest_heart_rate = _parse_lowest_heart_rate(d.pop("lowest_heart_rate"))

        def _parse_movement_30_sec(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        movement_30_sec = _parse_movement_30_sec(d.pop("movement_30_sec"))

        period = d.pop("period")

        def _parse_readiness(data: object) -> Union["ReadinessSummary", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                readiness_type_0 = ReadinessSummary.from_dict(data)

                return readiness_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ReadinessSummary", None], data)

        readiness = _parse_readiness(d.pop("readiness"))

        def _parse_readiness_score_delta(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        readiness_score_delta = _parse_readiness_score_delta(d.pop("readiness_score_delta"))

        def _parse_rem_sleep_duration(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        rem_sleep_duration = _parse_rem_sleep_duration(d.pop("rem_sleep_duration"))

        def _parse_restless_periods(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        restless_periods = _parse_restless_periods(d.pop("restless_periods"))

        def _parse_sleep_phase_5_min(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        sleep_phase_5_min = _parse_sleep_phase_5_min(d.pop("sleep_phase_5_min"))

        def _parse_sleep_score_delta(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        sleep_score_delta = _parse_sleep_score_delta(d.pop("sleep_score_delta"))

        def _parse_sleep_algorithm_version(data: object) -> Union[None, SleepAlgorithmVersion]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sleep_algorithm_version_type_0 = SleepAlgorithmVersion(data)

                return sleep_algorithm_version_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, SleepAlgorithmVersion], data)

        sleep_algorithm_version = _parse_sleep_algorithm_version(d.pop("sleep_algorithm_version"))

        time_in_bed = d.pop("time_in_bed")

        def _parse_total_sleep_duration(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        total_sleep_duration = _parse_total_sleep_duration(d.pop("total_sleep_duration"))

        type_ = SleepType(d.pop("type"))

        sleep_model = cls(
            id=id,
            average_breath=average_breath,
            average_heart_rate=average_heart_rate,
            average_hrv=average_hrv,
            awake_time=awake_time,
            bedtime_end=bedtime_end,
            bedtime_start=bedtime_start,
            day=day,
            deep_sleep_duration=deep_sleep_duration,
            efficiency=efficiency,
            heart_rate=heart_rate,
            hrv=hrv,
            latency=latency,
            light_sleep_duration=light_sleep_duration,
            low_battery_alert=low_battery_alert,
            lowest_heart_rate=lowest_heart_rate,
            movement_30_sec=movement_30_sec,
            period=period,
            readiness=readiness,
            readiness_score_delta=readiness_score_delta,
            rem_sleep_duration=rem_sleep_duration,
            restless_periods=restless_periods,
            sleep_phase_5_min=sleep_phase_5_min,
            sleep_score_delta=sleep_score_delta,
            sleep_algorithm_version=sleep_algorithm_version,
            time_in_bed=time_in_bed,
            total_sleep_duration=total_sleep_duration,
            type_=type_,
        )

        sleep_model.additional_properties = d
        return sleep_model

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
