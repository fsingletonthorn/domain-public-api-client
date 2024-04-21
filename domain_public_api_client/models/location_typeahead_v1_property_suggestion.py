from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.location_typeahead_v1_address_components import LocationTypeaheadV1AddressComponents


T = TypeVar("T", bound="LocationTypeaheadV1PropertySuggestion")


@_attrs_define
class LocationTypeaheadV1PropertySuggestion:
    """
    Attributes:
        address (Union[None, Unset, str]):
        address_components (Union[Unset, LocationTypeaheadV1AddressComponents]):
        id (Union[None, Unset, str]):
        relative_score (Union[Unset, int]):
    """

    address: Union[None, Unset, str] = UNSET
    address_components: Union[Unset, "LocationTypeaheadV1AddressComponents"] = UNSET
    id: Union[None, Unset, str] = UNSET
    relative_score: Union[Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        address: Union[None, Unset, str]
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        address_components: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address_components, Unset):
            address_components = self.address_components.to_dict()

        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        relative_score = self.relative_score

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if address_components is not UNSET:
            field_dict["addressComponents"] = address_components
        if id is not UNSET:
            field_dict["id"] = id
        if relative_score is not UNSET:
            field_dict["relativeScore"] = relative_score

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.location_typeahead_v1_address_components import LocationTypeaheadV1AddressComponents

        d = src_dict.copy()

        def _parse_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        address = _parse_address(d.pop("address", UNSET))

        _address_components = d.pop("addressComponents", UNSET)
        address_components: Union[Unset, LocationTypeaheadV1AddressComponents]
        if isinstance(_address_components, Unset):
            address_components = UNSET
        else:
            address_components = LocationTypeaheadV1AddressComponents.from_dict(_address_components)

        def _parse_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        id = _parse_id(d.pop("id", UNSET))

        relative_score = d.pop("relativeScore", UNSET)

        location_typeahead_v1_property_suggestion = cls(
            address=address,
            address_components=address_components,
            id=id,
            relative_score=relative_score,
        )

        return location_typeahead_v1_property_suggestion
