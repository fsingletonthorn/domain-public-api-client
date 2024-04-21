from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainAgentSearchV1ModelAutoSuggestAgentResultDto")


@_attrs_define
class DomainAgentSearchV1ModelAutoSuggestAgentResultDto:
    """
    Attributes:
        agent_id (Union[Unset, int]):
        name (Union[Unset, str]):
        agency_name (Union[Unset, str]):
        suburb (Union[Unset, str]):
        state (Union[Unset, str]):
        profile_url (Union[Unset, str]):
        thumbnail (Union[Unset, str]):
    """

    agent_id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    agency_name: Union[Unset, str] = UNSET
    suburb: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    profile_url: Union[Unset, str] = UNSET
    thumbnail: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        agent_id = self.agent_id

        name = self.name

        agency_name = self.agency_name

        suburb = self.suburb

        state = self.state

        profile_url = self.profile_url

        thumbnail = self.thumbnail

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if agent_id is not UNSET:
            field_dict["agentId"] = agent_id
        if name is not UNSET:
            field_dict["name"] = name
        if agency_name is not UNSET:
            field_dict["agencyName"] = agency_name
        if suburb is not UNSET:
            field_dict["suburb"] = suburb
        if state is not UNSET:
            field_dict["state"] = state
        if profile_url is not UNSET:
            field_dict["profileUrl"] = profile_url
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        agent_id = d.pop("agentId", UNSET)

        name = d.pop("name", UNSET)

        agency_name = d.pop("agencyName", UNSET)

        suburb = d.pop("suburb", UNSET)

        state = d.pop("state", UNSET)

        profile_url = d.pop("profileUrl", UNSET)

        thumbnail = d.pop("thumbnail", UNSET)

        domain_agent_search_v1_model_auto_suggest_agent_result_dto = cls(
            agent_id=agent_id,
            name=name,
            agency_name=agency_name,
            suburb=suburb,
            state=state,
            profile_url=profile_url,
            thumbnail=thumbnail,
        )

        domain_agent_search_v1_model_auto_suggest_agent_result_dto.additional_properties = d
        return domain_agent_search_v1_model_auto_suggest_agent_result_dto

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
