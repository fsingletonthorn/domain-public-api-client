import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingTenderDetails")


@_attrs_define
class DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingTenderDetails:
    """
    Attributes:
        tender_recipient_name (Union[Unset, str]):
        tender_address (Union[Unset, str]):
        tender_end_date (Union[Unset, datetime.datetime]):
    """

    tender_recipient_name: Union[Unset, str] = UNSET
    tender_address: Union[Unset, str] = UNSET
    tender_end_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tender_recipient_name = self.tender_recipient_name

        tender_address = self.tender_address

        tender_end_date: Union[Unset, str] = UNSET
        if not isinstance(self.tender_end_date, Unset):
            tender_end_date = self.tender_end_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tender_recipient_name is not UNSET:
            field_dict["tenderRecipientName"] = tender_recipient_name
        if tender_address is not UNSET:
            field_dict["tenderAddress"] = tender_address
        if tender_end_date is not UNSET:
            field_dict["tenderEndDate"] = tender_end_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tender_recipient_name = d.pop("tenderRecipientName", UNSET)

        tender_address = d.pop("tenderAddress", UNSET)

        _tender_end_date = d.pop("tenderEndDate", UNSET)
        tender_end_date: Union[Unset, datetime.datetime]
        if isinstance(_tender_end_date, Unset):
            tender_end_date = UNSET
        else:
            tender_end_date = isoparse(_tender_end_date)

        domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_tender_details = cls(
            tender_recipient_name=tender_recipient_name,
            tender_address=tender_address,
            tender_end_date=tender_end_date,
        )

        domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_tender_details.additional_properties = d
        return domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_tender_details

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
