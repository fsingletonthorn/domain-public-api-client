import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingsV2TenderDetails")


@_attrs_define
class ListingsV2TenderDetails:
    """Tender details

    Attributes:
        tender_recipient_name (Union[None, Unset, str]): Tender recipient name
        tender_address (Union[None, Unset, str]): Tender address
        tender_end_date (Union[None, Unset, datetime.datetime]): Tender closing date. DateTime is in a local timezone.
    """

    tender_recipient_name: Union[None, Unset, str] = UNSET
    tender_address: Union[None, Unset, str] = UNSET
    tender_end_date: Union[None, Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        tender_recipient_name: Union[None, Unset, str]
        if isinstance(self.tender_recipient_name, Unset):
            tender_recipient_name = UNSET
        else:
            tender_recipient_name = self.tender_recipient_name

        tender_address: Union[None, Unset, str]
        if isinstance(self.tender_address, Unset):
            tender_address = UNSET
        else:
            tender_address = self.tender_address

        tender_end_date: Union[None, Unset, str]
        if isinstance(self.tender_end_date, Unset):
            tender_end_date = UNSET
        elif isinstance(self.tender_end_date, datetime.datetime):
            tender_end_date = self.tender_end_date.isoformat()
        else:
            tender_end_date = self.tender_end_date

        field_dict: Dict[str, Any] = {}
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

        def _parse_tender_recipient_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        tender_recipient_name = _parse_tender_recipient_name(d.pop("tenderRecipientName", UNSET))

        def _parse_tender_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        tender_address = _parse_tender_address(d.pop("tenderAddress", UNSET))

        def _parse_tender_end_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                tender_end_date_type_0 = isoparse(data)

                return tender_end_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        tender_end_date = _parse_tender_end_date(d.pop("tenderEndDate", UNSET))

        listings_v2_tender_details = cls(
            tender_recipient_name=tender_recipient_name,
            tender_address=tender_address,
            tender_end_date=tender_end_date,
        )

        return listings_v2_tender_details
