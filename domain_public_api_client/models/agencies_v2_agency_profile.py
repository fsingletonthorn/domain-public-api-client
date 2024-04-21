from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agencies_v2_agency_photo import AgenciesV2AgencyPhoto


T = TypeVar("T", bound="AgenciesV2AgencyProfile")


@_attrs_define
class AgenciesV2AgencyProfile:
    """AgencyProfile

    Attributes:
        agency_photos (Union[List['AgenciesV2AgencyPhoto'], None, Unset]): Gets or Sets AgencyPhotos
        profile_website (Union[None, Unset, str]): Gets or Sets ProfileWebsite
        agency_banner (Union[None, Unset, str]): Gets or Sets AgencyBanner
        agency_website (Union[None, Unset, str]): Gets or Sets AgencyWebsite
        agency_logo_standard (Union[None, Unset, str]): Gets or Sets AgencyLogoStandard
        agency_logo_small (Union[None, Unset, str]): Gets or Sets AgencyLogoSmall
        logo_colour (Union[None, Unset, str]): Gets or Sets LogoColour
        primary_agency_colour (Union[None, Unset, str]): Gets or Sets PrimaryAgencyColour
        background_colour (Union[None, Unset, str]): Gets or Sets BackgroundColour
        map_latitude (Union[None, Unset, str]): Gets or Sets MapLatitude
        map_longitude (Union[None, Unset, str]): Gets or Sets MapLongitude
        map_certainty (Union[None, Unset, int]): Gets or Sets MapCertainty
        agency_video_url (Union[None, Unset, str]): Gets or Sets AgencyVideoUrl
        agency_description (Union[None, Unset, str]): Gets or Sets AgencyDescription
        agency_description_cre (Union[None, Unset, str]): Gets or Sets AgencyDescriptionCre
        cre_profile_website (Union[None, Unset, str]): Gets or Sets CreProfileWebsite
        agency_cre_banner (Union[None, Unset, str]): Gets or Sets AgencyCreBanner
        agency_cre_website (Union[None, Unset, str]): Gets or Sets AgencyCreWebsite
        agency_cre_logo_standard (Union[None, Unset, str]): Gets or Sets AgencyCreLogoStandard
        number_for_sale (Union[None, Unset, int]): Gets or Sets NumberForSale
        number_for_rent (Union[None, Unset, int]): Gets or Sets NumberForRent
        number_for_sale_commercial (Union[None, Unset, int]): Gets or Sets NumberForSaleCommercial
        number_for_rent_commercial (Union[None, Unset, int]): Gets or Sets NumberForRentCommercial
        cre_agency_video_url (Union[None, Unset, str]): Gets or Sets CreAgencyVideoUrl
    """

    agency_photos: Union[List["AgenciesV2AgencyPhoto"], None, Unset] = UNSET
    profile_website: Union[None, Unset, str] = UNSET
    agency_banner: Union[None, Unset, str] = UNSET
    agency_website: Union[None, Unset, str] = UNSET
    agency_logo_standard: Union[None, Unset, str] = UNSET
    agency_logo_small: Union[None, Unset, str] = UNSET
    logo_colour: Union[None, Unset, str] = UNSET
    primary_agency_colour: Union[None, Unset, str] = UNSET
    background_colour: Union[None, Unset, str] = UNSET
    map_latitude: Union[None, Unset, str] = UNSET
    map_longitude: Union[None, Unset, str] = UNSET
    map_certainty: Union[None, Unset, int] = UNSET
    agency_video_url: Union[None, Unset, str] = UNSET
    agency_description: Union[None, Unset, str] = UNSET
    agency_description_cre: Union[None, Unset, str] = UNSET
    cre_profile_website: Union[None, Unset, str] = UNSET
    agency_cre_banner: Union[None, Unset, str] = UNSET
    agency_cre_website: Union[None, Unset, str] = UNSET
    agency_cre_logo_standard: Union[None, Unset, str] = UNSET
    number_for_sale: Union[None, Unset, int] = UNSET
    number_for_rent: Union[None, Unset, int] = UNSET
    number_for_sale_commercial: Union[None, Unset, int] = UNSET
    number_for_rent_commercial: Union[None, Unset, int] = UNSET
    cre_agency_video_url: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        agency_photos: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.agency_photos, Unset):
            agency_photos = UNSET
        elif isinstance(self.agency_photos, list):
            agency_photos = []
            for agency_photos_type_0_item_data in self.agency_photos:
                agency_photos_type_0_item = agency_photos_type_0_item_data.to_dict()
                agency_photos.append(agency_photos_type_0_item)

        else:
            agency_photos = self.agency_photos

        profile_website: Union[None, Unset, str]
        if isinstance(self.profile_website, Unset):
            profile_website = UNSET
        else:
            profile_website = self.profile_website

        agency_banner: Union[None, Unset, str]
        if isinstance(self.agency_banner, Unset):
            agency_banner = UNSET
        else:
            agency_banner = self.agency_banner

        agency_website: Union[None, Unset, str]
        if isinstance(self.agency_website, Unset):
            agency_website = UNSET
        else:
            agency_website = self.agency_website

        agency_logo_standard: Union[None, Unset, str]
        if isinstance(self.agency_logo_standard, Unset):
            agency_logo_standard = UNSET
        else:
            agency_logo_standard = self.agency_logo_standard

        agency_logo_small: Union[None, Unset, str]
        if isinstance(self.agency_logo_small, Unset):
            agency_logo_small = UNSET
        else:
            agency_logo_small = self.agency_logo_small

        logo_colour: Union[None, Unset, str]
        if isinstance(self.logo_colour, Unset):
            logo_colour = UNSET
        else:
            logo_colour = self.logo_colour

        primary_agency_colour: Union[None, Unset, str]
        if isinstance(self.primary_agency_colour, Unset):
            primary_agency_colour = UNSET
        else:
            primary_agency_colour = self.primary_agency_colour

        background_colour: Union[None, Unset, str]
        if isinstance(self.background_colour, Unset):
            background_colour = UNSET
        else:
            background_colour = self.background_colour

        map_latitude: Union[None, Unset, str]
        if isinstance(self.map_latitude, Unset):
            map_latitude = UNSET
        else:
            map_latitude = self.map_latitude

        map_longitude: Union[None, Unset, str]
        if isinstance(self.map_longitude, Unset):
            map_longitude = UNSET
        else:
            map_longitude = self.map_longitude

        map_certainty: Union[None, Unset, int]
        if isinstance(self.map_certainty, Unset):
            map_certainty = UNSET
        else:
            map_certainty = self.map_certainty

        agency_video_url: Union[None, Unset, str]
        if isinstance(self.agency_video_url, Unset):
            agency_video_url = UNSET
        else:
            agency_video_url = self.agency_video_url

        agency_description: Union[None, Unset, str]
        if isinstance(self.agency_description, Unset):
            agency_description = UNSET
        else:
            agency_description = self.agency_description

        agency_description_cre: Union[None, Unset, str]
        if isinstance(self.agency_description_cre, Unset):
            agency_description_cre = UNSET
        else:
            agency_description_cre = self.agency_description_cre

        cre_profile_website: Union[None, Unset, str]
        if isinstance(self.cre_profile_website, Unset):
            cre_profile_website = UNSET
        else:
            cre_profile_website = self.cre_profile_website

        agency_cre_banner: Union[None, Unset, str]
        if isinstance(self.agency_cre_banner, Unset):
            agency_cre_banner = UNSET
        else:
            agency_cre_banner = self.agency_cre_banner

        agency_cre_website: Union[None, Unset, str]
        if isinstance(self.agency_cre_website, Unset):
            agency_cre_website = UNSET
        else:
            agency_cre_website = self.agency_cre_website

        agency_cre_logo_standard: Union[None, Unset, str]
        if isinstance(self.agency_cre_logo_standard, Unset):
            agency_cre_logo_standard = UNSET
        else:
            agency_cre_logo_standard = self.agency_cre_logo_standard

        number_for_sale: Union[None, Unset, int]
        if isinstance(self.number_for_sale, Unset):
            number_for_sale = UNSET
        else:
            number_for_sale = self.number_for_sale

        number_for_rent: Union[None, Unset, int]
        if isinstance(self.number_for_rent, Unset):
            number_for_rent = UNSET
        else:
            number_for_rent = self.number_for_rent

        number_for_sale_commercial: Union[None, Unset, int]
        if isinstance(self.number_for_sale_commercial, Unset):
            number_for_sale_commercial = UNSET
        else:
            number_for_sale_commercial = self.number_for_sale_commercial

        number_for_rent_commercial: Union[None, Unset, int]
        if isinstance(self.number_for_rent_commercial, Unset):
            number_for_rent_commercial = UNSET
        else:
            number_for_rent_commercial = self.number_for_rent_commercial

        cre_agency_video_url: Union[None, Unset, str]
        if isinstance(self.cre_agency_video_url, Unset):
            cre_agency_video_url = UNSET
        else:
            cre_agency_video_url = self.cre_agency_video_url

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if agency_photos is not UNSET:
            field_dict["agencyPhotos"] = agency_photos
        if profile_website is not UNSET:
            field_dict["profileWebsite"] = profile_website
        if agency_banner is not UNSET:
            field_dict["agencyBanner"] = agency_banner
        if agency_website is not UNSET:
            field_dict["agencyWebsite"] = agency_website
        if agency_logo_standard is not UNSET:
            field_dict["agencyLogoStandard"] = agency_logo_standard
        if agency_logo_small is not UNSET:
            field_dict["agencyLogoSmall"] = agency_logo_small
        if logo_colour is not UNSET:
            field_dict["logoColour"] = logo_colour
        if primary_agency_colour is not UNSET:
            field_dict["primaryAgencyColour"] = primary_agency_colour
        if background_colour is not UNSET:
            field_dict["backgroundColour"] = background_colour
        if map_latitude is not UNSET:
            field_dict["mapLatitude"] = map_latitude
        if map_longitude is not UNSET:
            field_dict["mapLongitude"] = map_longitude
        if map_certainty is not UNSET:
            field_dict["mapCertainty"] = map_certainty
        if agency_video_url is not UNSET:
            field_dict["agencyVideoUrl"] = agency_video_url
        if agency_description is not UNSET:
            field_dict["agencyDescription"] = agency_description
        if agency_description_cre is not UNSET:
            field_dict["agencyDescriptionCre"] = agency_description_cre
        if cre_profile_website is not UNSET:
            field_dict["creProfileWebsite"] = cre_profile_website
        if agency_cre_banner is not UNSET:
            field_dict["agencyCreBanner"] = agency_cre_banner
        if agency_cre_website is not UNSET:
            field_dict["agencyCreWebsite"] = agency_cre_website
        if agency_cre_logo_standard is not UNSET:
            field_dict["agencyCreLogoStandard"] = agency_cre_logo_standard
        if number_for_sale is not UNSET:
            field_dict["numberForSale"] = number_for_sale
        if number_for_rent is not UNSET:
            field_dict["numberForRent"] = number_for_rent
        if number_for_sale_commercial is not UNSET:
            field_dict["numberForSaleCommercial"] = number_for_sale_commercial
        if number_for_rent_commercial is not UNSET:
            field_dict["numberForRentCommercial"] = number_for_rent_commercial
        if cre_agency_video_url is not UNSET:
            field_dict["creAgencyVideoUrl"] = cre_agency_video_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.agencies_v2_agency_photo import AgenciesV2AgencyPhoto

        d = src_dict.copy()

        def _parse_agency_photos(data: object) -> Union[List["AgenciesV2AgencyPhoto"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                agency_photos_type_0 = []
                _agency_photos_type_0 = data
                for agency_photos_type_0_item_data in _agency_photos_type_0:
                    agency_photos_type_0_item = AgenciesV2AgencyPhoto.from_dict(agency_photos_type_0_item_data)

                    agency_photos_type_0.append(agency_photos_type_0_item)

                return agency_photos_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["AgenciesV2AgencyPhoto"], None, Unset], data)

        agency_photos = _parse_agency_photos(d.pop("agencyPhotos", UNSET))

        def _parse_profile_website(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        profile_website = _parse_profile_website(d.pop("profileWebsite", UNSET))

        def _parse_agency_banner(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        agency_banner = _parse_agency_banner(d.pop("agencyBanner", UNSET))

        def _parse_agency_website(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        agency_website = _parse_agency_website(d.pop("agencyWebsite", UNSET))

        def _parse_agency_logo_standard(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        agency_logo_standard = _parse_agency_logo_standard(d.pop("agencyLogoStandard", UNSET))

        def _parse_agency_logo_small(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        agency_logo_small = _parse_agency_logo_small(d.pop("agencyLogoSmall", UNSET))

        def _parse_logo_colour(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        logo_colour = _parse_logo_colour(d.pop("logoColour", UNSET))

        def _parse_primary_agency_colour(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        primary_agency_colour = _parse_primary_agency_colour(d.pop("primaryAgencyColour", UNSET))

        def _parse_background_colour(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        background_colour = _parse_background_colour(d.pop("backgroundColour", UNSET))

        def _parse_map_latitude(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        map_latitude = _parse_map_latitude(d.pop("mapLatitude", UNSET))

        def _parse_map_longitude(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        map_longitude = _parse_map_longitude(d.pop("mapLongitude", UNSET))

        def _parse_map_certainty(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        map_certainty = _parse_map_certainty(d.pop("mapCertainty", UNSET))

        def _parse_agency_video_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        agency_video_url = _parse_agency_video_url(d.pop("agencyVideoUrl", UNSET))

        def _parse_agency_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        agency_description = _parse_agency_description(d.pop("agencyDescription", UNSET))

        def _parse_agency_description_cre(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        agency_description_cre = _parse_agency_description_cre(d.pop("agencyDescriptionCre", UNSET))

        def _parse_cre_profile_website(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cre_profile_website = _parse_cre_profile_website(d.pop("creProfileWebsite", UNSET))

        def _parse_agency_cre_banner(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        agency_cre_banner = _parse_agency_cre_banner(d.pop("agencyCreBanner", UNSET))

        def _parse_agency_cre_website(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        agency_cre_website = _parse_agency_cre_website(d.pop("agencyCreWebsite", UNSET))

        def _parse_agency_cre_logo_standard(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        agency_cre_logo_standard = _parse_agency_cre_logo_standard(d.pop("agencyCreLogoStandard", UNSET))

        def _parse_number_for_sale(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        number_for_sale = _parse_number_for_sale(d.pop("numberForSale", UNSET))

        def _parse_number_for_rent(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        number_for_rent = _parse_number_for_rent(d.pop("numberForRent", UNSET))

        def _parse_number_for_sale_commercial(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        number_for_sale_commercial = _parse_number_for_sale_commercial(d.pop("numberForSaleCommercial", UNSET))

        def _parse_number_for_rent_commercial(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        number_for_rent_commercial = _parse_number_for_rent_commercial(d.pop("numberForRentCommercial", UNSET))

        def _parse_cre_agency_video_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cre_agency_video_url = _parse_cre_agency_video_url(d.pop("creAgencyVideoUrl", UNSET))

        agencies_v2_agency_profile = cls(
            agency_photos=agency_photos,
            profile_website=profile_website,
            agency_banner=agency_banner,
            agency_website=agency_website,
            agency_logo_standard=agency_logo_standard,
            agency_logo_small=agency_logo_small,
            logo_colour=logo_colour,
            primary_agency_colour=primary_agency_colour,
            background_colour=background_colour,
            map_latitude=map_latitude,
            map_longitude=map_longitude,
            map_certainty=map_certainty,
            agency_video_url=agency_video_url,
            agency_description=agency_description,
            agency_description_cre=agency_description_cre,
            cre_profile_website=cre_profile_website,
            agency_cre_banner=agency_cre_banner,
            agency_cre_website=agency_cre_website,
            agency_cre_logo_standard=agency_cre_logo_standard,
            number_for_sale=number_for_sale,
            number_for_rent=number_for_rent,
            number_for_sale_commercial=number_for_sale_commercial,
            number_for_rent_commercial=number_for_rent_commercial,
            cre_agency_video_url=cre_agency_video_url,
        )

        return agencies_v2_agency_profile
