import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="SocialBoostV1ContractInfo")


@_attrs_define
class SocialBoostV1ContractInfo:
    """ContractInfo

    Attributes:
        id (Union[None, Unset, int]): Gets or Sets Id
        booking_product_id (Union[None, Unset, int]): Gets or Sets BookingProductId
        agency_id (Union[None, Unset, int]): Gets or Sets AgencyId
        start_date (Union[None, Unset, datetime.datetime]): Gets or Sets StartDate
        end_date (Union[None, Unset, datetime.datetime]): Gets or Sets EndDate
        finished_date (Union[None, Unset, datetime.datetime]): Gets or Sets FinishedDate
        attributes (Union[None, Unset, str]): Gets or Sets Attributes
        agent_id (Union[None, Unset, str]): Gets or Sets AgentId
        is_agent_contract (Union[None, Unset, bool]): Gets or Sets IsAgentContract
    """

    id: Union[None, Unset, int] = UNSET
    booking_product_id: Union[None, Unset, int] = UNSET
    agency_id: Union[None, Unset, int] = UNSET
    start_date: Union[None, Unset, datetime.datetime] = UNSET
    end_date: Union[None, Unset, datetime.datetime] = UNSET
    finished_date: Union[None, Unset, datetime.datetime] = UNSET
    attributes: Union[None, Unset, str] = UNSET
    agent_id: Union[None, Unset, str] = UNSET
    is_agent_contract: Union[None, Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        id: Union[None, Unset, int]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        booking_product_id: Union[None, Unset, int]
        if isinstance(self.booking_product_id, Unset):
            booking_product_id = UNSET
        else:
            booking_product_id = self.booking_product_id

        agency_id: Union[None, Unset, int]
        if isinstance(self.agency_id, Unset):
            agency_id = UNSET
        else:
            agency_id = self.agency_id

        start_date: Union[None, Unset, str]
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        elif isinstance(self.start_date, datetime.datetime):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        end_date: Union[None, Unset, str]
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.datetime):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        finished_date: Union[None, Unset, str]
        if isinstance(self.finished_date, Unset):
            finished_date = UNSET
        elif isinstance(self.finished_date, datetime.datetime):
            finished_date = self.finished_date.isoformat()
        else:
            finished_date = self.finished_date

        attributes: Union[None, Unset, str]
        if isinstance(self.attributes, Unset):
            attributes = UNSET
        else:
            attributes = self.attributes

        agent_id: Union[None, Unset, str]
        if isinstance(self.agent_id, Unset):
            agent_id = UNSET
        else:
            agent_id = self.agent_id

        is_agent_contract: Union[None, Unset, bool]
        if isinstance(self.is_agent_contract, Unset):
            is_agent_contract = UNSET
        else:
            is_agent_contract = self.is_agent_contract

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if booking_product_id is not UNSET:
            field_dict["bookingProductId"] = booking_product_id
        if agency_id is not UNSET:
            field_dict["agencyId"] = agency_id
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if finished_date is not UNSET:
            field_dict["finishedDate"] = finished_date
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if agent_id is not UNSET:
            field_dict["agentId"] = agent_id
        if is_agent_contract is not UNSET:
            field_dict["isAgentContract"] = is_agent_contract

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_booking_product_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        booking_product_id = _parse_booking_product_id(d.pop("bookingProductId", UNSET))

        def _parse_agency_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        agency_id = _parse_agency_id(d.pop("agencyId", UNSET))

        def _parse_start_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_type_0 = isoparse(data)

                return start_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        start_date = _parse_start_date(d.pop("startDate", UNSET))

        def _parse_end_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = isoparse(data)

                return end_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        end_date = _parse_end_date(d.pop("endDate", UNSET))

        def _parse_finished_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                finished_date_type_0 = isoparse(data)

                return finished_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        finished_date = _parse_finished_date(d.pop("finishedDate", UNSET))

        def _parse_attributes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        attributes = _parse_attributes(d.pop("attributes", UNSET))

        def _parse_agent_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        agent_id = _parse_agent_id(d.pop("agentId", UNSET))

        def _parse_is_agent_contract(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_agent_contract = _parse_is_agent_contract(d.pop("isAgentContract", UNSET))

        social_boost_v1_contract_info = cls(
            id=id,
            booking_product_id=booking_product_id,
            agency_id=agency_id,
            start_date=start_date,
            end_date=end_date,
            finished_date=finished_date,
            attributes=attributes,
            agent_id=agent_id,
            is_agent_contract=is_agent_contract,
        )

        return social_boost_v1_contract_info
