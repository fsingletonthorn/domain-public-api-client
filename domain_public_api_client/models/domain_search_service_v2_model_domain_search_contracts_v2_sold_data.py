import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.domain_search_service_v2_model_domain_search_contracts_v2_sold_data_sale_method import (
    DomainSearchServiceV2ModelDomainSearchContractsV2SoldDataSaleMethod,
)
from ..models.domain_search_service_v2_model_domain_search_contracts_v2_sold_data_source import (
    DomainSearchServiceV2ModelDomainSearchContractsV2SoldDataSource,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DomainSearchServiceV2ModelDomainSearchContractsV2SoldData")


@_attrs_define
class DomainSearchServiceV2ModelDomainSearchContractsV2SoldData:
    """
    Attributes:
        source (Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2SoldDataSource]):
        sale_method (Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2SoldDataSaleMethod]):
        sold_date (Union[Unset, datetime.datetime]):
        sold_price (Union[Unset, int]):
    """

    source: Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2SoldDataSource] = UNSET
    sale_method: Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2SoldDataSaleMethod] = UNSET
    sold_date: Union[Unset, datetime.datetime] = UNSET
    sold_price: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        sale_method: Union[Unset, str] = UNSET
        if not isinstance(self.sale_method, Unset):
            sale_method = self.sale_method.value

        sold_date: Union[Unset, str] = UNSET
        if not isinstance(self.sold_date, Unset):
            sold_date = self.sold_date.isoformat()

        sold_price = self.sold_price

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source is not UNSET:
            field_dict["source"] = source
        if sale_method is not UNSET:
            field_dict["saleMethod"] = sale_method
        if sold_date is not UNSET:
            field_dict["soldDate"] = sold_date
        if sold_price is not UNSET:
            field_dict["soldPrice"] = sold_price

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _source = d.pop("source", UNSET)
        source: Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2SoldDataSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = DomainSearchServiceV2ModelDomainSearchContractsV2SoldDataSource(_source)

        _sale_method = d.pop("saleMethod", UNSET)
        sale_method: Union[Unset, DomainSearchServiceV2ModelDomainSearchContractsV2SoldDataSaleMethod]
        if isinstance(_sale_method, Unset):
            sale_method = UNSET
        else:
            sale_method = DomainSearchServiceV2ModelDomainSearchContractsV2SoldDataSaleMethod(_sale_method)

        _sold_date = d.pop("soldDate", UNSET)
        sold_date: Union[Unset, datetime.datetime]
        if isinstance(_sold_date, Unset):
            sold_date = UNSET
        else:
            sold_date = isoparse(_sold_date)

        sold_price = d.pop("soldPrice", UNSET)

        domain_search_service_v2_model_domain_search_contracts_v2_sold_data = cls(
            source=source,
            sale_method=sale_method,
            sold_date=sold_date,
            sold_price=sold_price,
        )

        domain_search_service_v2_model_domain_search_contracts_v2_sold_data.additional_properties = d
        return domain_search_service_v2_model_domain_search_contracts_v2_sold_data

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
