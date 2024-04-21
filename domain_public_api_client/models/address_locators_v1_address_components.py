from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.address_locators_v1_address_components_component import AddressLocatorsV1AddressComponentsComponent
from ..types import UNSET, Unset

T = TypeVar("T", bound="AddressLocatorsV1AddressComponents")


@_attrs_define
class AddressLocatorsV1AddressComponents:
    """APMAPIModelsTokenisedSearchV2AddressComponentModel

    Attributes:
        component (Union[Unset, AddressLocatorsV1AddressComponentsComponent]): Gets or Sets Component
        short_name (Union[None, Unset, str]): Gets or Sets ShortName
    """

    component: Union[Unset, AddressLocatorsV1AddressComponentsComponent] = UNSET
    short_name: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        component: Union[Unset, str] = UNSET
        if not isinstance(self.component, Unset):
            component = self.component.value

        short_name: Union[None, Unset, str]
        if isinstance(self.short_name, Unset):
            short_name = UNSET
        else:
            short_name = self.short_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if component is not UNSET:
            field_dict["component"] = component
        if short_name is not UNSET:
            field_dict["shortName"] = short_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _component = d.pop("component", UNSET)
        component: Union[Unset, AddressLocatorsV1AddressComponentsComponent]
        if isinstance(_component, Unset):
            component = UNSET
        else:
            component = AddressLocatorsV1AddressComponentsComponent(_component)

        def _parse_short_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        short_name = _parse_short_name(d.pop("shortName", UNSET))

        address_locators_v1_address_components = cls(
            component=component,
            short_name=short_name,
        )

        return address_locators_v1_address_components
