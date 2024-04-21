from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_location_profiles_service_v1_model_location_data_sales_growth_list import (
        DomainLocationProfilesServiceV1ModelLocationDataSalesGrowthList,
    )


T = TypeVar("T", bound="DomainLocationProfilesServiceV1ModelLocationDataPropertyCategories")


@_attrs_define
class DomainLocationProfilesServiceV1ModelLocationDataPropertyCategories:
    """
    Attributes:
        luxury_level_price (Union[Unset, float]):
        number_sold (Union[Unset, int]):
        estimated_repayments (Union[Unset, float]):
        for_sale (Union[Unset, int]):
        median_sold_price (Union[Unset, float]):
        median_rent_price (Union[Unset, float]):
        days_on_market (Union[Unset, float]):
        bedrooms (Union[Unset, int]):
        for_rent (Union[Unset, int]):
        entry_level_price (Union[Unset, float]):
        sales_growth_list (Union[Unset, List['DomainLocationProfilesServiceV1ModelLocationDataSalesGrowthList']]):
        auction_clearance_rate (Union[Unset, float]):
        property_category (Union[Unset, str]):
        most_recent_sale (Union[Unset, str]):
    """

    luxury_level_price: Union[Unset, float] = UNSET
    number_sold: Union[Unset, int] = UNSET
    estimated_repayments: Union[Unset, float] = UNSET
    for_sale: Union[Unset, int] = UNSET
    median_sold_price: Union[Unset, float] = UNSET
    median_rent_price: Union[Unset, float] = UNSET
    days_on_market: Union[Unset, float] = UNSET
    bedrooms: Union[Unset, int] = UNSET
    for_rent: Union[Unset, int] = UNSET
    entry_level_price: Union[Unset, float] = UNSET
    sales_growth_list: Union[Unset, List["DomainLocationProfilesServiceV1ModelLocationDataSalesGrowthList"]] = UNSET
    auction_clearance_rate: Union[Unset, float] = UNSET
    property_category: Union[Unset, str] = UNSET
    most_recent_sale: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        luxury_level_price = self.luxury_level_price

        number_sold = self.number_sold

        estimated_repayments = self.estimated_repayments

        for_sale = self.for_sale

        median_sold_price = self.median_sold_price

        median_rent_price = self.median_rent_price

        days_on_market = self.days_on_market

        bedrooms = self.bedrooms

        for_rent = self.for_rent

        entry_level_price = self.entry_level_price

        sales_growth_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sales_growth_list, Unset):
            sales_growth_list = []
            for sales_growth_list_item_data in self.sales_growth_list:
                sales_growth_list_item = sales_growth_list_item_data.to_dict()
                sales_growth_list.append(sales_growth_list_item)

        auction_clearance_rate = self.auction_clearance_rate

        property_category = self.property_category

        most_recent_sale = self.most_recent_sale

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if luxury_level_price is not UNSET:
            field_dict["luxuryLevelPrice"] = luxury_level_price
        if number_sold is not UNSET:
            field_dict["numberSold"] = number_sold
        if estimated_repayments is not UNSET:
            field_dict["estimatedRepayments"] = estimated_repayments
        if for_sale is not UNSET:
            field_dict["forSale"] = for_sale
        if median_sold_price is not UNSET:
            field_dict["medianSoldPrice"] = median_sold_price
        if median_rent_price is not UNSET:
            field_dict["medianRentPrice"] = median_rent_price
        if days_on_market is not UNSET:
            field_dict["daysOnMarket"] = days_on_market
        if bedrooms is not UNSET:
            field_dict["bedrooms"] = bedrooms
        if for_rent is not UNSET:
            field_dict["forRent"] = for_rent
        if entry_level_price is not UNSET:
            field_dict["entryLevelPrice"] = entry_level_price
        if sales_growth_list is not UNSET:
            field_dict["salesGrowthList"] = sales_growth_list
        if auction_clearance_rate is not UNSET:
            field_dict["auctionClearanceRate"] = auction_clearance_rate
        if property_category is not UNSET:
            field_dict["propertyCategory"] = property_category
        if most_recent_sale is not UNSET:
            field_dict["mostRecentSale"] = most_recent_sale

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_location_profiles_service_v1_model_location_data_sales_growth_list import (
            DomainLocationProfilesServiceV1ModelLocationDataSalesGrowthList,
        )

        d = src_dict.copy()
        luxury_level_price = d.pop("luxuryLevelPrice", UNSET)

        number_sold = d.pop("numberSold", UNSET)

        estimated_repayments = d.pop("estimatedRepayments", UNSET)

        for_sale = d.pop("forSale", UNSET)

        median_sold_price = d.pop("medianSoldPrice", UNSET)

        median_rent_price = d.pop("medianRentPrice", UNSET)

        days_on_market = d.pop("daysOnMarket", UNSET)

        bedrooms = d.pop("bedrooms", UNSET)

        for_rent = d.pop("forRent", UNSET)

        entry_level_price = d.pop("entryLevelPrice", UNSET)

        sales_growth_list = []
        _sales_growth_list = d.pop("salesGrowthList", UNSET)
        for sales_growth_list_item_data in _sales_growth_list or []:
            sales_growth_list_item = DomainLocationProfilesServiceV1ModelLocationDataSalesGrowthList.from_dict(
                sales_growth_list_item_data
            )

            sales_growth_list.append(sales_growth_list_item)

        auction_clearance_rate = d.pop("auctionClearanceRate", UNSET)

        property_category = d.pop("propertyCategory", UNSET)

        most_recent_sale = d.pop("mostRecentSale", UNSET)

        domain_location_profiles_service_v1_model_location_data_property_categories = cls(
            luxury_level_price=luxury_level_price,
            number_sold=number_sold,
            estimated_repayments=estimated_repayments,
            for_sale=for_sale,
            median_sold_price=median_sold_price,
            median_rent_price=median_rent_price,
            days_on_market=days_on_market,
            bedrooms=bedrooms,
            for_rent=for_rent,
            entry_level_price=entry_level_price,
            sales_growth_list=sales_growth_list,
            auction_clearance_rate=auction_clearance_rate,
            property_category=property_category,
            most_recent_sale=most_recent_sale,
        )

        domain_location_profiles_service_v1_model_location_data_property_categories.additional_properties = d
        return domain_location_profiles_service_v1_model_location_data_property_categories

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
