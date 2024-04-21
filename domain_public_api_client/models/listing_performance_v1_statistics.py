from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingPerformanceV1Statistics")


@_attrs_define
class ListingPerformanceV1Statistics:
    """Listing statistics

    Attributes:
        listing_id (Union[None, Unset, int]): Domain Advertisement Id
        total_listing_views (Union[None, Unset, int]): Total number of views for the listing details
        total_photo_views (Union[None, Unset, int]): Total number of listing photo views
        total_photo_gallery_views (Union[None, Unset, int]): Total number of listing photo gallery views
        total_floorplan_views (Union[None, Unset, int]): Total number of floorplan views
        total_map_views (Union[None, Unset, int]): Total number of address map views
        total_video_views (Union[None, Unset, int]): Total number of vedio views
        total_ebrochure_views (Union[None, Unset, int]): Total number of Ebrochure views
        total_agent_detail_views (Union[None, Unset, int]): Total number of agent detail views
        total_shortlisted (Union[None, Unset, int]): Total number of times the listing was shortlisted
        total_printed (Union[None, Unset, int]): Total number of time the listing detail was printed
        total_agent_phone_number_reveals (Union[None, Unset, int]): Total number of times the agent phone number was
            revealed for contact
        total_enquiries (Union[None, Unset, int]): Total number of enquiries
        total_email_to_friend (Union[None, Unset, int]): Total number of times the listing link was emailed
        total_shared_via_social_media (Union[None, Unset, int]): Total number of shares via social media
        total_inspection_time_saving (Union[None, Unset, int]): Total numnber of times when the inspection was saved to
            calendar
        total_call_to_agent_from_mobile (Union[None, Unset, int]): Total number of calls made to agent from inside the
            listing
        percentage_website_views (Union[None, Unset, float]): Percentage of total views from website
        percentage_mobile_site_views (Union[None, Unset, float]): Percentage of total views from mobile site
        percentage_smart_phone_views (Union[None, Unset, float]): Percentage of total views from smart phone apps
        percentage_tablet_views (Union[None, Unset, float]): Percentage of total views from tablets
    """

    listing_id: Union[None, Unset, int] = UNSET
    total_listing_views: Union[None, Unset, int] = UNSET
    total_photo_views: Union[None, Unset, int] = UNSET
    total_photo_gallery_views: Union[None, Unset, int] = UNSET
    total_floorplan_views: Union[None, Unset, int] = UNSET
    total_map_views: Union[None, Unset, int] = UNSET
    total_video_views: Union[None, Unset, int] = UNSET
    total_ebrochure_views: Union[None, Unset, int] = UNSET
    total_agent_detail_views: Union[None, Unset, int] = UNSET
    total_shortlisted: Union[None, Unset, int] = UNSET
    total_printed: Union[None, Unset, int] = UNSET
    total_agent_phone_number_reveals: Union[None, Unset, int] = UNSET
    total_enquiries: Union[None, Unset, int] = UNSET
    total_email_to_friend: Union[None, Unset, int] = UNSET
    total_shared_via_social_media: Union[None, Unset, int] = UNSET
    total_inspection_time_saving: Union[None, Unset, int] = UNSET
    total_call_to_agent_from_mobile: Union[None, Unset, int] = UNSET
    percentage_website_views: Union[None, Unset, float] = UNSET
    percentage_mobile_site_views: Union[None, Unset, float] = UNSET
    percentage_smart_phone_views: Union[None, Unset, float] = UNSET
    percentage_tablet_views: Union[None, Unset, float] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        listing_id: Union[None, Unset, int]
        if isinstance(self.listing_id, Unset):
            listing_id = UNSET
        else:
            listing_id = self.listing_id

        total_listing_views: Union[None, Unset, int]
        if isinstance(self.total_listing_views, Unset):
            total_listing_views = UNSET
        else:
            total_listing_views = self.total_listing_views

        total_photo_views: Union[None, Unset, int]
        if isinstance(self.total_photo_views, Unset):
            total_photo_views = UNSET
        else:
            total_photo_views = self.total_photo_views

        total_photo_gallery_views: Union[None, Unset, int]
        if isinstance(self.total_photo_gallery_views, Unset):
            total_photo_gallery_views = UNSET
        else:
            total_photo_gallery_views = self.total_photo_gallery_views

        total_floorplan_views: Union[None, Unset, int]
        if isinstance(self.total_floorplan_views, Unset):
            total_floorplan_views = UNSET
        else:
            total_floorplan_views = self.total_floorplan_views

        total_map_views: Union[None, Unset, int]
        if isinstance(self.total_map_views, Unset):
            total_map_views = UNSET
        else:
            total_map_views = self.total_map_views

        total_video_views: Union[None, Unset, int]
        if isinstance(self.total_video_views, Unset):
            total_video_views = UNSET
        else:
            total_video_views = self.total_video_views

        total_ebrochure_views: Union[None, Unset, int]
        if isinstance(self.total_ebrochure_views, Unset):
            total_ebrochure_views = UNSET
        else:
            total_ebrochure_views = self.total_ebrochure_views

        total_agent_detail_views: Union[None, Unset, int]
        if isinstance(self.total_agent_detail_views, Unset):
            total_agent_detail_views = UNSET
        else:
            total_agent_detail_views = self.total_agent_detail_views

        total_shortlisted: Union[None, Unset, int]
        if isinstance(self.total_shortlisted, Unset):
            total_shortlisted = UNSET
        else:
            total_shortlisted = self.total_shortlisted

        total_printed: Union[None, Unset, int]
        if isinstance(self.total_printed, Unset):
            total_printed = UNSET
        else:
            total_printed = self.total_printed

        total_agent_phone_number_reveals: Union[None, Unset, int]
        if isinstance(self.total_agent_phone_number_reveals, Unset):
            total_agent_phone_number_reveals = UNSET
        else:
            total_agent_phone_number_reveals = self.total_agent_phone_number_reveals

        total_enquiries: Union[None, Unset, int]
        if isinstance(self.total_enquiries, Unset):
            total_enquiries = UNSET
        else:
            total_enquiries = self.total_enquiries

        total_email_to_friend: Union[None, Unset, int]
        if isinstance(self.total_email_to_friend, Unset):
            total_email_to_friend = UNSET
        else:
            total_email_to_friend = self.total_email_to_friend

        total_shared_via_social_media: Union[None, Unset, int]
        if isinstance(self.total_shared_via_social_media, Unset):
            total_shared_via_social_media = UNSET
        else:
            total_shared_via_social_media = self.total_shared_via_social_media

        total_inspection_time_saving: Union[None, Unset, int]
        if isinstance(self.total_inspection_time_saving, Unset):
            total_inspection_time_saving = UNSET
        else:
            total_inspection_time_saving = self.total_inspection_time_saving

        total_call_to_agent_from_mobile: Union[None, Unset, int]
        if isinstance(self.total_call_to_agent_from_mobile, Unset):
            total_call_to_agent_from_mobile = UNSET
        else:
            total_call_to_agent_from_mobile = self.total_call_to_agent_from_mobile

        percentage_website_views: Union[None, Unset, float]
        if isinstance(self.percentage_website_views, Unset):
            percentage_website_views = UNSET
        else:
            percentage_website_views = self.percentage_website_views

        percentage_mobile_site_views: Union[None, Unset, float]
        if isinstance(self.percentage_mobile_site_views, Unset):
            percentage_mobile_site_views = UNSET
        else:
            percentage_mobile_site_views = self.percentage_mobile_site_views

        percentage_smart_phone_views: Union[None, Unset, float]
        if isinstance(self.percentage_smart_phone_views, Unset):
            percentage_smart_phone_views = UNSET
        else:
            percentage_smart_phone_views = self.percentage_smart_phone_views

        percentage_tablet_views: Union[None, Unset, float]
        if isinstance(self.percentage_tablet_views, Unset):
            percentage_tablet_views = UNSET
        else:
            percentage_tablet_views = self.percentage_tablet_views

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if total_listing_views is not UNSET:
            field_dict["totalListingViews"] = total_listing_views
        if total_photo_views is not UNSET:
            field_dict["totalPhotoViews"] = total_photo_views
        if total_photo_gallery_views is not UNSET:
            field_dict["totalPhotoGalleryViews"] = total_photo_gallery_views
        if total_floorplan_views is not UNSET:
            field_dict["totalFloorplanViews"] = total_floorplan_views
        if total_map_views is not UNSET:
            field_dict["totalMapViews"] = total_map_views
        if total_video_views is not UNSET:
            field_dict["totalVideoViews"] = total_video_views
        if total_ebrochure_views is not UNSET:
            field_dict["totalEbrochureViews"] = total_ebrochure_views
        if total_agent_detail_views is not UNSET:
            field_dict["totalAgentDetailViews"] = total_agent_detail_views
        if total_shortlisted is not UNSET:
            field_dict["totalShortlisted"] = total_shortlisted
        if total_printed is not UNSET:
            field_dict["totalPrinted"] = total_printed
        if total_agent_phone_number_reveals is not UNSET:
            field_dict["totalAgentPhoneNumberReveals"] = total_agent_phone_number_reveals
        if total_enquiries is not UNSET:
            field_dict["totalEnquiries"] = total_enquiries
        if total_email_to_friend is not UNSET:
            field_dict["totalEmailToFriend"] = total_email_to_friend
        if total_shared_via_social_media is not UNSET:
            field_dict["totalSharedViaSocialMedia"] = total_shared_via_social_media
        if total_inspection_time_saving is not UNSET:
            field_dict["totalInspectionTimeSaving"] = total_inspection_time_saving
        if total_call_to_agent_from_mobile is not UNSET:
            field_dict["totalCallToAgentFromMobile"] = total_call_to_agent_from_mobile
        if percentage_website_views is not UNSET:
            field_dict["percentageWebsiteViews"] = percentage_website_views
        if percentage_mobile_site_views is not UNSET:
            field_dict["percentageMobileSiteViews"] = percentage_mobile_site_views
        if percentage_smart_phone_views is not UNSET:
            field_dict["percentageSmartPhoneViews"] = percentage_smart_phone_views
        if percentage_tablet_views is not UNSET:
            field_dict["percentageTabletViews"] = percentage_tablet_views

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_listing_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        listing_id = _parse_listing_id(d.pop("listingId", UNSET))

        def _parse_total_listing_views(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        total_listing_views = _parse_total_listing_views(d.pop("totalListingViews", UNSET))

        def _parse_total_photo_views(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        total_photo_views = _parse_total_photo_views(d.pop("totalPhotoViews", UNSET))

        def _parse_total_photo_gallery_views(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        total_photo_gallery_views = _parse_total_photo_gallery_views(d.pop("totalPhotoGalleryViews", UNSET))

        def _parse_total_floorplan_views(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        total_floorplan_views = _parse_total_floorplan_views(d.pop("totalFloorplanViews", UNSET))

        def _parse_total_map_views(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        total_map_views = _parse_total_map_views(d.pop("totalMapViews", UNSET))

        def _parse_total_video_views(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        total_video_views = _parse_total_video_views(d.pop("totalVideoViews", UNSET))

        def _parse_total_ebrochure_views(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        total_ebrochure_views = _parse_total_ebrochure_views(d.pop("totalEbrochureViews", UNSET))

        def _parse_total_agent_detail_views(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        total_agent_detail_views = _parse_total_agent_detail_views(d.pop("totalAgentDetailViews", UNSET))

        def _parse_total_shortlisted(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        total_shortlisted = _parse_total_shortlisted(d.pop("totalShortlisted", UNSET))

        def _parse_total_printed(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        total_printed = _parse_total_printed(d.pop("totalPrinted", UNSET))

        def _parse_total_agent_phone_number_reveals(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        total_agent_phone_number_reveals = _parse_total_agent_phone_number_reveals(
            d.pop("totalAgentPhoneNumberReveals", UNSET)
        )

        def _parse_total_enquiries(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        total_enquiries = _parse_total_enquiries(d.pop("totalEnquiries", UNSET))

        def _parse_total_email_to_friend(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        total_email_to_friend = _parse_total_email_to_friend(d.pop("totalEmailToFriend", UNSET))

        def _parse_total_shared_via_social_media(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        total_shared_via_social_media = _parse_total_shared_via_social_media(d.pop("totalSharedViaSocialMedia", UNSET))

        def _parse_total_inspection_time_saving(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        total_inspection_time_saving = _parse_total_inspection_time_saving(d.pop("totalInspectionTimeSaving", UNSET))

        def _parse_total_call_to_agent_from_mobile(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        total_call_to_agent_from_mobile = _parse_total_call_to_agent_from_mobile(
            d.pop("totalCallToAgentFromMobile", UNSET)
        )

        def _parse_percentage_website_views(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        percentage_website_views = _parse_percentage_website_views(d.pop("percentageWebsiteViews", UNSET))

        def _parse_percentage_mobile_site_views(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        percentage_mobile_site_views = _parse_percentage_mobile_site_views(d.pop("percentageMobileSiteViews", UNSET))

        def _parse_percentage_smart_phone_views(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        percentage_smart_phone_views = _parse_percentage_smart_phone_views(d.pop("percentageSmartPhoneViews", UNSET))

        def _parse_percentage_tablet_views(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        percentage_tablet_views = _parse_percentage_tablet_views(d.pop("percentageTabletViews", UNSET))

        listing_performance_v1_statistics = cls(
            listing_id=listing_id,
            total_listing_views=total_listing_views,
            total_photo_views=total_photo_views,
            total_photo_gallery_views=total_photo_gallery_views,
            total_floorplan_views=total_floorplan_views,
            total_map_views=total_map_views,
            total_video_views=total_video_views,
            total_ebrochure_views=total_ebrochure_views,
            total_agent_detail_views=total_agent_detail_views,
            total_shortlisted=total_shortlisted,
            total_printed=total_printed,
            total_agent_phone_number_reveals=total_agent_phone_number_reveals,
            total_enquiries=total_enquiries,
            total_email_to_friend=total_email_to_friend,
            total_shared_via_social_media=total_shared_via_social_media,
            total_inspection_time_saving=total_inspection_time_saving,
            total_call_to_agent_from_mobile=total_call_to_agent_from_mobile,
            percentage_website_views=percentage_website_views,
            percentage_mobile_site_views=percentage_mobile_site_views,
            percentage_smart_phone_views=percentage_smart_phone_views,
            percentage_tablet_views=percentage_tablet_views,
        )

        return listing_performance_v1_statistics
