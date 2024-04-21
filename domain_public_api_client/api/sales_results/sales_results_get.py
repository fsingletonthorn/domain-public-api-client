from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.sales_results_v1_city_results_summary import SalesResultsV1CityResultsSummary
from ...types import Response


def _get_kwargs(
    city: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v1/salesResults/{city}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SalesResultsV1CityResultsSummary]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SalesResultsV1CityResultsSummary.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SalesResultsV1CityResultsSummary]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    city: str,
    *,
    client: AuthenticatedClient,
) -> Response[SalesResultsV1CityResultsSummary]:
    """Retrieves sales results for a given city

    Args:
        city (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SalesResultsV1CityResultsSummary]
    """

    kwargs = _get_kwargs(
        city=city,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    city: str,
    *,
    client: AuthenticatedClient,
) -> Optional[SalesResultsV1CityResultsSummary]:
    """Retrieves sales results for a given city

    Args:
        city (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SalesResultsV1CityResultsSummary
    """

    return sync_detailed(
        city=city,
        client=client,
    ).parsed


async def asyncio_detailed(
    city: str,
    *,
    client: AuthenticatedClient,
) -> Response[SalesResultsV1CityResultsSummary]:
    """Retrieves sales results for a given city

    Args:
        city (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SalesResultsV1CityResultsSummary]
    """

    kwargs = _get_kwargs(
        city=city,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    city: str,
    *,
    client: AuthenticatedClient,
) -> Optional[SalesResultsV1CityResultsSummary]:
    """Retrieves sales results for a given city

    Args:
        city (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SalesResultsV1CityResultsSummary
    """

    return (
        await asyncio_detailed(
            city=city,
            client=client,
        )
    ).parsed
