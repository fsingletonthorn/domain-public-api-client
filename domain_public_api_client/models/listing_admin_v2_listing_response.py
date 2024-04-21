from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.listing_admin_v2_listing_response_process_status import ListingAdminV2ListingResponseProcessStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingAdminV2ListingResponse")


@_attrs_define
class ListingAdminV2ListingResponse:
    """Represent the listing job.

    Attributes:
        id (Union[Unset, str]): The listing job Id.
            This job will eventually be processed.
        agency_id (Union[Unset, int]): Agency Id from Domain.
        provider_id (Union[Unset, str]): Provider Id for the agency.
        provider_ad_id (Union[Unset, str]): Listing identifier provided by CRM.
        version_id (Union[Unset, str]): Version Id
        process_status (Union[Unset, ListingAdminV2ListingResponseProcessStatus]): Status of listing been processed
    """

    id: Union[Unset, str] = UNSET
    agency_id: Union[Unset, int] = UNSET
    provider_id: Union[Unset, str] = UNSET
    provider_ad_id: Union[Unset, str] = UNSET
    version_id: Union[Unset, str] = UNSET
    process_status: Union[Unset, ListingAdminV2ListingResponseProcessStatus] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        agency_id = self.agency_id

        provider_id = self.provider_id

        provider_ad_id = self.provider_ad_id

        version_id = self.version_id

        process_status: Union[Unset, str] = UNSET
        if not isinstance(self.process_status, Unset):
            process_status = self.process_status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if agency_id is not UNSET:
            field_dict["agencyId"] = agency_id
        if provider_id is not UNSET:
            field_dict["providerId"] = provider_id
        if provider_ad_id is not UNSET:
            field_dict["providerAdId"] = provider_ad_id
        if version_id is not UNSET:
            field_dict["versionId"] = version_id
        if process_status is not UNSET:
            field_dict["processStatus"] = process_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        agency_id = d.pop("agencyId", UNSET)

        provider_id = d.pop("providerId", UNSET)

        provider_ad_id = d.pop("providerAdId", UNSET)

        version_id = d.pop("versionId", UNSET)

        _process_status = d.pop("processStatus", UNSET)
        process_status: Union[Unset, ListingAdminV2ListingResponseProcessStatus]
        if isinstance(_process_status, Unset):
            process_status = UNSET
        else:
            process_status = ListingAdminV2ListingResponseProcessStatus(_process_status)

        listing_admin_v2_listing_response = cls(
            id=id,
            agency_id=agency_id,
            provider_id=provider_id,
            provider_ad_id=provider_ad_id,
            version_id=version_id,
            process_status=process_status,
        )

        listing_admin_v2_listing_response.additional_properties = d
        return listing_admin_v2_listing_response

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
