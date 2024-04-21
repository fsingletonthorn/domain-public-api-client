from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.sales_results_v1_city_results_date import SalesResultsV1CityResultsDate
from ...types import Response


def _get_kwargs() -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v1/salesResults/_head",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SalesResultsV1CityResultsDate]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SalesResultsV1CityResultsDate.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SalesResultsV1CityResultsDate]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[SalesResultsV1CityResultsDate]:
    """Retrieves metadata regarding sales result data

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SalesResultsV1CityResultsDate]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> Optional[SalesResultsV1CityResultsDate]:
    """Retrieves metadata regarding sales result data

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SalesResultsV1CityResultsDate
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[SalesResultsV1CityResultsDate]:
    """Retrieves metadata regarding sales result data

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SalesResultsV1CityResultsDate]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> Optional[SalesResultsV1CityResultsDate]:
    """Retrieves metadata regarding sales result data

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SalesResultsV1CityResultsDate
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
