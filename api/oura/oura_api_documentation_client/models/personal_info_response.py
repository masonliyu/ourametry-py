from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PersonalInfoResponse")


@_attrs_define
class PersonalInfoResponse:
    """
    Attributes:
        id (str):
        age (Union[None, Unset, int]):
        weight (Union[None, Unset, float]):
        height (Union[None, Unset, float]):
        biological_sex (Union[None, Unset, str]):
        email (Union[None, Unset, str]):
    """

    id: str
    age: Union[None, Unset, int] = UNSET
    weight: Union[None, Unset, float] = UNSET
    height: Union[None, Unset, float] = UNSET
    biological_sex: Union[None, Unset, str] = UNSET
    email: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        age: Union[None, Unset, int]
        if isinstance(self.age, Unset):
            age = UNSET
        else:
            age = self.age

        weight: Union[None, Unset, float]
        if isinstance(self.weight, Unset):
            weight = UNSET
        else:
            weight = self.weight

        height: Union[None, Unset, float]
        if isinstance(self.height, Unset):
            height = UNSET
        else:
            height = self.height

        biological_sex: Union[None, Unset, str]
        if isinstance(self.biological_sex, Unset):
            biological_sex = UNSET
        else:
            biological_sex = self.biological_sex

        email: Union[None, Unset, str]
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if age is not UNSET:
            field_dict["age"] = age
        if weight is not UNSET:
            field_dict["weight"] = weight
        if height is not UNSET:
            field_dict["height"] = height
        if biological_sex is not UNSET:
            field_dict["biological_sex"] = biological_sex
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        def _parse_age(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        age = _parse_age(d.pop("age", UNSET))

        def _parse_weight(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        weight = _parse_weight(d.pop("weight", UNSET))

        def _parse_height(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        height = _parse_height(d.pop("height", UNSET))

        def _parse_biological_sex(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        biological_sex = _parse_biological_sex(d.pop("biological_sex", UNSET))

        def _parse_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        email = _parse_email(d.pop("email", UNSET))

        personal_info_response = cls(
            id=id,
            age=age,
            weight=weight,
            height=height,
            biological_sex=biological_sex,
            email=email,
        )

        personal_info_response.additional_properties = d
        return personal_info_response

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
