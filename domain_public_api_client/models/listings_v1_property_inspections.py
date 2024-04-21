from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.listings_v1_inspection import ListingsV1Inspection


T = TypeVar("T", bound="ListingsV1PropertyInspections")


@_attrs_define
class ListingsV1PropertyInspections:
    """Property Inspection(s) details

    Attributes:
        inspections (Union[List['ListingsV1Inspection'], None, Unset]): Inspection details for the property. e.g.
            opening and closing times
        past_inspections (Union[List['ListingsV1Inspection'], None, Unset]): Inspection details for the property. e.g.
            opening and closing times
        is_by_appointment_only (Union[None, Unset, bool]): True or False indicating whether the inspection is by
            appointment only
    """

    inspections: Union[List["ListingsV1Inspection"], None, Unset] = UNSET
    past_inspections: Union[List["ListingsV1Inspection"], None, Unset] = UNSET
    is_by_appointment_only: Union[None, Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        inspections: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.inspections, Unset):
            inspections = UNSET
        elif isinstance(self.inspections, list):
            inspections = []
            for inspections_type_0_item_data in self.inspections:
                inspections_type_0_item = inspections_type_0_item_data.to_dict()
                inspections.append(inspections_type_0_item)

        else:
            inspections = self.inspections

        past_inspections: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.past_inspections, Unset):
            past_inspections = UNSET
        elif isinstance(self.past_inspections, list):
            past_inspections = []
            for past_inspections_type_0_item_data in self.past_inspections:
                past_inspections_type_0_item = past_inspections_type_0_item_data.to_dict()
                past_inspections.append(past_inspections_type_0_item)

        else:
            past_inspections = self.past_inspections

        is_by_appointment_only: Union[None, Unset, bool]
        if isinstance(self.is_by_appointment_only, Unset):
            is_by_appointment_only = UNSET
        else:
            is_by_appointment_only = self.is_by_appointment_only

        field_dict: Dict[str, Any] = {}
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
        from ..models.listings_v1_inspection import ListingsV1Inspection

        d = src_dict.copy()

        def _parse_inspections(data: object) -> Union[List["ListingsV1Inspection"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                inspections_type_0 = []
                _inspections_type_0 = data
                for inspections_type_0_item_data in _inspections_type_0:
                    inspections_type_0_item = ListingsV1Inspection.from_dict(inspections_type_0_item_data)

                    inspections_type_0.append(inspections_type_0_item)

                return inspections_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ListingsV1Inspection"], None, Unset], data)

        inspections = _parse_inspections(d.pop("inspections", UNSET))

        def _parse_past_inspections(data: object) -> Union[List["ListingsV1Inspection"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                past_inspections_type_0 = []
                _past_inspections_type_0 = data
                for past_inspections_type_0_item_data in _past_inspections_type_0:
                    past_inspections_type_0_item = ListingsV1Inspection.from_dict(past_inspections_type_0_item_data)

                    past_inspections_type_0.append(past_inspections_type_0_item)

                return past_inspections_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["ListingsV1Inspection"], None, Unset], data)

        past_inspections = _parse_past_inspections(d.pop("pastInspections", UNSET))

        def _parse_is_by_appointment_only(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_by_appointment_only = _parse_is_by_appointment_only(d.pop("isByAppointmentOnly", UNSET))

        listings_v1_property_inspections = cls(
            inspections=inspections,
            past_inspections=past_inspections,
            is_by_appointment_only=is_by_appointment_only,
        )

        return listings_v1_property_inspections
