from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_price_details_gst_option import (
    DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetailsGstOption,
)
from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_price_details_hidden_reasons_item import (
    DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetailsHiddenReasonsItem,
)
from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_price_details_price_type import (
    DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetailsPriceType,
)
from ..models.domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_price_details_price_unit import (
    DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetailsPriceUnit,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails")


@_attrs_define
class DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetails:
    """
    Attributes:
        hidden_reasons (Union[Unset,
            List[DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetailsHiddenReasonsItem]]):
        gst_option (Union[Unset,
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetailsGstOption]):
        price_type (Union[Unset,
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetailsPriceType]):
        price_unit (Union[Unset,
            DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetailsPriceUnit]):
        price (Union[Unset, float]):
        price_from (Union[Unset, int]):
        price_to (Union[Unset, int]):
        price_prefix (Union[Unset, str]):
        can_display_price (Union[Unset, bool]):
        display_price (Union[Unset, str]):
        bond (Union[Unset, float]):
        price_reduction (Union[Unset, bool]):
    """

    hidden_reasons: Union[
        Unset, List[DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetailsHiddenReasonsItem]
    ] = UNSET
    gst_option: Union[
        Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetailsGstOption
    ] = UNSET
    price_type: Union[
        Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetailsPriceType
    ] = UNSET
    price_unit: Union[
        Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetailsPriceUnit
    ] = UNSET
    price: Union[Unset, float] = UNSET
    price_from: Union[Unset, int] = UNSET
    price_to: Union[Unset, int] = UNSET
    price_prefix: Union[Unset, str] = UNSET
    can_display_price: Union[Unset, bool] = UNSET
    display_price: Union[Unset, str] = UNSET
    bond: Union[Unset, float] = UNSET
    price_reduction: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hidden_reasons: Union[Unset, List[str]] = UNSET
        if not isinstance(self.hidden_reasons, Unset):
            hidden_reasons = []
            for hidden_reasons_item_data in self.hidden_reasons:
                hidden_reasons_item = hidden_reasons_item_data.value
                hidden_reasons.append(hidden_reasons_item)

        gst_option: Union[Unset, str] = UNSET
        if not isinstance(self.gst_option, Unset):
            gst_option = self.gst_option.value

        price_type: Union[Unset, str] = UNSET
        if not isinstance(self.price_type, Unset):
            price_type = self.price_type.value

        price_unit: Union[Unset, str] = UNSET
        if not isinstance(self.price_unit, Unset):
            price_unit = self.price_unit.value

        price = self.price

        price_from = self.price_from

        price_to = self.price_to

        price_prefix = self.price_prefix

        can_display_price = self.can_display_price

        display_price = self.display_price

        bond = self.bond

        price_reduction = self.price_reduction

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if hidden_reasons is not UNSET:
            field_dict["hiddenReasons"] = hidden_reasons
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
        hidden_reasons = []
        _hidden_reasons = d.pop("hiddenReasons", UNSET)
        for hidden_reasons_item_data in _hidden_reasons or []:
            hidden_reasons_item = (
                DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetailsHiddenReasonsItem(
                    hidden_reasons_item_data
                )
            )

            hidden_reasons.append(hidden_reasons_item)

        _gst_option = d.pop("gstOption", UNSET)
        gst_option: Union[
            Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetailsGstOption
        ]
        if isinstance(_gst_option, Unset):
            gst_option = UNSET
        else:
            gst_option = DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetailsGstOption(
                _gst_option
            )

        _price_type = d.pop("priceType", UNSET)
        price_type: Union[
            Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetailsPriceType
        ]
        if isinstance(_price_type, Unset):
            price_type = UNSET
        else:
            price_type = DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetailsPriceType(
                _price_type
            )

        _price_unit = d.pop("priceUnit", UNSET)
        price_unit: Union[
            Unset, DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetailsPriceUnit
        ]
        if isinstance(_price_unit, Unset):
            price_unit = UNSET
        else:
            price_unit = DomainListingsServiceV1ModelDomainListingsApiModelQueryResultsListingPriceDetailsPriceUnit(
                _price_unit
            )

        price = d.pop("price", UNSET)

        price_from = d.pop("priceFrom", UNSET)

        price_to = d.pop("priceTo", UNSET)

        price_prefix = d.pop("pricePrefix", UNSET)

        can_display_price = d.pop("canDisplayPrice", UNSET)

        display_price = d.pop("displayPrice", UNSET)

        bond = d.pop("bond", UNSET)

        price_reduction = d.pop("priceReduction", UNSET)

        domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_price_details = cls(
            hidden_reasons=hidden_reasons,
            gst_option=gst_option,
            price_type=price_type,
            price_unit=price_unit,
            price=price,
            price_from=price_from,
            price_to=price_to,
            price_prefix=price_prefix,
            can_display_price=can_display_price,
            display_price=display_price,
            bond=bond,
            price_reduction=price_reduction,
        )

        domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_price_details.additional_properties = d
        return domain_listings_service_v1_model_domain_listings_api_model_query_results_listing_price_details

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
