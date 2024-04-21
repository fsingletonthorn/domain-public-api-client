import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.listings_v1_inspection_recurrence import ListingsV1InspectionRecurrence
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingsV1Inspection")


@_attrs_define
class ListingsV1Inspection:
    """Encapsulates the details of a Listing's Inspection

    Attributes:
        recurrence (Union[Unset, ListingsV1InspectionRecurrence]): Gets or Sets Recurrence
        opening_date_time (Union[None, Unset, datetime.datetime]): Opening date and time of the inspection. e.g.
            2015-01-01T12:00:00.  Not provided by bulk uploaded listings, in these cases refer to the  inspection
            description field. DateTime is in a local timezone.
        closing_date_time (Union[None, Unset, datetime.datetime]): Closing date and time of the inspection. e.g.
            2015-01-01T12:00:00  Not provided by bulk uploaded listings, in these cases refer to the  inspection description
            field. DateTime is in a local timezone.
        description (Union[None, Unset, str]): Description of the inspection provided by the Advertiser.  When listings
            are bulk uploaded, inspection times are provided as a string.  Other inspection details will not be provided
    """

    recurrence: Union[Unset, ListingsV1InspectionRecurrence] = UNSET
    opening_date_time: Union[None, Unset, datetime.datetime] = UNSET
    closing_date_time: Union[None, Unset, datetime.datetime] = UNSET
    description: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        recurrence: Union[Unset, str] = UNSET
        if not isinstance(self.recurrence, Unset):
            recurrence = self.recurrence.value

        opening_date_time: Union[None, Unset, str]
        if isinstance(self.opening_date_time, Unset):
            opening_date_time = UNSET
        elif isinstance(self.opening_date_time, datetime.datetime):
            opening_date_time = self.opening_date_time.isoformat()
        else:
            opening_date_time = self.opening_date_time

        closing_date_time: Union[None, Unset, str]
        if isinstance(self.closing_date_time, Unset):
            closing_date_time = UNSET
        elif isinstance(self.closing_date_time, datetime.datetime):
            closing_date_time = self.closing_date_time.isoformat()
        else:
            closing_date_time = self.closing_date_time

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if recurrence is not UNSET:
            field_dict["recurrence"] = recurrence
        if opening_date_time is not UNSET:
            field_dict["openingDateTime"] = opening_date_time
        if closing_date_time is not UNSET:
            field_dict["closingDateTime"] = closing_date_time
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _recurrence = d.pop("recurrence", UNSET)
        recurrence: Union[Unset, ListingsV1InspectionRecurrence]
        if isinstance(_recurrence, Unset):
            recurrence = UNSET
        else:
            recurrence = ListingsV1InspectionRecurrence(_recurrence)

        def _parse_opening_date_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                opening_date_time_type_0 = isoparse(data)

                return opening_date_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        opening_date_time = _parse_opening_date_time(d.pop("openingDateTime", UNSET))

        def _parse_closing_date_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                closing_date_time_type_0 = isoparse(data)

                return closing_date_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        closing_date_time = _parse_closing_date_time(d.pop("closingDateTime", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        listings_v1_inspection = cls(
            recurrence=recurrence,
            opening_date_time=opening_date_time,
            closing_date_time=closing_date_time,
            description=description,
        )

        return listings_v1_inspection
