from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.property_enrichment_v2_address_basic import PropertyEnrichmentV2AddressBasic
    from ..models.property_enrichment_v2_rent_listing_history import PropertyEnrichmentV2RentListingHistory
    from ..models.property_enrichment_v2_sale_listing_history import PropertyEnrichmentV2SaleListingHistory


T = TypeVar("T", bound="PropertyEnrichmentV2PropertyListingResults")


@_attrs_define
class PropertyEnrichmentV2PropertyListingResults:
    """property listing history object

    Attributes:
        property_id (Union[Unset, str]):
        address_components (Union[Unset, PropertyEnrichmentV2AddressBasic]): Address of property
        sales_listing_history (Union[Unset, List['PropertyEnrichmentV2SaleListingHistory']]):
        rent_listing_history (Union[Unset, List['PropertyEnrichmentV2RentListingHistory']]):
    """

    property_id: Union[Unset, str] = UNSET
    address_components: Union[Unset, "PropertyEnrichmentV2AddressBasic"] = UNSET
    sales_listing_history: Union[Unset, List["PropertyEnrichmentV2SaleListingHistory"]] = UNSET
    rent_listing_history: Union[Unset, List["PropertyEnrichmentV2RentListingHistory"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        property_id = self.property_id

        address_components: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address_components, Unset):
            address_components = self.address_components.to_dict()

        sales_listing_history: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sales_listing_history, Unset):
            sales_listing_history = []
            for sales_listing_history_item_data in self.sales_listing_history:
                sales_listing_history_item = sales_listing_history_item_data.to_dict()
                sales_listing_history.append(sales_listing_history_item)

        rent_listing_history: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rent_listing_history, Unset):
            rent_listing_history = []
            for rent_listing_history_item_data in self.rent_listing_history:
                rent_listing_history_item = rent_listing_history_item_data.to_dict()
                rent_listing_history.append(rent_listing_history_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if property_id is not UNSET:
            field_dict["propertyId"] = property_id
        if address_components is not UNSET:
            field_dict["addressComponents"] = address_components
        if sales_listing_history is not UNSET:
            field_dict["salesListingHistory"] = sales_listing_history
        if rent_listing_history is not UNSET:
            field_dict["rentListingHistory"] = rent_listing_history

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.property_enrichment_v2_address_basic import PropertyEnrichmentV2AddressBasic
        from ..models.property_enrichment_v2_rent_listing_history import PropertyEnrichmentV2RentListingHistory
        from ..models.property_enrichment_v2_sale_listing_history import PropertyEnrichmentV2SaleListingHistory

        d = src_dict.copy()
        property_id = d.pop("propertyId", UNSET)

        _address_components = d.pop("addressComponents", UNSET)
        address_components: Union[Unset, PropertyEnrichmentV2AddressBasic]
        if isinstance(_address_components, Unset):
            address_components = UNSET
        else:
            address_components = PropertyEnrichmentV2AddressBasic.from_dict(_address_components)

        sales_listing_history = []
        _sales_listing_history = d.pop("salesListingHistory", UNSET)
        for sales_listing_history_item_data in _sales_listing_history or []:
            sales_listing_history_item = PropertyEnrichmentV2SaleListingHistory.from_dict(
                sales_listing_history_item_data
            )

            sales_listing_history.append(sales_listing_history_item)

        rent_listing_history = []
        _rent_listing_history = d.pop("rentListingHistory", UNSET)
        for rent_listing_history_item_data in _rent_listing_history or []:
            rent_listing_history_item = PropertyEnrichmentV2RentListingHistory.from_dict(rent_listing_history_item_data)

            rent_listing_history.append(rent_listing_history_item)

        property_enrichment_v2_property_listing_results = cls(
            property_id=property_id,
            address_components=address_components,
            sales_listing_history=sales_listing_history,
            rent_listing_history=rent_listing_history,
        )

        property_enrichment_v2_property_listing_results.additional_properties = d
        return property_enrichment_v2_property_listing_results

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
