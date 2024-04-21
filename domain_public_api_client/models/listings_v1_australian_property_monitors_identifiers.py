from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingsV1AustralianPropertyMonitorsIdentifiers")


@_attrs_define
class ListingsV1AustralianPropertyMonitorsIdentifiers:
    r"""APM Identifiers

    Attributes:
        address_id (Union[None, Unset, int]): APM address identifier
        street_id (Union[None, Unset, int]): APM street identifier
        suburb_id (Union[None, Unset, int]): APM suburb identifier
        cadastre_id (Union[None, Unset, int]): APM cadastre identifier
        postcode_id (Union[None, Unset, int]): APM postcode identifier
        state_id (Union[None, Unset, int]): State identifier
        state (Union[None, Unset, str]): APM State
        property_type_id (Union[None, Unset, int]): APM property type identifier
        property_type_category_id (Union[None, Unset, int]): APM property category type identifier
        street_number (Union[None, Unset, str]): APM washed and standardized address component for the street number,
            (including any prefixes, suffixed and composite numbers e.g. \"2-4a\")
    """

    address_id: Union[None, Unset, int] = UNSET
    street_id: Union[None, Unset, int] = UNSET
    suburb_id: Union[None, Unset, int] = UNSET
    cadastre_id: Union[None, Unset, int] = UNSET
    postcode_id: Union[None, Unset, int] = UNSET
    state_id: Union[None, Unset, int] = UNSET
    state: Union[None, Unset, str] = UNSET
    property_type_id: Union[None, Unset, int] = UNSET
    property_type_category_id: Union[None, Unset, int] = UNSET
    street_number: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        address_id: Union[None, Unset, int]
        if isinstance(self.address_id, Unset):
            address_id = UNSET
        else:
            address_id = self.address_id

        street_id: Union[None, Unset, int]
        if isinstance(self.street_id, Unset):
            street_id = UNSET
        else:
            street_id = self.street_id

        suburb_id: Union[None, Unset, int]
        if isinstance(self.suburb_id, Unset):
            suburb_id = UNSET
        else:
            suburb_id = self.suburb_id

        cadastre_id: Union[None, Unset, int]
        if isinstance(self.cadastre_id, Unset):
            cadastre_id = UNSET
        else:
            cadastre_id = self.cadastre_id

        postcode_id: Union[None, Unset, int]
        if isinstance(self.postcode_id, Unset):
            postcode_id = UNSET
        else:
            postcode_id = self.postcode_id

        state_id: Union[None, Unset, int]
        if isinstance(self.state_id, Unset):
            state_id = UNSET
        else:
            state_id = self.state_id

        state: Union[None, Unset, str]
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        property_type_id: Union[None, Unset, int]
        if isinstance(self.property_type_id, Unset):
            property_type_id = UNSET
        else:
            property_type_id = self.property_type_id

        property_type_category_id: Union[None, Unset, int]
        if isinstance(self.property_type_category_id, Unset):
            property_type_category_id = UNSET
        else:
            property_type_category_id = self.property_type_category_id

        street_number: Union[None, Unset, str]
        if isinstance(self.street_number, Unset):
            street_number = UNSET
        else:
            street_number = self.street_number

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if address_id is not UNSET:
            field_dict["addressId"] = address_id
        if street_id is not UNSET:
            field_dict["streetId"] = street_id
        if suburb_id is not UNSET:
            field_dict["suburbId"] = suburb_id
        if cadastre_id is not UNSET:
            field_dict["cadastreId"] = cadastre_id
        if postcode_id is not UNSET:
            field_dict["postcodeId"] = postcode_id
        if state_id is not UNSET:
            field_dict["stateId"] = state_id
        if state is not UNSET:
            field_dict["state"] = state
        if property_type_id is not UNSET:
            field_dict["propertyTypeId"] = property_type_id
        if property_type_category_id is not UNSET:
            field_dict["propertyTypeCategoryId"] = property_type_category_id
        if street_number is not UNSET:
            field_dict["streetNumber"] = street_number

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_address_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        address_id = _parse_address_id(d.pop("addressId", UNSET))

        def _parse_street_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        street_id = _parse_street_id(d.pop("streetId", UNSET))

        def _parse_suburb_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        suburb_id = _parse_suburb_id(d.pop("suburbId", UNSET))

        def _parse_cadastre_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        cadastre_id = _parse_cadastre_id(d.pop("cadastreId", UNSET))

        def _parse_postcode_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        postcode_id = _parse_postcode_id(d.pop("postcodeId", UNSET))

        def _parse_state_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        state_id = _parse_state_id(d.pop("stateId", UNSET))

        def _parse_state(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        state = _parse_state(d.pop("state", UNSET))

        def _parse_property_type_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        property_type_id = _parse_property_type_id(d.pop("propertyTypeId", UNSET))

        def _parse_property_type_category_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        property_type_category_id = _parse_property_type_category_id(d.pop("propertyTypeCategoryId", UNSET))

        def _parse_street_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        street_number = _parse_street_number(d.pop("streetNumber", UNSET))

        listings_v1_australian_property_monitors_identifiers = cls(
            address_id=address_id,
            street_id=street_id,
            suburb_id=suburb_id,
            cadastre_id=cadastre_id,
            postcode_id=postcode_id,
            state_id=state_id,
            state=state,
            property_type_id=property_type_id,
            property_type_category_id=property_type_category_id,
            street_number=street_number,
        )

        return listings_v1_australian_property_monitors_identifiers
