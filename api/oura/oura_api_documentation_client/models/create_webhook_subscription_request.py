from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ext_api_v2_data_type import ExtApiV2DataType
from ..models.webhook_operation import WebhookOperation

T = TypeVar("T", bound="CreateWebhookSubscriptionRequest")


@_attrs_define
class CreateWebhookSubscriptionRequest:
    """
    Attributes:
        callback_url (str):
        verification_token (str):
        event_type (WebhookOperation):
        data_type (ExtApiV2DataType):
    """

    callback_url: str
    verification_token: str
    event_type: WebhookOperation
    data_type: ExtApiV2DataType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        callback_url = self.callback_url

        verification_token = self.verification_token

        event_type = self.event_type.value

        data_type = self.data_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "callback_url": callback_url,
                "verification_token": verification_token,
                "event_type": event_type,
                "data_type": data_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        callback_url = d.pop("callback_url")

        verification_token = d.pop("verification_token")

        event_type = WebhookOperation(d.pop("event_type"))

        data_type = ExtApiV2DataType(d.pop("data_type"))

        create_webhook_subscription_request = cls(
            callback_url=callback_url,
            verification_token=verification_token,
            event_type=event_type,
            data_type=data_type,
        )

        create_webhook_subscription_request.additional_properties = d
        return create_webhook_subscription_request

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
