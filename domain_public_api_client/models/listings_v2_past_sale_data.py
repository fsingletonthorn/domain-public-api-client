from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingsV2PastSaleData")


@_attrs_define
class ListingsV2PastSaleData:
    """Information for past property sales

    Attributes:
        unit_number (Union[None, Unset, str]): Property unit number
        street_number (Union[None, Unset, str]): Property street number
        street (Union[None, Unset, str]): Property Street name
        suburb (Union[None, Unset, str]): Property suburb name
        postcode (Union[None, Unset, str]): Property postcode
        state (Union[None, Unset, str]): Property state
        display_address (Union[None, Unset, str]): display formatted address
        date_of_sale (Union[None, Unset, str]): Registered date of the sale
        sold_price (Union[None, Unset, int]): Property sold price
    """

    unit_number: Union[None, Unset, str] = UNSET
    street_number: Union[None, Unset, str] = UNSET
    street: Union[None, Unset, str] = UNSET
    suburb: Union[None, Unset, str] = UNSET
    postcode: Union[None, Unset, str] = UNSET
    state: Union[None, Unset, str] = UNSET
    display_address: Union[None, Unset, str] = UNSET
    date_of_sale: Union[None, Unset, str] = UNSET
    sold_price: Union[None, Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        unit_number: Union[None, Unset, str]
        if isinstance(self.unit_number, Unset):
            unit_number = UNSET
        else:
            unit_number = self.unit_number

        street_number: Union[None, Unset, str]
        if isinstance(self.street_number, Unset):
            street_number = UNSET
        else:
            street_number = self.street_number

        street: Union[None, Unset, str]
        if isinstance(self.street, Unset):
            street = UNSET
        else:
            street = self.street

        suburb: Union[None, Unset, str]
        if isinstance(self.suburb, Unset):
            suburb = UNSET
        else:
            suburb = self.suburb

        postcode: Union[None, Unset, str]
        if isinstance(self.postcode, Unset):
            postcode = UNSET
        else:
            postcode = self.postcode

        state: Union[None, Unset, str]
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        display_address: Union[None, Unset, str]
        if isinstance(self.display_address, Unset):
            display_address = UNSET
        else:
            display_address = self.display_address

        date_of_sale: Union[None, Unset, str]
        if isinstance(self.date_of_sale, Unset):
            date_of_sale = UNSET
        else:
            date_of_sale = self.date_of_sale

        sold_price: Union[None, Unset, int]
        if isinstance(self.sold_price, Unset):
            sold_price = UNSET
        else:
            sold_price = self.sold_price

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if unit_number is not UNSET:
            field_dict["unitNumber"] = unit_number
        if street_number is not UNSET:
            field_dict["streetNumber"] = street_number
        if street is not UNSET:
            field_dict["street"] = street
        if suburb is not UNSET:
            field_dict["suburb"] = suburb
        if postcode is not UNSET:
            field_dict["postcode"] = postcode
        if state is not UNSET:
            field_dict["state"] = state
        if display_address is not UNSET:
            field_dict["displayAddress"] = display_address
        if date_of_sale is not UNSET:
            field_dict["dateOfSale"] = date_of_sale
        if sold_price is not UNSET:
            field_dict["soldPrice"] = sold_price

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_unit_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        unit_number = _parse_unit_number(d.pop("unitNumber", UNSET))

        def _parse_street_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        street_number = _parse_street_number(d.pop("streetNumber", UNSET))

        def _parse_street(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        street = _parse_street(d.pop("street", UNSET))

        def _parse_suburb(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        suburb = _parse_suburb(d.pop("suburb", UNSET))

        def _parse_postcode(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        postcode = _parse_postcode(d.pop("postcode", UNSET))

        def _parse_state(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        state = _parse_state(d.pop("state", UNSET))

        def _parse_display_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        display_address = _parse_display_address(d.pop("displayAddress", UNSET))

        def _parse_date_of_sale(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        date_of_sale = _parse_date_of_sale(d.pop("dateOfSale", UNSET))

        def _parse_sold_price(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        sold_price = _parse_sold_price(d.pop("soldPrice", UNSET))

        listings_v2_past_sale_data = cls(
            unit_number=unit_number,
            street_number=street_number,
            street=street,
            suburb=suburb,
            postcode=postcode,
            state=state,
            display_address=display_address,
            date_of_sale=date_of_sale,
            sold_price=sold_price,
        )

        return listings_v2_past_sale_data
