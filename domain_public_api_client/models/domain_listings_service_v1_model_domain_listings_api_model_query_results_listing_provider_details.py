from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingProviderDetails")


@_attrs_define
class DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingProviderDetails:
    """
    Attributes:
        provider_system (Union[Unset, str]):
        provider_ad_id (Union[Unset, str]):
    """

    provider_system: Union[Unset, str] = UNSET
    provider_ad_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        provider_system = self.provider_system

        provider_ad_id = self.provider_ad_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if provider_system is not UNSET:
            field_dict["providerSystem"] = provider_system
        if provider_ad_id is not UNSET:
            field_dict["providerAdID"] = provider_ad_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        provider_system = d.pop("providerSystem", UNSET)

        provider_ad_id = d.pop("providerAdID", UNSET)

        domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_provider_details = cls(
            provider_system=provider_system,
            provider_ad_id=provider_ad_id,
        )

        domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_provider_details.additional_properties = d
        return domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_provider_details

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
