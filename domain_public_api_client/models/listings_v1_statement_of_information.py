from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.listings_v1_basic_price import ListingsV1BasicPrice
    from ..models.listings_v1_comparable_data import ListingsV1ComparableData
    from ..models.listings_v1_median_price_data import ListingsV1MedianPriceData


T = TypeVar("T", bound="ListingsV1StatementOfInformation")


@_attrs_define
class ListingsV1StatementOfInformation:
    """Statement of Information  Regarding sale listing

    Attributes:
        estimated_price (Union[Unset, ListingsV1BasicPrice]): Basic price information
        comparable_data (Union[Unset, ListingsV1ComparableData]): Information regarding the past comparable property
            sales that influenced the setting of the estimation price
        suburb_median_price (Union[Unset, ListingsV1MedianPriceData]): Information regarding median house/unit price
            for the suburb
        documentation_url (Union[None, Unset, str]): Link to the statement of information documentation file
    """

    estimated_price: Union[Unset, "ListingsV1BasicPrice"] = UNSET
    comparable_data: Union[Unset, "ListingsV1ComparableData"] = UNSET
    suburb_median_price: Union[Unset, "ListingsV1MedianPriceData"] = UNSET
    documentation_url: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        estimated_price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.estimated_price, Unset):
            estimated_price = self.estimated_price.to_dict()

        comparable_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.comparable_data, Unset):
            comparable_data = self.comparable_data.to_dict()

        suburb_median_price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.suburb_median_price, Unset):
            suburb_median_price = self.suburb_median_price.to_dict()

        documentation_url: Union[None, Unset, str]
        if isinstance(self.documentation_url, Unset):
            documentation_url = UNSET
        else:
            documentation_url = self.documentation_url

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if estimated_price is not UNSET:
            field_dict["estimatedPrice"] = estimated_price
        if comparable_data is not UNSET:
            field_dict["comparableData"] = comparable_data
        if suburb_median_price is not UNSET:
            field_dict["suburbMedianPrice"] = suburb_median_price
        if documentation_url is not UNSET:
            field_dict["documentationUrl"] = documentation_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.listings_v1_basic_price import ListingsV1BasicPrice
        from ..models.listings_v1_comparable_data import ListingsV1ComparableData
        from ..models.listings_v1_median_price_data import ListingsV1MedianPriceData

        d = src_dict.copy()
        _estimated_price = d.pop("estimatedPrice", UNSET)
        estimated_price: Union[Unset, ListingsV1BasicPrice]
        if isinstance(_estimated_price, Unset):
            estimated_price = UNSET
        else:
            estimated_price = ListingsV1BasicPrice.from_dict(_estimated_price)

        _comparable_data = d.pop("comparableData", UNSET)
        comparable_data: Union[Unset, ListingsV1ComparableData]
        if isinstance(_comparable_data, Unset):
            comparable_data = UNSET
        else:
            comparable_data = ListingsV1ComparableData.from_dict(_comparable_data)

        _suburb_median_price = d.pop("suburbMedianPrice", UNSET)
        suburb_median_price: Union[Unset, ListingsV1MedianPriceData]
        if isinstance(_suburb_median_price, Unset):
            suburb_median_price = UNSET
        else:
            suburb_median_price = ListingsV1MedianPriceData.from_dict(_suburb_median_price)

        def _parse_documentation_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        documentation_url = _parse_documentation_url(d.pop("documentationUrl", UNSET))

        listings_v1_statement_of_information = cls(
            estimated_price=estimated_price,
            comparable_data=comparable_data,
            suburb_median_price=suburb_median_price,
            documentation_url=documentation_url,
        )

        return listings_v1_statement_of_information
