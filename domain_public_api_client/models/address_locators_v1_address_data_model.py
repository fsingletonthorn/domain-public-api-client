from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.address_locators_v1_address_data_model_types_type_0_item import (
    AddressLocatorsV1AddressDataModelTypesType0Item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address_locators_v1_address_components import AddressLocatorsV1AddressComponents
    from ..models.address_locators_v1_apm_id_model import AddressLocatorsV1ApmIdModel


T = TypeVar("T", bound="AddressLocatorsV1AddressDataModel")


@_attrs_define
class AddressLocatorsV1AddressDataModel:
    """APMAPIModelsTokenisedSearchV3AddressDataModel

    Attributes:
        types (Union[List[AddressLocatorsV1AddressDataModelTypesType0Item], None, Unset]): Gets or Sets Types
        address_components (Union[List['AddressLocatorsV1AddressComponents'], None, Unset]): Gets or Sets
            AddressComponents
        ids (Union[List['AddressLocatorsV1ApmIdModel'], None, Unset]): Gets or Sets Ids
    """

    types: Union[List[AddressLocatorsV1AddressDataModelTypesType0Item], None, Unset] = UNSET
    address_components: Union[List["AddressLocatorsV1AddressComponents"], None, Unset] = UNSET
    ids: Union[List["AddressLocatorsV1ApmIdModel"], None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        types: Union[List[str], None, Unset]
        if isinstance(self.types, Unset):
            types = UNSET
        elif isinstance(self.types, list):
            types = []
            for types_type_0_item_data in self.types:
                types_type_0_item = types_type_0_item_data.value
                types.append(types_type_0_item)

        else:
            types = self.types

        address_components: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.address_components, Unset):
            address_components = UNSET
        elif isinstance(self.address_components, list):
            address_components = []
            for address_components_type_0_item_data in self.address_components:
                address_components_type_0_item = address_components_type_0_item_data.to_dict()
                address_components.append(address_components_type_0_item)

        else:
            address_components = self.address_components

        ids: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.ids, Unset):
            ids = UNSET
        elif isinstance(self.ids, list):
            ids = []
            for ids_type_0_item_data in self.ids:
                ids_type_0_item = ids_type_0_item_data.to_dict()
                ids.append(ids_type_0_item)

        else:
            ids = self.ids

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if types is not UNSET:
            field_dict["types"] = types
        if address_components is not UNSET:
            field_dict["addressComponents"] = address_components
        if ids is not UNSET:
            field_dict["ids"] = ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address_locators_v1_address_components import AddressLocatorsV1AddressComponents
        from ..models.address_locators_v1_apm_id_model import AddressLocatorsV1ApmIdModel

        d = src_dict.copy()

        def _parse_types(data: object) -> Union[List[AddressLocatorsV1AddressDataModelTypesType0Item], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                types_type_0 = []
                _types_type_0 = data
                for types_type_0_item_data in _types_type_0:
                    types_type_0_item = AddressLocatorsV1AddressDataModelTypesType0Item(types_type_0_item_data)

                    types_type_0.append(types_type_0_item)

                return types_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[AddressLocatorsV1AddressDataModelTypesType0Item], None, Unset], data)

        types = _parse_types(d.pop("types", UNSET))

        def _parse_address_components(data: object) -> Union[List["AddressLocatorsV1AddressComponents"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                address_components_type_0 = []
                _address_components_type_0 = data
                for address_components_type_0_item_data in _address_components_type_0:
                    address_components_type_0_item = AddressLocatorsV1AddressComponents.from_dict(
                        address_components_type_0_item_data
                    )

                    address_components_type_0.append(address_components_type_0_item)

                return address_components_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["AddressLocatorsV1AddressComponents"], None, Unset], data)

        address_components = _parse_address_components(d.pop("addressComponents", UNSET))

        def _parse_ids(data: object) -> Union[List["AddressLocatorsV1ApmIdModel"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                ids_type_0 = []
                _ids_type_0 = data
                for ids_type_0_item_data in _ids_type_0:
                    ids_type_0_item = AddressLocatorsV1ApmIdModel.from_dict(ids_type_0_item_data)

                    ids_type_0.append(ids_type_0_item)

                return ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["AddressLocatorsV1ApmIdModel"], None, Unset], data)

        ids = _parse_ids(d.pop("ids", UNSET))

        address_locators_v1_address_data_model = cls(
            types=types,
            address_components=address_components,
            ids=ids,
        )

        return address_locators_v1_address_data_model
