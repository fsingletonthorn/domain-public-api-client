from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domain_listing_admin_service_v1_model_listing_report_process_status import (
    DomainListingAdminServiceV1ModelListingReportProcessStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_listing_admin_service_v1_model_model_event import DomainListingAdminServiceV1ModelModelEvent
    from ..models.domain_listing_admin_service_v1_model_report_version import (
        DomainListingAdminServiceV1ModelReportVersion,
    )


T = TypeVar("T", bound="DomainListingAdminServiceV1ModelListingReport")


@_attrs_define
class DomainListingAdminServiceV1ModelListingReport:
    """Represent current listing status and aggregation of status messages

    Attributes:
        process_status (Union[Unset, DomainListingAdminServiceV1ModelListingReportProcessStatus]): Status of listing
            been processed  * Queued - We received request  * Processing - Request been processed  * Processed - Successful
            processed request  * Failed - Processing failed  * Error - Individual errors encountered
        agency_id (Union[Unset, int]): AgencyId from Domain
        provider_id (Union[Unset, str]): ProviderId for the agency
        provider_ad_id (Union[Unset, str]): Listing identifier provided by CRM
        ad_id (Union[Unset, List[int]]): Advertisement Id from domain
        quality_score (Union[Unset, int]): Quality score of the listing, based on data completeness
        events (Union[Unset, List['DomainListingAdminServiceV1ModelModelEvent']]): All Events associated with this
            processing request
        versions (Union[Unset, List['DomainListingAdminServiceV1ModelReportVersion']]): version list
    """

    process_status: Union[Unset, DomainListingAdminServiceV1ModelListingReportProcessStatus] = UNSET
    agency_id: Union[Unset, int] = UNSET
    provider_id: Union[Unset, str] = UNSET
    provider_ad_id: Union[Unset, str] = UNSET
    ad_id: Union[Unset, List[int]] = UNSET
    quality_score: Union[Unset, int] = UNSET
    events: Union[Unset, List["DomainListingAdminServiceV1ModelModelEvent"]] = UNSET
    versions: Union[Unset, List["DomainListingAdminServiceV1ModelReportVersion"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        process_status: Union[Unset, str] = UNSET
        if not isinstance(self.process_status, Unset):
            process_status = self.process_status.value

        agency_id = self.agency_id

        provider_id = self.provider_id

        provider_ad_id = self.provider_ad_id

        ad_id: Union[Unset, List[int]] = UNSET
        if not isinstance(self.ad_id, Unset):
            ad_id = self.ad_id

        quality_score = self.quality_score

        events: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()
                events.append(events_item)

        versions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.versions, Unset):
            versions = []
            for versions_item_data in self.versions:
                versions_item = versions_item_data.to_dict()
                versions.append(versions_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if process_status is not UNSET:
            field_dict["processStatus"] = process_status
        if agency_id is not UNSET:
            field_dict["agencyId"] = agency_id
        if provider_id is not UNSET:
            field_dict["providerId"] = provider_id
        if provider_ad_id is not UNSET:
            field_dict["providerAdId"] = provider_ad_id
        if ad_id is not UNSET:
            field_dict["adId"] = ad_id
        if quality_score is not UNSET:
            field_dict["qualityScore"] = quality_score
        if events is not UNSET:
            field_dict["events"] = events
        if versions is not UNSET:
            field_dict["versions"] = versions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_listing_admin_service_v1_model_model_event import (
            DomainListingAdminServiceV1ModelModelEvent,
        )
        from ..models.domain_listing_admin_service_v1_model_report_version import (
            DomainListingAdminServiceV1ModelReportVersion,
        )

        d = src_dict.copy()
        _process_status = d.pop("processStatus", UNSET)
        process_status: Union[Unset, DomainListingAdminServiceV1ModelListingReportProcessStatus]
        if isinstance(_process_status, Unset):
            process_status = UNSET
        else:
            process_status = DomainListingAdminServiceV1ModelListingReportProcessStatus(_process_status)

        agency_id = d.pop("agencyId", UNSET)

        provider_id = d.pop("providerId", UNSET)

        provider_ad_id = d.pop("providerAdId", UNSET)

        ad_id = cast(List[int], d.pop("adId", UNSET))

        quality_score = d.pop("qualityScore", UNSET)

        events = []
        _events = d.pop("events", UNSET)
        for events_item_data in _events or []:
            events_item = DomainListingAdminServiceV1ModelModelEvent.from_dict(events_item_data)

            events.append(events_item)

        versions = []
        _versions = d.pop("versions", UNSET)
        for versions_item_data in _versions or []:
            versions_item = DomainListingAdminServiceV1ModelReportVersion.from_dict(versions_item_data)

            versions.append(versions_item)

        domain_listing_admin_service_v1_model_listing_report = cls(
            process_status=process_status,
            agency_id=agency_id,
            provider_id=provider_id,
            provider_ad_id=provider_ad_id,
            ad_id=ad_id,
            quality_score=quality_score,
            events=events,
            versions=versions,
        )

        domain_listing_admin_service_v1_model_listing_report.additional_properties = d
        return domain_listing_admin_service_v1_model_listing_report

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
