from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainPublicAdapterWebApiModelsV1ListingsBusinessAd")


@_attrs_define
class DomainPublicAdapterWebApiModelsV1ListingsBusinessAd:
    """Listing details

    Attributes:
        ad_type (Union[Unset, str]): Product type
        url (Union[Unset, str]): URL of property details page on CRE website
    """

    ad_type: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ad_type = self.ad_type

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ad_type is not UNSET:
            field_dict["adType"] = ad_type
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ad_type = d.pop("adType", UNSET)

        url = d.pop("url", UNSET)

        domain_public_adapter_web_api_models_v1_listings_business_ad = cls(
            ad_type=ad_type,
            url=url,
        )

        domain_public_adapter_web_api_models_v1_listings_business_ad.additional_properties = d
        return domain_public_adapter_web_api_models_v1_listings_business_ad

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
