from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PreMarketV1AdvertiserIdentifiers")


@_attrs_define
class PreMarketV1AdvertiserIdentifiers:
    """
    Attributes:
        domain_agency_id (int): Domain Agency Id
        contact_ids (Union[List[int], None, Unset]): Identifier of each contact the advertiser has associated with the
            listing
        agent_ids (Union[List[str], None, Unset]): Identifier of each agent the advertiser has associated with the
            listing
    """

    domain_agency_id: int
    contact_ids: Union[List[int], None, Unset] = UNSET
    agent_ids: Union[List[str], None, Unset] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        domain_agency_id = self.domain_agency_id

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

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "domainAgencyId": domain_agency_id,
            }
        )
        if contact_ids is not UNSET:
            field_dict["contactIds"] = contact_ids
        if agent_ids is not UNSET:
            field_dict["agentIds"] = agent_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        domain_agency_id = d.pop("domainAgencyId")

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

        pre_market_v1_advertiser_identifiers = cls(
            domain_agency_id=domain_agency_id,
            contact_ids=contact_ids,
            agent_ids=agent_ids,
        )

        return pre_market_v1_advertiser_identifiers
