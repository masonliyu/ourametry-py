from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.daily_activity_model import DailyActivityModel


T = TypeVar("T", bound="MultiDocumentResponseDailyActivityModel")


@_attrs_define
class MultiDocumentResponseDailyActivityModel:
    """
    Attributes:
        data (list['DailyActivityModel']):
        next_token (Union[None, str]):
    """

    data: list["DailyActivityModel"]
    next_token: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        next_token: Union[None, str]
        next_token = self.next_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "next_token": next_token,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        from ..models.daily_activity_model import DailyActivityModel

        d = src_dict.copy()
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = DailyActivityModel.from_dict(data_item_data)

            data.append(data_item)

        def _parse_next_token(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        next_token = _parse_next_token(d.pop("next_token"))

        multi_document_response_daily_activity_model = cls(
            data=data,
            next_token=next_token,
        )

        multi_document_response_daily_activity_model.additional_properties = d
        return multi_document_response_daily_activity_model

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
