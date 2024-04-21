from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_search_service_v2_model_domain_search_contracts_v2_inspection import (
        DomainSearchServiceV2ModelDomainSearchContractsV2Inspection,
    )


T = TypeVar("T", bound="DomainSearchServiceV2ModelDomainSearchContractsV2InspectionSchedule")


@_attrs_define
class DomainSearchServiceV2ModelDomainSearchContractsV2InspectionSchedule:
    """
    Attributes:
        by_appointment (Union[Unset, bool]):
        recurring (Union[Unset, bool]):
        times (Union[Unset, List['DomainSearchServiceV2ModelDomainSearchContractsV2Inspection']]):
    """

    by_appointment: Union[Unset, bool] = UNSET
    recurring: Union[Unset, bool] = UNSET
    times: Union[Unset, List["DomainSearchServiceV2ModelDomainSearchContractsV2Inspection"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        by_appointment = self.by_appointment

        recurring = self.recurring

        times: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.times, Unset):
            times = []
            for times_item_data in self.times:
                times_item = times_item_data.to_dict()
                times.append(times_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if by_appointment is not UNSET:
            field_dict["byAppointment"] = by_appointment
        if recurring is not UNSET:
            field_dict["recurring"] = recurring
        if times is not UNSET:
            field_dict["times"] = times

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_search_service_v2_model_domain_search_contracts_v2_inspection import (
            DomainSearchServiceV2ModelDomainSearchContractsV2Inspection,
        )

        d = src_dict.copy()
        by_appointment = d.pop("byAppointment", UNSET)

        recurring = d.pop("recurring", UNSET)

        times = []
        _times = d.pop("times", UNSET)
        for times_item_data in _times or []:
            times_item = DomainSearchServiceV2ModelDomainSearchContractsV2Inspection.from_dict(times_item_data)

            times.append(times_item)

        domain_search_service_v2_model_domain_search_contracts_v2_inspection_schedule = cls(
            by_appointment=by_appointment,
            recurring=recurring,
            times=times,
        )

        domain_search_service_v2_model_domain_search_contracts_v2_inspection_schedule.additional_properties = d
        return domain_search_service_v2_model_domain_search_contracts_v2_inspection_schedule

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
