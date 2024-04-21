from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.domain_avm_v1_address import DomainAvmV1Address


T = TypeVar("T", bound="DomainAvmV1Response")


@_attrs_define
class DomainAvmV1Response:
    """The response model used to provide the bank grade valuation.

    Attributes:
        val_ex_job_number (Union[None, Unset, str]): The client identification for the valuation transaction from
            request.
        estimate (Union[None, Unset, int]): The estimate.
        estimate_low (Union[None, Unset, int]): The estimate low range.
        estimate_high (Union[None, Unset, int]): The estimate high range.
        confidence (Union[None, Unset, str]): The confidence level of the estimates.
        percent_fsd (Union[None, Unset, float]): The forecast standard deviation of the property.
        estimate_date (Union[None, Unset, str]): The date the estimates were generated.
        property_type (Union[None, Unset, str]): Property type used when estimating the value of property. Valid values:
            [House, Unit].
        year_built (Union[None, Unset, str]): The year of construction.
        bedrooms (Union[None, Unset, int]): The amount of bedrooms.
        bathrooms (Union[None, Unset, int]): The amount of bathrooms.
        carparks (Union[None, Unset, int]): The amount of carparks.
        building_area (Union[None, Unset, float]): Building area in square meters to be used when estimating value of
            property, for houses only not units.
        land_area (Union[None, Unset, float]): Land area in square meters to be used when estimating value of property,
            for houses only not units.
        address (Union[Unset, DomainAvmV1Address]): The Address model used.
        report (Union[None, Unset, str]): The B64 encoded pdf of the valuation report.
    """

    val_ex_job_number: Union[None, Unset, str] = UNSET
    estimate: Union[None, Unset, int] = UNSET
    estimate_low: Union[None, Unset, int] = UNSET
    estimate_high: Union[None, Unset, int] = UNSET
    confidence: Union[None, Unset, str] = UNSET
    percent_fsd: Union[None, Unset, float] = UNSET
    estimate_date: Union[None, Unset, str] = UNSET
    property_type: Union[None, Unset, str] = UNSET
    year_built: Union[None, Unset, str] = UNSET
    bedrooms: Union[None, Unset, int] = UNSET
    bathrooms: Union[None, Unset, int] = UNSET
    carparks: Union[None, Unset, int] = UNSET
    building_area: Union[None, Unset, float] = UNSET
    land_area: Union[None, Unset, float] = UNSET
    address: Union[Unset, "DomainAvmV1Address"] = UNSET
    report: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        val_ex_job_number: Union[None, Unset, str]
        if isinstance(self.val_ex_job_number, Unset):
            val_ex_job_number = UNSET
        else:
            val_ex_job_number = self.val_ex_job_number

        estimate: Union[None, Unset, int]
        if isinstance(self.estimate, Unset):
            estimate = UNSET
        else:
            estimate = self.estimate

        estimate_low: Union[None, Unset, int]
        if isinstance(self.estimate_low, Unset):
            estimate_low = UNSET
        else:
            estimate_low = self.estimate_low

        estimate_high: Union[None, Unset, int]
        if isinstance(self.estimate_high, Unset):
            estimate_high = UNSET
        else:
            estimate_high = self.estimate_high

        confidence: Union[None, Unset, str]
        if isinstance(self.confidence, Unset):
            confidence = UNSET
        else:
            confidence = self.confidence

        percent_fsd: Union[None, Unset, float]
        if isinstance(self.percent_fsd, Unset):
            percent_fsd = UNSET
        else:
            percent_fsd = self.percent_fsd

        estimate_date: Union[None, Unset, str]
        if isinstance(self.estimate_date, Unset):
            estimate_date = UNSET
        else:
            estimate_date = self.estimate_date

        property_type: Union[None, Unset, str]
        if isinstance(self.property_type, Unset):
            property_type = UNSET
        else:
            property_type = self.property_type

        year_built: Union[None, Unset, str]
        if isinstance(self.year_built, Unset):
            year_built = UNSET
        else:
            year_built = self.year_built

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

        building_area: Union[None, Unset, float]
        if isinstance(self.building_area, Unset):
            building_area = UNSET
        else:
            building_area = self.building_area

        land_area: Union[None, Unset, float]
        if isinstance(self.land_area, Unset):
            land_area = UNSET
        else:
            land_area = self.land_area

        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        report: Union[None, Unset, str]
        if isinstance(self.report, Unset):
            report = UNSET
        else:
            report = self.report

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if val_ex_job_number is not UNSET:
            field_dict["valExJobNumber"] = val_ex_job_number
        if estimate is not UNSET:
            field_dict["estimate"] = estimate
        if estimate_low is not UNSET:
            field_dict["estimateLow"] = estimate_low
        if estimate_high is not UNSET:
            field_dict["estimateHigh"] = estimate_high
        if confidence is not UNSET:
            field_dict["confidence"] = confidence
        if percent_fsd is not UNSET:
            field_dict["percentFsd"] = percent_fsd
        if estimate_date is not UNSET:
            field_dict["estimateDate"] = estimate_date
        if property_type is not UNSET:
            field_dict["propertyType"] = property_type
        if year_built is not UNSET:
            field_dict["yearBuilt"] = year_built
        if bedrooms is not UNSET:
            field_dict["bedrooms"] = bedrooms
        if bathrooms is not UNSET:
            field_dict["bathrooms"] = bathrooms
        if carparks is not UNSET:
            field_dict["carparks"] = carparks
        if building_area is not UNSET:
            field_dict["buildingArea"] = building_area
        if land_area is not UNSET:
            field_dict["landArea"] = land_area
        if address is not UNSET:
            field_dict["address"] = address
        if report is not UNSET:
            field_dict["report"] = report

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.domain_avm_v1_address import DomainAvmV1Address

        d = src_dict.copy()

        def _parse_val_ex_job_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        val_ex_job_number = _parse_val_ex_job_number(d.pop("valExJobNumber", UNSET))

        def _parse_estimate(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        estimate = _parse_estimate(d.pop("estimate", UNSET))

        def _parse_estimate_low(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        estimate_low = _parse_estimate_low(d.pop("estimateLow", UNSET))

        def _parse_estimate_high(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        estimate_high = _parse_estimate_high(d.pop("estimateHigh", UNSET))

        def _parse_confidence(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        confidence = _parse_confidence(d.pop("confidence", UNSET))

        def _parse_percent_fsd(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        percent_fsd = _parse_percent_fsd(d.pop("percentFsd", UNSET))

        def _parse_estimate_date(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        estimate_date = _parse_estimate_date(d.pop("estimateDate", UNSET))

        def _parse_property_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        property_type = _parse_property_type(d.pop("propertyType", UNSET))

        def _parse_year_built(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        year_built = _parse_year_built(d.pop("yearBuilt", UNSET))

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

        def _parse_building_area(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        building_area = _parse_building_area(d.pop("buildingArea", UNSET))

        def _parse_land_area(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        land_area = _parse_land_area(d.pop("landArea", UNSET))

        _address = d.pop("address", UNSET)
        address: Union[Unset, DomainAvmV1Address]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = DomainAvmV1Address.from_dict(_address)

        def _parse_report(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        report = _parse_report(d.pop("report", UNSET))

        domain_avm_v1_response = cls(
            val_ex_job_number=val_ex_job_number,
            estimate=estimate,
            estimate_low=estimate_low,
            estimate_high=estimate_high,
            confidence=confidence,
            percent_fsd=percent_fsd,
            estimate_date=estimate_date,
            property_type=property_type,
            year_built=year_built,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            carparks=carparks,
            building_area=building_area,
            land_area=land_area,
            address=address,
            report=report,
        )

        return domain_avm_v1_response
