from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_avm_v1_address import DomainAvmV1Address


T = TypeVar("T", bound="DomainAvmV1Request")


@_attrs_define
class DomainAvmV1Request:
    """The model used to request a bank grade valuation.

    Attributes:
        val_ex_job_number (str): The client identification for the valuation transaction.
        address (Union[Unset, DomainAvmV1Address]): The Address model used.
        purchase_price (Union[None, Unset, int]): The purchase price of the property to nearest AUD.
        property_type (Union[None, Unset, str]): Property type to be used when estimating value of property. Valid
            values: [House, Unit].
        landarea (Union[None, Unset, int]): Land area in square meters to be used when estimating value of property, for
            houses only not units.
        bedrooms (Union[None, Unset, int]): Number of bedrooms to be used when estimating value of property.
        bathrooms (Union[None, Unset, int]): Number of bathrooms to be used when estimating value of property.
        carparks (Union[None, Unset, int]): Number of carparks to be used when estimating value of property.
        gnaf_p_id (Union[None, Unset, str]): Geocoded National Address File. A G-NAF Persistent ID is a unique
            combination of address detail used to identify each property in Australia.
    """

    val_ex_job_number: str
    address: Union[Unset, "DomainAvmV1Address"] = UNSET
    purchase_price: Union[None, Unset, int] = UNSET
    property_type: Union[None, Unset, str] = UNSET
    landarea: Union[None, Unset, int] = UNSET
    bedrooms: Union[None, Unset, int] = UNSET
    bathrooms: Union[None, Unset, int] = UNSET
    carparks: Union[None, Unset, int] = UNSET
    gnaf_p_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        val_ex_job_number = self.val_ex_job_number

        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        purchase_price: Union[None, Unset, int]
        if isinstance(self.purchase_price, Unset):
            purchase_price = UNSET
        else:
            purchase_price = self.purchase_price

        property_type: Union[None, Unset, str]
        if isinstance(self.property_type, Unset):
            property_type = UNSET
        else:
            property_type = self.property_type

        landarea: Union[None, Unset, int]
        if isinstance(self.landarea, Unset):
            landarea = UNSET
        else:
            landarea = self.landarea

        bedrooms: Union[None, Unset, int]
        if isinstance(self.bedrooms, Unset):
            bedrooms = UNSET
        else:
            bedrooms = self.bedrooms

        bathrooms: Union[None, Unset, int]
        if isinstance(self.bathrooms, Unset):
            bathrooms = UNSET
        else:
            bathrooms = self.bathrooms

        carparks: Union[None, Unset, int]
        if isinstance(self.carparks, Unset):
            carparks = UNSET
        else:
            carparks = self.carparks

        gnaf_p_id: Union[None, Unset, str]
        if isinstance(self.gnaf_p_id, Unset):
            gnaf_p_id = UNSET
        else:
            gnaf_p_id = self.gnaf_p_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "valExJobNumber": val_ex_job_number,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address
        if purchase_price is not UNSET:
            field_dict["purchasePrice"] = purchase_price
        if property_type is not UNSET:
            field_dict["propertyType"] = property_type
        if landarea is not UNSET:
            field_dict["landarea"] = landarea
        if bedrooms is not UNSET:
            field_dict["bedrooms"] = bedrooms
        if bathrooms is not UNSET:
            field_dict["bathrooms"] = bathrooms
        if carparks is not UNSET:
            field_dict["carparks"] = carparks
        if gnaf_p_id is not UNSET:
            field_dict["gnafPId"] = gnaf_p_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_avm_v1_address import DomainAvmV1Address

        d = src_dict.copy()
        val_ex_job_number = d.pop("valExJobNumber")

        _address = d.pop("address", UNSET)
        address: Union[Unset, DomainAvmV1Address]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = DomainAvmV1Address.from_dict(_address)

        def _parse_purchase_price(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        purchase_price = _parse_purchase_price(d.pop("purchasePrice", UNSET))

        def _parse_property_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        property_type = _parse_property_type(d.pop("propertyType", UNSET))

        def _parse_landarea(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        landarea = _parse_landarea(d.pop("landarea", UNSET))

        def _parse_bedrooms(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        bedrooms = _parse_bedrooms(d.pop("bedrooms", UNSET))

        def _parse_bathrooms(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        bathrooms = _parse_bathrooms(d.pop("bathrooms", UNSET))

        def _parse_carparks(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        carparks = _parse_carparks(d.pop("carparks", UNSET))

        def _parse_gnaf_p_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        gnaf_p_id = _parse_gnaf_p_id(d.pop("gnafPId", UNSET))

        domain_avm_v1_request = cls(
            val_ex_job_number=val_ex_job_number,
            address=address,
            purchase_price=purchase_price,
            property_type=property_type,
            landarea=landarea,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            carparks=carparks,
            gnaf_p_id=gnaf_p_id,
        )

        return domain_avm_v1_request
