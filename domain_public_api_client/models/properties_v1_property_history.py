from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.properties_v1_rental_activity import PropertiesV1RentalActivity
    from ..models.properties_v1_sale_activity import PropertiesV1SaleActivity


T = TypeVar("T", bound="PropertiesV1PropertyHistory")


@_attrs_define
class PropertiesV1PropertyHistory:
    """
    Attributes:
        rentals (Union[List['PropertiesV1RentalActivity'], None, Unset]):
        sales (Union[List['PropertiesV1SaleActivity'], None, Unset]):
        suppress (Union[None, Unset, bool]): Gets or Sets Suppress
    """

    rentals: Union[List["PropertiesV1RentalActivity"], None, Unset] = UNSET
    sales: Union[List["PropertiesV1SaleActivity"], None, Unset] = UNSET
    suppress: Union[None, Unset, bool] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        rentals: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.rentals, Unset):
            rentals = UNSET
        elif isinstance(self.rentals, list):
            rentals = []
            for rentals_type_0_item_data in self.rentals:
                rentals_type_0_item = rentals_type_0_item_data.to_dict()
                rentals.append(rentals_type_0_item)

        else:
            rentals = self.rentals

        sales: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.sales, Unset):
            sales = UNSET
        elif isinstance(self.sales, list):
            sales = []
            for sales_type_0_item_data in self.sales:
                sales_type_0_item = sales_type_0_item_data.to_dict()
                sales.append(sales_type_0_item)

        else:
            sales = self.sales

        suppress: Union[None, Unset, bool]
        if isinstance(self.suppress, Unset):
            suppress = UNSET
        else:
            suppress = self.suppress

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if rentals is not UNSET:
            field_dict["rentals"] = rentals
        if sales is not UNSET:
            field_dict["sales"] = sales
        if suppress is not UNSET:
            field_dict["suppress"] = suppress

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.properties_v1_rental_activity import PropertiesV1RentalActivity
        from ..models.properties_v1_sale_activity import PropertiesV1SaleActivity

        d = src_dict.copy()

        def _parse_rentals(data: object) -> Union[List["PropertiesV1RentalActivity"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                rentals_type_0 = []
                _rentals_type_0 = data
                for rentals_type_0_item_data in _rentals_type_0:
                    rentals_type_0_item = PropertiesV1RentalActivity.from_dict(rentals_type_0_item_data)

                    rentals_type_0.append(rentals_type_0_item)

                return rentals_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["PropertiesV1RentalActivity"], None, Unset], data)

        rentals = _parse_rentals(d.pop("rentals", UNSET))

        def _parse_sales(data: object) -> Union[List["PropertiesV1SaleActivity"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                sales_type_0 = []
                _sales_type_0 = data
                for sales_type_0_item_data in _sales_type_0:
                    sales_type_0_item = PropertiesV1SaleActivity.from_dict(sales_type_0_item_data)

                    sales_type_0.append(sales_type_0_item)

                return sales_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["PropertiesV1SaleActivity"], None, Unset], data)

        sales = _parse_sales(d.pop("sales", UNSET))

        def _parse_suppress(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        suppress = _parse_suppress(d.pop("suppress", UNSET))

        properties_v1_property_history = cls(
            rentals=rentals,
            sales=sales,
            suppress=suppress,
        )

        return properties_v1_property_history
