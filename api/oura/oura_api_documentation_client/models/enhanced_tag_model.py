import datetime
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="EnhancedTagModel")


@_attrs_define
class EnhancedTagModel:
    """An EnhancedTagModel maps an ASSATag. An ASSATag in ExtAPIV2 is called a EnhancedTag
    An EnhancedTagModel will be populated by data from an ASSATag
    The fields in the EnhancedTagModel map to fields in an ASSATag

        Attributes:
            id (str):
            start_time (str):
            start_day (datetime.date): Day of the tag (if no duration) or the start day of the tag (with duration).
            tag_type_code (Union[None, Unset, str]): The unique code of the selected tag type, `NULL` for text-only tags, or
                `custom` for custom tag types.
            end_time (Union[None, Unset, str]): Timestamp of the tag's end for events with duration or `NULL` if there is no
                duration.
            end_day (Union[None, Unset, datetime.date]): Day of the tag's end for events with duration or `NULL` if there is
                no duration.
            comment (Union[None, Unset, str]): Additional freeform text on the tag.
            custom_name (Union[None, Unset, str]): The name of the tag if the tag_type_code is `custom`.
    """

    id: str
    start_time: str
    start_day: datetime.date
    tag_type_code: Union[None, Unset, str] = UNSET
    end_time: Union[None, Unset, str] = UNSET
    end_day: Union[None, Unset, datetime.date] = UNSET
    comment: Union[None, Unset, str] = UNSET
    custom_name: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        start_time = self.start_time

        start_day = self.start_day.isoformat()

        tag_type_code: Union[None, Unset, str]
        if isinstance(self.tag_type_code, Unset):
            tag_type_code = UNSET
        else:
            tag_type_code = self.tag_type_code

        end_time: Union[None, Unset, str]
        if isinstance(self.end_time, Unset):
            end_time = UNSET
        else:
            end_time = self.end_time

        end_day: Union[None, Unset, str]
        if isinstance(self.end_day, Unset):
            end_day = UNSET
        elif isinstance(self.end_day, datetime.date):
            end_day = self.end_day.isoformat()
        else:
            end_day = self.end_day

        comment: Union[None, Unset, str]
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        custom_name: Union[None, Unset, str]
        if isinstance(self.custom_name, Unset):
            custom_name = UNSET
        else:
            custom_name = self.custom_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "start_time": start_time,
                "start_day": start_day,
            }
        )
        if tag_type_code is not UNSET:
            field_dict["tag_type_code"] = tag_type_code
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if end_day is not UNSET:
            field_dict["end_day"] = end_day
        if comment is not UNSET:
            field_dict["comment"] = comment
        if custom_name is not UNSET:
            field_dict["custom_name"] = custom_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        start_time = d.pop("start_time")

        start_day = isoparse(d.pop("start_day")).date()

        def _parse_tag_type_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        tag_type_code = _parse_tag_type_code(d.pop("tag_type_code", UNSET))

        def _parse_end_time(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        end_time = _parse_end_time(d.pop("end_time", UNSET))

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

        def _parse_comment(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        comment = _parse_comment(d.pop("comment", UNSET))

        def _parse_custom_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        custom_name = _parse_custom_name(d.pop("custom_name", UNSET))

        enhanced_tag_model = cls(
            id=id,
            start_time=start_time,
            start_day=start_day,
            tag_type_code=tag_type_code,
            end_time=end_time,
            end_day=end_day,
            comment=comment,
            custom_name=custom_name,
        )

        enhanced_tag_model.additional_properties = d
        return enhanced_tag_model

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
