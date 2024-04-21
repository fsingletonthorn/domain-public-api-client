import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListingPerformanceV1DailyProjectStatistics")


@_attrs_define
class ListingPerformanceV1DailyProjectStatistics:
    """
    Attributes:
        total_photo_views (Union[None, Unset, int]): Total number of photo views
        total_floorplan_views (Union[None, Unset, int]): Total number of floorplan views
        total_map_views (Union[None, Unset, int]): Total number of address map views
        total_video_views (Union[None, Unset, int]): Total number of video views
        total_agent_detail_views (Union[None, Unset, int]): Total number of agent detail views
        total_search_carousel_views (Union[None, Unset, int]): Total number of views under search carousel
        total_agent_phone_number_reveals (Union[None, Unset, int]): Total number of times the agent phone number was
            revealed for contact
        total_enquiries (Union[None, Unset, int]): Total number of email enquiries
        total_email_to_friend (Union[None, Unset, int]): Total number of times the link was emailed
        total_shared_via_social_media (Union[None, Unset, int]): Total number of shares via social media
        total_inspection_time_saving (Union[None, Unset, int]): Total number of times when the inspection was saved to
            calendar
        total_call_to_agent_from_mobile (Union[None, Unset, int]): Total number of calls made to agent
        dev_project_id (Union[None, Unset, int]): Domain Advertisement Id
        total_views (Union[None, Unset, int]): Total number of views
        total_individual_image_views (Union[None, Unset, int]): Total number of individual image views
        total_ad_click (Union[None, Unset, int]): Total number of ads clicked
        total_clicks_to_project_listing (Union[None, Unset, int]): Total number of click throughs to project listings
        total_external_website_views (Union[None, Unset, int]): Total number of external website view
        total_email_enquiries (Union[None, Unset, int]): Total number of email enquiries
        event_date (Union[None, Unset, datetime.datetime]):
    """

    total_photo_views: Union[None, Unset, int] = UNSET
    total_floorplan_views: Union[None, Unset, int] = UNSET
    total_map_views: Union[None, Unset, int] = UNSET
    total_video_views: Union[None, Unset, int] = UNSET
    total_agent_detail_views: Union[None, Unset, int] = UNSET
    total_search_carousel_views: Union[None, Unset, int] = UNSET
    total_agent_phone_number_reveals: Union[None, Unset, int] = UNSET
    total_enquiries: Union[None, Unset, int] = UNSET
    total_email_to_friend: Union[None, Unset, int] = UNSET
    total_shared_via_social_media: Union[None, Unset, int] = UNSET
    total_inspection_time_saving: Union[None, Unset, int] = UNSET
    total_call_to_agent_from_mobile: Union[None, Unset, int] = UNSET
    dev_project_id: Union[None, Unset, int] = UNSET
    total_views: Union[None, Unset, int] = UNSET
    total_individual_image_views: Union[None, Unset, int] = UNSET
    total_ad_click: Union[None, Unset, int] = UNSET
    total_clicks_to_project_listing: Union[None, Unset, int] = UNSET
    total_external_website_views: Union[None, Unset, int] = UNSET
    total_email_enquiries: Union[None, Unset, int] = UNSET
    event_date: Union[None, Unset, datetime.datetime] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        total_photo_views: Union[None, Unset, int]
        if isinstance(self.total_photo_views, Unset):
            total_photo_views = UNSET
        else:
            total_photo_views = self.total_photo_views

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

        total_agent_detail_views: Union[None, Unset, int]
        if isinstance(self.total_agent_detail_views, Unset):
            total_agent_detail_views = UNSET
        else:
            total_agent_detail_views = self.total_agent_detail_views

        total_search_carousel_views: Union[None, Unset, int]
        if isinstance(self.total_search_carousel_views, Unset):
            total_search_carousel_views = UNSET
        else:
            total_search_carousel_views = self.total_search_carousel_views

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

        dev_project_id: Union[None, Unset, int]
        if isinstance(self.dev_project_id, Unset):
            dev_project_id = UNSET
        else:
            dev_project_id = self.dev_project_id

        total_views: Union[None, Unset, int]
        if isinstance(self.total_views, Unset):
            total_views = UNSET
        else:
            total_views = self.total_views

        total_individual_image_views: Union[None, Unset, int]
        if isinstance(self.total_individual_image_views, Unset):
            total_individual_image_views = UNSET
        else:
            total_individual_image_views = self.total_individual_image_views

        total_ad_click: Union[None, Unset, int]
        if isinstance(self.total_ad_click, Unset):
            total_ad_click = UNSET
        else:
            total_ad_click = self.total_ad_click

        total_clicks_to_project_listing: Union[None, Unset, int]
        if isinstance(self.total_clicks_to_project_listing, Unset):
            total_clicks_to_project_listing = UNSET
        else:
            total_clicks_to_project_listing = self.total_clicks_to_project_listing

        total_external_website_views: Union[None, Unset, int]
        if isinstance(self.total_external_website_views, Unset):
            total_external_website_views = UNSET
        else:
            total_external_website_views = self.total_external_website_views

        total_email_enquiries: Union[None, Unset, int]
        if isinstance(self.total_email_enquiries, Unset):
            total_email_enquiries = UNSET
        else:
            total_email_enquiries = self.total_email_enquiries

        event_date: Union[None, Unset, str]
        if isinstance(self.event_date, Unset):
            event_date = UNSET
        elif isinstance(self.event_date, datetime.datetime):
            event_date = self.event_date.isoformat()
        else:
            event_date = self.event_date

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if total_photo_views is not UNSET:
            field_dict["totalPhotoViews"] = total_photo_views
        if total_floorplan_views is not UNSET:
            field_dict["totalFloorplanViews"] = total_floorplan_views
        if total_map_views is not UNSET:
            field_dict["totalMapViews"] = total_map_views
        if total_video_views is not UNSET:
            field_dict["totalVideoViews"] = total_video_views
        if total_agent_detail_views is not UNSET:
            field_dict["totalAgentDetailViews"] = total_agent_detail_views
        if total_search_carousel_views is not UNSET:
            field_dict["totalSearchCarouselViews"] = total_search_carousel_views
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
        if dev_project_id is not UNSET:
            field_dict["devProjectId"] = dev_project_id
        if total_views is not UNSET:
            field_dict["totalViews"] = total_views
        if total_individual_image_views is not UNSET:
            field_dict["totalIndividualImageViews"] = total_individual_image_views
        if total_ad_click is not UNSET:
            field_dict["totalAdClick"] = total_ad_click
        if total_clicks_to_project_listing is not UNSET:
            field_dict["totalClicksToProjectListing"] = total_clicks_to_project_listing
        if total_external_website_views is not UNSET:
            field_dict["totalExternalWebsiteViews"] = total_external_website_views
        if total_email_enquiries is not UNSET:
            field_dict["totalEmailEnquiries"] = total_email_enquiries
        if event_date is not UNSET:
            field_dict["eventDate"] = event_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_total_photo_views(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        total_photo_views = _parse_total_photo_views(d.pop("totalPhotoViews", UNSET))

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

        def _parse_total_agent_detail_views(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        total_agent_detail_views = _parse_total_agent_detail_views(d.pop("totalAgentDetailViews", UNSET))

        def _parse_total_search_carousel_views(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        total_search_carousel_views = _parse_total_search_carousel_views(d.pop("totalSearchCarouselViews", UNSET))

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

        def _parse_dev_project_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        dev_project_id = _parse_dev_project_id(d.pop("devProjectId", UNSET))

        def _parse_total_views(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        total_views = _parse_total_views(d.pop("totalViews", UNSET))

        def _parse_total_individual_image_views(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        total_individual_image_views = _parse_total_individual_image_views(d.pop("totalIndividualImageViews", UNSET))

        def _parse_total_ad_click(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        total_ad_click = _parse_total_ad_click(d.pop("totalAdClick", UNSET))

        def _parse_total_clicks_to_project_listing(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        total_clicks_to_project_listing = _parse_total_clicks_to_project_listing(
            d.pop("totalClicksToProjectListing", UNSET)
        )

        def _parse_total_external_website_views(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        total_external_website_views = _parse_total_external_website_views(d.pop("totalExternalWebsiteViews", UNSET))

        def _parse_total_email_enquiries(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        total_email_enquiries = _parse_total_email_enquiries(d.pop("totalEmailEnquiries", UNSET))

        def _parse_event_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                event_date_type_0 = isoparse(data)

                return event_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        event_date = _parse_event_date(d.pop("eventDate", UNSET))

        listing_performance_v1_daily_project_statistics = cls(
            total_photo_views=total_photo_views,
            total_floorplan_views=total_floorplan_views,
            total_map_views=total_map_views,
            total_video_views=total_video_views,
            total_agent_detail_views=total_agent_detail_views,
            total_search_carousel_views=total_search_carousel_views,
            total_agent_phone_number_reveals=total_agent_phone_number_reveals,
            total_enquiries=total_enquiries,
            total_email_to_friend=total_email_to_friend,
            total_shared_via_social_media=total_shared_via_social_media,
            total_inspection_time_saving=total_inspection_time_saving,
            total_call_to_agent_from_mobile=total_call_to_agent_from_mobile,
            dev_project_id=dev_project_id,
            total_views=total_views,
            total_individual_image_views=total_individual_image_views,
            total_ad_click=total_ad_click,
            total_clicks_to_project_listing=total_clicks_to_project_listing,
            total_external_website_views=total_external_website_views,
            total_email_enquiries=total_email_enquiries,
            event_date=event_date,
        )

        return listing_performance_v1_daily_project_statistics
