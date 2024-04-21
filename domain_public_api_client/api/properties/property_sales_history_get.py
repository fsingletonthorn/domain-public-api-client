from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.property_enrichment_v2_multiple_property_results import PropertyEnrichmentV2MultiplePropertyResults
from ...models.property_enrichment_v2_sale_history import PropertyEnrichmentV2SaleHistory
from ...models.property_sales_history_get_state import PropertySalesHistoryGetState
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    property_id: Union[Unset, str] = UNSET,
    gnaf_id: Union[Unset, str] = UNSET,
    flat_number: Union[Unset, str] = UNSET,
    street_number: Union[Unset, str] = UNSET,
    street_name: Union[Unset, str] = UNSET,
    street_type: Union[Unset, str] = UNSET,
    postcode: Union[Unset, str] = UNSET,
    suburb_name: Union[Unset, str] = UNSET,
    state: Union[Unset, PropertySalesHistoryGetState] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["propertyId"] = property_id

    params["gnafId"] = gnaf_id

    params["flatNumber"] = flat_number

    params["streetNumber"] = street_number

    params["streetName"] = street_name

    params["streetType"] = street_type

    params["postcode"] = postcode

    params["suburbName"] = suburb_name

    json_state: Union[Unset, str] = UNSET
    if not isinstance(state, Unset):
        json_state = state.value

    params["state"] = json_state

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v1/properties/salesHistory",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PropertyEnrichmentV2MultiplePropertyResults, PropertyEnrichmentV2SaleHistory]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PropertyEnrichmentV2SaleHistory.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.MULTIPLE_CHOICES:
        response_300 = PropertyEnrichmentV2MultiplePropertyResults.from_dict(response.json())

        return response_300
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, PropertyEnrichmentV2MultiplePropertyResults, PropertyEnrichmentV2SaleHistory]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    property_id: Union[Unset, str] = UNSET,
    gnaf_id: Union[Unset, str] = UNSET,
    flat_number: Union[Unset, str] = UNSET,
    street_number: Union[Unset, str] = UNSET,
    street_name: Union[Unset, str] = UNSET,
    street_type: Union[Unset, str] = UNSET,
    postcode: Union[Unset, str] = UNSET,
    suburb_name: Union[Unset, str] = UNSET,
    state: Union[Unset, PropertySalesHistoryGetState] = UNSET,
) -> Response[Union[Any, PropertyEnrichmentV2MultiplePropertyResults, PropertyEnrichmentV2SaleHistory]]:
    """Sales Listing History

     Search for a specific property's activities and provide sale/rental activity if found. Supply either
    propertyId, gnafId, or all address fields (with flatNumber optional)

    Args:
        property_id (Union[Unset, str]):
        gnaf_id (Union[Unset, str]):
        flat_number (Union[Unset, str]):
        street_number (Union[Unset, str]):
        street_name (Union[Unset, str]):
        street_type (Union[Unset, str]):
        postcode (Union[Unset, str]):
        suburb_name (Union[Unset, str]):
        state (Union[Unset, PropertySalesHistoryGetState]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PropertyEnrichmentV2MultiplePropertyResults, PropertyEnrichmentV2SaleHistory]]
    """

    kwargs = _get_kwargs(
        property_id=property_id,
        gnaf_id=gnaf_id,
        flat_number=flat_number,
        street_number=street_number,
        street_name=street_name,
        street_type=street_type,
        postcode=postcode,
        suburb_name=suburb_name,
        state=state,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    property_id: Union[Unset, str] = UNSET,
    gnaf_id: Union[Unset, str] = UNSET,
    flat_number: Union[Unset, str] = UNSET,
    street_number: Union[Unset, str] = UNSET,
    street_name: Union[Unset, str] = UNSET,
    street_type: Union[Unset, str] = UNSET,
    postcode: Union[Unset, str] = UNSET,
    suburb_name: Union[Unset, str] = UNSET,
    state: Union[Unset, PropertySalesHistoryGetState] = UNSET,
) -> Optional[Union[Any, PropertyEnrichmentV2MultiplePropertyResults, PropertyEnrichmentV2SaleHistory]]:
    """Sales Listing History

     Search for a specific property's activities and provide sale/rental activity if found. Supply either
    propertyId, gnafId, or all address fields (with flatNumber optional)

    Args:
        property_id (Union[Unset, str]):
        gnaf_id (Union[Unset, str]):
        flat_number (Union[Unset, str]):
        street_number (Union[Unset, str]):
        street_name (Union[Unset, str]):
        street_type (Union[Unset, str]):
        postcode (Union[Unset, str]):
        suburb_name (Union[Unset, str]):
        state (Union[Unset, PropertySalesHistoryGetState]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PropertyEnrichmentV2MultiplePropertyResults, PropertyEnrichmentV2SaleHistory]
    """

    return sync_detailed(
        client=client,
        property_id=property_id,
        gnaf_id=gnaf_id,
        flat_number=flat_number,
        street_number=street_number,
        street_name=street_name,
        street_type=street_type,
        postcode=postcode,
        suburb_name=suburb_name,
        state=state,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    property_id: Union[Unset, str] = UNSET,
    gnaf_id: Union[Unset, str] = UNSET,
    flat_number: Union[Unset, str] = UNSET,
    street_number: Union[Unset, str] = UNSET,
    street_name: Union[Unset, str] = UNSET,
    street_type: Union[Unset, str] = UNSET,
    postcode: Union[Unset, str] = UNSET,
    suburb_name: Union[Unset, str] = UNSET,
    state: Union[Unset, PropertySalesHistoryGetState] = UNSET,
) -> Response[Union[Any, PropertyEnrichmentV2MultiplePropertyResults, PropertyEnrichmentV2SaleHistory]]:
    """Sales Listing History

     Search for a specific property's activities and provide sale/rental activity if found. Supply either
    propertyId, gnafId, or all address fields (with flatNumber optional)

    Args:
        property_id (Union[Unset, str]):
        gnaf_id (Union[Unset, str]):
        flat_number (Union[Unset, str]):
        street_number (Union[Unset, str]):
        street_name (Union[Unset, str]):
        street_type (Union[Unset, str]):
        postcode (Union[Unset, str]):
        suburb_name (Union[Unset, str]):
        state (Union[Unset, PropertySalesHistoryGetState]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PropertyEnrichmentV2MultiplePropertyResults, PropertyEnrichmentV2SaleHistory]]
    """

    kwargs = _get_kwargs(
        property_id=property_id,
        gnaf_id=gnaf_id,
        flat_number=flat_number,
        street_number=street_number,
        street_name=street_name,
        street_type=street_type,
        postcode=postcode,
        suburb_name=suburb_name,
        state=state,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    property_id: Union[Unset, str] = UNSET,
    gnaf_id: Union[Unset, str] = UNSET,
    flat_number: Union[Unset, str] = UNSET,
    street_number: Union[Unset, str] = UNSET,
    street_name: Union[Unset, str] = UNSET,
    street_type: Union[Unset, str] = UNSET,
    postcode: Union[Unset, str] = UNSET,
    suburb_name: Union[Unset, str] = UNSET,
    state: Union[Unset, PropertySalesHistoryGetState] = UNSET,
) -> Optional[Union[Any, PropertyEnrichmentV2MultiplePropertyResults, PropertyEnrichmentV2SaleHistory]]:
    """Sales Listing History

     Search for a specific property's activities and provide sale/rental activity if found. Supply either
    propertyId, gnafId, or all address fields (with flatNumber optional)

    Args:
        property_id (Union[Unset, str]):
        gnaf_id (Union[Unset, str]):
        flat_number (Union[Unset, str]):
        street_number (Union[Unset, str]):
        street_name (Union[Unset, str]):
        street_type (Union[Unset, str]):
        postcode (Union[Unset, str]):
        suburb_name (Union[Unset, str]):
        state (Union[Unset, PropertySalesHistoryGetState]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PropertyEnrichmentV2MultiplePropertyResults, PropertyEnrichmentV2SaleHistory]
    """

    return (
        await asyncio_detailed(
            client=client,
            property_id=property_id,
            gnaf_id=gnaf_id,
            flat_number=flat_number,
            street_number=street_number,
            street_name=street_name,
            street_type=street_type,
            postcode=postcode,
            suburb_name=suburb_name,
            state=state,
        )
    ).parsed
