from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_listing_media_category import (
    DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingListingMediaCategory,
)
from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_listing_media_type import (
    DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingListingMediaType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingListingMedia")


@_attrs_define
class DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingListingMedia:
    """
    Attributes:
        category (Union[Unset,
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingListingMediaCategory]):
        type (Union[Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingListingMediaType]):
        url (Union[Unset, str]):
    """

    category: Union[
        Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingListingMediaCategory
    ] = UNSET
    type: Union[Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingListingMediaType] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        category: Union[Unset, str] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category is not UNSET:
            field_dict["category"] = category
        if type is not UNSET:
            field_dict["type"] = type
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _category = d.pop("category", UNSET)
        category: Union[
            Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingListingMediaCategory
        ]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingListingMediaCategory(
                _category
            )

        _type = d.pop("type", UNSET)
        type: Union[Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingListingMediaType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingListingMediaType(_type)

        url = d.pop("url", UNSET)

        domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_listing_media = cls(
            category=category,
            type=type,
            url=url,
        )

        domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_listing_media.additional_properties = d
        return domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_listing_media

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
