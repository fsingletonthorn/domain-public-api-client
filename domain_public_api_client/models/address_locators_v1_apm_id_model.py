from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.address_locators_v1_apm_id_model_level import AddressLocatorsV1ApmIdModelLevel
from ..types import UNSET, Unset

T = TypeVar("T", bound="AddressLocatorsV1ApmIdModel")


@_attrs_define
class AddressLocatorsV1ApmIdModel:
    """APMAPIModelsTokenisedSearchV3ApmIdModel

    Attributes:
        level (Union[Unset, AddressLocatorsV1ApmIdModelLevel]): Gets or Sets Level
        id (Union[None, Unset, int]): Gets or Sets Id
    """

    level: Union[Unset, AddressLocatorsV1ApmIdModelLevel] = UNSET
    id: Union[None, Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        level: Union[Unset, str] = UNSET
        if not isinstance(self.level, Unset):
            level = self.level.value

        id: Union[None, Unset, int]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if level is not UNSET:
            field_dict["level"] = level
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _level = d.pop("level", UNSET)
        level: Union[Unset, AddressLocatorsV1ApmIdModelLevel]
        if isinstance(_level, Unset):
            level = UNSET
        else:
            level = AddressLocatorsV1ApmIdModelLevel(_level)

        def _parse_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        id = _parse_id(d.pop("id", UNSET))

        address_locators_v1_apm_id_model = cls(
            level=level,
            id=id,
        )

        return address_locators_v1_apm_id_model
