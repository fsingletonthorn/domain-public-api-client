from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="AgenciesV2AgencyOptions")


@_attrs_define
class AgenciesV2AgencyOptions:
    """AgencyOptions

    Attributes:
        sale_listings_gst_option (int): Gets or Sets SaleListingsGstOption
        lease_listings_gst_option (int): Gets or Sets LeaseListingsGstOption
        receive_look_for_property_requests (bool): Gets or Sets ReceiveLookForPropertyRequests
        receive_sell_property_requests (bool): Gets or Sets ReceiveSellPropertyRequests
        receive_property_valuation_requests (bool): Gets or Sets ReceivePropertyValuationRequests
        agent_directory_listing (bool): Gets or Sets AgentDirectoryListing
    """

    sale_listings_gst_option: int
    lease_listings_gst_option: int
    receive_look_for_property_requests: bool
    receive_sell_property_requests: bool
    receive_property_valuation_requests: bool
    agent_directory_listing: bool

    def to_dict(self) -> Dict[str, Any]:
        sale_listings_gst_option = self.sale_listings_gst_option

        lease_listings_gst_option = self.lease_listings_gst_option

        receive_look_for_property_requests = self.receive_look_for_property_requests

        receive_sell_property_requests = self.receive_sell_property_requests

        receive_property_valuation_requests = self.receive_property_valuation_requests

        agent_directory_listing = self.agent_directory_listing

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "saleListingsGstOption": sale_listings_gst_option,
                "leaseListingsGstOption": lease_listings_gst_option,
                "receiveLookForPropertyRequests": receive_look_for_property_requests,
                "receiveSellPropertyRequests": receive_sell_property_requests,
                "receivePropertyValuationRequests": receive_property_valuation_requests,
                "agentDirectoryListing": agent_directory_listing,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sale_listings_gst_option = d.pop("saleListingsGstOption")

        lease_listings_gst_option = d.pop("leaseListingsGstOption")

        receive_look_for_property_requests = d.pop("receiveLookForPropertyRequests")

        receive_sell_property_requests = d.pop("receiveSellPropertyRequests")

        receive_property_valuation_requests = d.pop("receivePropertyValuationRequests")

        agent_directory_listing = d.pop("agentDirectoryListing")

        agencies_v2_agency_options = cls(
            sale_listings_gst_option=sale_listings_gst_option,
            lease_listings_gst_option=lease_listings_gst_option,
            receive_look_for_property_requests=receive_look_for_property_requests,
            receive_sell_property_requests=receive_sell_property_requests,
            receive_property_valuation_requests=receive_property_valuation_requests,
            agent_directory_listing=agent_directory_listing,
        )

        return agencies_v2_agency_options
