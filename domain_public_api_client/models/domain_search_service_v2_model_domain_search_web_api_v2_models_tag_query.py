from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domain_search_service_v2_model_domain_search_web_api_v2_models_tag_query_criteria import (
    DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsTagQueryCriteria,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsTagQuery")


@_attrs_define
class DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsTagQuery:
    """
    Attributes:
        criteria (Union[Unset, DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsTagQueryCriteria]):
        tag (Union[Unset, str]):
    """

    criteria: Union[Unset, DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsTagQueryCriteria] = UNSET
    tag: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        criteria: Union[Unset, str] = UNSET
        if not isinstance(self.criteria, Unset):
            criteria = self.criteria.value

        tag = self.tag

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if criteria is not UNSET:
            field_dict["criteria"] = criteria
        if tag is not UNSET:
            field_dict["tag"] = tag

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _criteria = d.pop("criteria", UNSET)
        criteria: Union[Unset, DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsTagQueryCriteria]
        if isinstance(_criteria, Unset):
            criteria = UNSET
        else:
            criteria = DomainSearchServiceV2ModelDomainSearchWebApiV2ModelsTagQueryCriteria(_criteria)

        tag = d.pop("tag", UNSET)

        domain_search_service_v2_model_domain_search_web_api_v2_models_tag_query = cls(
            criteria=criteria,
            tag=tag,
        )

        domain_search_service_v2_model_domain_search_web_api_v2_models_tag_query.additional_properties = d
        return domain_search_service_v2_model_domain_search_web_api_v2_models_tag_query

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
