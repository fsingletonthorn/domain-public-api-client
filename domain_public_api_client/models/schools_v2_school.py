from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.schools_v2_school_gender import SchoolsV2SchoolGender
from ..models.schools_v2_school_school_sector import SchoolsV2SchoolSchoolSector
from ..models.schools_v2_school_school_type import SchoolsV2SchoolSchoolType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schools_v2_school_catchment import SchoolsV2SchoolCatchment
    from ..models.schools_v2_school_profile import SchoolsV2SchoolProfile


T = TypeVar("T", bound="SchoolsV2School")


@_attrs_define
class SchoolsV2School:
    """School

    Attributes:
        school_sector (Union[Unset, SchoolsV2SchoolSchoolSector]): Gets or Sets SchoolSector
        school_type (Union[Unset, SchoolsV2SchoolSchoolType]): Gets or Sets SchoolType
        gender (Union[Unset, SchoolsV2SchoolGender]): Gets or Sets Gender
        name (Union[None, Unset, str]): Gets or Sets Name
        suburb (Union[None, Unset, str]): Gets or Sets Suburb
        state (Union[None, Unset, str]): Gets or Sets State
        postcode (Union[None, Unset, str]): Gets or Sets Postcode
        centroid (Union[None, Unset, str]): Gets or Sets Centroid
        profile (Union[Unset, SchoolsV2SchoolProfile]): SchoolProfile
        catchments (Union[List['SchoolsV2SchoolCatchment'], None, Unset]): Gets or Sets Catchments
        domain_id (Union[None, Unset, int]): Gets or Sets DomainId
    """

    school_sector: Union[Unset, SchoolsV2SchoolSchoolSector] = UNSET
    school_type: Union[Unset, SchoolsV2SchoolSchoolType] = UNSET
    gender: Union[Unset, SchoolsV2SchoolGender] = UNSET
    name: Union[None, Unset, str] = UNSET
    suburb: Union[None, Unset, str] = UNSET
    state: Union[None, Unset, str] = UNSET
    postcode: Union[None, Unset, str] = UNSET
    centroid: Union[None, Unset, str] = UNSET
    profile: Union[Unset, "SchoolsV2SchoolProfile"] = UNSET
    catchments: Union[List["SchoolsV2SchoolCatchment"], None, Unset] = UNSET
    domain_id: Union[None, Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        school_sector: Union[Unset, str] = UNSET
        if not isinstance(self.school_sector, Unset):
            school_sector = self.school_sector.value

        school_type: Union[Unset, str] = UNSET
        if not isinstance(self.school_type, Unset):
            school_type = self.school_type.value

        gender: Union[Unset, str] = UNSET
        if not isinstance(self.gender, Unset):
            gender = self.gender.value

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        suburb: Union[None, Unset, str]
        if isinstance(self.suburb, Unset):
            suburb = UNSET
        else:
            suburb = self.suburb

        state: Union[None, Unset, str]
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        postcode: Union[None, Unset, str]
        if isinstance(self.postcode, Unset):
            postcode = UNSET
        else:
            postcode = self.postcode

        centroid: Union[None, Unset, str]
        if isinstance(self.centroid, Unset):
            centroid = UNSET
        else:
            centroid = self.centroid

        profile: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.profile, Unset):
            profile = self.profile.to_dict()

        catchments: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.catchments, Unset):
            catchments = UNSET
        elif isinstance(self.catchments, list):
            catchments = []
            for catchments_type_0_item_data in self.catchments:
                catchments_type_0_item = catchments_type_0_item_data.to_dict()
                catchments.append(catchments_type_0_item)

        else:
            catchments = self.catchments

        domain_id: Union[None, Unset, int]
        if isinstance(self.domain_id, Unset):
            domain_id = UNSET
        else:
            domain_id = self.domain_id

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if school_sector is not UNSET:
            field_dict["schoolSector"] = school_sector
        if school_type is not UNSET:
            field_dict["schoolType"] = school_type
        if gender is not UNSET:
            field_dict["gender"] = gender
        if name is not UNSET:
            field_dict["name"] = name
        if suburb is not UNSET:
            field_dict["suburb"] = suburb
        if state is not UNSET:
            field_dict["state"] = state
        if postcode is not UNSET:
            field_dict["postcode"] = postcode
        if centroid is not UNSET:
            field_dict["centroid"] = centroid
        if profile is not UNSET:
            field_dict["profile"] = profile
        if catchments is not UNSET:
            field_dict["catchments"] = catchments
        if domain_id is not UNSET:
            field_dict["domainId"] = domain_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.schools_v2_school_catchment import SchoolsV2SchoolCatchment
        from ..models.schools_v2_school_profile import SchoolsV2SchoolProfile

        d = src_dict.copy()
        _school_sector = d.pop("schoolSector", UNSET)
        school_sector: Union[Unset, SchoolsV2SchoolSchoolSector]
        if isinstance(_school_sector, Unset):
            school_sector = UNSET
        else:
            school_sector = SchoolsV2SchoolSchoolSector(_school_sector)

        _school_type = d.pop("schoolType", UNSET)
        school_type: Union[Unset, SchoolsV2SchoolSchoolType]
        if isinstance(_school_type, Unset):
            school_type = UNSET
        else:
            school_type = SchoolsV2SchoolSchoolType(_school_type)

        _gender = d.pop("gender", UNSET)
        gender: Union[Unset, SchoolsV2SchoolGender]
        if isinstance(_gender, Unset):
            gender = UNSET
        else:
            gender = SchoolsV2SchoolGender(_gender)

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_suburb(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        suburb = _parse_suburb(d.pop("suburb", UNSET))

        def _parse_state(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        state = _parse_state(d.pop("state", UNSET))

        def _parse_postcode(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        postcode = _parse_postcode(d.pop("postcode", UNSET))

        def _parse_centroid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        centroid = _parse_centroid(d.pop("centroid", UNSET))

        _profile = d.pop("profile", UNSET)
        profile: Union[Unset, SchoolsV2SchoolProfile]
        if isinstance(_profile, Unset):
            profile = UNSET
        else:
            profile = SchoolsV2SchoolProfile.from_dict(_profile)

        def _parse_catchments(data: object) -> Union[List["SchoolsV2SchoolCatchment"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                catchments_type_0 = []
                _catchments_type_0 = data
                for catchments_type_0_item_data in _catchments_type_0:
                    catchments_type_0_item = SchoolsV2SchoolCatchment.from_dict(catchments_type_0_item_data)

                    catchments_type_0.append(catchments_type_0_item)

                return catchments_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["SchoolsV2SchoolCatchment"], None, Unset], data)

        catchments = _parse_catchments(d.pop("catchments", UNSET))

        def _parse_domain_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        domain_id = _parse_domain_id(d.pop("domainId", UNSET))

        schools_v2_school = cls(
            school_sector=school_sector,
            school_type=school_type,
            gender=gender,
            name=name,
            suburb=suburb,
            state=state,
            postcode=postcode,
            centroid=centroid,
            profile=profile,
            catchments=catchments,
            domain_id=domain_id,
        )

        return schools_v2_school
