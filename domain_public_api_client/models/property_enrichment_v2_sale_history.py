from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.property_enrichment_v2_address_basic import PropertyEnrichmentV2AddressBasic
    from ..models.property_enrichment_v2_rent_history_listing import PropertyEnrichmentV2RentHistoryListing
    from ..models.property_enrichment_v2_sale_history_listing import PropertyEnrichmentV2SaleHistoryListing


T = TypeVar("T", bound="PropertyEnrichmentV2SaleHistory")


@_attrs_define
class PropertyEnrichmentV2SaleHistory:
    """
    Attributes:
        property_id (Union[Unset, str]): Unique ID for the property
        address_components (Union[Unset, PropertyEnrichmentV2AddressBasic]): Address of property
        sales_history (Union[Unset, List['PropertyEnrichmentV2SaleHistoryListing']]): An array of the sale histories for
            the listing
        rent_history (Union[Unset, List['PropertyEnrichmentV2RentHistoryListing']]): An array of the rent histories for
            the listing
    """

    property_id: Union[Unset, str] = UNSET
    address_components: Union[Unset, "PropertyEnrichmentV2AddressBasic"] = UNSET
    sales_history: Union[Unset, List["PropertyEnrichmentV2SaleHistoryListing"]] = UNSET
    rent_history: Union[Unset, List["PropertyEnrichmentV2RentHistoryListing"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        property_id = self.property_id

        address_components: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address_components, Unset):
            address_components = self.address_components.to_dict()

        sales_history: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sales_history, Unset):
            sales_history = []
            for sales_history_item_data in self.sales_history:
                sales_history_item = sales_history_item_data.to_dict()
                sales_history.append(sales_history_item)

        rent_history: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rent_history, Unset):
            rent_history = []
            for rent_history_item_data in self.rent_history:
                rent_history_item = rent_history_item_data.to_dict()
                rent_history.append(rent_history_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if property_id is not UNSET:
            field_dict["propertyId"] = property_id
        if address_components is not UNSET:
            field_dict["addressComponents"] = address_components
        if sales_history is not UNSET:
            field_dict["salesHistory"] = sales_history
        if rent_history is not UNSET:
            field_dict["rentHistory"] = rent_history

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.property_enrichment_v2_address_basic import PropertyEnrichmentV2AddressBasic
        from ..models.property_enrichment_v2_rent_history_listing import PropertyEnrichmentV2RentHistoryListing
        from ..models.property_enrichment_v2_sale_history_listing import PropertyEnrichmentV2SaleHistoryListing

        d = src_dict.copy()
        property_id = d.pop("propertyId", UNSET)

        _address_components = d.pop("addressComponents", UNSET)
        address_components: Union[Unset, PropertyEnrichmentV2AddressBasic]
        if isinstance(_address_components, Unset):
            address_components = UNSET
        else:
            address_components = PropertyEnrichmentV2AddressBasic.from_dict(_address_components)

        sales_history = []
        _sales_history = d.pop("salesHistory", UNSET)
        for sales_history_item_data in _sales_history or []:
            sales_history_item = PropertyEnrichmentV2SaleHistoryListing.from_dict(sales_history_item_data)

            sales_history.append(sales_history_item)

        rent_history = []
        _rent_history = d.pop("rentHistory", UNSET)
        for rent_history_item_data in _rent_history or []:
            rent_history_item = PropertyEnrichmentV2RentHistoryListing.from_dict(rent_history_item_data)

            rent_history.append(rent_history_item)

        property_enrichment_v2_sale_history = cls(
            property_id=property_id,
            address_components=address_components,
            sales_history=sales_history,
            rent_history=rent_history,
        )

        property_enrichment_v2_sale_history.additional_properties = d
        return property_enrichment_v2_sale_history

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
