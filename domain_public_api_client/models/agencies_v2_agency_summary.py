from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgenciesV2AgencySummary")


@_attrs_define
class AgenciesV2AgencySummary:
    """AgencySummary

    Attributes:
        in_suburb (Union[None, Unset, bool]): Gets or Sets InSuburb
        query_suburb (Union[None, Unset, str]): Gets or Sets QuerySuburb
        has_recently_sold (Union[None, Unset, bool]): Gets or Sets HasRecentlySold
        id (Union[None, Unset, int]): Gets or Sets Id
        name (Union[None, Unset, str]): Gets or Sets Name
        suburb (Union[None, Unset, str]): Gets or Sets Suburb
        logo_url (Union[None, Unset, str]): Gets or Sets LogoUrl
        base_url (Union[None, Unset, str]): Gets or Sets BaseUrl
        address1 (Union[None, Unset, str]): Gets or Sets Address1
        address2 (Union[None, Unset, str]): Gets or Sets Address2
        telephone (Union[None, Unset, str]): Gets or Sets Telephone
        rental_telephone (Union[None, Unset, str]): Gets or Sets RentalTelephone
        mobile (Union[None, Unset, str]): Gets or Sets Mobile
        fax (Union[None, Unset, str]): Gets or Sets Fax
        state (Union[None, Unset, str]): Gets or Sets State
        description (Union[None, Unset, str]): Gets or Sets Description
        email (Union[None, Unset, str]): Gets or Sets Email
        rental_email (Union[None, Unset, str]): Gets or Sets RentalEmail
        home_page_search_options (Union[None, Unset, str]): Gets or Sets HomePageSearchOptions
        account_type (Union[None, Unset, int]): Gets or Sets AccountType
        number_for_sale (Union[None, Unset, int]): Gets or Sets NumberForSale
        number_for_rent (Union[None, Unset, int]): Gets or Sets NumberForRent
        domain_url (Union[None, Unset, str]): Gets or Sets DomainUrl
        show_tab_sold_last_year (Union[None, Unset, bool]): Gets or Sets ShowTabSoldLastYear
    """

    in_suburb: Union[None, Unset, bool] = UNSET
    query_suburb: Union[None, Unset, str] = UNSET
    has_recently_sold: Union[None, Unset, bool] = UNSET
    id: Union[None, Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    suburb: Union[None, Unset, str] = UNSET
    logo_url: Union[None, Unset, str] = UNSET
    base_url: Union[None, Unset, str] = UNSET
    address1: Union[None, Unset, str] = UNSET
    address2: Union[None, Unset, str] = UNSET
    telephone: Union[None, Unset, str] = UNSET
    rental_telephone: Union[None, Unset, str] = UNSET
    mobile: Union[None, Unset, str] = UNSET
    fax: Union[None, Unset, str] = UNSET
    state: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    email: Union[None, Unset, str] = UNSET
    rental_email: Union[None, Unset, str] = UNSET
    home_page_search_options: Union[None, Unset, str] = UNSET
    account_type: Union[None, Unset, int] = UNSET
    number_for_sale: Union[None, Unset, int] = UNSET
    number_for_rent: Union[None, Unset, int] = UNSET
    domain_url: Union[None, Unset, str] = UNSET
    show_tab_sold_last_year: Union[None, Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        in_suburb: Union[None, Unset, bool]
        if isinstance(self.in_suburb, Unset):
            in_suburb = UNSET
        else:
            in_suburb = self.in_suburb

        query_suburb: Union[None, Unset, str]
        if isinstance(self.query_suburb, Unset):
            query_suburb = UNSET
        else:
            query_suburb = self.query_suburb

        has_recently_sold: Union[None, Unset, bool]
        if isinstance(self.has_recently_sold, Unset):
            has_recently_sold = UNSET
        else:
            has_recently_sold = self.has_recently_sold

        id: Union[None, Unset, int]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        suburb: Union[None, Unset, str]
        if isinstance(self.suburb, Unset):
            suburb = UNSET
        else:
            suburb = self.suburb

        logo_url: Union[None, Unset, str]
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        base_url: Union[None, Unset, str]
        if isinstance(self.base_url, Unset):
            base_url = UNSET
        else:
            base_url = self.base_url

        address1: Union[None, Unset, str]
        if isinstance(self.address1, Unset):
            address1 = UNSET
        else:
            address1 = self.address1

        address2: Union[None, Unset, str]
        if isinstance(self.address2, Unset):
            address2 = UNSET
        else:
            address2 = self.address2

        telephone: Union[None, Unset, str]
        if isinstance(self.telephone, Unset):
            telephone = UNSET
        else:
            telephone = self.telephone

        rental_telephone: Union[None, Unset, str]
        if isinstance(self.rental_telephone, Unset):
            rental_telephone = UNSET
        else:
            rental_telephone = self.rental_telephone

        mobile: Union[None, Unset, str]
        if isinstance(self.mobile, Unset):
            mobile = UNSET
        else:
            mobile = self.mobile

        fax: Union[None, Unset, str]
        if isinstance(self.fax, Unset):
            fax = UNSET
        else:
            fax = self.fax

        state: Union[None, Unset, str]
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        email: Union[None, Unset, str]
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        rental_email: Union[None, Unset, str]
        if isinstance(self.rental_email, Unset):
            rental_email = UNSET
        else:
            rental_email = self.rental_email

        home_page_search_options: Union[None, Unset, str]
        if isinstance(self.home_page_search_options, Unset):
            home_page_search_options = UNSET
        else:
            home_page_search_options = self.home_page_search_options

        account_type: Union[None, Unset, int]
        if isinstance(self.account_type, Unset):
            account_type = UNSET
        else:
            account_type = self.account_type

        number_for_sale: Union[None, Unset, int]
        if isinstance(self.number_for_sale, Unset):
            number_for_sale = UNSET
        else:
            number_for_sale = self.number_for_sale

        number_for_rent: Union[None, Unset, int]
        if isinstance(self.number_for_rent, Unset):
            number_for_rent = UNSET
        else:
            number_for_rent = self.number_for_rent

        domain_url: Union[None, Unset, str]
        if isinstance(self.domain_url, Unset):
            domain_url = UNSET
        else:
            domain_url = self.domain_url

        show_tab_sold_last_year: Union[None, Unset, bool]
        if isinstance(self.show_tab_sold_last_year, Unset):
            show_tab_sold_last_year = UNSET
        else:
            show_tab_sold_last_year = self.show_tab_sold_last_year

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if in_suburb is not UNSET:
            field_dict["inSuburb"] = in_suburb
        if query_suburb is not UNSET:
            field_dict["querySuburb"] = query_suburb
        if has_recently_sold is not UNSET:
            field_dict["hasRecentlySold"] = has_recently_sold
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if suburb is not UNSET:
            field_dict["suburb"] = suburb
        if logo_url is not UNSET:
            field_dict["logoUrl"] = logo_url
        if base_url is not UNSET:
            field_dict["baseUrl"] = base_url
        if address1 is not UNSET:
            field_dict["address1"] = address1
        if address2 is not UNSET:
            field_dict["address2"] = address2
        if telephone is not UNSET:
            field_dict["telephone"] = telephone
        if rental_telephone is not UNSET:
            field_dict["rentalTelephone"] = rental_telephone
        if mobile is not UNSET:
            field_dict["mobile"] = mobile
        if fax is not UNSET:
            field_dict["fax"] = fax
        if state is not UNSET:
            field_dict["state"] = state
        if description is not UNSET:
            field_dict["description"] = description
        if email is not UNSET:
            field_dict["email"] = email
        if rental_email is not UNSET:
            field_dict["rentalEmail"] = rental_email
        if home_page_search_options is not UNSET:
            field_dict["homePageSearchOptions"] = home_page_search_options
        if account_type is not UNSET:
            field_dict["accountType"] = account_type
        if number_for_sale is not UNSET:
            field_dict["numberForSale"] = number_for_sale
        if number_for_rent is not UNSET:
            field_dict["numberForRent"] = number_for_rent
        if domain_url is not UNSET:
            field_dict["domainUrl"] = domain_url
        if show_tab_sold_last_year is not UNSET:
            field_dict["showTabSoldLastYear"] = show_tab_sold_last_year

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_in_suburb(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        in_suburb = _parse_in_suburb(d.pop("inSuburb", UNSET))

        def _parse_query_suburb(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        query_suburb = _parse_query_suburb(d.pop("querySuburb", UNSET))

        def _parse_has_recently_sold(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        has_recently_sold = _parse_has_recently_sold(d.pop("hasRecentlySold", UNSET))

        def _parse_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_suburb(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        suburb = _parse_suburb(d.pop("suburb", UNSET))

        def _parse_logo_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        logo_url = _parse_logo_url(d.pop("logoUrl", UNSET))

        def _parse_base_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        base_url = _parse_base_url(d.pop("baseUrl", UNSET))

        def _parse_address1(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        address1 = _parse_address1(d.pop("address1", UNSET))

        def _parse_address2(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        address2 = _parse_address2(d.pop("address2", UNSET))

        def _parse_telephone(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        telephone = _parse_telephone(d.pop("telephone", UNSET))

        def _parse_rental_telephone(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        rental_telephone = _parse_rental_telephone(d.pop("rentalTelephone", UNSET))

        def _parse_mobile(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mobile = _parse_mobile(d.pop("mobile", UNSET))

        def _parse_fax(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        fax = _parse_fax(d.pop("fax", UNSET))

        def _parse_state(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        state = _parse_state(d.pop("state", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_rental_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        rental_email = _parse_rental_email(d.pop("rentalEmail", UNSET))

        def _parse_home_page_search_options(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        home_page_search_options = _parse_home_page_search_options(d.pop("homePageSearchOptions", UNSET))

        def _parse_account_type(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        account_type = _parse_account_type(d.pop("accountType", UNSET))

        def _parse_number_for_sale(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        number_for_sale = _parse_number_for_sale(d.pop("numberForSale", UNSET))

        def _parse_number_for_rent(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        number_for_rent = _parse_number_for_rent(d.pop("numberForRent", UNSET))

        def _parse_domain_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        domain_url = _parse_domain_url(d.pop("domainUrl", UNSET))

        def _parse_show_tab_sold_last_year(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        show_tab_sold_last_year = _parse_show_tab_sold_last_year(d.pop("showTabSoldLastYear", UNSET))

        agencies_v2_agency_summary = cls(
            in_suburb=in_suburb,
            query_suburb=query_suburb,
            has_recently_sold=has_recently_sold,
            id=id,
            name=name,
            suburb=suburb,
            logo_url=logo_url,
            base_url=base_url,
            address1=address1,
            address2=address2,
            telephone=telephone,
            rental_telephone=rental_telephone,
            mobile=mobile,
            fax=fax,
            state=state,
            description=description,
            email=email,
            rental_email=rental_email,
            home_page_search_options=home_page_search_options,
            account_type=account_type,
            number_for_sale=number_for_sale,
            number_for_rent=number_for_rent,
            domain_url=domain_url,
            show_tab_sold_last_year=show_tab_sold_last_year,
        )

        return agencies_v2_agency_summary
