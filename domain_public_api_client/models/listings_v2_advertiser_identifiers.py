from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.listings_v2_advertiser_identifiers_advertiser_type import ListingsV2AdvertiserIdentifiersAdvertiserType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingsV2AdvertiserIdentifiers")


@_attrs_define
class ListingsV2AdvertiserIdentifiers:
    """Encapsulates the listing's advertiser identifiers

    Attributes:
        advertiser_type (Union[Unset, ListingsV2AdvertiserIdentifiersAdvertiserType]): Gets or Sets AdvertiserType
        advertiser_id (Union[None, Unset, int]): Advertiser's identifier
        contact_ids (Union[List[int], None, Unset]): Identifier of each contact the advertiser has associated with the
            listing
        agent_ids (Union[List[str], None, Unset]): Identifier of each agent the advertiser has associated with the
            listing
        conjunction_contact_ids (Union[List[int], None, Unset]): Identifier of each conjunctional contact associated
            with the listing
        conjunction_agent_ids (Union[List[str], None, Unset]): Identifier of each conjunctional agent associated with
            the listing
    """

    advertiser_type: Union[Unset, ListingsV2AdvertiserIdentifiersAdvertiserType] = UNSET
    advertiser_id: Union[None, Unset, int] = UNSET
    contact_ids: Union[List[int], None, Unset] = UNSET
    agent_ids: Union[List[str], None, Unset] = UNSET
    conjunction_contact_ids: Union[List[int], None, Unset] = UNSET
    conjunction_agent_ids: Union[List[str], None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        advertiser_type: Union[Unset, str] = UNSET
        if not isinstance(self.advertiser_type, Unset):
            advertiser_type = self.advertiser_type.value

        advertiser_id: Union[None, Unset, int]
        if isinstance(self.advertiser_id, Unset):
            advertiser_id = UNSET
        else:
            advertiser_id = self.advertiser_id

        contact_ids: Union[List[int], None, Unset]
        if isinstance(self.contact_ids, Unset):
            contact_ids = UNSET
        elif isinstance(self.contact_ids, list):
            contact_ids = self.contact_ids

        else:
            contact_ids = self.contact_ids

        agent_ids: Union[List[str], None, Unset]
        if isinstance(self.agent_ids, Unset):
            agent_ids = UNSET
        elif isinstance(self.agent_ids, list):
            agent_ids = self.agent_ids

        else:
            agent_ids = self.agent_ids

        conjunction_contact_ids: Union[List[int], None, Unset]
        if isinstance(self.conjunction_contact_ids, Unset):
            conjunction_contact_ids = UNSET
        elif isinstance(self.conjunction_contact_ids, list):
            conjunction_contact_ids = self.conjunction_contact_ids

        else:
            conjunction_contact_ids = self.conjunction_contact_ids

        conjunction_agent_ids: Union[List[str], None, Unset]
        if isinstance(self.conjunction_agent_ids, Unset):
            conjunction_agent_ids = UNSET
        elif isinstance(self.conjunction_agent_ids, list):
            conjunction_agent_ids = self.conjunction_agent_ids

        else:
            conjunction_agent_ids = self.conjunction_agent_ids

        field_dict: Dict[str, Any] = {}
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
        advertiser_type: Union[Unset, ListingsV2AdvertiserIdentifiersAdvertiserType]
        if isinstance(_advertiser_type, Unset):
            advertiser_type = UNSET
        else:
            advertiser_type = ListingsV2AdvertiserIdentifiersAdvertiserType(_advertiser_type)

        def _parse_advertiser_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        advertiser_id = _parse_advertiser_id(d.pop("advertiserId", UNSET))

        def _parse_contact_ids(data: object) -> Union[List[int], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                contact_ids_type_0 = cast(List[int], data)

                return contact_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[int], None, Unset], data)

        contact_ids = _parse_contact_ids(d.pop("contactIds", UNSET))

        def _parse_agent_ids(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                agent_ids_type_0 = cast(List[str], data)

                return agent_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        agent_ids = _parse_agent_ids(d.pop("agentIds", UNSET))

        def _parse_conjunction_contact_ids(data: object) -> Union[List[int], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                conjunction_contact_ids_type_0 = cast(List[int], data)

                return conjunction_contact_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[int], None, Unset], data)

        conjunction_contact_ids = _parse_conjunction_contact_ids(d.pop("conjunctionContactIds", UNSET))

        def _parse_conjunction_agent_ids(data: object) -> Union[List[str], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                conjunction_agent_ids_type_0 = cast(List[str], data)

                return conjunction_agent_ids_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[str], None, Unset], data)

        conjunction_agent_ids = _parse_conjunction_agent_ids(d.pop("conjunctionAgentIds", UNSET))

        listings_v2_advertiser_identifiers = cls(
            advertiser_type=advertiser_type,
            advertiser_id=advertiser_id,
            contact_ids=contact_ids,
            agent_ids=agent_ids,
            conjunction_contact_ids=conjunction_contact_ids,
            conjunction_agent_ids=conjunction_agent_ids,
        )

        return listings_v2_advertiser_identifiers
