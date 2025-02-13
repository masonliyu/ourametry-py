import datetime
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.daily_sp_o2_aggregated_values_model import DailySpO2AggregatedValuesModel


T = TypeVar("T", bound="DailySpO2Model")


@_attrs_define
class DailySpO2Model:
    """
    Attributes:
        id (str):
        day (datetime.date):
        spo2_percentage (Union['DailySpO2AggregatedValuesModel', None]): The SpO2 percentage value aggregated over a
            single day.
        breathing_disturbance_index (Union[None, int]): Breathing Disturbance Index (BDI) calculated using detected SpO2
            drops from timeseries. Values should be in range [0, 100]
    """

    id: str
    day: datetime.date
    spo2_percentage: Union["DailySpO2AggregatedValuesModel", None]
    breathing_disturbance_index: Union[None, int]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.daily_sp_o2_aggregated_values_model import DailySpO2AggregatedValuesModel

        id = self.id

        day = self.day.isoformat()

        spo2_percentage: Union[None, dict[str, Any]]
        if isinstance(self.spo2_percentage, DailySpO2AggregatedValuesModel):
            spo2_percentage = self.spo2_percentage.to_dict()
        else:
            spo2_percentage = self.spo2_percentage

        breathing_disturbance_index: Union[None, int]
        breathing_disturbance_index = self.breathing_disturbance_index

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "day": day,
                "spo2_percentage": spo2_percentage,
                "breathing_disturbance_index": breathing_disturbance_index,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.daily_sp_o2_aggregated_values_model import DailySpO2AggregatedValuesModel

        d = src_dict.copy()
        id = d.pop("id")

        day = isoparse(d.pop("day")).date()

        def _parse_spo2_percentage(data: object) -> Union["DailySpO2AggregatedValuesModel", None]:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                spo2_percentage_type_0 = DailySpO2AggregatedValuesModel.from_dict(data)

                return spo2_percentage_type_0
            except:  # noqa: E722
                pass
            return cast(Union["DailySpO2AggregatedValuesModel", None], data)

        spo2_percentage = _parse_spo2_percentage(d.pop("spo2_percentage"))

        def _parse_breathing_disturbance_index(data: object) -> Union[None, int]:
            if data is None:
                return data
            return cast(Union[None, int], data)

        breathing_disturbance_index = _parse_breathing_disturbance_index(d.pop("breathing_disturbance_index"))

        daily_sp_o2_model = cls(
            id=id,
            day=day,
            spo2_percentage=spo2_percentage,
            breathing_disturbance_index=breathing_disturbance_index,
        )

        daily_sp_o2_model.additional_properties = d
        return daily_sp_o2_model

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
