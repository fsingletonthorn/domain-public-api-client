from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domain_public_adapter_web_api_models_v1_listings_listing_location import (
    DomainPublicAdapterWebApiModelsV1ListingsListingLocation,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    terms: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["terms"] = terms

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v1/listings/locations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["DomainPublicAdapterWebApiModelsV1ListingsListingLocation"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DomainPublicAdapterWebApiModelsV1ListingsListingLocation.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["DomainPublicAdapterWebApiModelsV1ListingsListingLocation"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    terms: Union[Unset, str] = UNSET,
) -> Response[List["DomainPublicAdapterWebApiModelsV1ListingsListingLocation"]]:
    r"""Suggests listing locations

     The resulting suggested location can be of type \"suburb\" / \"area\" / \"region\".

    The `name` property corresponds to the type of location returned.

    The area name / region name can be fed into the corresponding fields search fields.  See [`v1/listin
    gs/residential/_search`](/docs/v1/apis/pkg_agents_listings/references/listings_detailedresidentialse
    arch)

    Args:
        terms (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['DomainPublicAdapterWebApiModelsV1ListingsListingLocation']]
    """

    kwargs = _get_kwargs(
        terms=terms,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    terms: Union[Unset, str] = UNSET,
) -> Optional[List["DomainPublicAdapterWebApiModelsV1ListingsListingLocation"]]:
    r"""Suggests listing locations

     The resulting suggested location can be of type \"suburb\" / \"area\" / \"region\".

    The `name` property corresponds to the type of location returned.

    The area name / region name can be fed into the corresponding fields search fields.  See [`v1/listin
    gs/residential/_search`](/docs/v1/apis/pkg_agents_listings/references/listings_detailedresidentialse
    arch)

    Args:
        terms (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['DomainPublicAdapterWebApiModelsV1ListingsListingLocation']
    """

    return sync_detailed(
        client=client,
        terms=terms,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    terms: Union[Unset, str] = UNSET,
) -> Response[List["DomainPublicAdapterWebApiModelsV1ListingsListingLocation"]]:
    r"""Suggests listing locations

     The resulting suggested location can be of type \"suburb\" / \"area\" / \"region\".

    The `name` property corresponds to the type of location returned.

    The area name / region name can be fed into the corresponding fields search fields.  See [`v1/listin
    gs/residential/_search`](/docs/v1/apis/pkg_agents_listings/references/listings_detailedresidentialse
    arch)

    Args:
        terms (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['DomainPublicAdapterWebApiModelsV1ListingsListingLocation']]
    """

    kwargs = _get_kwargs(
        terms=terms,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    terms: Union[Unset, str] = UNSET,
) -> Optional[List["DomainPublicAdapterWebApiModelsV1ListingsListingLocation"]]:
    r"""Suggests listing locations

     The resulting suggested location can be of type \"suburb\" / \"area\" / \"region\".

    The `name` property corresponds to the type of location returned.

    The area name / region name can be fed into the corresponding fields search fields.  See [`v1/listin
    gs/residential/_search`](/docs/v1/apis/pkg_agents_listings/references/listings_detailedresidentialse
    arch)

    Args:
        terms (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['DomainPublicAdapterWebApiModelsV1ListingsListingLocation']
    """

    return (
        await asyncio_detailed(
            client=client,
            terms=terms,
        )
    ).parsed
