from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domain_listing_admin_service_v1_model_listing_response_process_status import (
    DomainListingAdminServiceV1ModelListingResponseProcessStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainListingAdminServiceV1ModelListingResponse")


@_attrs_define
class DomainListingAdminServiceV1ModelListingResponse:
    """Represent the listing job.

    Attributes:
        process_status (Union[Unset, DomainListingAdminServiceV1ModelListingResponseProcessStatus]): Status of listing
            been processed
        id (Union[Unset, str]): The listing job Id.   This job will eventually be processed.
        agency_id (Union[Unset, int]): Agency Id from Domain.
        provider_id (Union[Unset, str]): Provider Id for the agency.
        provider_ad_id (Union[Unset, str]): Listing identifier provided by CRM.
        version_id (Union[Unset, str]): Version Id
    """

    process_status: Union[Unset, DomainListingAdminServiceV1ModelListingResponseProcessStatus] = UNSET
    id: Union[Unset, str] = UNSET
    agency_id: Union[Unset, int] = UNSET
    provider_id: Union[Unset, str] = UNSET
    provider_ad_id: Union[Unset, str] = UNSET
    version_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        process_status: Union[Unset, str] = UNSET
        if not isinstance(self.process_status, Unset):
            process_status = self.process_status.value

        id = self.id

        agency_id = self.agency_id

        provider_id = self.provider_id

        provider_ad_id = self.provider_ad_id

        version_id = self.version_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if process_status is not UNSET:
            field_dict["processStatus"] = process_status
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

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _process_status = d.pop("processStatus", UNSET)
        process_status: Union[Unset, DomainListingAdminServiceV1ModelListingResponseProcessStatus]
        if isinstance(_process_status, Unset):
            process_status = UNSET
        else:
            process_status = DomainListingAdminServiceV1ModelListingResponseProcessStatus(_process_status)

        id = d.pop("id", UNSET)

        agency_id = d.pop("agencyId", UNSET)

        provider_id = d.pop("providerId", UNSET)

        provider_ad_id = d.pop("providerAdId", UNSET)

        version_id = d.pop("versionId", UNSET)

        domain_listing_admin_service_v1_model_listing_response = cls(
            process_status=process_status,
            id=id,
            agency_id=agency_id,
            provider_id=provider_id,
            provider_ad_id=provider_ad_id,
            version_id=version_id,
        )

        domain_listing_admin_service_v1_model_listing_response.additional_properties = d
        return domain_listing_admin_service_v1_model_listing_response

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
