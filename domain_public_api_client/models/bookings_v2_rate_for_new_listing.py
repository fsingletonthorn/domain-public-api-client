import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="BookingsV2RateForNewListing")


@_attrs_define
class BookingsV2RateForNewListing:
    """NewListingRateResponse

    Attributes:
        cost_ex_gst (Union[None, Unset, float]): Gets or Sets CostExGst
        cost_inc_gst (Union[None, Unset, float]): Gets or Sets CostIncGst
        contract_end_date (Union[None, Unset, datetime.datetime]): Gets or Sets ContractEndDate
        message (Union[None, Unset, str]): Gets or Sets Message
        price_matrix_id (Union[None, Unset, int]): Gets or Sets PriceMatrixId
        product_name (Union[None, Unset, str]): Gets or Sets ProductName
    """

    cost_ex_gst: Union[None, Unset, float] = UNSET
    cost_inc_gst: Union[None, Unset, float] = UNSET
    contract_end_date: Union[None, Unset, datetime.datetime] = UNSET
    message: Union[None, Unset, str] = UNSET
    price_matrix_id: Union[None, Unset, int] = UNSET
    product_name: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        cost_ex_gst: Union[None, Unset, float]
        if isinstance(self.cost_ex_gst, Unset):
            cost_ex_gst = UNSET
        else:
            cost_ex_gst = self.cost_ex_gst

        cost_inc_gst: Union[None, Unset, float]
        if isinstance(self.cost_inc_gst, Unset):
            cost_inc_gst = UNSET
        else:
            cost_inc_gst = self.cost_inc_gst

        contract_end_date: Union[None, Unset, str]
        if isinstance(self.contract_end_date, Unset):
            contract_end_date = UNSET
        elif isinstance(self.contract_end_date, datetime.datetime):
            contract_end_date = self.contract_end_date.isoformat()
        else:
            contract_end_date = self.contract_end_date

        message: Union[None, Unset, str]
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        price_matrix_id: Union[None, Unset, int]
        if isinstance(self.price_matrix_id, Unset):
            price_matrix_id = UNSET
        else:
            price_matrix_id = self.price_matrix_id

        product_name: Union[None, Unset, str]
        if isinstance(self.product_name, Unset):
            product_name = UNSET
        else:
            product_name = self.product_name

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if cost_ex_gst is not UNSET:
            field_dict["costExGst"] = cost_ex_gst
        if cost_inc_gst is not UNSET:
            field_dict["costIncGst"] = cost_inc_gst
        if contract_end_date is not UNSET:
            field_dict["contractEndDate"] = contract_end_date
        if message is not UNSET:
            field_dict["message"] = message
        if price_matrix_id is not UNSET:
            field_dict["priceMatrixId"] = price_matrix_id
        if product_name is not UNSET:
            field_dict["productName"] = product_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_cost_ex_gst(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        cost_ex_gst = _parse_cost_ex_gst(d.pop("costExGst", UNSET))

        def _parse_cost_inc_gst(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        cost_inc_gst = _parse_cost_inc_gst(d.pop("costIncGst", UNSET))

        def _parse_contract_end_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                contract_end_date_type_0 = isoparse(data)

                return contract_end_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        contract_end_date = _parse_contract_end_date(d.pop("contractEndDate", UNSET))

        def _parse_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        message = _parse_message(d.pop("message", UNSET))

        def _parse_price_matrix_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        price_matrix_id = _parse_price_matrix_id(d.pop("priceMatrixId", UNSET))

        def _parse_product_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        product_name = _parse_product_name(d.pop("productName", UNSET))

        bookings_v2_rate_for_new_listing = cls(
            cost_ex_gst=cost_ex_gst,
            cost_inc_gst=cost_inc_gst,
            contract_end_date=contract_end_date,
            message=message,
            price_matrix_id=price_matrix_id,
            product_name=product_name,
        )

        return bookings_v2_rate_for_new_listing
