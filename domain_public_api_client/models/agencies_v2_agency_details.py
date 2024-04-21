from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgenciesV2AgencyDetails")


@_attrs_define
class AgenciesV2AgencyDetails:
    """AgencyDetails

    Attributes:
        street_address_1 (str): Gets or Sets StreetAddress1
        suburb (str): Gets or Sets Suburb
        state (str): Gets or Sets State
        postcode (str): Gets or Sets Postcode
        hide_market_price_estimate (bool): Gets or Sets HideMarketPriceEstimate
        limit_email_domain (bool): Gets or Sets LimitEmailDomain
        street_address_2 (Union[None, Unset, str]): Gets or Sets StreetAddress2
        agency_website (Union[None, Unset, str]): Gets or Sets AgencyWebsite
        principal_name (Union[None, Unset, str]): Gets or Sets PrincipalName
        principal_email (Union[None, Unset, str]): Gets or Sets PrincipalEmail
        show_past_sales_prices (Union[None, Unset, bool]): Gets or Sets ShowPastSalesPrices
        is_agency_report_enabled (Union[None, Unset, bool]): Gets or Sets IsAgencyReportEnabled
        sales_email (Union[None, Unset, str]): Gets or Sets SalesEmail
        rental_email (Union[None, Unset, str]): Gets or Sets RentalEmail
        is_promotional_telephone_active (Union[None, Unset, bool]): Gets or Sets IsPromotionalTelephoneActive
        show_tab_sold_last_year (Union[None, Unset, bool]): Gets or Sets ShowTabSoldLastYear
    """

    street_address_1: str
    suburb: str
    state: str
    postcode: str
    hide_market_price_estimate: bool
    limit_email_domain: bool
    street_address_2: Union[None, Unset, str] = UNSET
    agency_website: Union[None, Unset, str] = UNSET
    principal_name: Union[None, Unset, str] = UNSET
    principal_email: Union[None, Unset, str] = UNSET
    show_past_sales_prices: Union[None, Unset, bool] = UNSET
    is_agency_report_enabled: Union[None, Unset, bool] = UNSET
    sales_email: Union[None, Unset, str] = UNSET
    rental_email: Union[None, Unset, str] = UNSET
    is_promotional_telephone_active: Union[None, Unset, bool] = UNSET
    show_tab_sold_last_year: Union[None, Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        street_address_1 = self.street_address_1

        suburb = self.suburb

        state = self.state

        postcode = self.postcode

        hide_market_price_estimate = self.hide_market_price_estimate

        limit_email_domain = self.limit_email_domain

        street_address_2: Union[None, Unset, str]
        if isinstance(self.street_address_2, Unset):
            street_address_2 = UNSET
        else:
            street_address_2 = self.street_address_2

        agency_website: Union[None, Unset, str]
        if isinstance(self.agency_website, Unset):
            agency_website = UNSET
        else:
            agency_website = self.agency_website

        principal_name: Union[None, Unset, str]
        if isinstance(self.principal_name, Unset):
            principal_name = UNSET
        else:
            principal_name = self.principal_name

        principal_email: Union[None, Unset, str]
        if isinstance(self.principal_email, Unset):
            principal_email = UNSET
        else:
            principal_email = self.principal_email

        show_past_sales_prices: Union[None, Unset, bool]
        if isinstance(self.show_past_sales_prices, Unset):
            show_past_sales_prices = UNSET
        else:
            show_past_sales_prices = self.show_past_sales_prices

        is_agency_report_enabled: Union[None, Unset, bool]
        if isinstance(self.is_agency_report_enabled, Unset):
            is_agency_report_enabled = UNSET
        else:
            is_agency_report_enabled = self.is_agency_report_enabled

        sales_email: Union[None, Unset, str]
        if isinstance(self.sales_email, Unset):
            sales_email = UNSET
        else:
            sales_email = self.sales_email

        rental_email: Union[None, Unset, str]
        if isinstance(self.rental_email, Unset):
            rental_email = UNSET
        else:
            rental_email = self.rental_email

        is_promotional_telephone_active: Union[None, Unset, bool]
        if isinstance(self.is_promotional_telephone_active, Unset):
            is_promotional_telephone_active = UNSET
        else:
            is_promotional_telephone_active = self.is_promotional_telephone_active

        show_tab_sold_last_year: Union[None, Unset, bool]
        if isinstance(self.show_tab_sold_last_year, Unset):
            show_tab_sold_last_year = UNSET
        else:
            show_tab_sold_last_year = self.show_tab_sold_last_year

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "streetAddress1": street_address_1,
                "suburb": suburb,
                "state": state,
                "postcode": postcode,
                "hideMarketPriceEstimate": hide_market_price_estimate,
                "limitEmailDomain": limit_email_domain,
            }
        )
        if street_address_2 is not UNSET:
            field_dict["streetAddress2"] = street_address_2
        if agency_website is not UNSET:
            field_dict["agencyWebsite"] = agency_website
        if principal_name is not UNSET:
            field_dict["principalName"] = principal_name
        if principal_email is not UNSET:
            field_dict["principalEmail"] = principal_email
        if show_past_sales_prices is not UNSET:
            field_dict["showPastSalesPrices"] = show_past_sales_prices
        if is_agency_report_enabled is not UNSET:
            field_dict["isAgencyReportEnabled"] = is_agency_report_enabled
        if sales_email is not UNSET:
            field_dict["salesEmail"] = sales_email
        if rental_email is not UNSET:
            field_dict["rentalEmail"] = rental_email
        if is_promotional_telephone_active is not UNSET:
            field_dict["isPromotionalTelephoneActive"] = is_promotional_telephone_active
        if show_tab_sold_last_year is not UNSET:
            field_dict["showTabSoldLastYear"] = show_tab_sold_last_year

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        street_address_1 = d.pop("streetAddress1")

        suburb = d.pop("suburb")

        state = d.pop("state")

        postcode = d.pop("postcode")

        hide_market_price_estimate = d.pop("hideMarketPriceEstimate")

        limit_email_domain = d.pop("limitEmailDomain")

        def _parse_street_address_2(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        street_address_2 = _parse_street_address_2(d.pop("streetAddress2", UNSET))

        def _parse_agency_website(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        agency_website = _parse_agency_website(d.pop("agencyWebsite", UNSET))

        def _parse_principal_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        principal_name = _parse_principal_name(d.pop("principalName", UNSET))

        def _parse_principal_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        principal_email = _parse_principal_email(d.pop("principalEmail", UNSET))

        def _parse_show_past_sales_prices(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        show_past_sales_prices = _parse_show_past_sales_prices(d.pop("showPastSalesPrices", UNSET))

        def _parse_is_agency_report_enabled(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_agency_report_enabled = _parse_is_agency_report_enabled(d.pop("isAgencyReportEnabled", UNSET))

        def _parse_sales_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sales_email = _parse_sales_email(d.pop("salesEmail", UNSET))

        def _parse_rental_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        rental_email = _parse_rental_email(d.pop("rentalEmail", UNSET))

        def _parse_is_promotional_telephone_active(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_promotional_telephone_active = _parse_is_promotional_telephone_active(
            d.pop("isPromotionalTelephoneActive", UNSET)
        )

        def _parse_show_tab_sold_last_year(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        show_tab_sold_last_year = _parse_show_tab_sold_last_year(d.pop("showTabSoldLastYear", UNSET))

        agencies_v2_agency_details = cls(
            street_address_1=street_address_1,
            suburb=suburb,
            state=state,
            postcode=postcode,
            hide_market_price_estimate=hide_market_price_estimate,
            limit_email_domain=limit_email_domain,
            street_address_2=street_address_2,
            agency_website=agency_website,
            principal_name=principal_name,
            principal_email=principal_email,
            show_past_sales_prices=show_past_sales_prices,
            is_agency_report_enabled=is_agency_report_enabled,
            sales_email=sales_email,
            rental_email=rental_email,
            is_promotional_telephone_active=is_promotional_telephone_active,
            show_tab_sold_last_year=show_tab_sold_last_year,
        )

        return agencies_v2_agency_details
