import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.authorities_v1_address import AuthoritiesV1Address
    from ..models.authorities_v1_agent_request import AuthoritiesV1AgentRequest
    from ..models.authorities_v1_crm_details import AuthoritiesV1CrmDetails
    from ..models.authorities_v1_marketing_campaign_request import AuthoritiesV1MarketingCampaignRequest
    from ..models.authorities_v1_vendor_request import AuthoritiesV1VendorRequest


T = TypeVar("T", bound="AuthoritiesV1AuthorityRequest")


@_attrs_define
class AuthoritiesV1AuthorityRequest:
    """
    Attributes:
        address (AuthoritiesV1Address):
        bathrooms (int):  Example: 2.
        bedrooms (int):  Example: 3.
        parking (int):  Example: 1.
        property_type (str): Available options are: `ApartmentUnitFlat`, `House`, `Townhouse`, `VacantLand` Example:
            ApartmentUnitFlat.
        type (str): Available options are: `Exclusive Auction`, `Exclusive Sale`, `General Sale`, `Appraisal` Example:
            Exclusive Sale.
        id (Union[Unset, str]):  Example: cf52bbf4-8d00-45e5-917a-8f27631a7da0.
        marketing_campaigns (Union[Unset, List['AuthoritiesV1MarketingCampaignRequest']]):
        vendors (Union[Unset, List['AuthoritiesV1VendorRequest']]):
        agents (Union[Unset, List['AuthoritiesV1AgentRequest']]):
        created (Union[Unset, datetime.datetime]):  Example: 2016-10-22T09:29:24.8137700+11:00.
        modified (Union[Unset, datetime.datetime]):  Example: 2016-10-22T09:29:24.8137700+11:00.
        status (Union[Unset, str]): Available options are: `draft`, `missing sign`, `executed` Example: executed.
        created_at (Union[Unset, datetime.datetime]):  Example: 2016-10-22T09:29:24.8137700+11:00.
        updated_at (Union[Unset, datetime.datetime]):  Example: 2016-10-22T09:29:24.8137700+11:00.
        administration_fee (Union[Unset, str]):
        agent_details_date (Union[Unset, datetime.datetime]):  Example: 2016-08-29T09:12:33.0010000+00:00.
        auction_date (Union[Unset, datetime.datetime]):  Example: 2016-08-29T09:12:33.0010000+00:00.
        auction_type (Union[Unset, str]):  Example: Onsite.
        chattels_excluded (Union[Unset, str]):  Example: Value.
        chattels_included (Union[Unset, List[str]]):
        continuing_period (Union[Unset, float]):  Example: 90.
        esp_range_higher (Union[Unset, float]):  Example: 200000.
        esp_range_lower (Union[Unset, float]):  Example: 100000.
        exclusive_period (Union[Unset, float]):  Example: 60.
        exclusive_period_start_date (Union[Unset, datetime.datetime]):  Example: 2016-08-29T09:12:33.0010000+00:00.
        exclusive_sold_as (Union[None, Unset, str]): Available options are: `Private Sale`, `Expression of Interest with
            the reserve to be advised prior to closing date` Example: Private Sale.
        is_owners_corporation_managed (Union[Unset, bool]):
        is_property_tenanted (Union[Unset, bool]):
        occupation_state (Union[None, Unset, str]): Available options are: `With vacant possession`, `Subject to any
            tenancy`, `Both` Example: Both.
        opt_out_information (Union[Unset, bool]):
        payable_in (Union[Unset, List[str]]):
        payment_method (Union[None, Unset, str]): Available options are: `Full purchase price`, `Payment of full
            deposit` Example: Payment of full deposit.
        payment_sum (Union[Unset, float]):  Example: 100000.
        reserve_price (Union[Unset, float]):  Example: 100000.
        sale_price_gst_type (Union[Unset, str]):  Example: l.
        sale_sign_permission (Union[Unset, bool]):
        search_criteria_amount (Union[Unset, float]):  Example: 100000.
        search_criteria_price_type (Union[Unset, str]): Available options are: `amount`, `range`, `other` Example:
            amount.
        transaction_type (Union[Unset, str]):  Example: AUTH.
        vendor_mkt_price_na (Union[Unset, bool]):  Example: True.
        waived_cooling_off (Union[Unset, bool]):
        lot (Union[Unset, str]):
        plan (Union[Unset, str]):
        title_reference (Union[Unset, str]):
        certificate_of_title_type (Union[Unset, str]): This field is unique to SA
        certificate_of_title_folio (Union[Unset, str]): This field is unique to SA
        certificate_of_title_volume (Union[Unset, str]): This field is unique to SA
        improved_land (Union[Unset, bool]): This field is unique to SA Default: False.
        crm_details (Union[Unset, AuthoritiesV1CrmDetails]): Details of CRM
    """

    address: "AuthoritiesV1Address"
    bathrooms: int
    bedrooms: int
    parking: int
    property_type: str
    type: str
    id: Union[Unset, str] = UNSET
    marketing_campaigns: Union[Unset, List["AuthoritiesV1MarketingCampaignRequest"]] = UNSET
    vendors: Union[Unset, List["AuthoritiesV1VendorRequest"]] = UNSET
    agents: Union[Unset, List["AuthoritiesV1AgentRequest"]] = UNSET
    created: Union[Unset, datetime.datetime] = UNSET
    modified: Union[Unset, datetime.datetime] = UNSET
    status: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    administration_fee: Union[Unset, str] = UNSET
    agent_details_date: Union[Unset, datetime.datetime] = UNSET
    auction_date: Union[Unset, datetime.datetime] = UNSET
    auction_type: Union[Unset, str] = UNSET
    chattels_excluded: Union[Unset, str] = UNSET
    chattels_included: Union[Unset, List[str]] = UNSET
    continuing_period: Union[Unset, float] = UNSET
    esp_range_higher: Union[Unset, float] = UNSET
    esp_range_lower: Union[Unset, float] = UNSET
    exclusive_period: Union[Unset, float] = UNSET
    exclusive_period_start_date: Union[Unset, datetime.datetime] = UNSET
    exclusive_sold_as: Union[None, Unset, str] = UNSET
    is_owners_corporation_managed: Union[Unset, bool] = UNSET
    is_property_tenanted: Union[Unset, bool] = UNSET
    occupation_state: Union[None, Unset, str] = UNSET
    opt_out_information: Union[Unset, bool] = UNSET
    payable_in: Union[Unset, List[str]] = UNSET
    payment_method: Union[None, Unset, str] = UNSET
    payment_sum: Union[Unset, float] = UNSET
    reserve_price: Union[Unset, float] = UNSET
    sale_price_gst_type: Union[Unset, str] = UNSET
    sale_sign_permission: Union[Unset, bool] = UNSET
    search_criteria_amount: Union[Unset, float] = UNSET
    search_criteria_price_type: Union[Unset, str] = UNSET
    transaction_type: Union[Unset, str] = UNSET
    vendor_mkt_price_na: Union[Unset, bool] = UNSET
    waived_cooling_off: Union[Unset, bool] = UNSET
    lot: Union[Unset, str] = UNSET
    plan: Union[Unset, str] = UNSET
    title_reference: Union[Unset, str] = UNSET
    certificate_of_title_type: Union[Unset, str] = UNSET
    certificate_of_title_folio: Union[Unset, str] = UNSET
    certificate_of_title_volume: Union[Unset, str] = UNSET
    improved_land: Union[Unset, bool] = False
    crm_details: Union[Unset, "AuthoritiesV1CrmDetails"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address = self.address.to_dict()

        bathrooms = self.bathrooms

        bedrooms = self.bedrooms

        parking = self.parking

        property_type = self.property_type

        type = self.type

        id = self.id

        marketing_campaigns: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.marketing_campaigns, Unset):
            marketing_campaigns = []
            for marketing_campaigns_item_data in self.marketing_campaigns:
                marketing_campaigns_item = marketing_campaigns_item_data.to_dict()
                marketing_campaigns.append(marketing_campaigns_item)

        vendors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.vendors, Unset):
            vendors = []
            for vendors_item_data in self.vendors:
                vendors_item = vendors_item_data.to_dict()
                vendors.append(vendors_item)

        agents: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.agents, Unset):
            agents = []
            for agents_item_data in self.agents:
                agents_item = agents_item_data.to_dict()
                agents.append(agents_item)

        created: Union[Unset, str] = UNSET
        if not isinstance(self.created, Unset):
            created = self.created.isoformat()

        modified: Union[Unset, str] = UNSET
        if not isinstance(self.modified, Unset):
            modified = self.modified.isoformat()

        status = self.status

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        administration_fee = self.administration_fee

        agent_details_date: Union[Unset, str] = UNSET
        if not isinstance(self.agent_details_date, Unset):
            agent_details_date = self.agent_details_date.isoformat()

        auction_date: Union[Unset, str] = UNSET
        if not isinstance(self.auction_date, Unset):
            auction_date = self.auction_date.isoformat()

        auction_type = self.auction_type

        chattels_excluded = self.chattels_excluded

        chattels_included: Union[Unset, List[str]] = UNSET
        if not isinstance(self.chattels_included, Unset):
            chattels_included = self.chattels_included

        continuing_period = self.continuing_period

        esp_range_higher = self.esp_range_higher

        esp_range_lower = self.esp_range_lower

        exclusive_period = self.exclusive_period

        exclusive_period_start_date: Union[Unset, str] = UNSET
        if not isinstance(self.exclusive_period_start_date, Unset):
            exclusive_period_start_date = self.exclusive_period_start_date.isoformat()

        exclusive_sold_as: Union[None, Unset, str]
        if isinstance(self.exclusive_sold_as, Unset):
            exclusive_sold_as = UNSET
        else:
            exclusive_sold_as = self.exclusive_sold_as

        is_owners_corporation_managed = self.is_owners_corporation_managed

        is_property_tenanted = self.is_property_tenanted

        occupation_state: Union[None, Unset, str]
        if isinstance(self.occupation_state, Unset):
            occupation_state = UNSET
        else:
            occupation_state = self.occupation_state

        opt_out_information = self.opt_out_information

        payable_in: Union[Unset, List[str]] = UNSET
        if not isinstance(self.payable_in, Unset):
            payable_in = self.payable_in

        payment_method: Union[None, Unset, str]
        if isinstance(self.payment_method, Unset):
            payment_method = UNSET
        else:
            payment_method = self.payment_method

        payment_sum = self.payment_sum

        reserve_price = self.reserve_price

        sale_price_gst_type = self.sale_price_gst_type

        sale_sign_permission = self.sale_sign_permission

        search_criteria_amount = self.search_criteria_amount

        search_criteria_price_type = self.search_criteria_price_type

        transaction_type = self.transaction_type

        vendor_mkt_price_na = self.vendor_mkt_price_na

        waived_cooling_off = self.waived_cooling_off

        lot = self.lot

        plan = self.plan

        title_reference = self.title_reference

        certificate_of_title_type = self.certificate_of_title_type

        certificate_of_title_folio = self.certificate_of_title_folio

        certificate_of_title_volume = self.certificate_of_title_volume

        improved_land = self.improved_land

        crm_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.crm_details, Unset):
            crm_details = self.crm_details.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "address": address,
                "bathrooms": bathrooms,
                "bedrooms": bedrooms,
                "parking": parking,
                "propertyType": property_type,
                "type": type,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if marketing_campaigns is not UNSET:
            field_dict["marketingCampaigns"] = marketing_campaigns
        if vendors is not UNSET:
            field_dict["vendors"] = vendors
        if agents is not UNSET:
            field_dict["agents"] = agents
        if created is not UNSET:
            field_dict["created"] = created
        if modified is not UNSET:
            field_dict["modified"] = modified
        if status is not UNSET:
            field_dict["status"] = status
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if administration_fee is not UNSET:
            field_dict["administrationFee"] = administration_fee
        if agent_details_date is not UNSET:
            field_dict["agentDetailsDate"] = agent_details_date
        if auction_date is not UNSET:
            field_dict["auctionDate"] = auction_date
        if auction_type is not UNSET:
            field_dict["auctionType"] = auction_type
        if chattels_excluded is not UNSET:
            field_dict["chattelsExcluded"] = chattels_excluded
        if chattels_included is not UNSET:
            field_dict["chattelsIncluded"] = chattels_included
        if continuing_period is not UNSET:
            field_dict["continuingPeriod"] = continuing_period
        if esp_range_higher is not UNSET:
            field_dict["espRangeHigher"] = esp_range_higher
        if esp_range_lower is not UNSET:
            field_dict["espRangeLower"] = esp_range_lower
        if exclusive_period is not UNSET:
            field_dict["exclusivePeriod"] = exclusive_period
        if exclusive_period_start_date is not UNSET:
            field_dict["exclusivePeriodStartDate"] = exclusive_period_start_date
        if exclusive_sold_as is not UNSET:
            field_dict["exclusiveSoldAs"] = exclusive_sold_as
        if is_owners_corporation_managed is not UNSET:
            field_dict["isOwnersCorporationManaged"] = is_owners_corporation_managed
        if is_property_tenanted is not UNSET:
            field_dict["isPropertyTenanted"] = is_property_tenanted
        if occupation_state is not UNSET:
            field_dict["occupationState"] = occupation_state
        if opt_out_information is not UNSET:
            field_dict["optOutInformation"] = opt_out_information
        if payable_in is not UNSET:
            field_dict["payableIn"] = payable_in
        if payment_method is not UNSET:
            field_dict["paymentMethod"] = payment_method
        if payment_sum is not UNSET:
            field_dict["paymentSum"] = payment_sum
        if reserve_price is not UNSET:
            field_dict["reservePrice"] = reserve_price
        if sale_price_gst_type is not UNSET:
            field_dict["salePriceGstType"] = sale_price_gst_type
        if sale_sign_permission is not UNSET:
            field_dict["saleSignPermission"] = sale_sign_permission
        if search_criteria_amount is not UNSET:
            field_dict["searchCriteriaAmount"] = search_criteria_amount
        if search_criteria_price_type is not UNSET:
            field_dict["searchCriteriaPriceType"] = search_criteria_price_type
        if transaction_type is not UNSET:
            field_dict["transactionType"] = transaction_type
        if vendor_mkt_price_na is not UNSET:
            field_dict["vendorMktPriceNa"] = vendor_mkt_price_na
        if waived_cooling_off is not UNSET:
            field_dict["waivedCoolingOff"] = waived_cooling_off
        if lot is not UNSET:
            field_dict["lot"] = lot
        if plan is not UNSET:
            field_dict["plan"] = plan
        if title_reference is not UNSET:
            field_dict["titleReference"] = title_reference
        if certificate_of_title_type is not UNSET:
            field_dict["certificateOfTitleType"] = certificate_of_title_type
        if certificate_of_title_folio is not UNSET:
            field_dict["certificateOfTitleFolio"] = certificate_of_title_folio
        if certificate_of_title_volume is not UNSET:
            field_dict["certificateOfTitleVolume"] = certificate_of_title_volume
        if improved_land is not UNSET:
            field_dict["improvedLand"] = improved_land
        if crm_details is not UNSET:
            field_dict["crmDetails"] = crm_details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.authorities_v1_address import AuthoritiesV1Address
        from ..models.authorities_v1_agent_request import AuthoritiesV1AgentRequest
        from ..models.authorities_v1_crm_details import AuthoritiesV1CrmDetails
        from ..models.authorities_v1_marketing_campaign_request import AuthoritiesV1MarketingCampaignRequest
        from ..models.authorities_v1_vendor_request import AuthoritiesV1VendorRequest

        d = src_dict.copy()
        address = AuthoritiesV1Address.from_dict(d.pop("address"))

        bathrooms = d.pop("bathrooms")

        bedrooms = d.pop("bedrooms")

        parking = d.pop("parking")

        property_type = d.pop("propertyType")

        type = d.pop("type")

        id = d.pop("id", UNSET)

        marketing_campaigns = []
        _marketing_campaigns = d.pop("marketingCampaigns", UNSET)
        for marketing_campaigns_item_data in _marketing_campaigns or []:
            marketing_campaigns_item = AuthoritiesV1MarketingCampaignRequest.from_dict(marketing_campaigns_item_data)

            marketing_campaigns.append(marketing_campaigns_item)

        vendors = []
        _vendors = d.pop("vendors", UNSET)
        for vendors_item_data in _vendors or []:
            vendors_item = AuthoritiesV1VendorRequest.from_dict(vendors_item_data)

            vendors.append(vendors_item)

        agents = []
        _agents = d.pop("agents", UNSET)
        for agents_item_data in _agents or []:
            agents_item = AuthoritiesV1AgentRequest.from_dict(agents_item_data)

            agents.append(agents_item)

        _created = d.pop("created", UNSET)
        created: Union[Unset, datetime.datetime]
        if isinstance(_created, Unset):
            created = UNSET
        else:
            created = isoparse(_created)

        _modified = d.pop("modified", UNSET)
        modified: Union[Unset, datetime.datetime]
        if isinstance(_modified, Unset):
            modified = UNSET
        else:
            modified = isoparse(_modified)

        status = d.pop("status", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        administration_fee = d.pop("administrationFee", UNSET)

        _agent_details_date = d.pop("agentDetailsDate", UNSET)
        agent_details_date: Union[Unset, datetime.datetime]
        if isinstance(_agent_details_date, Unset):
            agent_details_date = UNSET
        else:
            agent_details_date = isoparse(_agent_details_date)

        _auction_date = d.pop("auctionDate", UNSET)
        auction_date: Union[Unset, datetime.datetime]
        if isinstance(_auction_date, Unset):
            auction_date = UNSET
        else:
            auction_date = isoparse(_auction_date)

        auction_type = d.pop("auctionType", UNSET)

        chattels_excluded = d.pop("chattelsExcluded", UNSET)

        chattels_included = cast(List[str], d.pop("chattelsIncluded", UNSET))

        continuing_period = d.pop("continuingPeriod", UNSET)

        esp_range_higher = d.pop("espRangeHigher", UNSET)

        esp_range_lower = d.pop("espRangeLower", UNSET)

        exclusive_period = d.pop("exclusivePeriod", UNSET)

        _exclusive_period_start_date = d.pop("exclusivePeriodStartDate", UNSET)
        exclusive_period_start_date: Union[Unset, datetime.datetime]
        if isinstance(_exclusive_period_start_date, Unset):
            exclusive_period_start_date = UNSET
        else:
            exclusive_period_start_date = isoparse(_exclusive_period_start_date)

        def _parse_exclusive_sold_as(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        exclusive_sold_as = _parse_exclusive_sold_as(d.pop("exclusiveSoldAs", UNSET))

        is_owners_corporation_managed = d.pop("isOwnersCorporationManaged", UNSET)

        is_property_tenanted = d.pop("isPropertyTenanted", UNSET)

        def _parse_occupation_state(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        occupation_state = _parse_occupation_state(d.pop("occupationState", UNSET))

        opt_out_information = d.pop("optOutInformation", UNSET)

        payable_in = cast(List[str], d.pop("payableIn", UNSET))

        def _parse_payment_method(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        payment_method = _parse_payment_method(d.pop("paymentMethod", UNSET))

        payment_sum = d.pop("paymentSum", UNSET)

        reserve_price = d.pop("reservePrice", UNSET)

        sale_price_gst_type = d.pop("salePriceGstType", UNSET)

        sale_sign_permission = d.pop("saleSignPermission", UNSET)

        search_criteria_amount = d.pop("searchCriteriaAmount", UNSET)

        search_criteria_price_type = d.pop("searchCriteriaPriceType", UNSET)

        transaction_type = d.pop("transactionType", UNSET)

        vendor_mkt_price_na = d.pop("vendorMktPriceNa", UNSET)

        waived_cooling_off = d.pop("waivedCoolingOff", UNSET)

        lot = d.pop("lot", UNSET)

        plan = d.pop("plan", UNSET)

        title_reference = d.pop("titleReference", UNSET)

        certificate_of_title_type = d.pop("certificateOfTitleType", UNSET)

        certificate_of_title_folio = d.pop("certificateOfTitleFolio", UNSET)

        certificate_of_title_volume = d.pop("certificateOfTitleVolume", UNSET)

        improved_land = d.pop("improvedLand", UNSET)

        _crm_details = d.pop("crmDetails", UNSET)
        crm_details: Union[Unset, AuthoritiesV1CrmDetails]
        if isinstance(_crm_details, Unset):
            crm_details = UNSET
        else:
            crm_details = AuthoritiesV1CrmDetails.from_dict(_crm_details)

        authorities_v1_authority_request = cls(
            address=address,
            bathrooms=bathrooms,
            bedrooms=bedrooms,
            parking=parking,
            property_type=property_type,
            type=type,
            id=id,
            marketing_campaigns=marketing_campaigns,
            vendors=vendors,
            agents=agents,
            created=created,
            modified=modified,
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            administration_fee=administration_fee,
            agent_details_date=agent_details_date,
            auction_date=auction_date,
            auction_type=auction_type,
            chattels_excluded=chattels_excluded,
            chattels_included=chattels_included,
            continuing_period=continuing_period,
            esp_range_higher=esp_range_higher,
            esp_range_lower=esp_range_lower,
            exclusive_period=exclusive_period,
            exclusive_period_start_date=exclusive_period_start_date,
            exclusive_sold_as=exclusive_sold_as,
            is_owners_corporation_managed=is_owners_corporation_managed,
            is_property_tenanted=is_property_tenanted,
            occupation_state=occupation_state,
            opt_out_information=opt_out_information,
            payable_in=payable_in,
            payment_method=payment_method,
            payment_sum=payment_sum,
            reserve_price=reserve_price,
            sale_price_gst_type=sale_price_gst_type,
            sale_sign_permission=sale_sign_permission,
            search_criteria_amount=search_criteria_amount,
            search_criteria_price_type=search_criteria_price_type,
            transaction_type=transaction_type,
            vendor_mkt_price_na=vendor_mkt_price_na,
            waived_cooling_off=waived_cooling_off,
            lot=lot,
            plan=plan,
            title_reference=title_reference,
            certificate_of_title_type=certificate_of_title_type,
            certificate_of_title_folio=certificate_of_title_folio,
            certificate_of_title_volume=certificate_of_title_volume,
            improved_land=improved_land,
            crm_details=crm_details,
        )

        authorities_v1_authority_request.additional_properties = d
        return authorities_v1_authority_request

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
