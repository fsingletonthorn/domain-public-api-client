from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agencies_v2_email_domain import AgenciesV2EmailDomain
    from ..models.agencies_v2_email_phone import AgenciesV2EmailPhone
    from ..models.agencies_v2_general_agency_contact_details import AgenciesV2GeneralAgencyContactDetails


T = TypeVar("T", bound="AgenciesV2AgencyContactDetails")


@_attrs_define
class AgenciesV2AgencyContactDetails:
    """AgencyContactDetails

    Attributes:
        business_sale (Union[Unset, AgenciesV2EmailPhone]): EmailPhone
        business_rent (Union[Unset, AgenciesV2EmailPhone]): EmailPhone
        commercial_lease (Union[Unset, AgenciesV2EmailPhone]): EmailPhone
        commercial_sale (Union[Unset, AgenciesV2EmailPhone]): EmailPhone
        email_domains (Union[List['AgenciesV2EmailDomain'], None, Unset]): Gets or Sets EmailDomains
        general (Union[Unset, AgenciesV2GeneralAgencyContactDetails]): GeneralAgencyContactDetails
        residential_rent (Union[Unset, AgenciesV2EmailPhone]): EmailPhone
        residential_sale (Union[Unset, AgenciesV2EmailPhone]): EmailPhone
    """

    business_sale: Union[Unset, "AgenciesV2EmailPhone"] = UNSET
    business_rent: Union[Unset, "AgenciesV2EmailPhone"] = UNSET
    commercial_lease: Union[Unset, "AgenciesV2EmailPhone"] = UNSET
    commercial_sale: Union[Unset, "AgenciesV2EmailPhone"] = UNSET
    email_domains: Union[List["AgenciesV2EmailDomain"], None, Unset] = UNSET
    general: Union[Unset, "AgenciesV2GeneralAgencyContactDetails"] = UNSET
    residential_rent: Union[Unset, "AgenciesV2EmailPhone"] = UNSET
    residential_sale: Union[Unset, "AgenciesV2EmailPhone"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        business_sale: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.business_sale, Unset):
            business_sale = self.business_sale.to_dict()

        business_rent: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.business_rent, Unset):
            business_rent = self.business_rent.to_dict()

        commercial_lease: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.commercial_lease, Unset):
            commercial_lease = self.commercial_lease.to_dict()

        commercial_sale: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.commercial_sale, Unset):
            commercial_sale = self.commercial_sale.to_dict()

        email_domains: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.email_domains, Unset):
            email_domains = UNSET
        elif isinstance(self.email_domains, list):
            email_domains = []
            for email_domains_type_0_item_data in self.email_domains:
                email_domains_type_0_item = email_domains_type_0_item_data.to_dict()
                email_domains.append(email_domains_type_0_item)

        else:
            email_domains = self.email_domains

        general: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.general, Unset):
            general = self.general.to_dict()

        residential_rent: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.residential_rent, Unset):
            residential_rent = self.residential_rent.to_dict()

        residential_sale: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.residential_sale, Unset):
            residential_sale = self.residential_sale.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if business_sale is not UNSET:
            field_dict["businessSale"] = business_sale
        if business_rent is not UNSET:
            field_dict["businessRent"] = business_rent
        if commercial_lease is not UNSET:
            field_dict["commercialLease"] = commercial_lease
        if commercial_sale is not UNSET:
            field_dict["commercialSale"] = commercial_sale
        if email_domains is not UNSET:
            field_dict["emailDomains"] = email_domains
        if general is not UNSET:
            field_dict["general"] = general
        if residential_rent is not UNSET:
            field_dict["residentialRent"] = residential_rent
        if residential_sale is not UNSET:
            field_dict["residentialSale"] = residential_sale

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.agencies_v2_email_domain import AgenciesV2EmailDomain
        from ..models.agencies_v2_email_phone import AgenciesV2EmailPhone
        from ..models.agencies_v2_general_agency_contact_details import AgenciesV2GeneralAgencyContactDetails

        d = src_dict.copy()
        _business_sale = d.pop("businessSale", UNSET)
        business_sale: Union[Unset, AgenciesV2EmailPhone]
        if isinstance(_business_sale, Unset):
            business_sale = UNSET
        else:
            business_sale = AgenciesV2EmailPhone.from_dict(_business_sale)

        _business_rent = d.pop("businessRent", UNSET)
        business_rent: Union[Unset, AgenciesV2EmailPhone]
        if isinstance(_business_rent, Unset):
            business_rent = UNSET
        else:
            business_rent = AgenciesV2EmailPhone.from_dict(_business_rent)

        _commercial_lease = d.pop("commercialLease", UNSET)
        commercial_lease: Union[Unset, AgenciesV2EmailPhone]
        if isinstance(_commercial_lease, Unset):
            commercial_lease = UNSET
        else:
            commercial_lease = AgenciesV2EmailPhone.from_dict(_commercial_lease)

        _commercial_sale = d.pop("commercialSale", UNSET)
        commercial_sale: Union[Unset, AgenciesV2EmailPhone]
        if isinstance(_commercial_sale, Unset):
            commercial_sale = UNSET
        else:
            commercial_sale = AgenciesV2EmailPhone.from_dict(_commercial_sale)

        def _parse_email_domains(data: object) -> Union[List["AgenciesV2EmailDomain"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                email_domains_type_0 = []
                _email_domains_type_0 = data
                for email_domains_type_0_item_data in _email_domains_type_0:
                    email_domains_type_0_item = AgenciesV2EmailDomain.from_dict(email_domains_type_0_item_data)

                    email_domains_type_0.append(email_domains_type_0_item)

                return email_domains_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["AgenciesV2EmailDomain"], None, Unset], data)

        email_domains = _parse_email_domains(d.pop("emailDomains", UNSET))

        _general = d.pop("general", UNSET)
        general: Union[Unset, AgenciesV2GeneralAgencyContactDetails]
        if isinstance(_general, Unset):
            general = UNSET
        else:
            general = AgenciesV2GeneralAgencyContactDetails.from_dict(_general)

        _residential_rent = d.pop("residentialRent", UNSET)
        residential_rent: Union[Unset, AgenciesV2EmailPhone]
        if isinstance(_residential_rent, Unset):
            residential_rent = UNSET
        else:
            residential_rent = AgenciesV2EmailPhone.from_dict(_residential_rent)

        _residential_sale = d.pop("residentialSale", UNSET)
        residential_sale: Union[Unset, AgenciesV2EmailPhone]
        if isinstance(_residential_sale, Unset):
            residential_sale = UNSET
        else:
            residential_sale = AgenciesV2EmailPhone.from_dict(_residential_sale)

        agencies_v2_agency_contact_details = cls(
            business_sale=business_sale,
            business_rent=business_rent,
            commercial_lease=commercial_lease,
            commercial_sale=commercial_sale,
            email_domains=email_domains,
            general=general,
            residential_rent=residential_rent,
            residential_sale=residential_sale,
        )

        return agencies_v2_agency_contact_details
