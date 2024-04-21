import datetime
from typing import Any, Dict, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgenciesV1Agent")


@_attrs_define
class AgenciesV1Agent:
    """AgentDto

    Attributes:
        date_updated (Union[None, Unset, datetime.datetime]): Gets or Sets DateUpdated
        agency_id (Union[None, Unset, int]): Gets or Sets AgencyId
        agent_id (Union[None, Unset, int]): Gets or Sets AgentId
        email (Union[None, Unset, str]): Gets or Sets Email
        first_name (Union[None, Unset, str]): Gets or Sets FirstName
        mobile (Union[None, Unset, str]): Gets or Sets Mobile
        photo (Union[None, Unset, str]): Gets or Sets Photo
        last_name (Union[None, Unset, str]): Gets or Sets LastName
        is_active_profile_page (Union[None, Unset, str]): Gets or Sets IsActiveProfilePage
        phone (Union[None, Unset, str]): Gets or Sets Phone
        sale_active (Union[None, Unset, bool]): Gets or Sets SaleActive
        rental_active (Union[None, Unset, bool]): Gets or Sets RentalActive
        secondary_email (Union[None, Unset, str]): Gets or Sets SecondaryEmail
        facebook_url (Union[None, Unset, str]): Gets or Sets FacebookUrl
        twitter_url (Union[None, Unset, str]): Gets or Sets TwitterUrl
        agent_video (Union[None, Unset, str]): Gets or Sets AgentVideo
        profile_text (Union[None, Unset, str]): Gets or Sets ProfileText
        is_hide_sold_leased_listings (Union[None, Unset, bool]): Gets or Sets IsHideSoldLeasedListings
        google_plus_url (Union[None, Unset, str]): Gets or Sets GooglePlusUrl
        personal_website_url (Union[None, Unset, str]): Gets or Sets PersonalWebsiteUrl
        linked_in_url (Union[None, Unset, str]): Gets or Sets LinkedInUrl
        fax (Union[None, Unset, str]): Gets or Sets Fax
        mug_shot_url (Union[None, Unset, str]): Gets or Sets MugShotURL
        mug_shot_new (Union[None, Unset, str]): Gets or Sets MugShotNew
        contact_type_code (Union[None, Unset, int]): Gets or Sets ContactTypeCode
        receives_requests (Union[None, Unset, bool]): Gets or Sets ReceivesRequests
        cre_agent_video_url (Union[None, Unset, str]): Gets or Sets CreAgentVideoURL
        receive_scheduled_report_email (Union[None, Unset, bool]): Gets or Sets ReceiveScheduledReportEmail
        profile_url (Union[None, Unset, str]): Gets or Sets ProfileUrl
        job_position (Union[None, Unset, str]): Gets or Sets JobPosition
    """

    date_updated: Union[None, Unset, datetime.datetime] = UNSET
    agency_id: Union[None, Unset, int] = UNSET
    agent_id: Union[None, Unset, int] = UNSET
    email: Union[None, Unset, str] = UNSET
    first_name: Union[None, Unset, str] = UNSET
    mobile: Union[None, Unset, str] = UNSET
    photo: Union[None, Unset, str] = UNSET
    last_name: Union[None, Unset, str] = UNSET
    is_active_profile_page: Union[None, Unset, str] = UNSET
    phone: Union[None, Unset, str] = UNSET
    sale_active: Union[None, Unset, bool] = UNSET
    rental_active: Union[None, Unset, bool] = UNSET
    secondary_email: Union[None, Unset, str] = UNSET
    facebook_url: Union[None, Unset, str] = UNSET
    twitter_url: Union[None, Unset, str] = UNSET
    agent_video: Union[None, Unset, str] = UNSET
    profile_text: Union[None, Unset, str] = UNSET
    is_hide_sold_leased_listings: Union[None, Unset, bool] = UNSET
    google_plus_url: Union[None, Unset, str] = UNSET
    personal_website_url: Union[None, Unset, str] = UNSET
    linked_in_url: Union[None, Unset, str] = UNSET
    fax: Union[None, Unset, str] = UNSET
    mug_shot_url: Union[None, Unset, str] = UNSET
    mug_shot_new: Union[None, Unset, str] = UNSET
    contact_type_code: Union[None, Unset, int] = UNSET
    receives_requests: Union[None, Unset, bool] = UNSET
    cre_agent_video_url: Union[None, Unset, str] = UNSET
    receive_scheduled_report_email: Union[None, Unset, bool] = UNSET
    profile_url: Union[None, Unset, str] = UNSET
    job_position: Union[None, Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        date_updated: Union[None, Unset, str]
        if isinstance(self.date_updated, Unset):
            date_updated = UNSET
        elif isinstance(self.date_updated, datetime.datetime):
            date_updated = self.date_updated.isoformat()
        else:
            date_updated = self.date_updated

        agency_id: Union[None, Unset, int]
        if isinstance(self.agency_id, Unset):
            agency_id = UNSET
        else:
            agency_id = self.agency_id

        agent_id: Union[None, Unset, int]
        if isinstance(self.agent_id, Unset):
            agent_id = UNSET
        else:
            agent_id = self.agent_id

        email: Union[None, Unset, str]
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        first_name: Union[None, Unset, str]
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        mobile: Union[None, Unset, str]
        if isinstance(self.mobile, Unset):
            mobile = UNSET
        else:
            mobile = self.mobile

        photo: Union[None, Unset, str]
        if isinstance(self.photo, Unset):
            photo = UNSET
        else:
            photo = self.photo

        last_name: Union[None, Unset, str]
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        is_active_profile_page: Union[None, Unset, str]
        if isinstance(self.is_active_profile_page, Unset):
            is_active_profile_page = UNSET
        else:
            is_active_profile_page = self.is_active_profile_page

        phone: Union[None, Unset, str]
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        sale_active: Union[None, Unset, bool]
        if isinstance(self.sale_active, Unset):
            sale_active = UNSET
        else:
            sale_active = self.sale_active

        rental_active: Union[None, Unset, bool]
        if isinstance(self.rental_active, Unset):
            rental_active = UNSET
        else:
            rental_active = self.rental_active

        secondary_email: Union[None, Unset, str]
        if isinstance(self.secondary_email, Unset):
            secondary_email = UNSET
        else:
            secondary_email = self.secondary_email

        facebook_url: Union[None, Unset, str]
        if isinstance(self.facebook_url, Unset):
            facebook_url = UNSET
        else:
            facebook_url = self.facebook_url

        twitter_url: Union[None, Unset, str]
        if isinstance(self.twitter_url, Unset):
            twitter_url = UNSET
        else:
            twitter_url = self.twitter_url

        agent_video: Union[None, Unset, str]
        if isinstance(self.agent_video, Unset):
            agent_video = UNSET
        else:
            agent_video = self.agent_video

        profile_text: Union[None, Unset, str]
        if isinstance(self.profile_text, Unset):
            profile_text = UNSET
        else:
            profile_text = self.profile_text

        is_hide_sold_leased_listings: Union[None, Unset, bool]
        if isinstance(self.is_hide_sold_leased_listings, Unset):
            is_hide_sold_leased_listings = UNSET
        else:
            is_hide_sold_leased_listings = self.is_hide_sold_leased_listings

        google_plus_url: Union[None, Unset, str]
        if isinstance(self.google_plus_url, Unset):
            google_plus_url = UNSET
        else:
            google_plus_url = self.google_plus_url

        personal_website_url: Union[None, Unset, str]
        if isinstance(self.personal_website_url, Unset):
            personal_website_url = UNSET
        else:
            personal_website_url = self.personal_website_url

        linked_in_url: Union[None, Unset, str]
        if isinstance(self.linked_in_url, Unset):
            linked_in_url = UNSET
        else:
            linked_in_url = self.linked_in_url

        fax: Union[None, Unset, str]
        if isinstance(self.fax, Unset):
            fax = UNSET
        else:
            fax = self.fax

        mug_shot_url: Union[None, Unset, str]
        if isinstance(self.mug_shot_url, Unset):
            mug_shot_url = UNSET
        else:
            mug_shot_url = self.mug_shot_url

        mug_shot_new: Union[None, Unset, str]
        if isinstance(self.mug_shot_new, Unset):
            mug_shot_new = UNSET
        else:
            mug_shot_new = self.mug_shot_new

        contact_type_code: Union[None, Unset, int]
        if isinstance(self.contact_type_code, Unset):
            contact_type_code = UNSET
        else:
            contact_type_code = self.contact_type_code

        receives_requests: Union[None, Unset, bool]
        if isinstance(self.receives_requests, Unset):
            receives_requests = UNSET
        else:
            receives_requests = self.receives_requests

        cre_agent_video_url: Union[None, Unset, str]
        if isinstance(self.cre_agent_video_url, Unset):
            cre_agent_video_url = UNSET
        else:
            cre_agent_video_url = self.cre_agent_video_url

        receive_scheduled_report_email: Union[None, Unset, bool]
        if isinstance(self.receive_scheduled_report_email, Unset):
            receive_scheduled_report_email = UNSET
        else:
            receive_scheduled_report_email = self.receive_scheduled_report_email

        profile_url: Union[None, Unset, str]
        if isinstance(self.profile_url, Unset):
            profile_url = UNSET
        else:
            profile_url = self.profile_url

        job_position: Union[None, Unset, str]
        if isinstance(self.job_position, Unset):
            job_position = UNSET
        else:
            job_position = self.job_position

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if date_updated is not UNSET:
            field_dict["dateUpdated"] = date_updated
        if agency_id is not UNSET:
            field_dict["agencyId"] = agency_id
        if agent_id is not UNSET:
            field_dict["agentId"] = agent_id
        if email is not UNSET:
            field_dict["email"] = email
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if mobile is not UNSET:
            field_dict["mobile"] = mobile
        if photo is not UNSET:
            field_dict["photo"] = photo
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if is_active_profile_page is not UNSET:
            field_dict["isActiveProfilePage"] = is_active_profile_page
        if phone is not UNSET:
            field_dict["phone"] = phone
        if sale_active is not UNSET:
            field_dict["saleActive"] = sale_active
        if rental_active is not UNSET:
            field_dict["rentalActive"] = rental_active
        if secondary_email is not UNSET:
            field_dict["secondaryEmail"] = secondary_email
        if facebook_url is not UNSET:
            field_dict["facebookUrl"] = facebook_url
        if twitter_url is not UNSET:
            field_dict["twitterUrl"] = twitter_url
        if agent_video is not UNSET:
            field_dict["agentVideo"] = agent_video
        if profile_text is not UNSET:
            field_dict["profileText"] = profile_text
        if is_hide_sold_leased_listings is not UNSET:
            field_dict["isHideSoldLeasedListings"] = is_hide_sold_leased_listings
        if google_plus_url is not UNSET:
            field_dict["googlePlusUrl"] = google_plus_url
        if personal_website_url is not UNSET:
            field_dict["personalWebsiteUrl"] = personal_website_url
        if linked_in_url is not UNSET:
            field_dict["linkedInUrl"] = linked_in_url
        if fax is not UNSET:
            field_dict["fax"] = fax
        if mug_shot_url is not UNSET:
            field_dict["mugShotURL"] = mug_shot_url
        if mug_shot_new is not UNSET:
            field_dict["mugShotNew"] = mug_shot_new
        if contact_type_code is not UNSET:
            field_dict["contactTypeCode"] = contact_type_code
        if receives_requests is not UNSET:
            field_dict["receivesRequests"] = receives_requests
        if cre_agent_video_url is not UNSET:
            field_dict["creAgentVideoURL"] = cre_agent_video_url
        if receive_scheduled_report_email is not UNSET:
            field_dict["receiveScheduledReportEmail"] = receive_scheduled_report_email
        if profile_url is not UNSET:
            field_dict["profileUrl"] = profile_url
        if job_position is not UNSET:
            field_dict["jobPosition"] = job_position

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_date_updated(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_updated_type_0 = isoparse(data)

                return date_updated_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        date_updated = _parse_date_updated(d.pop("dateUpdated", UNSET))

        def _parse_agency_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        agency_id = _parse_agency_id(d.pop("agencyId", UNSET))

        def _parse_agent_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        agent_id = _parse_agent_id(d.pop("agentId", UNSET))

        def _parse_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_first_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        first_name = _parse_first_name(d.pop("firstName", UNSET))

        def _parse_mobile(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mobile = _parse_mobile(d.pop("mobile", UNSET))

        def _parse_photo(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        photo = _parse_photo(d.pop("photo", UNSET))

        def _parse_last_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        last_name = _parse_last_name(d.pop("lastName", UNSET))

        def _parse_is_active_profile_page(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        is_active_profile_page = _parse_is_active_profile_page(d.pop("isActiveProfilePage", UNSET))

        def _parse_phone(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        phone = _parse_phone(d.pop("phone", UNSET))

        def _parse_sale_active(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        sale_active = _parse_sale_active(d.pop("saleActive", UNSET))

        def _parse_rental_active(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        rental_active = _parse_rental_active(d.pop("rentalActive", UNSET))

        def _parse_secondary_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        secondary_email = _parse_secondary_email(d.pop("secondaryEmail", UNSET))

        def _parse_facebook_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        facebook_url = _parse_facebook_url(d.pop("facebookUrl", UNSET))

        def _parse_twitter_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        twitter_url = _parse_twitter_url(d.pop("twitterUrl", UNSET))

        def _parse_agent_video(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        agent_video = _parse_agent_video(d.pop("agentVideo", UNSET))

        def _parse_profile_text(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        profile_text = _parse_profile_text(d.pop("profileText", UNSET))

        def _parse_is_hide_sold_leased_listings(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        is_hide_sold_leased_listings = _parse_is_hide_sold_leased_listings(d.pop("isHideSoldLeasedListings", UNSET))

        def _parse_google_plus_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        google_plus_url = _parse_google_plus_url(d.pop("googlePlusUrl", UNSET))

        def _parse_personal_website_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        personal_website_url = _parse_personal_website_url(d.pop("personalWebsiteUrl", UNSET))

        def _parse_linked_in_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        linked_in_url = _parse_linked_in_url(d.pop("linkedInUrl", UNSET))

        def _parse_fax(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        fax = _parse_fax(d.pop("fax", UNSET))

        def _parse_mug_shot_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mug_shot_url = _parse_mug_shot_url(d.pop("mugShotURL", UNSET))

        def _parse_mug_shot_new(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mug_shot_new = _parse_mug_shot_new(d.pop("mugShotNew", UNSET))

        def _parse_contact_type_code(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        contact_type_code = _parse_contact_type_code(d.pop("contactTypeCode", UNSET))

        def _parse_receives_requests(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        receives_requests = _parse_receives_requests(d.pop("receivesRequests", UNSET))

        def _parse_cre_agent_video_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cre_agent_video_url = _parse_cre_agent_video_url(d.pop("creAgentVideoURL", UNSET))

        def _parse_receive_scheduled_report_email(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        receive_scheduled_report_email = _parse_receive_scheduled_report_email(
            d.pop("receiveScheduledReportEmail", UNSET)
        )

        def _parse_profile_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        profile_url = _parse_profile_url(d.pop("profileUrl", UNSET))

        def _parse_job_position(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        job_position = _parse_job_position(d.pop("jobPosition", UNSET))

        agencies_v1_agent = cls(
            date_updated=date_updated,
            agency_id=agency_id,
            agent_id=agent_id,
            email=email,
            first_name=first_name,
            mobile=mobile,
            photo=photo,
            last_name=last_name,
            is_active_profile_page=is_active_profile_page,
            phone=phone,
            sale_active=sale_active,
            rental_active=rental_active,
            secondary_email=secondary_email,
            facebook_url=facebook_url,
            twitter_url=twitter_url,
            agent_video=agent_video,
            profile_text=profile_text,
            is_hide_sold_leased_listings=is_hide_sold_leased_listings,
            google_plus_url=google_plus_url,
            personal_website_url=personal_website_url,
            linked_in_url=linked_in_url,
            fax=fax,
            mug_shot_url=mug_shot_url,
            mug_shot_new=mug_shot_new,
            contact_type_code=contact_type_code,
            receives_requests=receives_requests,
            cre_agent_video_url=cre_agent_video_url,
            receive_scheduled_report_email=receive_scheduled_report_email,
            profile_url=profile_url,
            job_position=job_position,
        )

        return agencies_v1_agent
