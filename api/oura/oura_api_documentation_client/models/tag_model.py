import datetime
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="TagModel")


@_attrs_define
class TagModel:
    """A TagModel maps to an ASSANote. An ASSANote in ExtAPIV2 is called a Tag
    A TagModel will be populated by data from an ASSANote
    The fields in the TagModel map to fields in an ASSANote

        Attributes:
            id (str):
            day (datetime.date): Day that the note belongs to.
            text (Union[None, str]): Textual contents of the note.
            timestamp (datetime.datetime): Timestamp of the note.
            tags (list[str]): Selected tags for the tag.
    """

    id: str
    day: datetime.date
    text: Union[None, str]
    timestamp: datetime.datetime
    tags: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        day = self.day.isoformat()

        text: Union[None, str]
        text = self.text

        timestamp = self.timestamp.isoformat()

        tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "day": day,
                "text": text,
                "timestamp": timestamp,
                "tags": tags,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        day = isoparse(d.pop("day")).date()

        def _parse_text(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        text = _parse_text(d.pop("text"))

        timestamp = isoparse(d.pop("timestamp"))

        tags = cast(list[str], d.pop("tags"))

        tag_model = cls(
            id=id,
            day=day,
            text=text,
            timestamp=timestamp,
            tags=tags,
        )

        tag_model.additional_properties = d
        return tag_model

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
