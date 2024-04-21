from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.listings_v1_price_details_gst_option import ListingsV1PriceDetailsGstOption
from ..models.listings_v1_price_details_hidden_reasons_type_0_item import ListingsV1PriceDetailsHiddenReasonsType0Item
from ..models.listings_v1_price_details_price_type import ListingsV1PriceDetailsPriceType
from ..models.listings_v1_price_details_price_unit import ListingsV1PriceDetailsPriceUnit
from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingsV1PriceDetails")


@_attrs_define
class ListingsV1PriceDetails:
    """Encapsulates a listing's price information

    Attributes:
        gst_option (Union[Unset, ListingsV1PriceDetailsGstOption]): Gets or Sets GstOption
        price_type (Union[Unset, ListingsV1PriceDetailsPriceType]): Gets or Sets PriceType
        price_unit (Union[Unset, ListingsV1PriceDetailsPriceUnit]): Gets or Sets PriceUnit
        price (Union[None, Unset, float]): Price of the property
        price_from (Union[None, Unset, int]): Price starting range of the property
        price_to (Union[None, Unset, int]): Upper price range of the property
        price_prefix (Union[None, Unset, str]): Display price for the advertisement
        can_display_price (Union[None, Unset, bool]): Flag indicating whether the advertiser has chosen to display the
            property price
        hidden_reasons (Union[List[ListingsV1PriceDetailsHiddenReasonsType0Item], None, Unset]): Reasons when price need
            to be hidden
        display_price (Union[None, Unset, str]): A string provided by the Advertiser representing the
            ByIdListingPriceQueryResult of the Listing e.g. Over $1,000,000   This should be the default price field for
            client to use
        bond (Union[None, Unset, float]): Rental bond
        price_reduction (Union[None, Unset, bool]): Indicates if this property is under price reduction
    """

    gst_option: Union[Unset, ListingsV1PriceDetailsGstOption] = UNSET
    price_type: Union[Unset, ListingsV1PriceDetailsPriceType] = UNSET
    price_unit: Union[Unset, ListingsV1PriceDetailsPriceUnit] = UNSET
    price: Union[None, Unset, float] = UNSET
    price_from: Union[None, Unset, int] = UNSET
    price_to: Union[None, Unset, int] = UNSET
    price_prefix: Union[None, Unset, str] = UNSET
    can_display_price: Union[None, Unset, bool] = UNSET
    hidden_reasons: Union[List[ListingsV1PriceDetailsHiddenReasonsType0Item], None, Unset] = UNSET
    display_price: Union[None, Unset, str] = UNSET
    bond: Union[None, Unset, float] = UNSET
    price_reduction: Union[None, Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        gst_option: Union[Unset, str] = UNSET
        if not isinstance(self.gst_option, Unset):
            gst_option = self.gst_option.value

        price_type: Union[Unset, str] = UNSET
        if not isinstance(self.price_type, Unset):
            price_type = self.price_type.value

        price_unit: Union[Unset, str] = UNSET
        if not isinstance(self.price_unit, Unset):
            price_unit = self.price_unit.value

        price: Union[None, Unset, float]
        if isinstance(self.price, Unset):
            price = UNSET
        else:
            price = self.price

        price_from: Union[None, Unset, int]
        if isinstance(self.price_from, Unset):
            price_from = UNSET
        else:
            price_from = self.price_from

        price_to: Union[None, Unset, int]
        if isinstance(self.price_to, Unset):
            price_to = UNSET
        else:
            price_to = self.price_to

        price_prefix: Union[None, Unset, str]
        if isinstance(self.price_prefix, Unset):
            price_prefix = UNSET
        else:
            price_prefix = self.price_prefix

        can_display_price: Union[None, Unset, bool]
        if isinstance(self.can_display_price, Unset):
            can_display_price = UNSET
        else:
            can_display_price = self.can_display_price

        hidden_reasons: Union[List[str], None, Unset]
        if isinstance(self.hidden_reasons, Unset):
            hidden_reasons = UNSET
        elif isinstance(self.hidden_reasons, list):
            hidden_reasons = []
            for hidden_reasons_type_0_item_data in self.hidden_reasons:
                hidden_reasons_type_0_item = hidden_reasons_type_0_item_data.value
                hidden_reasons.append(hidden_reasons_type_0_item)

        else:
            hidden_reasons = self.hidden_reasons

        display_price: Union[None, Unset, str]
        if isinstance(self.display_price, Unset):
            display_price = UNSET
        else:
            display_price = self.display_price

        bond: Union[None, Unset, float]
        if isinstance(self.bond, Unset):
            bond = UNSET
        else:
            bond = self.bond

        price_reduction: Union[None, Unset, bool]
        if isinstance(self.price_reduction, Unset):
            price_reduction = UNSET
        else:
            price_reduction = self.price_reduction

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if gst_option is not UNSET:
            field_dict["gstOption"] = gst_option
        if price_type is not UNSET:
            field_dict["priceType"] = price_type
        if price_unit is not UNSET:
            field_dict["priceUnit"] = price_unit
        if price is not UNSET:
            field_dict["price"] = price
        if price_from is not UNSET:
            field_dict["priceFrom"] = price_from
        if price_to is not UNSET:
            field_dict["priceTo"] = price_to
        if price_prefix is not UNSET:
            field_dict["pricePrefix"] = price_prefix
        if can_display_price is not UNSET:
            field_dict["canDisplayPrice"] = can_display_price
        if hidden_reasons is not UNSET:
            field_dict["hiddenReasons"] = hidden_reasons
        if display_price is not UNSET:
            field_dict["displayPrice"] = display_price
        if bond is not UNSET:
            field_dict["bond"] = bond
        if price_reduction is not UNSET:
            field_dict["priceReduction"] = price_reduction

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _gst_option = d.pop("gstOption", UNSET)
        gst_option: Union[Unset, ListingsV1PriceDetailsGstOption]
        if isinstance(_gst_option, Unset):
            gst_option = UNSET
        else:
            gst_option = ListingsV1PriceDetailsGstOption(_gst_option)

        _price_type = d.pop("priceType", UNSET)
        price_type: Union[Unset, ListingsV1PriceDetailsPriceType]
        if isinstance(_price_type, Unset):
            price_type = UNSET
        else:
            price_type = ListingsV1PriceDetailsPriceType(_price_type)

        _price_unit = d.pop("priceUnit", UNSET)
        price_unit: Union[Unset, ListingsV1PriceDetailsPriceUnit]
        if isinstance(_price_unit, Unset):
            price_unit = UNSET
        else:
            price_unit = ListingsV1PriceDetailsPriceUnit(_price_unit)

        def _parse_price(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        price = _parse_price(d.pop("price", UNSET))

        def _parse_price_from(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        price_from = _parse_price_from(d.pop("priceFrom", UNSET))

        def _parse_price_to(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        price_to = _parse_price_to(d.pop("priceTo", UNSET))

        def _parse_price_prefix(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        price_prefix = _parse_price_prefix(d.pop("pricePrefix", UNSET))

        def _parse_can_display_price(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        can_display_price = _parse_can_display_price(d.pop("canDisplayPrice", UNSET))

        def _parse_hidden_reasons(
            data: object,
        ) -> Union[List[ListingsV1PriceDetailsHiddenReasonsType0Item], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                hidden_reasons_type_0 = []
                _hidden_reasons_type_0 = data
                for hidden_reasons_type_0_item_data in _hidden_reasons_type_0:
                    hidden_reasons_type_0_item = ListingsV1PriceDetailsHiddenReasonsType0Item(
                        hidden_reasons_type_0_item_data
                    )

                    hidden_reasons_type_0.append(hidden_reasons_type_0_item)

                return hidden_reasons_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[ListingsV1PriceDetailsHiddenReasonsType0Item], None, Unset], data)

        hidden_reasons = _parse_hidden_reasons(d.pop("hiddenReasons", UNSET))

        def _parse_display_price(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        display_price = _parse_display_price(d.pop("displayPrice", UNSET))

        def _parse_bond(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        bond = _parse_bond(d.pop("bond", UNSET))

        def _parse_price_reduction(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        price_reduction = _parse_price_reduction(d.pop("priceReduction", UNSET))

        listings_v1_price_details = cls(
            gst_option=gst_option,
            price_type=price_type,
            price_unit=price_unit,
            price=price,
            price_from=price_from,
            price_to=price_to,
            price_prefix=price_prefix,
            can_display_price=can_display_price,
            hidden_reasons=hidden_reasons,
            display_price=display_price,
            bond=bond,
            price_reduction=price_reduction,
        )

        return listings_v1_price_details
