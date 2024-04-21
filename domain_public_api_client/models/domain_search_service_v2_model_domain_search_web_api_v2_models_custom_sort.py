from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_search_service_v2_model_domain_search_web_api_v2_models_custom_sort_element import (
        DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsCustomSortElement,
    )


T = TypeVar("T", bound="DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsCustomSort")


@_attrs_define
class DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsCustomSort:
    """
    Attributes:
        elements (Union[Unset, List['DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsCustomSortElement']]):
        boost_primary_suburbs (Union[Unset, bool]):
    """

    elements: Union[Unset, List["DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsCustomSortElement"]] = UNSET
    boost_primary_suburbs: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        elements: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.elements, Unset):
            elements = []
            for elements_item_data in self.elements:
                elements_item = elements_item_data.to_dict()
                elements.append(elements_item)

        boost_primary_suburbs = self.boost_primary_suburbs

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if elements is not UNSET:
            field_dict["elements"] = elements
        if boost_primary_suburbs is not UNSET:
            field_dict["boostPrimarySuburbs"] = boost_primary_suburbs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_search_service_v2_model_domain_search_web_api_v2_models_custom_sort_element import (
            DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsCustomSortElement,
        )

        d = src_dict.copy()
        elements = []
        _elements = d.pop("elements", UNSET)
        for elements_item_data in _elements or []:
            elements_item = DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsCustomSortElement.from_dict(
                elements_item_data
            )

            elements.append(elements_item)

        boost_primary_suburbs = d.pop("boostPrimarySuburbs", UNSET)

        domain_search_service_v2_model_domain_search_web_api_v2_models_custom_sort = cls(
            elements=elements,
            boost_primary_suburbs=boost_primary_suburbs,
        )

        domain_search_service_v2_model_domain_search_web_api_v2_models_custom_sort.additional_properties = d
        return domain_search_service_v2_model_domain_search_web_api_v2_models_custom_sort

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
