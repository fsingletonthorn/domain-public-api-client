from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.listing_admin_v2_commercial_price_gst_option_type import ListingAdminV2CommercialPriceGstOptionType
from ..models.listing_admin_v2_commercial_price_price_type import ListingAdminV2CommercialPricePriceType
from ..models.listing_admin_v2_commercial_price_price_unit_type import ListingAdminV2CommercialPricePriceUnitType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingAdminV2CommercialPrice")


@_attrs_define
class ListingAdminV2CommercialPrice:
    """Commercial component for price

    Attributes:
        from_ (int): Lowest price the property is expected to sell/rent for to set search price. For a fixed price, set
            this value the same as To
        to (int): Highest price the property is expected to sell/rent for to set search price.
            For a fixed price, set this value the same as From
        price_unit_type (Union[Unset, ListingAdminV2CommercialPricePriceUnitType]): Price Unit type. Can have the values
            "TotalAmount", "PerSqm". Default = "TotalAmount"
        price_type (Union[Unset, ListingAdminV2CommercialPricePriceType]): Type can have the values "Gross", "Net".
            Default "Net"
        gst_option_type (Union[Unset, ListingAdminV2CommercialPriceGstOptionType]): GST Option Type. Can have the values
            "NA", "Inc", "Ex". Default = "NA"
        price_reduction (Union[Unset, bool]): Indicates if this property is under price reduction
        display_text (Union[Unset, str]): When provided this will be shown instead of the price range, e.g.: "Offers
            over $450K considered"
    """

    from_: int
    to: int
    price_unit_type: Union[Unset, ListingAdminV2CommercialPricePriceUnitType] = UNSET
    price_type: Union[Unset, ListingAdminV2CommercialPricePriceType] = UNSET
    gst_option_type: Union[Unset, ListingAdminV2CommercialPriceGstOptionType] = UNSET
    price_reduction: Union[Unset, bool] = UNSET
    display_text: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from_ = self.from_

        to = self.to

        price_unit_type: Union[Unset, str] = UNSET
        if not isinstance(self.price_unit_type, Unset):
            price_unit_type = self.price_unit_type.value

        price_type: Union[Unset, str] = UNSET
        if not isinstance(self.price_type, Unset):
            price_type = self.price_type.value

        gst_option_type: Union[Unset, str] = UNSET
        if not isinstance(self.gst_option_type, Unset):
            gst_option_type = self.gst_option_type.value

        price_reduction = self.price_reduction

        display_text = self.display_text

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from": from_,
                "to": to,
            }
        )
        if price_unit_type is not UNSET:
            field_dict["priceUnitType"] = price_unit_type
        if price_type is not UNSET:
            field_dict["priceType"] = price_type
        if gst_option_type is not UNSET:
            field_dict["gstOptionType"] = gst_option_type
        if price_reduction is not UNSET:
            field_dict["priceReduction"] = price_reduction
        if display_text is not UNSET:
            field_dict["displayText"] = display_text

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        from_ = d.pop("from")

        to = d.pop("to")

        _price_unit_type = d.pop("priceUnitType", UNSET)
        price_unit_type: Union[Unset, ListingAdminV2CommercialPricePriceUnitType]
        if isinstance(_price_unit_type, Unset):
            price_unit_type = UNSET
        else:
            price_unit_type = ListingAdminV2CommercialPricePriceUnitType(_price_unit_type)

        _price_type = d.pop("priceType", UNSET)
        price_type: Union[Unset, ListingAdminV2CommercialPricePriceType]
        if isinstance(_price_type, Unset):
            price_type = UNSET
        else:
            price_type = ListingAdminV2CommercialPricePriceType(_price_type)

        _gst_option_type = d.pop("gstOptionType", UNSET)
        gst_option_type: Union[Unset, ListingAdminV2CommercialPriceGstOptionType]
        if isinstance(_gst_option_type, Unset):
            gst_option_type = UNSET
        else:
            gst_option_type = ListingAdminV2CommercialPriceGstOptionType(_gst_option_type)

        price_reduction = d.pop("priceReduction", UNSET)

        display_text = d.pop("displayText", UNSET)

        listing_admin_v2_commercial_price = cls(
            from_=from_,
            to=to,
            price_unit_type=price_unit_type,
            price_type=price_type,
            gst_option_type=gst_option_type,
            price_reduction=price_reduction,
            display_text=display_text,
        )

        listing_admin_v2_commercial_price.additional_properties = d
        return listing_admin_v2_commercial_price

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
