from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_inspection import (
        DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingInspection,
    )


T = TypeVar("T", bound="DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPropertyInspections")


@_attrs_define
class DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPropertyInspections:
    """
    Attributes:
        inspections (Union[Unset,
            List['DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingInspection']]):
        past_inspections (Union[Unset,
            List['DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingInspection']]):
        is_by_appointment_only (Union[Unset, bool]):
    """

    inspections: Union[
        Unset, List["DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingInspection"]
    ] = UNSET
    past_inspections: Union[
        Unset, List["DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingInspection"]
    ] = UNSET
    is_by_appointment_only: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        inspections: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.inspections, Unset):
            inspections = []
            for inspections_item_data in self.inspections:
                inspections_item = inspections_item_data.to_dict()
                inspections.append(inspections_item)

        past_inspections: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.past_inspections, Unset):
            past_inspections = []
            for past_inspections_item_data in self.past_inspections:
                past_inspections_item = past_inspections_item_data.to_dict()
                past_inspections.append(past_inspections_item)

        is_by_appointment_only = self.is_by_appointment_only

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inspections is not UNSET:
            field_dict["inspections"] = inspections
        if past_inspections is not UNSET:
            field_dict["pastInspections"] = past_inspections
        if is_by_appointment_only is not UNSET:
            field_dict["isByAppointmentOnly"] = is_by_appointment_only

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_inspection import (
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingInspection,
        )

        d = src_dict.copy()
        inspections = []
        _inspections = d.pop("inspections", UNSET)
        for inspections_item_data in _inspections or []:
            inspections_item = (
                DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingInspection.from_dict(
                    inspections_item_data
                )
            )

            inspections.append(inspections_item)

        past_inspections = []
        _past_inspections = d.pop("pastInspections", UNSET)
        for past_inspections_item_data in _past_inspections or []:
            past_inspections_item = (
                DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingInspection.from_dict(
                    past_inspections_item_data
                )
            )

            past_inspections.append(past_inspections_item)

        is_by_appointment_only = d.pop("isByAppointmentOnly", UNSET)

        domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_property_inspections = cls(
            inspections=inspections,
            past_inspections=past_inspections,
            is_by_appointment_only=is_by_appointment_only,
        )

        domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_property_inspections.additional_properties = d
        return domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_property_inspections

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
