import datetime
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.ext_api_v2_data_type import ExtApiV2DataType
from ..models.webhook_operation import WebhookOperation

T = TypeVar("T", bound="WebhookSubscriptionModel")


@_attrs_define
class WebhookSubscriptionModel:
    """
    Attributes:
        id (str):
        callback_url (str):
        event_type (WebhookOperation):
        data_type (ExtApiV2DataType):
        expiration_time (datetime.datetime):
    """

    id: str
    callback_url: str
    event_type: WebhookOperation
    data_type: ExtApiV2DataType
    expiration_time: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        callback_url = self.callback_url

        event_type = self.event_type.value

        data_type = self.data_type.value

        expiration_time = self.expiration_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "callback_url": callback_url,
                "event_type": event_type,
                "data_type": data_type,
                "expiration_time": expiration_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        callback_url = d.pop("callback_url")

        event_type = WebhookOperation(d.pop("event_type"))

        data_type = ExtApiV2DataType(d.pop("data_type"))

        expiration_time = isoparse(d.pop("expiration_time"))

        webhook_subscription_model = cls(
            id=id,
            callback_url=callback_url,
            event_type=event_type,
            data_type=data_type,
            expiration_time=expiration_time,
        )

        webhook_subscription_model.additional_properties = d
        return webhook_subscription_model

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
