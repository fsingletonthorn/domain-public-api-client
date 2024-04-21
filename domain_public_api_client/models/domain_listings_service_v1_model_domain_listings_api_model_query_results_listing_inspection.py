import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_inspection_recurrence import (
    DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingInspectionRecurrence,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingInspection")


@_attrs_define
class DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingInspection:
    """
    Attributes:
        recurrence (Union[Unset,
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingInspectionRecurrence]):
        closing_date_time (Union[Unset, datetime.datetime]):
        description (Union[Unset, str]):
        opening_date_time (Union[Unset, datetime.datetime]):
    """

    recurrence: Union[
        Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingInspectionRecurrence
    ] = UNSET
    closing_date_time: Union[Unset, datetime.datetime] = UNSET
    description: Union[Unset, str] = UNSET
    opening_date_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        recurrence: Union[Unset, str] = UNSET
        if not isinstance(self.recurrence, Unset):
            recurrence = self.recurrence.value

        closing_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.closing_date_time, Unset):
            closing_date_time = self.closing_date_time.isoformat()

        description = self.description

        opening_date_time: Union[Unset, str] = UNSET
        if not isinstance(self.opening_date_time, Unset):
            opening_date_time = self.opening_date_time.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if recurrence is not UNSET:
            field_dict["recurrence"] = recurrence
        if closing_date_time is not UNSET:
            field_dict["closingDateTime"] = closing_date_time
        if description is not UNSET:
            field_dict["description"] = description
        if opening_date_time is not UNSET:
            field_dict["openingDateTime"] = opening_date_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _recurrence = d.pop("recurrence", UNSET)
        recurrence: Union[
            Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingInspectionRecurrence
        ]
        if isinstance(_recurrence, Unset):
            recurrence = UNSET
        else:
            recurrence = DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingInspectionRecurrence(
                _recurrence
            )

        _closing_date_time = d.pop("closingDateTime", UNSET)
        closing_date_time: Union[Unset, datetime.datetime]
        if isinstance(_closing_date_time, Unset):
            closing_date_time = UNSET
        else:
            closing_date_time = isoparse(_closing_date_time)

        description = d.pop("description", UNSET)

        _opening_date_time = d.pop("openingDateTime", UNSET)
        opening_date_time: Union[Unset, datetime.datetime]
        if isinstance(_opening_date_time, Unset):
            opening_date_time = UNSET
        else:
            opening_date_time = isoparse(_opening_date_time)

        domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_inspection = cls(
            recurrence=recurrence,
            closing_date_time=closing_date_time,
            description=description,
            opening_date_time=opening_date_time,
        )

        domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_inspection.additional_properties = d
        return domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_inspection

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
