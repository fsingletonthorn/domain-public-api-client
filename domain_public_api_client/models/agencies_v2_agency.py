import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.agencies_v2_agency_account_type import AgenciesV2AgencyAccountType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agencies_v2_agency_contact_details import AgenciesV2AgencyContactDetails
    from ..models.agencies_v2_agency_details import AgenciesV2AgencyDetails
    from ..models.agencies_v2_agency_options import AgenciesV2AgencyOptions
    from ..models.agencies_v2_agency_profile import AgenciesV2AgencyProfile
    from ..models.agencies_v2_contact_in_agency_list import AgenciesV2ContactInAgencyList


T = TypeVar("T", bound="AgenciesV2Agency")


@_attrs_define
class AgenciesV2Agency:
    """Agency

    Attributes:
        account_type (Union[Unset, AgenciesV2AgencyAccountType]): Gets or Sets AccountType
        profile (Union[Unset, AgenciesV2AgencyProfile]): AgencyProfile
        date_updated (Union[None, Unset, datetime.datetime]): Gets or Sets DateUpdated
        name (Union[None, Unset, str]): Gets or Sets Name
        details (Union[Unset, AgenciesV2AgencyDetails]): AgencyDetails
        id (Union[None, Unset, int]): Gets or Sets Id
        cre_id (Union[None, Unset, int]): Gets or Sets CreId
        agents (Union[List['AgenciesV2ContactInAgencyList'], None, Unset]): Gets or Sets Agents
        contact_details (Union[Unset, AgenciesV2AgencyContactDetails]): AgencyContactDetails
        homepass_enabled (Union[None, Unset, bool]): Gets or Sets HomepassEnabled
        suburbs_served (Union[None, Unset, str]): Gets or Sets SuburbsServed
        subscribed_to_agency_performance_report (Union[None, Unset, bool]): Gets or Sets
            SubscribedToAgencyPerformanceReport
        agency_options (Union[Unset, AgenciesV2AgencyOptions]): AgencyOptions
        welcome_message (Union[None, Unset, str]): Gets or Sets WelcomeMessage
        ad_format (Union[None, Unset, str]): Gets or Sets AdFormat
        provider_agency_id (Union[None, Unset, str]): Gets or Sets ProviderAgencyId
    """

    account_type: Union[Unset, AgenciesV2AgencyAccountType] = UNSET
    profile: Union[Unset, "AgenciesV2AgencyProfile"] = UNSET
    date_updated: Union[None, Unset, datetime.datetime] = UNSET
    name: Union[None, Unset, str] = UNSET
    details: Union[Unset, "AgenciesV2AgencyDetails"] = UNSET
    id: Union[None, Unset, int] = UNSET
    cre_id: Union[None, Unset, int] = UNSET
    agents: Union[List["AgenciesV2ContactInAgencyList"], None, Unset] = UNSET
    contact_details: Union[Unset, "AgenciesV2AgencyContactDetails"] = UNSET
    homepass_enabled: Union[None, Unset, bool] = UNSET
    suburbs_served: Union[None, Unset, str] = UNSET
    subscribed_to_agency_performance_report: Union[None, Unset, bool] = UNSET
    agency_options: Union[Unset, "AgenciesV2AgencyOptions"] = UNSET
    welcome_message: Union[None, Unset, str] = UNSET
    ad_format: Union[None, Unset, str] = UNSET
    provider_agency_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        account_type: Union[Unset, str] = UNSET
        if not isinstance(self.account_type, Unset):
            account_type = self.account_type.value

        profile: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.profile, Unset):
            profile = self.profile.to_dict()

        date_updated: Union[None, Unset, str]
        if isinstance(self.date_updated, Unset):
            date_updated = UNSET
        elif isinstance(self.date_updated, datetime.datetime):
            date_updated = self.date_updated.isoformat()
        else:
            date_updated = self.date_updated

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        id: Union[None, Unset, int]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        cre_id: Union[None, Unset, int]
        if isinstance(self.cre_id, Unset):
            cre_id = UNSET
        else:
            cre_id = self.cre_id

        agents: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.agents, Unset):
            agents = UNSET
        elif isinstance(self.agents, list):
            agents = []
            for agents_type_0_item_data in self.agents:
                agents_type_0_item = agents_type_0_item_data.to_dict()
                agents.append(agents_type_0_item)

        else:
            agents = self.agents

        contact_details: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.contact_details, Unset):
            contact_details = self.contact_details.to_dict()

        homepass_enabled: Union[None, Unset, bool]
        if isinstance(self.homepass_enabled, Unset):
            homepass_enabled = UNSET
        else:
            homepass_enabled = self.homepass_enabled

        suburbs_served: Union[None, Unset, str]
        if isinstance(self.suburbs_served, Unset):
            suburbs_served = UNSET
        else:
            suburbs_served = self.suburbs_served

        subscribed_to_agency_performance_report: Union[None, Unset, bool]
        if isinstance(self.subscribed_to_agency_performance_report, Unset):
            subscribed_to_agency_performance_report = UNSET
        else:
            subscribed_to_agency_performance_report = self.subscribed_to_agency_performance_report

        agency_options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.agency_options, Unset):
            agency_options = self.agency_options.to_dict()

        welcome_message: Union[None, Unset, str]
        if isinstance(self.welcome_message, Unset):
            welcome_message = UNSET
        else:
            welcome_message = self.welcome_message

        ad_format: Union[None, Unset, str]
        if isinstance(self.ad_format, Unset):
            ad_format = UNSET
        else:
            ad_format = self.ad_format

        provider_agency_id: Union[None, Unset, str]
        if isinstance(self.provider_agency_id, Unset):
            provider_agency_id = UNSET
        else:
            provider_agency_id = self.provider_agency_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if account_type is not UNSET:
            field_dict["accountType"] = account_type
        if profile is not UNSET:
            field_dict["profile"] = profile
        if date_updated is not UNSET:
            field_dict["dateUpdated"] = date_updated
        if name is not UNSET:
            field_dict["name"] = name
        if details is not UNSET:
            field_dict["details"] = details
        if id is not UNSET:
            field_dict["id"] = id
        if cre_id is not UNSET:
            field_dict["creId"] = cre_id
        if agents is not UNSET:
            field_dict["agents"] = agents
        if contact_details is not UNSET:
            field_dict["contactDetails"] = contact_details
        if homepass_enabled is not UNSET:
            field_dict["homepassEnabled"] = homepass_enabled
        if suburbs_served is not UNSET:
            field_dict["suburbsServed"] = suburbs_served
        if subscribed_to_agency_performance_report is not UNSET:
            field_dict["subscribedToAgencyPerformanceReport"] = subscribed_to_agency_performance_report
        if agency_options is not UNSET:
            field_dict["agencyOptions"] = agency_options
        if welcome_message is not UNSET:
            field_dict["welcomeMessage"] = welcome_message
        if ad_format is not UNSET:
            field_dict["adFormat"] = ad_format
        if provider_agency_id is not UNSET:
            field_dict["providerAgencyId"] = provider_agency_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.agencies_v2_agency_contact_details import AgenciesV2AgencyContactDetails
        from ..models.agencies_v2_agency_details import AgenciesV2AgencyDetails
        from ..models.agencies_v2_agency_options import AgenciesV2AgencyOptions
        from ..models.agencies_v2_agency_profile import AgenciesV2AgencyProfile
        from ..models.agencies_v2_contact_in_agency_list import AgenciesV2ContactInAgencyList

        d = src_dict.copy()
        _account_type = d.pop("accountType", UNSET)
        account_type: Union[Unset, AgenciesV2AgencyAccountType]
        if isinstance(_account_type, Unset):
            account_type = UNSET
        else:
            account_type = AgenciesV2AgencyAccountType(_account_type)

        _profile = d.pop("profile", UNSET)
        profile: Union[Unset, AgenciesV2AgencyProfile]
        if isinstance(_profile, Unset):
            profile = UNSET
        else:
            profile = AgenciesV2AgencyProfile.from_dict(_profile)

        def _parse_date_updated(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_updated_type_0 = isoparse(data)

                return date_updated_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        date_updated = _parse_date_updated(d.pop("dateUpdated", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        _details = d.pop("details", UNSET)
        details: Union[Unset, AgenciesV2AgencyDetails]
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = AgenciesV2AgencyDetails.from_dict(_details)

        def _parse_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_cre_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        cre_id = _parse_cre_id(d.pop("creId", UNSET))

        def _parse_agents(data: object) -> Union[List["AgenciesV2ContactInAgencyList"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                agents_type_0 = []
                _agents_type_0 = data
                for agents_type_0_item_data in _agents_type_0:
                    agents_type_0_item = AgenciesV2ContactInAgencyList.from_dict(agents_type_0_item_data)

                    agents_type_0.append(agents_type_0_item)

                return agents_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["AgenciesV2ContactInAgencyList"], None, Unset], data)

        agents = _parse_agents(d.pop("agents", UNSET))

        _contact_details = d.pop("contactDetails", UNSET)
        contact_details: Union[Unset, AgenciesV2AgencyContactDetails]
        if isinstance(_contact_details, Unset):
            contact_details = UNSET
        else:
            contact_details = AgenciesV2AgencyContactDetails.from_dict(_contact_details)

        def _parse_homepass_enabled(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        homepass_enabled = _parse_homepass_enabled(d.pop("homepassEnabled", UNSET))

        def _parse_suburbs_served(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        suburbs_served = _parse_suburbs_served(d.pop("suburbsServed", UNSET))

        def _parse_subscribed_to_agency_performance_report(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        subscribed_to_agency_performance_report = _parse_subscribed_to_agency_performance_report(
            d.pop("subscribedToAgencyPerformanceReport", UNSET)
        )

        _agency_options = d.pop("agencyOptions", UNSET)
        agency_options: Union[Unset, AgenciesV2AgencyOptions]
        if isinstance(_agency_options, Unset):
            agency_options = UNSET
        else:
            agency_options = AgenciesV2AgencyOptions.from_dict(_agency_options)

        def _parse_welcome_message(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        welcome_message = _parse_welcome_message(d.pop("welcomeMessage", UNSET))

        def _parse_ad_format(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        ad_format = _parse_ad_format(d.pop("adFormat", UNSET))

        def _parse_provider_agency_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        provider_agency_id = _parse_provider_agency_id(d.pop("providerAgencyId", UNSET))

        agencies_v2_agency = cls(
            account_type=account_type,
            profile=profile,
            date_updated=date_updated,
            name=name,
            details=details,
            id=id,
            cre_id=cre_id,
            agents=agents,
            contact_details=contact_details,
            homepass_enabled=homepass_enabled,
            suburbs_served=suburbs_served,
            subscribed_to_agency_performance_report=subscribed_to_agency_performance_report,
            agency_options=agency_options,
            welcome_message=welcome_message,
            ad_format=ad_format,
            provider_agency_id=provider_agency_id,
        )

        return agencies_v2_agency
