from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.listing_admin_v2_commercial_listing_v2 import ListingAdminV2CommercialListingV2
from ...models.listing_admin_v2_listing_response import ListingAdminV2ListingResponse
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        ListingAdminV2CommercialListingV2,
        ListingAdminV2CommercialListingV2,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": "/v2/listings/commercial",
    }

    if isinstance(body, ListingAdminV2CommercialListingV2):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, ListingAdminV2CommercialListingV2):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ListingAdminV2ListingResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListingAdminV2ListingResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = ListingAdminV2ListingResponse.from_dict(response.json())

        return response_202
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ListingAdminV2ListingResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        ListingAdminV2CommercialListingV2,
        ListingAdminV2CommercialListingV2,
    ],
) -> Response[Union[Any, ListingAdminV2ListingResponse]]:
    """Creates a commercial listing.

    Args:
        body (ListingAdminV2CommercialListingV2): Commercial Listing V2 Example: {'salePrice':
            {'priceUnitType': 'totalAmount', 'priceType': 'gross', 'gstOptionType': 'ex',
            'priceReduction': True, 'displayText': 'Price Guide $2,200,000', 'from': 2200000, 'to':
            2200000}, 'leasePrice': {'priceUnitType': 'totalAmount', 'priceType': 'gross',
            'gstOptionType': 'ex', 'priceReduction': True, 'displayText': 'Price Guide $2,200',
            'from': 2200, 'to': 2200}, 'lease': {'termOfLeaseFrom': 1, 'termOfLeaseTo': 3,
            'leaseOutgoings': 3200}, 'tenant': {'leaseStart': '2021-11-11T16:31:07.5504369+11:00',
            'leaseEnd': '2022-11-11T16:31:07.5504369+11:00', 'name': 'John Smith', 'rentalDetails':
            'Annual CPI reviews', 'leaseOptions': '5+5 year lease which commenced May 2013',
            'tenantInfoTermOfLeaseFrom': 2, 'tenantInfoTermOfLeaseTo': 3, 'leaseDateVariable': False},
            'tender': {'recipientName': 'Joe Russ', 'address': '10,Pyrmont st, Pyrmont,NSW 2011',
            'endDate': '2022-10-21T16:31:07.5504369+11:00'}, 'occupancyType': 'tenanted',
            'annualReturn': 10, 'unitsOffered': 1, 'nabers': 4.5, 'saleTerms': 'will be started after
            3 days', 'auction': {'auctionTerms': '10% deposit, balance 60 days.', 'dateTime':
            '2022-10-11T16:31:07.5504369+11:00', 'location': 'On Site', 'url':
            'https://ljhookermosman.agentboxcrm.com.au/www/fp-1-1P3679-1721283621.html'},
            'propertyDetails': {'propertyType': ['retail'], 'buildingType': 'whole', 'parking':
            {'parkingType': 'noParking', 'numberOnSite': 0}, 'pdfs': [], 'images': [{'resourceType':
            'floorPlan', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/fp-1-1P3679-1721283621.jpg'},
            {'resourceType': 'photograph', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/lt-1-1P3679-0316165440.jpg'},
            {'resourceType': 'photograph', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/lt-1-1P3679-0316165441.jpg'}], 'address':
            {'unitNumber': 'Suite 11A', 'street': 'Military Road', 'displayOption': 'fullAddress',
            'streetNumber': '287', 'suburb': 'Cremorne', 'postcode': '2090', 'state': 'nsw'}, 'area':
            {'value': 174, 'unit': 'squareMetres'}, 'landArea': {'unit': 'squareMetres', 'value':
            194}}, 'conjunctionAgents': [{'agencyId': 12346, 'domainAgentId': 484442, 'firstName':
            'Sam', 'lastName': 'Karri', 'phone': '02 8356 7127', 'fax': '23444 444 44', 'mobile':
            '0411 345 877', 'email': 'a@a.com', 'receiveEmails': True}], 'highlights': ['Hightlight
            1', 'Hightlight 2', 'Hightlight 3'], 'underOfferOrContract': False, 'listingProvider':
            'YOUR_LISTING_PROVIDER', 'domainAgencyID': 13, 'providerAdId': 'YOUR_PROVIDER_AD_ID',
            'features': ' Air conditioning, Alarm System, Intercom', 'description': 'Situated within
            Cremorne Town Shopping Centre, anchored by Supa IGA supermarket, this property represents
            a fantastic opportunity to own a tenanted strata retail shop in a successful shopping
            centre.', 'summary': 'Entry Level Investment Opportunity!', 'inspectionDetails':
            {'inspections': [{'from': '2022-10-11T17:00:00.0000000+11:00', 'to':
            '2022-10-11T18:00:00.0000000+11:00', 'repeat': False}, {'from':
            '2022-10-13T17:00:00.0000000+11:00', 'to': '2022-10-13T18:00:00.0000000+11:00', 'repeat':
            False}, {'from': '2022-10-15T17:00:00.0000000+11:00', 'to':
            '2022-10-15T18:00:00.0000000+11:00', 'repeat': False}, {'from':
            '2022-10-17T17:00:00.0000000+11:00', 'to': '2022-10-17T18:00:00.0000000+11:00', 'repeat':
            False}, {'from': '2022-10-19T17:00:00.0000000+11:00', 'to':
            '2022-10-19T18:00:00.0000000+11:00', 'repeat': False}]}, 'media': [{'resourceType':
            'video', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/fp-1-1P3679-1721283621.mp4'},
            {'resourceType': 'virtualTour', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/fp-1-1P3679-1721283621.html'},
            {'resourceType': 'webLink', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/fp-1-1P3679-1721283621.html'}],
            'listingAction': 'saleAndLease', 'contacts': [{'domainAgentId': 881492, 'firstName':
            'Jack', 'lastName': 'King', 'phone': '02 8356 7127', 'fax': '23444 444 44', 'mobile':
            '0411 245 777', 'email': 'a@a.com', 'receiveEmails': True}], 'otherEnquiryEmail':
            'b@a.com,d@c.co,f@e.io', 'receiveEmailsToDefaultAddress': False}.
        body (ListingAdminV2CommercialListingV2): Commercial Listing V2 Example: {'salePrice':
            {'priceUnitType': 'totalAmount', 'priceType': 'gross', 'gstOptionType': 'ex',
            'priceReduction': True, 'displayText': 'Price Guide $2,200,000', 'from': 2200000, 'to':
            2200000}, 'leasePrice': {'priceUnitType': 'totalAmount', 'priceType': 'gross',
            'gstOptionType': 'ex', 'priceReduction': True, 'displayText': 'Price Guide $2,200',
            'from': 2200, 'to': 2200}, 'lease': {'termOfLeaseFrom': 1, 'termOfLeaseTo': 3,
            'leaseOutgoings': 3200}, 'tenant': {'leaseStart': '2021-11-11T16:31:07.5504369+11:00',
            'leaseEnd': '2022-11-11T16:31:07.5504369+11:00', 'name': 'John Smith', 'rentalDetails':
            'Annual CPI reviews', 'leaseOptions': '5+5 year lease which commenced May 2013',
            'tenantInfoTermOfLeaseFrom': 2, 'tenantInfoTermOfLeaseTo': 3, 'leaseDateVariable': False},
            'tender': {'recipientName': 'Joe Russ', 'address': '10,Pyrmont st, Pyrmont,NSW 2011',
            'endDate': '2022-10-21T16:31:07.5504369+11:00'}, 'occupancyType': 'tenanted',
            'annualReturn': 10, 'unitsOffered': 1, 'nabers': 4.5, 'saleTerms': 'will be started after
            3 days', 'auction': {'auctionTerms': '10% deposit, balance 60 days.', 'dateTime':
            '2022-10-11T16:31:07.5504369+11:00', 'location': 'On Site', 'url':
            'https://ljhookermosman.agentboxcrm.com.au/www/fp-1-1P3679-1721283621.html'},
            'propertyDetails': {'propertyType': ['retail'], 'buildingType': 'whole', 'parking':
            {'parkingType': 'noParking', 'numberOnSite': 0}, 'pdfs': [], 'images': [{'resourceType':
            'floorPlan', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/fp-1-1P3679-1721283621.jpg'},
            {'resourceType': 'photograph', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/lt-1-1P3679-0316165440.jpg'},
            {'resourceType': 'photograph', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/lt-1-1P3679-0316165441.jpg'}], 'address':
            {'unitNumber': 'Suite 11A', 'street': 'Military Road', 'displayOption': 'fullAddress',
            'streetNumber': '287', 'suburb': 'Cremorne', 'postcode': '2090', 'state': 'nsw'}, 'area':
            {'value': 174, 'unit': 'squareMetres'}, 'landArea': {'unit': 'squareMetres', 'value':
            194}}, 'conjunctionAgents': [{'agencyId': 12346, 'domainAgentId': 484442, 'firstName':
            'Sam', 'lastName': 'Karri', 'phone': '02 8356 7127', 'fax': '23444 444 44', 'mobile':
            '0411 345 877', 'email': 'a@a.com', 'receiveEmails': True}], 'highlights': ['Hightlight
            1', 'Hightlight 2', 'Hightlight 3'], 'underOfferOrContract': False, 'listingProvider':
            'YOUR_LISTING_PROVIDER', 'domainAgencyID': 13, 'providerAdId': 'YOUR_PROVIDER_AD_ID',
            'features': ' Air conditioning, Alarm System, Intercom', 'description': 'Situated within
            Cremorne Town Shopping Centre, anchored by Supa IGA supermarket, this property represents
            a fantastic opportunity to own a tenanted strata retail shop in a successful shopping
            centre.', 'summary': 'Entry Level Investment Opportunity!', 'inspectionDetails':
            {'inspections': [{'from': '2022-10-11T17:00:00.0000000+11:00', 'to':
            '2022-10-11T18:00:00.0000000+11:00', 'repeat': False}, {'from':
            '2022-10-13T17:00:00.0000000+11:00', 'to': '2022-10-13T18:00:00.0000000+11:00', 'repeat':
            False}, {'from': '2022-10-15T17:00:00.0000000+11:00', 'to':
            '2022-10-15T18:00:00.0000000+11:00', 'repeat': False}, {'from':
            '2022-10-17T17:00:00.0000000+11:00', 'to': '2022-10-17T18:00:00.0000000+11:00', 'repeat':
            False}, {'from': '2022-10-19T17:00:00.0000000+11:00', 'to':
            '2022-10-19T18:00:00.0000000+11:00', 'repeat': False}]}, 'media': [{'resourceType':
            'video', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/fp-1-1P3679-1721283621.mp4'},
            {'resourceType': 'virtualTour', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/fp-1-1P3679-1721283621.html'},
            {'resourceType': 'webLink', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/fp-1-1P3679-1721283621.html'}],
            'listingAction': 'saleAndLease', 'contacts': [{'domainAgentId': 881492, 'firstName':
            'Jack', 'lastName': 'King', 'phone': '02 8356 7127', 'fax': '23444 444 44', 'mobile':
            '0411 245 777', 'email': 'a@a.com', 'receiveEmails': True}], 'otherEnquiryEmail':
            'b@a.com,d@c.co,f@e.io', 'receiveEmailsToDefaultAddress': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListingAdminV2ListingResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: Union[
        ListingAdminV2CommercialListingV2,
        ListingAdminV2CommercialListingV2,
    ],
) -> Optional[Union[Any, ListingAdminV2ListingResponse]]:
    """Creates a commercial listing.

    Args:
        body (ListingAdminV2CommercialListingV2): Commercial Listing V2 Example: {'salePrice':
            {'priceUnitType': 'totalAmount', 'priceType': 'gross', 'gstOptionType': 'ex',
            'priceReduction': True, 'displayText': 'Price Guide $2,200,000', 'from': 2200000, 'to':
            2200000}, 'leasePrice': {'priceUnitType': 'totalAmount', 'priceType': 'gross',
            'gstOptionType': 'ex', 'priceReduction': True, 'displayText': 'Price Guide $2,200',
            'from': 2200, 'to': 2200}, 'lease': {'termOfLeaseFrom': 1, 'termOfLeaseTo': 3,
            'leaseOutgoings': 3200}, 'tenant': {'leaseStart': '2021-11-11T16:31:07.5504369+11:00',
            'leaseEnd': '2022-11-11T16:31:07.5504369+11:00', 'name': 'John Smith', 'rentalDetails':
            'Annual CPI reviews', 'leaseOptions': '5+5 year lease which commenced May 2013',
            'tenantInfoTermOfLeaseFrom': 2, 'tenantInfoTermOfLeaseTo': 3, 'leaseDateVariable': False},
            'tender': {'recipientName': 'Joe Russ', 'address': '10,Pyrmont st, Pyrmont,NSW 2011',
            'endDate': '2022-10-21T16:31:07.5504369+11:00'}, 'occupancyType': 'tenanted',
            'annualReturn': 10, 'unitsOffered': 1, 'nabers': 4.5, 'saleTerms': 'will be started after
            3 days', 'auction': {'auctionTerms': '10% deposit, balance 60 days.', 'dateTime':
            '2022-10-11T16:31:07.5504369+11:00', 'location': 'On Site', 'url':
            'https://ljhookermosman.agentboxcrm.com.au/www/fp-1-1P3679-1721283621.html'},
            'propertyDetails': {'propertyType': ['retail'], 'buildingType': 'whole', 'parking':
            {'parkingType': 'noParking', 'numberOnSite': 0}, 'pdfs': [], 'images': [{'resourceType':
            'floorPlan', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/fp-1-1P3679-1721283621.jpg'},
            {'resourceType': 'photograph', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/lt-1-1P3679-0316165440.jpg'},
            {'resourceType': 'photograph', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/lt-1-1P3679-0316165441.jpg'}], 'address':
            {'unitNumber': 'Suite 11A', 'street': 'Military Road', 'displayOption': 'fullAddress',
            'streetNumber': '287', 'suburb': 'Cremorne', 'postcode': '2090', 'state': 'nsw'}, 'area':
            {'value': 174, 'unit': 'squareMetres'}, 'landArea': {'unit': 'squareMetres', 'value':
            194}}, 'conjunctionAgents': [{'agencyId': 12346, 'domainAgentId': 484442, 'firstName':
            'Sam', 'lastName': 'Karri', 'phone': '02 8356 7127', 'fax': '23444 444 44', 'mobile':
            '0411 345 877', 'email': 'a@a.com', 'receiveEmails': True}], 'highlights': ['Hightlight
            1', 'Hightlight 2', 'Hightlight 3'], 'underOfferOrContract': False, 'listingProvider':
            'YOUR_LISTING_PROVIDER', 'domainAgencyID': 13, 'providerAdId': 'YOUR_PROVIDER_AD_ID',
            'features': ' Air conditioning, Alarm System, Intercom', 'description': 'Situated within
            Cremorne Town Shopping Centre, anchored by Supa IGA supermarket, this property represents
            a fantastic opportunity to own a tenanted strata retail shop in a successful shopping
            centre.', 'summary': 'Entry Level Investment Opportunity!', 'inspectionDetails':
            {'inspections': [{'from': '2022-10-11T17:00:00.0000000+11:00', 'to':
            '2022-10-11T18:00:00.0000000+11:00', 'repeat': False}, {'from':
            '2022-10-13T17:00:00.0000000+11:00', 'to': '2022-10-13T18:00:00.0000000+11:00', 'repeat':
            False}, {'from': '2022-10-15T17:00:00.0000000+11:00', 'to':
            '2022-10-15T18:00:00.0000000+11:00', 'repeat': False}, {'from':
            '2022-10-17T17:00:00.0000000+11:00', 'to': '2022-10-17T18:00:00.0000000+11:00', 'repeat':
            False}, {'from': '2022-10-19T17:00:00.0000000+11:00', 'to':
            '2022-10-19T18:00:00.0000000+11:00', 'repeat': False}]}, 'media': [{'resourceType':
            'video', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/fp-1-1P3679-1721283621.mp4'},
            {'resourceType': 'virtualTour', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/fp-1-1P3679-1721283621.html'},
            {'resourceType': 'webLink', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/fp-1-1P3679-1721283621.html'}],
            'listingAction': 'saleAndLease', 'contacts': [{'domainAgentId': 881492, 'firstName':
            'Jack', 'lastName': 'King', 'phone': '02 8356 7127', 'fax': '23444 444 44', 'mobile':
            '0411 245 777', 'email': 'a@a.com', 'receiveEmails': True}], 'otherEnquiryEmail':
            'b@a.com,d@c.co,f@e.io', 'receiveEmailsToDefaultAddress': False}.
        body (ListingAdminV2CommercialListingV2): Commercial Listing V2 Example: {'salePrice':
            {'priceUnitType': 'totalAmount', 'priceType': 'gross', 'gstOptionType': 'ex',
            'priceReduction': True, 'displayText': 'Price Guide $2,200,000', 'from': 2200000, 'to':
            2200000}, 'leasePrice': {'priceUnitType': 'totalAmount', 'priceType': 'gross',
            'gstOptionType': 'ex', 'priceReduction': True, 'displayText': 'Price Guide $2,200',
            'from': 2200, 'to': 2200}, 'lease': {'termOfLeaseFrom': 1, 'termOfLeaseTo': 3,
            'leaseOutgoings': 3200}, 'tenant': {'leaseStart': '2021-11-11T16:31:07.5504369+11:00',
            'leaseEnd': '2022-11-11T16:31:07.5504369+11:00', 'name': 'John Smith', 'rentalDetails':
            'Annual CPI reviews', 'leaseOptions': '5+5 year lease which commenced May 2013',
            'tenantInfoTermOfLeaseFrom': 2, 'tenantInfoTermOfLeaseTo': 3, 'leaseDateVariable': False},
            'tender': {'recipientName': 'Joe Russ', 'address': '10,Pyrmont st, Pyrmont,NSW 2011',
            'endDate': '2022-10-21T16:31:07.5504369+11:00'}, 'occupancyType': 'tenanted',
            'annualReturn': 10, 'unitsOffered': 1, 'nabers': 4.5, 'saleTerms': 'will be started after
            3 days', 'auction': {'auctionTerms': '10% deposit, balance 60 days.', 'dateTime':
            '2022-10-11T16:31:07.5504369+11:00', 'location': 'On Site', 'url':
            'https://ljhookermosman.agentboxcrm.com.au/www/fp-1-1P3679-1721283621.html'},
            'propertyDetails': {'propertyType': ['retail'], 'buildingType': 'whole', 'parking':
            {'parkingType': 'noParking', 'numberOnSite': 0}, 'pdfs': [], 'images': [{'resourceType':
            'floorPlan', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/fp-1-1P3679-1721283621.jpg'},
            {'resourceType': 'photograph', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/lt-1-1P3679-0316165440.jpg'},
            {'resourceType': 'photograph', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/lt-1-1P3679-0316165441.jpg'}], 'address':
            {'unitNumber': 'Suite 11A', 'street': 'Military Road', 'displayOption': 'fullAddress',
            'streetNumber': '287', 'suburb': 'Cremorne', 'postcode': '2090', 'state': 'nsw'}, 'area':
            {'value': 174, 'unit': 'squareMetres'}, 'landArea': {'unit': 'squareMetres', 'value':
            194}}, 'conjunctionAgents': [{'agencyId': 12346, 'domainAgentId': 484442, 'firstName':
            'Sam', 'lastName': 'Karri', 'phone': '02 8356 7127', 'fax': '23444 444 44', 'mobile':
            '0411 345 877', 'email': 'a@a.com', 'receiveEmails': True}], 'highlights': ['Hightlight
            1', 'Hightlight 2', 'Hightlight 3'], 'underOfferOrContract': False, 'listingProvider':
            'YOUR_LISTING_PROVIDER', 'domainAgencyID': 13, 'providerAdId': 'YOUR_PROVIDER_AD_ID',
            'features': ' Air conditioning, Alarm System, Intercom', 'description': 'Situated within
            Cremorne Town Shopping Centre, anchored by Supa IGA supermarket, this property represents
            a fantastic opportunity to own a tenanted strata retail shop in a successful shopping
            centre.', 'summary': 'Entry Level Investment Opportunity!', 'inspectionDetails':
            {'inspections': [{'from': '2022-10-11T17:00:00.0000000+11:00', 'to':
            '2022-10-11T18:00:00.0000000+11:00', 'repeat': False}, {'from':
            '2022-10-13T17:00:00.0000000+11:00', 'to': '2022-10-13T18:00:00.0000000+11:00', 'repeat':
            False}, {'from': '2022-10-15T17:00:00.0000000+11:00', 'to':
            '2022-10-15T18:00:00.0000000+11:00', 'repeat': False}, {'from':
            '2022-10-17T17:00:00.0000000+11:00', 'to': '2022-10-17T18:00:00.0000000+11:00', 'repeat':
            False}, {'from': '2022-10-19T17:00:00.0000000+11:00', 'to':
            '2022-10-19T18:00:00.0000000+11:00', 'repeat': False}]}, 'media': [{'resourceType':
            'video', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/fp-1-1P3679-1721283621.mp4'},
            {'resourceType': 'virtualTour', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/fp-1-1P3679-1721283621.html'},
            {'resourceType': 'webLink', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/fp-1-1P3679-1721283621.html'}],
            'listingAction': 'saleAndLease', 'contacts': [{'domainAgentId': 881492, 'firstName':
            'Jack', 'lastName': 'King', 'phone': '02 8356 7127', 'fax': '23444 444 44', 'mobile':
            '0411 245 777', 'email': 'a@a.com', 'receiveEmails': True}], 'otherEnquiryEmail':
            'b@a.com,d@c.co,f@e.io', 'receiveEmailsToDefaultAddress': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListingAdminV2ListingResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        ListingAdminV2CommercialListingV2,
        ListingAdminV2CommercialListingV2,
    ],
) -> Response[Union[Any, ListingAdminV2ListingResponse]]:
    """Creates a commercial listing.

    Args:
        body (ListingAdminV2CommercialListingV2): Commercial Listing V2 Example: {'salePrice':
            {'priceUnitType': 'totalAmount', 'priceType': 'gross', 'gstOptionType': 'ex',
            'priceReduction': True, 'displayText': 'Price Guide $2,200,000', 'from': 2200000, 'to':
            2200000}, 'leasePrice': {'priceUnitType': 'totalAmount', 'priceType': 'gross',
            'gstOptionType': 'ex', 'priceReduction': True, 'displayText': 'Price Guide $2,200',
            'from': 2200, 'to': 2200}, 'lease': {'termOfLeaseFrom': 1, 'termOfLeaseTo': 3,
            'leaseOutgoings': 3200}, 'tenant': {'leaseStart': '2021-11-11T16:31:07.5504369+11:00',
            'leaseEnd': '2022-11-11T16:31:07.5504369+11:00', 'name': 'John Smith', 'rentalDetails':
            'Annual CPI reviews', 'leaseOptions': '5+5 year lease which commenced May 2013',
            'tenantInfoTermOfLeaseFrom': 2, 'tenantInfoTermOfLeaseTo': 3, 'leaseDateVariable': False},
            'tender': {'recipientName': 'Joe Russ', 'address': '10,Pyrmont st, Pyrmont,NSW 2011',
            'endDate': '2022-10-21T16:31:07.5504369+11:00'}, 'occupancyType': 'tenanted',
            'annualReturn': 10, 'unitsOffered': 1, 'nabers': 4.5, 'saleTerms': 'will be started after
            3 days', 'auction': {'auctionTerms': '10% deposit, balance 60 days.', 'dateTime':
            '2022-10-11T16:31:07.5504369+11:00', 'location': 'On Site', 'url':
            'https://ljhookermosman.agentboxcrm.com.au/www/fp-1-1P3679-1721283621.html'},
            'propertyDetails': {'propertyType': ['retail'], 'buildingType': 'whole', 'parking':
            {'parkingType': 'noParking', 'numberOnSite': 0}, 'pdfs': [], 'images': [{'resourceType':
            'floorPlan', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/fp-1-1P3679-1721283621.jpg'},
            {'resourceType': 'photograph', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/lt-1-1P3679-0316165440.jpg'},
            {'resourceType': 'photograph', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/lt-1-1P3679-0316165441.jpg'}], 'address':
            {'unitNumber': 'Suite 11A', 'street': 'Military Road', 'displayOption': 'fullAddress',
            'streetNumber': '287', 'suburb': 'Cremorne', 'postcode': '2090', 'state': 'nsw'}, 'area':
            {'value': 174, 'unit': 'squareMetres'}, 'landArea': {'unit': 'squareMetres', 'value':
            194}}, 'conjunctionAgents': [{'agencyId': 12346, 'domainAgentId': 484442, 'firstName':
            'Sam', 'lastName': 'Karri', 'phone': '02 8356 7127', 'fax': '23444 444 44', 'mobile':
            '0411 345 877', 'email': 'a@a.com', 'receiveEmails': True}], 'highlights': ['Hightlight
            1', 'Hightlight 2', 'Hightlight 3'], 'underOfferOrContract': False, 'listingProvider':
            'YOUR_LISTING_PROVIDER', 'domainAgencyID': 13, 'providerAdId': 'YOUR_PROVIDER_AD_ID',
            'features': ' Air conditioning, Alarm System, Intercom', 'description': 'Situated within
            Cremorne Town Shopping Centre, anchored by Supa IGA supermarket, this property represents
            a fantastic opportunity to own a tenanted strata retail shop in a successful shopping
            centre.', 'summary': 'Entry Level Investment Opportunity!', 'inspectionDetails':
            {'inspections': [{'from': '2022-10-11T17:00:00.0000000+11:00', 'to':
            '2022-10-11T18:00:00.0000000+11:00', 'repeat': False}, {'from':
            '2022-10-13T17:00:00.0000000+11:00', 'to': '2022-10-13T18:00:00.0000000+11:00', 'repeat':
            False}, {'from': '2022-10-15T17:00:00.0000000+11:00', 'to':
            '2022-10-15T18:00:00.0000000+11:00', 'repeat': False}, {'from':
            '2022-10-17T17:00:00.0000000+11:00', 'to': '2022-10-17T18:00:00.0000000+11:00', 'repeat':
            False}, {'from': '2022-10-19T17:00:00.0000000+11:00', 'to':
            '2022-10-19T18:00:00.0000000+11:00', 'repeat': False}]}, 'media': [{'resourceType':
            'video', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/fp-1-1P3679-1721283621.mp4'},
            {'resourceType': 'virtualTour', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/fp-1-1P3679-1721283621.html'},
            {'resourceType': 'webLink', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/fp-1-1P3679-1721283621.html'}],
            'listingAction': 'saleAndLease', 'contacts': [{'domainAgentId': 881492, 'firstName':
            'Jack', 'lastName': 'King', 'phone': '02 8356 7127', 'fax': '23444 444 44', 'mobile':
            '0411 245 777', 'email': 'a@a.com', 'receiveEmails': True}], 'otherEnquiryEmail':
            'b@a.com,d@c.co,f@e.io', 'receiveEmailsToDefaultAddress': False}.
        body (ListingAdminV2CommercialListingV2): Commercial Listing V2 Example: {'salePrice':
            {'priceUnitType': 'totalAmount', 'priceType': 'gross', 'gstOptionType': 'ex',
            'priceReduction': True, 'displayText': 'Price Guide $2,200,000', 'from': 2200000, 'to':
            2200000}, 'leasePrice': {'priceUnitType': 'totalAmount', 'priceType': 'gross',
            'gstOptionType': 'ex', 'priceReduction': True, 'displayText': 'Price Guide $2,200',
            'from': 2200, 'to': 2200}, 'lease': {'termOfLeaseFrom': 1, 'termOfLeaseTo': 3,
            'leaseOutgoings': 3200}, 'tenant': {'leaseStart': '2021-11-11T16:31:07.5504369+11:00',
            'leaseEnd': '2022-11-11T16:31:07.5504369+11:00', 'name': 'John Smith', 'rentalDetails':
            'Annual CPI reviews', 'leaseOptions': '5+5 year lease which commenced May 2013',
            'tenantInfoTermOfLeaseFrom': 2, 'tenantInfoTermOfLeaseTo': 3, 'leaseDateVariable': False},
            'tender': {'recipientName': 'Joe Russ', 'address': '10,Pyrmont st, Pyrmont,NSW 2011',
            'endDate': '2022-10-21T16:31:07.5504369+11:00'}, 'occupancyType': 'tenanted',
            'annualReturn': 10, 'unitsOffered': 1, 'nabers': 4.5, 'saleTerms': 'will be started after
            3 days', 'auction': {'auctionTerms': '10% deposit, balance 60 days.', 'dateTime':
            '2022-10-11T16:31:07.5504369+11:00', 'location': 'On Site', 'url':
            'https://ljhookermosman.agentboxcrm.com.au/www/fp-1-1P3679-1721283621.html'},
            'propertyDetails': {'propertyType': ['retail'], 'buildingType': 'whole', 'parking':
            {'parkingType': 'noParking', 'numberOnSite': 0}, 'pdfs': [], 'images': [{'resourceType':
            'floorPlan', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/fp-1-1P3679-1721283621.jpg'},
            {'resourceType': 'photograph', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/lt-1-1P3679-0316165440.jpg'},
            {'resourceType': 'photograph', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/lt-1-1P3679-0316165441.jpg'}], 'address':
            {'unitNumber': 'Suite 11A', 'street': 'Military Road', 'displayOption': 'fullAddress',
            'streetNumber': '287', 'suburb': 'Cremorne', 'postcode': '2090', 'state': 'nsw'}, 'area':
            {'value': 174, 'unit': 'squareMetres'}, 'landArea': {'unit': 'squareMetres', 'value':
            194}}, 'conjunctionAgents': [{'agencyId': 12346, 'domainAgentId': 484442, 'firstName':
            'Sam', 'lastName': 'Karri', 'phone': '02 8356 7127', 'fax': '23444 444 44', 'mobile':
            '0411 345 877', 'email': 'a@a.com', 'receiveEmails': True}], 'highlights': ['Hightlight
            1', 'Hightlight 2', 'Hightlight 3'], 'underOfferOrContract': False, 'listingProvider':
            'YOUR_LISTING_PROVIDER', 'domainAgencyID': 13, 'providerAdId': 'YOUR_PROVIDER_AD_ID',
            'features': ' Air conditioning, Alarm System, Intercom', 'description': 'Situated within
            Cremorne Town Shopping Centre, anchored by Supa IGA supermarket, this property represents
            a fantastic opportunity to own a tenanted strata retail shop in a successful shopping
            centre.', 'summary': 'Entry Level Investment Opportunity!', 'inspectionDetails':
            {'inspections': [{'from': '2022-10-11T17:00:00.0000000+11:00', 'to':
            '2022-10-11T18:00:00.0000000+11:00', 'repeat': False}, {'from':
            '2022-10-13T17:00:00.0000000+11:00', 'to': '2022-10-13T18:00:00.0000000+11:00', 'repeat':
            False}, {'from': '2022-10-15T17:00:00.0000000+11:00', 'to':
            '2022-10-15T18:00:00.0000000+11:00', 'repeat': False}, {'from':
            '2022-10-17T17:00:00.0000000+11:00', 'to': '2022-10-17T18:00:00.0000000+11:00', 'repeat':
            False}, {'from': '2022-10-19T17:00:00.0000000+11:00', 'to':
            '2022-10-19T18:00:00.0000000+11:00', 'repeat': False}]}, 'media': [{'resourceType':
            'video', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/fp-1-1P3679-1721283621.mp4'},
            {'resourceType': 'virtualTour', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/fp-1-1P3679-1721283621.html'},
            {'resourceType': 'webLink', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/fp-1-1P3679-1721283621.html'}],
            'listingAction': 'saleAndLease', 'contacts': [{'domainAgentId': 881492, 'firstName':
            'Jack', 'lastName': 'King', 'phone': '02 8356 7127', 'fax': '23444 444 44', 'mobile':
            '0411 245 777', 'email': 'a@a.com', 'receiveEmails': True}], 'otherEnquiryEmail':
            'b@a.com,d@c.co,f@e.io', 'receiveEmailsToDefaultAddress': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListingAdminV2ListingResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Union[
        ListingAdminV2CommercialListingV2,
        ListingAdminV2CommercialListingV2,
    ],
) -> Optional[Union[Any, ListingAdminV2ListingResponse]]:
    """Creates a commercial listing.

    Args:
        body (ListingAdminV2CommercialListingV2): Commercial Listing V2 Example: {'salePrice':
            {'priceUnitType': 'totalAmount', 'priceType': 'gross', 'gstOptionType': 'ex',
            'priceReduction': True, 'displayText': 'Price Guide $2,200,000', 'from': 2200000, 'to':
            2200000}, 'leasePrice': {'priceUnitType': 'totalAmount', 'priceType': 'gross',
            'gstOptionType': 'ex', 'priceReduction': True, 'displayText': 'Price Guide $2,200',
            'from': 2200, 'to': 2200}, 'lease': {'termOfLeaseFrom': 1, 'termOfLeaseTo': 3,
            'leaseOutgoings': 3200}, 'tenant': {'leaseStart': '2021-11-11T16:31:07.5504369+11:00',
            'leaseEnd': '2022-11-11T16:31:07.5504369+11:00', 'name': 'John Smith', 'rentalDetails':
            'Annual CPI reviews', 'leaseOptions': '5+5 year lease which commenced May 2013',
            'tenantInfoTermOfLeaseFrom': 2, 'tenantInfoTermOfLeaseTo': 3, 'leaseDateVariable': False},
            'tender': {'recipientName': 'Joe Russ', 'address': '10,Pyrmont st, Pyrmont,NSW 2011',
            'endDate': '2022-10-21T16:31:07.5504369+11:00'}, 'occupancyType': 'tenanted',
            'annualReturn': 10, 'unitsOffered': 1, 'nabers': 4.5, 'saleTerms': 'will be started after
            3 days', 'auction': {'auctionTerms': '10% deposit, balance 60 days.', 'dateTime':
            '2022-10-11T16:31:07.5504369+11:00', 'location': 'On Site', 'url':
            'https://ljhookermosman.agentboxcrm.com.au/www/fp-1-1P3679-1721283621.html'},
            'propertyDetails': {'propertyType': ['retail'], 'buildingType': 'whole', 'parking':
            {'parkingType': 'noParking', 'numberOnSite': 0}, 'pdfs': [], 'images': [{'resourceType':
            'floorPlan', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/fp-1-1P3679-1721283621.jpg'},
            {'resourceType': 'photograph', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/lt-1-1P3679-0316165440.jpg'},
            {'resourceType': 'photograph', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/lt-1-1P3679-0316165441.jpg'}], 'address':
            {'unitNumber': 'Suite 11A', 'street': 'Military Road', 'displayOption': 'fullAddress',
            'streetNumber': '287', 'suburb': 'Cremorne', 'postcode': '2090', 'state': 'nsw'}, 'area':
            {'value': 174, 'unit': 'squareMetres'}, 'landArea': {'unit': 'squareMetres', 'value':
            194}}, 'conjunctionAgents': [{'agencyId': 12346, 'domainAgentId': 484442, 'firstName':
            'Sam', 'lastName': 'Karri', 'phone': '02 8356 7127', 'fax': '23444 444 44', 'mobile':
            '0411 345 877', 'email': 'a@a.com', 'receiveEmails': True}], 'highlights': ['Hightlight
            1', 'Hightlight 2', 'Hightlight 3'], 'underOfferOrContract': False, 'listingProvider':
            'YOUR_LISTING_PROVIDER', 'domainAgencyID': 13, 'providerAdId': 'YOUR_PROVIDER_AD_ID',
            'features': ' Air conditioning, Alarm System, Intercom', 'description': 'Situated within
            Cremorne Town Shopping Centre, anchored by Supa IGA supermarket, this property represents
            a fantastic opportunity to own a tenanted strata retail shop in a successful shopping
            centre.', 'summary': 'Entry Level Investment Opportunity!', 'inspectionDetails':
            {'inspections': [{'from': '2022-10-11T17:00:00.0000000+11:00', 'to':
            '2022-10-11T18:00:00.0000000+11:00', 'repeat': False}, {'from':
            '2022-10-13T17:00:00.0000000+11:00', 'to': '2022-10-13T18:00:00.0000000+11:00', 'repeat':
            False}, {'from': '2022-10-15T17:00:00.0000000+11:00', 'to':
            '2022-10-15T18:00:00.0000000+11:00', 'repeat': False}, {'from':
            '2022-10-17T17:00:00.0000000+11:00', 'to': '2022-10-17T18:00:00.0000000+11:00', 'repeat':
            False}, {'from': '2022-10-19T17:00:00.0000000+11:00', 'to':
            '2022-10-19T18:00:00.0000000+11:00', 'repeat': False}]}, 'media': [{'resourceType':
            'video', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/fp-1-1P3679-1721283621.mp4'},
            {'resourceType': 'virtualTour', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/fp-1-1P3679-1721283621.html'},
            {'resourceType': 'webLink', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/fp-1-1P3679-1721283621.html'}],
            'listingAction': 'saleAndLease', 'contacts': [{'domainAgentId': 881492, 'firstName':
            'Jack', 'lastName': 'King', 'phone': '02 8356 7127', 'fax': '23444 444 44', 'mobile':
            '0411 245 777', 'email': 'a@a.com', 'receiveEmails': True}], 'otherEnquiryEmail':
            'b@a.com,d@c.co,f@e.io', 'receiveEmailsToDefaultAddress': False}.
        body (ListingAdminV2CommercialListingV2): Commercial Listing V2 Example: {'salePrice':
            {'priceUnitType': 'totalAmount', 'priceType': 'gross', 'gstOptionType': 'ex',
            'priceReduction': True, 'displayText': 'Price Guide $2,200,000', 'from': 2200000, 'to':
            2200000}, 'leasePrice': {'priceUnitType': 'totalAmount', 'priceType': 'gross',
            'gstOptionType': 'ex', 'priceReduction': True, 'displayText': 'Price Guide $2,200',
            'from': 2200, 'to': 2200}, 'lease': {'termOfLeaseFrom': 1, 'termOfLeaseTo': 3,
            'leaseOutgoings': 3200}, 'tenant': {'leaseStart': '2021-11-11T16:31:07.5504369+11:00',
            'leaseEnd': '2022-11-11T16:31:07.5504369+11:00', 'name': 'John Smith', 'rentalDetails':
            'Annual CPI reviews', 'leaseOptions': '5+5 year lease which commenced May 2013',
            'tenantInfoTermOfLeaseFrom': 2, 'tenantInfoTermOfLeaseTo': 3, 'leaseDateVariable': False},
            'tender': {'recipientName': 'Joe Russ', 'address': '10,Pyrmont st, Pyrmont,NSW 2011',
            'endDate': '2022-10-21T16:31:07.5504369+11:00'}, 'occupancyType': 'tenanted',
            'annualReturn': 10, 'unitsOffered': 1, 'nabers': 4.5, 'saleTerms': 'will be started after
            3 days', 'auction': {'auctionTerms': '10% deposit, balance 60 days.', 'dateTime':
            '2022-10-11T16:31:07.5504369+11:00', 'location': 'On Site', 'url':
            'https://ljhookermosman.agentboxcrm.com.au/www/fp-1-1P3679-1721283621.html'},
            'propertyDetails': {'propertyType': ['retail'], 'buildingType': 'whole', 'parking':
            {'parkingType': 'noParking', 'numberOnSite': 0}, 'pdfs': [], 'images': [{'resourceType':
            'floorPlan', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/fp-1-1P3679-1721283621.jpg'},
            {'resourceType': 'photograph', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/lt-1-1P3679-0316165440.jpg'},
            {'resourceType': 'photograph', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/lt-1-1P3679-0316165441.jpg'}], 'address':
            {'unitNumber': 'Suite 11A', 'street': 'Military Road', 'displayOption': 'fullAddress',
            'streetNumber': '287', 'suburb': 'Cremorne', 'postcode': '2090', 'state': 'nsw'}, 'area':
            {'value': 174, 'unit': 'squareMetres'}, 'landArea': {'unit': 'squareMetres', 'value':
            194}}, 'conjunctionAgents': [{'agencyId': 12346, 'domainAgentId': 484442, 'firstName':
            'Sam', 'lastName': 'Karri', 'phone': '02 8356 7127', 'fax': '23444 444 44', 'mobile':
            '0411 345 877', 'email': 'a@a.com', 'receiveEmails': True}], 'highlights': ['Hightlight
            1', 'Hightlight 2', 'Hightlight 3'], 'underOfferOrContract': False, 'listingProvider':
            'YOUR_LISTING_PROVIDER', 'domainAgencyID': 13, 'providerAdId': 'YOUR_PROVIDER_AD_ID',
            'features': ' Air conditioning, Alarm System, Intercom', 'description': 'Situated within
            Cremorne Town Shopping Centre, anchored by Supa IGA supermarket, this property represents
            a fantastic opportunity to own a tenanted strata retail shop in a successful shopping
            centre.', 'summary': 'Entry Level Investment Opportunity!', 'inspectionDetails':
            {'inspections': [{'from': '2022-10-11T17:00:00.0000000+11:00', 'to':
            '2022-10-11T18:00:00.0000000+11:00', 'repeat': False}, {'from':
            '2022-10-13T17:00:00.0000000+11:00', 'to': '2022-10-13T18:00:00.0000000+11:00', 'repeat':
            False}, {'from': '2022-10-15T17:00:00.0000000+11:00', 'to':
            '2022-10-15T18:00:00.0000000+11:00', 'repeat': False}, {'from':
            '2022-10-17T17:00:00.0000000+11:00', 'to': '2022-10-17T18:00:00.0000000+11:00', 'repeat':
            False}, {'from': '2022-10-19T17:00:00.0000000+11:00', 'to':
            '2022-10-19T18:00:00.0000000+11:00', 'repeat': False}]}, 'media': [{'resourceType':
            'video', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/fp-1-1P3679-1721283621.mp4'},
            {'resourceType': 'virtualTour', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/fp-1-1P3679-1721283621.html'},
            {'resourceType': 'webLink', 'url':
            'http://www.ljhookermosman.agentboxcrm.com.au/fp-1-1P3679-1721283621.html'}],
            'listingAction': 'saleAndLease', 'contacts': [{'domainAgentId': 881492, 'firstName':
            'Jack', 'lastName': 'King', 'phone': '02 8356 7127', 'fax': '23444 444 44', 'mobile':
            '0411 245 777', 'email': 'a@a.com', 'receiveEmails': True}], 'otherEnquiryEmail':
            'b@a.com,d@c.co,f@e.io', 'receiveEmailsToDefaultAddress': False}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListingAdminV2ListingResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
