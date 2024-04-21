from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domain_search_service_v2_model_domain_search_contracts_v2_search_result_type import (
    DomainSearchServiceV2ModelDomainSearchContractsV2SearchResultType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_search_service_v2_model_domain_search_contracts_v2_project import (
        DomainSearchServiceV2ModelDomainSearchContractsV2Project,
    )
    from ..models.domain_search_service_v2_model_domain_search_contracts_v2_property_listing import (
        DomainSearchServiceV2ModelDomainSearchContractsV2PropertyListing,
    )


T = TypeVar("T", bound="DomainSearchServiceV2ModelDomainSearchContractsV2SearchResult")


@_attrs_define
class DomainSearchServiceV2ModelDomainSearchContractsV2SearchResult:
    """
    Attributes:
        type (Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2SearchResultType]):
        listing (Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2PropertyListing]):
        listings (Union[Unset, List['DomainSearchServiceV2ModelDomainSearchContractsV2PropertyListing']]):
        project (Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2Project]):
    """

    type: Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2SearchResultType] = UNSET
    listing: Union[Unset, "DomainSearchServiceV2ModelDomainSearchContractsV2PropertyListing"] = UNSET
    listings: Union[Unset, List["DomainSearchServiceV2ModelDomainSearchContractsV2PropertyListing"]] = UNSET
    project: Union[Unset, "DomainSearchServiceV2ModelDomainSearchContractsV2Project"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        listing: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.listing, Unset):
            listing = self.listing.to_dict()

        listings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.listings, Unset):
            listings = []
            for listings_item_data in self.listings:
                listings_item = listings_item_data.to_dict()
                listings.append(listings_item)

        project: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.project, Unset):
            project = self.project.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if listing is not UNSET:
            field_dict["listing"] = listing
        if listings is not UNSET:
            field_dict["listings"] = listings
        if project is not UNSET:
            field_dict["project"] = project

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_search_service_v2_model_domain_search_contracts_v2_project import (
            DomainSearchServiceV2ModelDomainSearchContractsV2Project,
        )
        from ..models.domain_search_service_v2_model_domain_search_contracts_v2_property_listing import (
            DomainSearchServiceV2ModelDomainSearchContractsV2PropertyListing,
        )

        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2SearchResultType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = DomainSearchServiceV2ModelDomainSearchContractsV2SearchResultType(_type)

        _listing = d.pop("listing", UNSET)
        listing: Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2PropertyListing]
        if isinstance(_listing, Unset):
            listing = UNSET
        else:
            listing = DomainSearchServiceV2ModelDomainSearchContractsV2PropertyListing.from_dict(_listing)

        listings = []
        _listings = d.pop("listings", UNSET)
        for listings_item_data in _listings or []:
            listings_item = DomainSearchServiceV2ModelDomainSearchContractsV2PropertyListing.from_dict(
                listings_item_data
            )

            listings.append(listings_item)

        _project = d.pop("project", UNSET)
        project: Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2Project]
        if isinstance(_project, Unset):
            project = UNSET
        else:
            project = DomainSearchServiceV2ModelDomainSearchContractsV2Project.from_dict(_project)

        domain_search_service_v2_model_domain_search_contracts_v2_search_result = cls(
            type=type,
            listing=listing,
            listings=listings,
            project=project,
        )

        domain_search_service_v2_model_domain_search_contracts_v2_search_result.additional_properties = d
        return domain_search_service_v2_model_domain_search_contracts_v2_search_result

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
