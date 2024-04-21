from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainPublicAdapterWebApiModelsV1ListingsBusinessAdvertiserImages")


@_attrs_define
class DomainPublicAdapterWebApiModelsV1ListingsBusinessAdvertiserImages:
    """Agency images (logos, banners)

    Attributes:
        agency_banner_image_url (Union[Unset, str]): Agency branding banner image URL
        agency_banner_wide_image_url (Union[Unset, str]): Not used
        logo_url (Union[Unset, str]): Agency logo. Note: CRE has two logo sizes.
    """

    agency_banner_image_url: Union[Unset, str] = UNSET
    agency_banner_wide_image_url: Union[Unset, str] = UNSET
    logo_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        agency_banner_image_url = self.agency_banner_image_url

        agency_banner_wide_image_url = self.agency_banner_wide_image_url

        logo_url = self.logo_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if agency_banner_image_url is not UNSET:
            field_dict["agencyBannerImageUrl"] = agency_banner_image_url
        if agency_banner_wide_image_url is not UNSET:
            field_dict["agencyBannerWideImageUrl"] = agency_banner_wide_image_url
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        agency_banner_image_url = d.pop("agencyBannerImageUrl", UNSET)

        agency_banner_wide_image_url = d.pop("agencyBannerWideImageUrl", UNSET)

        logo_url = d.pop("logoUrl", UNSET)

        domain_public_adapter_web_api_models_v1_listings_business_advertiser_images = cls(
            agency_banner_image_url=agency_banner_image_url,
            agency_banner_wide_image_url=agency_banner_wide_image_url,
            logo_url=logo_url,
        )

        domain_public_adapter_web_api_models_v1_listings_business_advertiser_images.additional_properties = d
        return domain_public_adapter_web_api_models_v1_listings_business_advertiser_images

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
