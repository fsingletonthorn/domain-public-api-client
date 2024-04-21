from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_property_report_service_v1_model_property_report_container import (
        DomainPropertyReportServiceV1ModelPropertyReportContainer,
    )
    from ..models.domain_property_report_service_v1_model_washed_location import (
        DomainPropertyReportServiceV1ModelWashedLocation,
    )


T = TypeVar("T", bound="DomainPropertyReportServiceV1ModelPropertyReportGenerationResult")


@_attrs_define
class DomainPropertyReportServiceV1ModelPropertyReportGenerationResult:
    """
    Attributes:
        washed_location (Union[Unset, DomainPropertyReportServiceV1ModelWashedLocation]):
        report (Union[Unset, DomainPropertyReportServiceV1ModelPropertyReportContainer]):
    """

    washed_location: Union[Unset, "DomainPropertyReportServiceV1ModelWashedLocation"] = UNSET
    report: Union[Unset, "DomainPropertyReportServiceV1ModelPropertyReportContainer"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        washed_location: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.washed_location, Unset):
            washed_location = self.washed_location.to_dict()

        report: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.report, Unset):
            report = self.report.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if washed_location is not UNSET:
            field_dict["washedLocation"] = washed_location
        if report is not UNSET:
            field_dict["report"] = report

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_property_report_service_v1_model_property_report_container import (
            DomainPropertyReportServiceV1ModelPropertyReportContainer,
        )
        from ..models.domain_property_report_service_v1_model_washed_location import (
            DomainPropertyReportServiceV1ModelWashedLocation,
        )

        d = src_dict.copy()
        _washed_location = d.pop("washedLocation", UNSET)
        washed_location: Union[Unset, DomainPropertyReportServiceV1ModelWashedLocation]
        if isinstance(_washed_location, Unset):
            washed_location = UNSET
        else:
            washed_location = DomainPropertyReportServiceV1ModelWashedLocation.from_dict(_washed_location)

        _report = d.pop("report", UNSET)
        report: Union[Unset, DomainPropertyReportServiceV1ModelPropertyReportContainer]
        if isinstance(_report, Unset):
            report = UNSET
        else:
            report = DomainPropertyReportServiceV1ModelPropertyReportContainer.from_dict(_report)

        domain_property_report_service_v1_model_property_report_generation_result = cls(
            washed_location=washed_location,
            report=report,
        )

        domain_property_report_service_v1_model_property_report_generation_result.additional_properties = d
        return domain_property_report_service_v1_model_property_report_generation_result

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
