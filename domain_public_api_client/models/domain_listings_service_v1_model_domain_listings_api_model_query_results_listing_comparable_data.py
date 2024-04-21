from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_past_sale_data import (
        DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPastSaleData,
    )


T = TypeVar("T", bound="DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingComparableData")


@_attrs_define
class DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingComparableData:
    """
    Attributes:
        comparable_property (Union[Unset,
            List['DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPastSaleData']]):
        declaration_text (Union[Unset, str]):
    """

    comparable_property: Union[
        Unset, List["DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPastSaleData"]
    ] = UNSET
    declaration_text: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        comparable_property: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.comparable_property, Unset):
            comparable_property = []
            for comparable_property_item_data in self.comparable_property:
                comparable_property_item = comparable_property_item_data.to_dict()
                comparable_property.append(comparable_property_item)

        declaration_text = self.declaration_text

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comparable_property is not UNSET:
            field_dict["comparableProperty"] = comparable_property
        if declaration_text is not UNSET:
            field_dict["declarationText"] = declaration_text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_past_sale_data import (
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPastSaleData,
        )

        d = src_dict.copy()
        comparable_property = []
        _comparable_property = d.pop("comparableProperty", UNSET)
        for comparable_property_item_data in _comparable_property or []:
            comparable_property_item = (
                DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPastSaleData.from_dict(
                    comparable_property_item_data
                )
            )

            comparable_property.append(comparable_property_item)

        declaration_text = d.pop("declarationText", UNSET)

        domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_comparable_data = cls(
            comparable_property=comparable_property,
            declaration_text=declaration_text,
        )

        domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_comparable_data.additional_properties = d
        return domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_comparable_data

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
