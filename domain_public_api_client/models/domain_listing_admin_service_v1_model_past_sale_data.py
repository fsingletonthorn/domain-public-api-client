import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_listing_admin_service_v1_model_past_sale_address import (
        DomainListingAdminServiceV1ModelPastSaleAddress,
    )


T = TypeVar("T", bound="DomainListingAdminServiceV1ModelPastSaleData")


@_attrs_define
class DomainListingAdminServiceV1ModelPastSaleData:
    """Information for past property sales

    Attributes:
        address (Union[Unset, DomainListingAdminServiceV1ModelPastSaleAddress]): Address for past sold listing
        date_of_sale (Union[Unset, datetime.datetime]): Registered date of the sale
        sold_price (Union[Unset, int]): Price property has been sold
    """

    address: Union[Unset, "DomainListingAdminServiceV1ModelPastSaleAddress"] = UNSET
    date_of_sale: Union[Unset, datetime.datetime] = UNSET
    sold_price: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        date_of_sale: Union[Unset, str] = UNSET
        if not isinstance(self.date_of_sale, Unset):
            date_of_sale = self.date_of_sale.isoformat()

        sold_price = self.sold_price

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if date_of_sale is not UNSET:
            field_dict["dateOfSale"] = date_of_sale
        if sold_price is not UNSET:
            field_dict["soldPrice"] = sold_price

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_listing_admin_service_v1_model_past_sale_address import (
            DomainListingAdminServiceV1ModelPastSaleAddress,
        )

        d = src_dict.copy()
        _address = d.pop("address", UNSET)
        address: Union[Unset, DomainListingAdminServiceV1ModelPastSaleAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = DomainListingAdminServiceV1ModelPastSaleAddress.from_dict(_address)

        _date_of_sale = d.pop("dateOfSale", UNSET)
        date_of_sale: Union[Unset, datetime.datetime]
        if isinstance(_date_of_sale, Unset):
            date_of_sale = UNSET
        else:
            date_of_sale = isoparse(_date_of_sale)

        sold_price = d.pop("soldPrice", UNSET)

        domain_listing_admin_service_v1_model_past_sale_data = cls(
            address=address,
            date_of_sale=date_of_sale,
            sold_price=sold_price,
        )

        domain_listing_admin_service_v1_model_past_sale_data.additional_properties = d
        return domain_listing_admin_service_v1_model_past_sale_data

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
