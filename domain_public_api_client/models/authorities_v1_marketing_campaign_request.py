import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.authorities_v1_marketing_campaign_item_request import AuthoritiesV1MarketingCampaignItemRequest


T = TypeVar("T", bound="AuthoritiesV1MarketingCampaignRequest")


@_attrs_define
class AuthoritiesV1MarketingCampaignRequest:
    """
    Attributes:
        campaign_type (str): Available options are: `To Be Advised`, `Paper Based`, `Campaign Track`, `Realhub` Example:
            Paper Based.
        advertising (Union[Unset, str]): advertising cost of this marketing campaign Example: 3000.00.
        marketing_campaign_items (Union[Unset, List['AuthoritiesV1MarketingCampaignItemRequest']]):
        comments (Union[Unset, str]):  Example: {"children":[{"children":null,"hidden":false,"hides_children":false,"pla
            ceholders":null,"remove_css_class":null,"selected":false,"tag_key":null,"text":"Written Request","text_convertib
            le":true,"type":"option_radio"}],"hidden":false,"placeholders":null,"required":false,"text":null,"text_convertib
            le":true,"type":"group_radio"}.
        comments_fallback (Union[Unset, str]):
        discount_amount (Union[None, Unset, str]):  Example: 1000.00.
        discount_percent (Union[None, Unset, str]):  Example: 10.00.
        expense (Union[None, Unset, str]): Available options are: `Signing of this Authority`, `Written request`,
            `Specific Date`, `Signing of this Form 6`, `Signing of this Agency Agreement`, `Upon Invoice or Account`, `Prior
            to the commencement of marketing campaign`, `On Settlement or Withdrawal whichever occurs first`, `Vendor to pay
            through Campaign Agent v2`, `Vendor to pay through Market Now`, `Vendor to pay through Rello`, `Vendor to pay
            through List Ready` Example: Signing of this Authority.
        other (Union[Unset, str]):  Example: 1000.00.
        payable_on (Union[None, Unset, datetime.date]):  Example: 2016-10-22.
        total (Union[Unset, str]): Total cost of this marketing campaign. Total of the items cost if there are items or
            (advertising + other) cost for other types Example: 4000.00.
        realhub_quote_id (Union[None, Unset, str]):  Example: 1234567890.
    """

    campaign_type: str
    advertising: Union[Unset, str] = UNSET
    marketing_campaign_items: Union[Unset, List["AuthoritiesV1MarketingCampaignItemRequest"]] = UNSET
    comments: Union[Unset, str] = UNSET
    comments_fallback: Union[Unset, str] = UNSET
    discount_amount: Union[None, Unset, str] = UNSET
    discount_percent: Union[None, Unset, str] = UNSET
    expense: Union[None, Unset, str] = UNSET
    other: Union[Unset, str] = UNSET
    payable_on: Union[None, Unset, datetime.date] = UNSET
    total: Union[Unset, str] = UNSET
    realhub_quote_id: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        campaign_type = self.campaign_type

        advertising = self.advertising

        marketing_campaign_items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.marketing_campaign_items, Unset):
            marketing_campaign_items = []
            for marketing_campaign_items_item_data in self.marketing_campaign_items:
                marketing_campaign_items_item = marketing_campaign_items_item_data.to_dict()
                marketing_campaign_items.append(marketing_campaign_items_item)

        comments = self.comments

        comments_fallback = self.comments_fallback

        discount_amount: Union[None, Unset, str]
        if isinstance(self.discount_amount, Unset):
            discount_amount = UNSET
        else:
            discount_amount = self.discount_amount

        discount_percent: Union[None, Unset, str]
        if isinstance(self.discount_percent, Unset):
            discount_percent = UNSET
        else:
            discount_percent = self.discount_percent

        expense: Union[None, Unset, str]
        if isinstance(self.expense, Unset):
            expense = UNSET
        else:
            expense = self.expense

        other = self.other

        payable_on: Union[None, Unset, str]
        if isinstance(self.payable_on, Unset):
            payable_on = UNSET
        elif isinstance(self.payable_on, datetime.date):
            payable_on = self.payable_on.isoformat()
        else:
            payable_on = self.payable_on

        total = self.total

        realhub_quote_id: Union[None, Unset, str]
        if isinstance(self.realhub_quote_id, Unset):
            realhub_quote_id = UNSET
        else:
            realhub_quote_id = self.realhub_quote_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "campaignType": campaign_type,
            }
        )
        if advertising is not UNSET:
            field_dict["advertising"] = advertising
        if marketing_campaign_items is not UNSET:
            field_dict["marketingCampaignItems"] = marketing_campaign_items
        if comments is not UNSET:
            field_dict["comments"] = comments
        if comments_fallback is not UNSET:
            field_dict["commentsFallback"] = comments_fallback
        if discount_amount is not UNSET:
            field_dict["discountAmount"] = discount_amount
        if discount_percent is not UNSET:
            field_dict["discountPercent"] = discount_percent
        if expense is not UNSET:
            field_dict["expense"] = expense
        if other is not UNSET:
            field_dict["other"] = other
        if payable_on is not UNSET:
            field_dict["payableOn"] = payable_on
        if total is not UNSET:
            field_dict["total"] = total
        if realhub_quote_id is not UNSET:
            field_dict["realhubQuoteId"] = realhub_quote_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.authorities_v1_marketing_campaign_item_request import AuthoritiesV1MarketingCampaignItemRequest

        d = src_dict.copy()
        campaign_type = d.pop("campaignType")

        advertising = d.pop("advertising", UNSET)

        marketing_campaign_items = []
        _marketing_campaign_items = d.pop("marketingCampaignItems", UNSET)
        for marketing_campaign_items_item_data in _marketing_campaign_items or []:
            marketing_campaign_items_item = AuthoritiesV1MarketingCampaignItemRequest.from_dict(
                marketing_campaign_items_item_data
            )

            marketing_campaign_items.append(marketing_campaign_items_item)

        comments = d.pop("comments", UNSET)

        comments_fallback = d.pop("commentsFallback", UNSET)

        def _parse_discount_amount(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        discount_amount = _parse_discount_amount(d.pop("discountAmount", UNSET))

        def _parse_discount_percent(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        discount_percent = _parse_discount_percent(d.pop("discountPercent", UNSET))

        def _parse_expense(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        expense = _parse_expense(d.pop("expense", UNSET))

        other = d.pop("other", UNSET)

        def _parse_payable_on(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                payable_on_type_0 = isoparse(data).date()

                return payable_on_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        payable_on = _parse_payable_on(d.pop("payableOn", UNSET))

        total = d.pop("total", UNSET)

        def _parse_realhub_quote_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        realhub_quote_id = _parse_realhub_quote_id(d.pop("realhubQuoteId", UNSET))

        authorities_v1_marketing_campaign_request = cls(
            campaign_type=campaign_type,
            advertising=advertising,
            marketing_campaign_items=marketing_campaign_items,
            comments=comments,
            comments_fallback=comments_fallback,
            discount_amount=discount_amount,
            discount_percent=discount_percent,
            expense=expense,
            other=other,
            payable_on=payable_on,
            total=total,
            realhub_quote_id=realhub_quote_id,
        )

        authorities_v1_marketing_campaign_request.additional_properties = d
        return authorities_v1_marketing_campaign_request

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
