from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.ext_api_v2_data_type import ExtApiV2DataType
from ..models.webhook_operation import WebhookOperation
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateWebhookSubscriptionRequest")


@_attrs_define
class UpdateWebhookSubscriptionRequest:
    """
    Attributes:
        verification_token (str):
        callback_url (Union[None, Unset, str]):
        event_type (Union[None, Unset, WebhookOperation]):
        data_type (Union[ExtApiV2DataType, None, Unset]):
    """

    verification_token: str
    callback_url: Union[None, Unset, str] = UNSET
    event_type: Union[None, Unset, WebhookOperation] = UNSET
    data_type: Union[ExtApiV2DataType, None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        verification_token = self.verification_token

        callback_url: Union[None, Unset, str]
        if isinstance(self.callback_url, Unset):
            callback_url = UNSET
        else:
            callback_url = self.callback_url

        event_type: Union[None, Unset, str]
        if isinstance(self.event_type, Unset):
            event_type = UNSET
        elif isinstance(self.event_type, WebhookOperation):
            event_type = self.event_type.value
        else:
            event_type = self.event_type

        data_type: Union[None, Unset, str]
        if isinstance(self.data_type, Unset):
            data_type = UNSET
        elif isinstance(self.data_type, ExtApiV2DataType):
            data_type = self.data_type.value
        else:
            data_type = self.data_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "verification_token": verification_token,
            }
        )
        if callback_url is not UNSET:
            field_dict["callback_url"] = callback_url
        if event_type is not UNSET:
            field_dict["event_type"] = event_type
        if data_type is not UNSET:
            field_dict["data_type"] = data_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        verification_token = d.pop("verification_token")

        def _parse_callback_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        callback_url = _parse_callback_url(d.pop("callback_url", UNSET))

        def _parse_event_type(data: object) -> Union[None, Unset, WebhookOperation]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                event_type_type_0 = WebhookOperation(data)

                return event_type_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, WebhookOperation], data)

        event_type = _parse_event_type(d.pop("event_type", UNSET))

        def _parse_data_type(data: object) -> Union[ExtApiV2DataType, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                data_type_type_0 = ExtApiV2DataType(data)

                return data_type_type_0
            except:  # noqa: E722
                pass
            return cast(Union[ExtApiV2DataType, None, Unset], data)

        data_type = _parse_data_type(d.pop("data_type", UNSET))

        update_webhook_subscription_request = cls(
            verification_token=verification_token,
            callback_url=callback_url,
            event_type=event_type,
            data_type=data_type,
        )

        update_webhook_subscription_request.additional_properties = d
        return update_webhook_subscription_request

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
