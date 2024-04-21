import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainListingAdminServiceV1ModelReportVersion")


@_attrs_define
class DomainListingAdminServiceV1ModelReportVersion:
    """Report Version

    Attributes:
        operations (Union[Unset, List[str]]): Operations performed on a completed version ['none', 'dataReceived',
            'processStarted', 'priceValidated', 'geoCoded', 'pdfsProcessed', 'primaryImagesProcessed', 'allImagesProcessed',
            'listingDataSaved', 'listingDeleted', 'reportEmailSent', 'offMarketProcessed', 'listingIndexed',
            'propertyTypesProcessed', 'contactsProcessed', 'messagesPublished', 'listingSentLive', 'listingUpdated',
            'listingRestored', 'allImageSizesProcessed', 'patchProcessed', 'externalSaleProcessed', 'soiProcessed',
            'duplicateDetection', 'listingMerged', 'supplementaryProcessed', 'listingHeldInMigration',
            'linkedProjectsProcessed', 'linkedListingsProcessed', 'allMediaProcessed', 'projectProcessed',
            'projectDeleted'].
        version_id (Union[Unset, str]): Version Id
        processed_date (Union[Unset, datetime.datetime]): Date this version of data been processed
        data_url (Union[Unset, str]): Url to access s3 file
        process_count (Union[Unset, int]): Retry count
    """

    operations: Union[Unset, List[str]] = UNSET
    version_id: Union[Unset, str] = UNSET
    processed_date: Union[Unset, datetime.datetime] = UNSET
    data_url: Union[Unset, str] = UNSET
    process_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        operations: Union[Unset, List[str]] = UNSET
        if not isinstance(self.operations, Unset):
            operations = self.operations

        version_id = self.version_id

        processed_date: Union[Unset, str] = UNSET
        if not isinstance(self.processed_date, Unset):
            processed_date = self.processed_date.isoformat()

        data_url = self.data_url

        process_count = self.process_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if operations is not UNSET:
            field_dict["operations"] = operations
        if version_id is not UNSET:
            field_dict["versionId"] = version_id
        if processed_date is not UNSET:
            field_dict["processedDate"] = processed_date
        if data_url is not UNSET:
            field_dict["dataUrl"] = data_url
        if process_count is not UNSET:
            field_dict["processCount"] = process_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        operations = cast(List[str], d.pop("operations", UNSET))

        version_id = d.pop("versionId", UNSET)

        _processed_date = d.pop("processedDate", UNSET)
        processed_date: Union[Unset, datetime.datetime]
        if isinstance(_processed_date, Unset):
            processed_date = UNSET
        else:
            processed_date = isoparse(_processed_date)

        data_url = d.pop("dataUrl", UNSET)

        process_count = d.pop("processCount", UNSET)

        domain_listing_admin_service_v1_model_report_version = cls(
            operations=operations,
            version_id=version_id,
            processed_date=processed_date,
            data_url=data_url,
            process_count=process_count,
        )

        domain_listing_admin_service_v1_model_report_version.additional_properties = d
        return domain_listing_admin_service_v1_model_report_version

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
