from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_advertiser_identifiers_advertiser_type import (
    DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiersAdvertiserType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiers")


@_attrs_define
class DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiers:
    """
    Attributes:
        advertiser_type (Union[Unset,
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiersAdvertiserType]):
        advertiser_id (Union[Unset, int]):
        contact_ids (Union[Unset, List[int]]):
        agent_ids (Union[Unset, List[str]]):
        conjunction_contact_ids (Union[Unset, List[int]]):
        conjunction_agent_ids (Union[Unset, List[str]]):
    """

    advertiser_type: Union[
        Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiersAdvertiserType
    ] = UNSET
    advertiser_id: Union[Unset, int] = UNSET
    contact_ids: Union[Unset, List[int]] = UNSET
    agent_ids: Union[Unset, List[str]] = UNSET
    conjunction_contact_ids: Union[Unset, List[int]] = UNSET
    conjunction_agent_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        advertiser_type: Union[Unset, str] = UNSET
        if not isinstance(self.advertiser_type, Unset):
            advertiser_type = self.advertiser_type.value

        advertiser_id = self.advertiser_id

        contact_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.contact_ids, Unset):
            contact_ids = self.contact_ids

        agent_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.agent_ids, Unset):
            agent_ids = self.agent_ids

        conjunction_contact_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.conjunction_contact_ids, Unset):
            conjunction_contact_ids = self.conjunction_contact_ids

        conjunction_agent_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.conjunction_agent_ids, Unset):
            conjunction_agent_ids = self.conjunction_agent_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if advertiser_type is not UNSET:
            field_dict["advertiserType"] = advertiser_type
        if advertiser_id is not UNSET:
            field_dict["advertiserId"] = advertiser_id
        if contact_ids is not UNSET:
            field_dict["contactIds"] = contact_ids
        if agent_ids is not UNSET:
            field_dict["agentIds"] = agent_ids
        if conjunction_contact_ids is not UNSET:
            field_dict["conjunctionContactIds"] = conjunction_contact_ids
        if conjunction_agent_ids is not UNSET:
            field_dict["conjunctionAgentIds"] = conjunction_agent_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _advertiser_type = d.pop("advertiserType", UNSET)
        advertiser_type: Union[
            Unset,
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiersAdvertiserType,
        ]
        if isinstance(_advertiser_type, Unset):
            advertiser_type = UNSET
        else:
            advertiser_type = DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingAdvertiserIdentifiersAdvertiserType(
                _advertiser_type
            )

        advertiser_id = d.pop("advertiserId", UNSET)

        contact_ids = cast(List[int], d.pop("contactIds", UNSET))

        agent_ids = cast(List[str], d.pop("agentIds", UNSET))

        conjunction_contact_ids = cast(List[int], d.pop("conjunctionContactIds", UNSET))

        conjunction_agent_ids = cast(List[str], d.pop("conjunctionAgentIds", UNSET))

        domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_advertiser_identifiers = cls(
            advertiser_type=advertiser_type,
            advertiser_id=advertiser_id,
            contact_ids=contact_ids,
            agent_ids=agent_ids,
            conjunction_contact_ids=conjunction_contact_ids,
            conjunction_agent_ids=conjunction_agent_ids,
        )

        domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_advertiser_identifiers.additional_properties = d
        return domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_advertiser_identifiers

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
