from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SchoolsV2SchoolProfile")


@_attrs_define
class SchoolsV2SchoolProfile:
    """SchoolProfile

    Attributes:
        url (Union[None, Unset, str]): Website for the school
        year_range (Union[None, Unset, str]): The range of year levels offered by the school.
        icsea (Union[None, Unset, int]): The Index of Community Socio-Educational Advantage score for the school. This
            score is derived from a number of variables including parental school and non-school education and occupation,
            the school’s geographical location and proportion of Indigenous students.
        bottom_sea_quarter (Union[None, Unset, int]): The percentage of students positioned in the lowest socio-
            educational advantage quarter.
        lower_middle_sea_quarter (Union[None, Unset, int]): The percentage of students positioned in the lower middle
            socio-educational advantage quarter.
        upper_middle_sea_quarter (Union[None, Unset, int]): The percentage of students positioned in the higher middle
            socio-educational advantage quarter.
        top_sea_quarter (Union[None, Unset, int]): The percentage of students positioned in the highest socio-
            educational advantage quarter.
        total_enrolments (Union[None, Unset, int]): The total number of students, including both full-time and part-time
            students, who are enrolled at the school in the calendar year specified.
        girls_enrolments (Union[None, Unset, int]): The total number of female students, including both full-time and
            part-time students, who are enrolled at the school in the calendar year specified.
        boys_enrolments (Union[None, Unset, int]): The total number of male students, including full-time and part-time
            students, who are enrolled at the school in the calendar year specified.
    """

    url: Union[None, Unset, str] = UNSET
    year_range: Union[None, Unset, str] = UNSET
    icsea: Union[None, Unset, int] = UNSET
    bottom_sea_quarter: Union[None, Unset, int] = UNSET
    lower_middle_sea_quarter: Union[None, Unset, int] = UNSET
    upper_middle_sea_quarter: Union[None, Unset, int] = UNSET
    top_sea_quarter: Union[None, Unset, int] = UNSET
    total_enrolments: Union[None, Unset, int] = UNSET
    girls_enrolments: Union[None, Unset, int] = UNSET
    boys_enrolments: Union[None, Unset, int] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        url: Union[None, Unset, str]
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        year_range: Union[None, Unset, str]
        if isinstance(self.year_range, Unset):
            year_range = UNSET
        else:
            year_range = self.year_range

        icsea: Union[None, Unset, int]
        if isinstance(self.icsea, Unset):
            icsea = UNSET
        else:
            icsea = self.icsea

        bottom_sea_quarter: Union[None, Unset, int]
        if isinstance(self.bottom_sea_quarter, Unset):
            bottom_sea_quarter = UNSET
        else:
            bottom_sea_quarter = self.bottom_sea_quarter

        lower_middle_sea_quarter: Union[None, Unset, int]
        if isinstance(self.lower_middle_sea_quarter, Unset):
            lower_middle_sea_quarter = UNSET
        else:
            lower_middle_sea_quarter = self.lower_middle_sea_quarter

        upper_middle_sea_quarter: Union[None, Unset, int]
        if isinstance(self.upper_middle_sea_quarter, Unset):
            upper_middle_sea_quarter = UNSET
        else:
            upper_middle_sea_quarter = self.upper_middle_sea_quarter

        top_sea_quarter: Union[None, Unset, int]
        if isinstance(self.top_sea_quarter, Unset):
            top_sea_quarter = UNSET
        else:
            top_sea_quarter = self.top_sea_quarter

        total_enrolments: Union[None, Unset, int]
        if isinstance(self.total_enrolments, Unset):
            total_enrolments = UNSET
        else:
            total_enrolments = self.total_enrolments

        girls_enrolments: Union[None, Unset, int]
        if isinstance(self.girls_enrolments, Unset):
            girls_enrolments = UNSET
        else:
            girls_enrolments = self.girls_enrolments

        boys_enrolments: Union[None, Unset, int]
        if isinstance(self.boys_enrolments, Unset):
            boys_enrolments = UNSET
        else:
            boys_enrolments = self.boys_enrolments

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if year_range is not UNSET:
            field_dict["yearRange"] = year_range
        if icsea is not UNSET:
            field_dict["icsea"] = icsea
        if bottom_sea_quarter is not UNSET:
            field_dict["bottomSeaQuarter"] = bottom_sea_quarter
        if lower_middle_sea_quarter is not UNSET:
            field_dict["lowerMiddleSeaQuarter"] = lower_middle_sea_quarter
        if upper_middle_sea_quarter is not UNSET:
            field_dict["upperMiddleSeaQuarter"] = upper_middle_sea_quarter
        if top_sea_quarter is not UNSET:
            field_dict["topSeaQuarter"] = top_sea_quarter
        if total_enrolments is not UNSET:
            field_dict["totalEnrolments"] = total_enrolments
        if girls_enrolments is not UNSET:
            field_dict["girlsEnrolments"] = girls_enrolments
        if boys_enrolments is not UNSET:
            field_dict["boysEnrolments"] = boys_enrolments

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_year_range(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        year_range = _parse_year_range(d.pop("yearRange", UNSET))

        def _parse_icsea(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        icsea = _parse_icsea(d.pop("icsea", UNSET))

        def _parse_bottom_sea_quarter(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        bottom_sea_quarter = _parse_bottom_sea_quarter(d.pop("bottomSeaQuarter", UNSET))

        def _parse_lower_middle_sea_quarter(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        lower_middle_sea_quarter = _parse_lower_middle_sea_quarter(d.pop("lowerMiddleSeaQuarter", UNSET))

        def _parse_upper_middle_sea_quarter(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        upper_middle_sea_quarter = _parse_upper_middle_sea_quarter(d.pop("upperMiddleSeaQuarter", UNSET))

        def _parse_top_sea_quarter(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        top_sea_quarter = _parse_top_sea_quarter(d.pop("topSeaQuarter", UNSET))

        def _parse_total_enrolments(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        total_enrolments = _parse_total_enrolments(d.pop("totalEnrolments", UNSET))

        def _parse_girls_enrolments(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        girls_enrolments = _parse_girls_enrolments(d.pop("girlsEnrolments", UNSET))

        def _parse_boys_enrolments(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        boys_enrolments = _parse_boys_enrolments(d.pop("boysEnrolments", UNSET))

        schools_v2_school_profile = cls(
            url=url,
            year_range=year_range,
            icsea=icsea,
            bottom_sea_quarter=bottom_sea_quarter,
            lower_middle_sea_quarter=lower_middle_sea_quarter,
            upper_middle_sea_quarter=upper_middle_sea_quarter,
            top_sea_quarter=top_sea_quarter,
            total_enrolments=total_enrolments,
            girls_enrolments=girls_enrolments,
            boys_enrolments=boys_enrolments,
        )

        return schools_v2_school_profile
