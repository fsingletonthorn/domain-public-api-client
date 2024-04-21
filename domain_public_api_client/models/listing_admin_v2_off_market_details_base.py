import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.listing_admin_v2_off_market_details_base_off_market_action import (
    ListingAdminV2OffMarketDetailsBaseOffMarketAction,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.listing_admin_v2_leased_details import ListingAdminV2LeasedDetails
    from ..models.listing_admin_v2_sold_details import ListingAdminV2SoldDetails


T = TypeVar("T", bound="ListingAdminV2OffMarketDetailsBase")


@_attrs_define
class ListingAdminV2OffMarketDetailsBase:
    """Off market details base

    Attributes:
        off_market_action (ListingAdminV2OffMarketDetailsBaseOffMarketAction): Off Market Action
        action_date (datetime.datetime): The date property was sold, leased or withdrawn
        sold_details (Union[Unset, ListingAdminV2SoldDetails]): Sold Details
        leased_details (Union[Unset, ListingAdminV2LeasedDetails]): Leased Details
        comment (Union[Unset, str]): Extra details for off market action
    """

    off_market_action: ListingAdminV2OffMarketDetailsBaseOffMarketAction
    action_date: datetime.datetime
    sold_details: Union[Unset, "ListingAdminV2SoldDetails"] = UNSET
    leased_details: Union[Unset, "ListingAdminV2LeasedDetails"] = UNSET
    comment: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        off_market_action = self.off_market_action.value

        action_date = self.action_date.isoformat()

        sold_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sold_details, Unset):
            sold_details = self.sold_details.to_dict()

        leased_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.leased_details, Unset):
            leased_details = self.leased_details.to_dict()

        comment = self.comment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "offMarketAction": off_market_action,
                "actionDate": action_date,
            }
        )
        if sold_details is not UNSET:
            field_dict["soldDetails"] = sold_details
        if leased_details is not UNSET:
            field_dict["leasedDetails"] = leased_details
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.listing_admin_v2_leased_details import ListingAdminV2LeasedDetails
        from ..models.listing_admin_v2_sold_details import ListingAdminV2SoldDetails

        d = src_dict.copy()
        off_market_action = ListingAdminV2OffMarketDetailsBaseOffMarketAction(d.pop("offMarketAction"))

        action_date = isoparse(d.pop("actionDate"))

        _sold_details = d.pop("soldDetails", UNSET)
        sold_details: Union[Unset, ListingAdminV2SoldDetails]
        if isinstance(_sold_details, Unset):
            sold_details = UNSET
        else:
            sold_details = ListingAdminV2SoldDetails.from_dict(_sold_details)

        _leased_details = d.pop("leasedDetails", UNSET)
        leased_details: Union[Unset, ListingAdminV2LeasedDetails]
        if isinstance(_leased_details, Unset):
            leased_details = UNSET
        else:
            leased_details = ListingAdminV2LeasedDetails.from_dict(_leased_details)

        comment = d.pop("comment", UNSET)

        listing_admin_v2_off_market_details_base = cls(
            off_market_action=off_market_action,
            action_date=action_date,
            sold_details=sold_details,
            leased_details=leased_details,
            comment=comment,
        )

        listing_admin_v2_off_market_details_base.additional_properties = d
        return listing_admin_v2_off_market_details_base

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
