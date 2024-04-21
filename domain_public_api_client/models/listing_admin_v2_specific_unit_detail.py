from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.listing_admin_v2_specific_unit_detail_occupancy import ListingAdminV2SpecificUnitDetailOccupancy
from ..models.listing_admin_v2_specific_unit_detail_price_unit import ListingAdminV2SpecificUnitDetailPriceUnit
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingAdminV2SpecificUnitDetail")


@_attrs_define
class ListingAdminV2SpecificUnitDetail:
    """offered units details

    Attributes:
        name (Union[Unset, str]): Unit number
        size (Union[Unset, int]): Unit size
        price (Union[Unset, float]): Unit price
        notes (Union[Unset, str]): Additional notes
        is_sold_or_leased (Union[Unset, bool]): Is it available?
        occupancy (Union[Unset, ListingAdminV2SpecificUnitDetailOccupancy]): Occupancy type
        price_unit (Union[Unset, ListingAdminV2SpecificUnitDetailPriceUnit]): Price unit type
        lease_price_for_saleor_lease (Union[Unset, float]): Lease price for sale or lease
    """

    name: Union[Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    price: Union[Unset, float] = UNSET
    notes: Union[Unset, str] = UNSET
    is_sold_or_leased: Union[Unset, bool] = UNSET
    occupancy: Union[Unset, ListingAdminV2SpecificUnitDetailOccupancy] = UNSET
    price_unit: Union[Unset, ListingAdminV2SpecificUnitDetailPriceUnit] = UNSET
    lease_price_for_saleor_lease: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name

        size = self.size

        price = self.price

        notes = self.notes

        is_sold_or_leased = self.is_sold_or_leased

        occupancy: Union[Unset, str] = UNSET
        if not isinstance(self.occupancy, Unset):
            occupancy = self.occupancy.value

        price_unit: Union[Unset, str] = UNSET
        if not isinstance(self.price_unit, Unset):
            price_unit = self.price_unit.value

        lease_price_for_saleor_lease = self.lease_price_for_saleor_lease

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if size is not UNSET:
            field_dict["size"] = size
        if price is not UNSET:
            field_dict["price"] = price
        if notes is not UNSET:
            field_dict["notes"] = notes
        if is_sold_or_leased is not UNSET:
            field_dict["isSoldOrLeased"] = is_sold_or_leased
        if occupancy is not UNSET:
            field_dict["occupancy"] = occupancy
        if price_unit is not UNSET:
            field_dict["priceUnit"] = price_unit
        if lease_price_for_saleor_lease is not UNSET:
            field_dict["leasePriceForSaleorLease"] = lease_price_for_saleor_lease

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        size = d.pop("size", UNSET)

        price = d.pop("price", UNSET)

        notes = d.pop("notes", UNSET)

        is_sold_or_leased = d.pop("isSoldOrLeased", UNSET)

        _occupancy = d.pop("occupancy", UNSET)
        occupancy: Union[Unset, ListingAdminV2SpecificUnitDetailOccupancy]
        if isinstance(_occupancy, Unset):
            occupancy = UNSET
        else:
            occupancy = ListingAdminV2SpecificUnitDetailOccupancy(_occupancy)

        _price_unit = d.pop("priceUnit", UNSET)
        price_unit: Union[Unset, ListingAdminV2SpecificUnitDetailPriceUnit]
        if isinstance(_price_unit, Unset):
            price_unit = UNSET
        else:
            price_unit = ListingAdminV2SpecificUnitDetailPriceUnit(_price_unit)

        lease_price_for_saleor_lease = d.pop("leasePriceForSaleorLease", UNSET)

        listing_admin_v2_specific_unit_detail = cls(
            name=name,
            size=size,
            price=price,
            notes=notes,
            is_sold_or_leased=is_sold_or_leased,
            occupancy=occupancy,
            price_unit=price_unit,
            lease_price_for_saleor_lease=lease_price_for_saleor_lease,
        )

        listing_admin_v2_specific_unit_detail.additional_properties = d
        return listing_admin_v2_specific_unit_detail

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
