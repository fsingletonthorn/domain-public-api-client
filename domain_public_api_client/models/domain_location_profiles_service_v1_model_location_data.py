from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_location_profiles_service_v1_model_location_data_property_categories import (
        DomainLocationProfilesServiceV1ModelLocationDataPropertyCategories,
    )


T = TypeVar("T", bound="DomainLocationProfilesServiceV1ModelLocationData")


@_attrs_define
class DomainLocationProfilesServiceV1ModelLocationData:
    """
    Attributes:
        studios_for_rent (Union[Unset, int]):
        terraced_houses_for_sale (Union[Unset, int]):
        semi_detached_houses_for_sale (Union[Unset, int]):
        townhouses_for_rent (Union[Unset, int]):
        apartments_and_units_for_sale (Union[Unset, int]):
        apartments_and_units_for_rent (Union[Unset, int]):
        villas_for_sale (Union[Unset, int]):
        duplexes_for_sale (Union[Unset, int]):
        semi_detached_houses_for_rent (Union[Unset, int]):
        studios_for_sale (Union[Unset, int]):
        single_percentage (Union[Unset, float]):
        most_common_age_bracket (Union[Unset, str]):
        renter_percentage (Union[Unset, float]):
        penthouses_for_sale (Union[Unset, int]):
        villas_for_rent (Union[Unset, int]):
        duplexes_for_rent (Union[Unset, int]):
        houses_for_sale (Union[Unset, int]):
        owner_occupier_percentage (Union[Unset, float]):
        property_categories (Union[Unset, List['DomainLocationProfilesServiceV1ModelLocationDataPropertyCategories']]):
        population (Union[Unset, float]):
        penthouses_for_rent (Union[Unset, int]):
        townhouses_for_sale (Union[Unset, int]):
        terraced_houses_for_rent (Union[Unset, int]):
        married_percentage (Union[Unset, float]):
        houses_for_rent (Union[Unset, int]):
        block_of_units_for_sale (Union[Unset, int]):
    """

    studios_for_rent: Union[Unset, int] = UNSET
    terraced_houses_for_sale: Union[Unset, int] = UNSET
    semi_detached_houses_for_sale: Union[Unset, int] = UNSET
    townhouses_for_rent: Union[Unset, int] = UNSET
    apartments_and_units_for_sale: Union[Unset, int] = UNSET
    apartments_and_units_for_rent: Union[Unset, int] = UNSET
    villas_for_sale: Union[Unset, int] = UNSET
    duplexes_for_sale: Union[Unset, int] = UNSET
    semi_detached_houses_for_rent: Union[Unset, int] = UNSET
    studios_for_sale: Union[Unset, int] = UNSET
    single_percentage: Union[Unset, float] = UNSET
    most_common_age_bracket: Union[Unset, str] = UNSET
    renter_percentage: Union[Unset, float] = UNSET
    penthouses_for_sale: Union[Unset, int] = UNSET
    villas_for_rent: Union[Unset, int] = UNSET
    duplexes_for_rent: Union[Unset, int] = UNSET
    houses_for_sale: Union[Unset, int] = UNSET
    owner_occupier_percentage: Union[Unset, float] = UNSET
    property_categories: Union[Unset, List["DomainLocationProfilesServiceV1ModelLocationDataPropertyCategories"]] = (
        UNSET
    )
    population: Union[Unset, float] = UNSET
    penthouses_for_rent: Union[Unset, int] = UNSET
    townhouses_for_sale: Union[Unset, int] = UNSET
    terraced_houses_for_rent: Union[Unset, int] = UNSET
    married_percentage: Union[Unset, float] = UNSET
    houses_for_rent: Union[Unset, int] = UNSET
    block_of_units_for_sale: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        studios_for_rent = self.studios_for_rent

        terraced_houses_for_sale = self.terraced_houses_for_sale

        semi_detached_houses_for_sale = self.semi_detached_houses_for_sale

        townhouses_for_rent = self.townhouses_for_rent

        apartments_and_units_for_sale = self.apartments_and_units_for_sale

        apartments_and_units_for_rent = self.apartments_and_units_for_rent

        villas_for_sale = self.villas_for_sale

        duplexes_for_sale = self.duplexes_for_sale

        semi_detached_houses_for_rent = self.semi_detached_houses_for_rent

        studios_for_sale = self.studios_for_sale

        single_percentage = self.single_percentage

        most_common_age_bracket = self.most_common_age_bracket

        renter_percentage = self.renter_percentage

        penthouses_for_sale = self.penthouses_for_sale

        villas_for_rent = self.villas_for_rent

        duplexes_for_rent = self.duplexes_for_rent

        houses_for_sale = self.houses_for_sale

        owner_occupier_percentage = self.owner_occupier_percentage

        property_categories: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.property_categories, Unset):
            property_categories = []
            for property_categories_item_data in self.property_categories:
                property_categories_item = property_categories_item_data.to_dict()
                property_categories.append(property_categories_item)

        population = self.population

        penthouses_for_rent = self.penthouses_for_rent

        townhouses_for_sale = self.townhouses_for_sale

        terraced_houses_for_rent = self.terraced_houses_for_rent

        married_percentage = self.married_percentage

        houses_for_rent = self.houses_for_rent

        block_of_units_for_sale = self.block_of_units_for_sale

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if studios_for_rent is not UNSET:
            field_dict["studiosForRent"] = studios_for_rent
        if terraced_houses_for_sale is not UNSET:
            field_dict["terracedHousesForSale"] = terraced_houses_for_sale
        if semi_detached_houses_for_sale is not UNSET:
            field_dict["semiDetachedHousesForSale"] = semi_detached_houses_for_sale
        if townhouses_for_rent is not UNSET:
            field_dict["townhousesForRent"] = townhouses_for_rent
        if apartments_and_units_for_sale is not UNSET:
            field_dict["apartmentsAndUnitsForSale"] = apartments_and_units_for_sale
        if apartments_and_units_for_rent is not UNSET:
            field_dict["apartmentsAndUnitsForRent"] = apartments_and_units_for_rent
        if villas_for_sale is not UNSET:
            field_dict["villasForSale"] = villas_for_sale
        if duplexes_for_sale is not UNSET:
            field_dict["duplexesForSale"] = duplexes_for_sale
        if semi_detached_houses_for_rent is not UNSET:
            field_dict["semiDetachedHousesForRent"] = semi_detached_houses_for_rent
        if studios_for_sale is not UNSET:
            field_dict["studiosForSale"] = studios_for_sale
        if single_percentage is not UNSET:
            field_dict["singlePercentage"] = single_percentage
        if most_common_age_bracket is not UNSET:
            field_dict["mostCommonAgeBracket"] = most_common_age_bracket
        if renter_percentage is not UNSET:
            field_dict["renterPercentage"] = renter_percentage
        if penthouses_for_sale is not UNSET:
            field_dict["penthousesForSale"] = penthouses_for_sale
        if villas_for_rent is not UNSET:
            field_dict["villasForRent"] = villas_for_rent
        if duplexes_for_rent is not UNSET:
            field_dict["duplexesForRent"] = duplexes_for_rent
        if houses_for_sale is not UNSET:
            field_dict["housesForSale"] = houses_for_sale
        if owner_occupier_percentage is not UNSET:
            field_dict["ownerOccupierPercentage"] = owner_occupier_percentage
        if property_categories is not UNSET:
            field_dict["propertyCategories"] = property_categories
        if population is not UNSET:
            field_dict["population"] = population
        if penthouses_for_rent is not UNSET:
            field_dict["penthousesForRent"] = penthouses_for_rent
        if townhouses_for_sale is not UNSET:
            field_dict["townhousesForSale"] = townhouses_for_sale
        if terraced_houses_for_rent is not UNSET:
            field_dict["terracedHousesForRent"] = terraced_houses_for_rent
        if married_percentage is not UNSET:
            field_dict["marriedPercentage"] = married_percentage
        if houses_for_rent is not UNSET:
            field_dict["housesForRent"] = houses_for_rent
        if block_of_units_for_sale is not UNSET:
            field_dict["blockOfUnitsForSale"] = block_of_units_for_sale

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_location_profiles_service_v1_model_location_data_property_categories import (
            DomainLocationProfilesServiceV1ModelLocationDataPropertyCategories,
        )

        d = src_dict.copy()
        studios_for_rent = d.pop("studiosForRent", UNSET)

        terraced_houses_for_sale = d.pop("terracedHousesForSale", UNSET)

        semi_detached_houses_for_sale = d.pop("semiDetachedHousesForSale", UNSET)

        townhouses_for_rent = d.pop("townhousesForRent", UNSET)

        apartments_and_units_for_sale = d.pop("apartmentsAndUnitsForSale", UNSET)

        apartments_and_units_for_rent = d.pop("apartmentsAndUnitsForRent", UNSET)

        villas_for_sale = d.pop("villasForSale", UNSET)

        duplexes_for_sale = d.pop("duplexesForSale", UNSET)

        semi_detached_houses_for_rent = d.pop("semiDetachedHousesForRent", UNSET)

        studios_for_sale = d.pop("studiosForSale", UNSET)

        single_percentage = d.pop("singlePercentage", UNSET)

        most_common_age_bracket = d.pop("mostCommonAgeBracket", UNSET)

        renter_percentage = d.pop("renterPercentage", UNSET)

        penthouses_for_sale = d.pop("penthousesForSale", UNSET)

        villas_for_rent = d.pop("villasForRent", UNSET)

        duplexes_for_rent = d.pop("duplexesForRent", UNSET)

        houses_for_sale = d.pop("housesForSale", UNSET)

        owner_occupier_percentage = d.pop("ownerOccupierPercentage", UNSET)

        property_categories = []
        _property_categories = d.pop("propertyCategories", UNSET)
        for property_categories_item_data in _property_categories or []:
            property_categories_item = DomainLocationProfilesServiceV1ModelLocationDataPropertyCategories.from_dict(
                property_categories_item_data
            )

            property_categories.append(property_categories_item)

        population = d.pop("population", UNSET)

        penthouses_for_rent = d.pop("penthousesForRent", UNSET)

        townhouses_for_sale = d.pop("townhousesForSale", UNSET)

        terraced_houses_for_rent = d.pop("terracedHousesForRent", UNSET)

        married_percentage = d.pop("marriedPercentage", UNSET)

        houses_for_rent = d.pop("housesForRent", UNSET)

        block_of_units_for_sale = d.pop("blockOfUnitsForSale", UNSET)

        domain_location_profiles_service_v1_model_location_data = cls(
            studios_for_rent=studios_for_rent,
            terraced_houses_for_sale=terraced_houses_for_sale,
            semi_detached_houses_for_sale=semi_detached_houses_for_sale,
            townhouses_for_rent=townhouses_for_rent,
            apartments_and_units_for_sale=apartments_and_units_for_sale,
            apartments_and_units_for_rent=apartments_and_units_for_rent,
            villas_for_sale=villas_for_sale,
            duplexes_for_sale=duplexes_for_sale,
            semi_detached_houses_for_rent=semi_detached_houses_for_rent,
            studios_for_sale=studios_for_sale,
            single_percentage=single_percentage,
            most_common_age_bracket=most_common_age_bracket,
            renter_percentage=renter_percentage,
            penthouses_for_sale=penthouses_for_sale,
            villas_for_rent=villas_for_rent,
            duplexes_for_rent=duplexes_for_rent,
            houses_for_sale=houses_for_sale,
            owner_occupier_percentage=owner_occupier_percentage,
            property_categories=property_categories,
            population=population,
            penthouses_for_rent=penthouses_for_rent,
            townhouses_for_sale=townhouses_for_sale,
            terraced_houses_for_rent=terraced_houses_for_rent,
            married_percentage=married_percentage,
            houses_for_rent=houses_for_rent,
            block_of_units_for_sale=block_of_units_for_sale,
        )

        domain_location_profiles_service_v1_model_location_data.additional_properties = d
        return domain_location_profiles_service_v1_model_location_data

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
