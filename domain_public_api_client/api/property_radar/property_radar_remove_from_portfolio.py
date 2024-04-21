from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.property_radar_remove_from_portfolio_response_200 import PropertyRadarRemoveFromPortfolioResponse200
from ...types import Response


def _get_kwargs(
    portfolio_id: str,
    *,
    body: Any,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/v1/propertyradar/portfolio/{portfolio_id}/property/delete",
    }

    _body: Any
    _body = body

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PropertyRadarRemoveFromPortfolioResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PropertyRadarRemoveFromPortfolioResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, PropertyRadarRemoveFromPortfolioResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    portfolio_id: str,
    *,
    client: AuthenticatedClient,
    body: Any,
) -> Response[Union[Any, PropertyRadarRemoveFromPortfolioResponse200]]:
    """Remove Properties from Portfolio

     Removes properties from a portfolio by property id's and/or gnaf id's, returning any id's that did
    not exist within the portfolio

    Args:
        portfolio_id (str):
        body (Any): Portfolio Details

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PropertyRadarRemoveFromPortfolioResponse200]]
    """

    kwargs = _get_kwargs(
        portfolio_id=portfolio_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    portfolio_id: str,
    *,
    client: AuthenticatedClient,
    body: Any,
) -> Optional[Union[Any, PropertyRadarRemoveFromPortfolioResponse200]]:
    """Remove Properties from Portfolio

     Removes properties from a portfolio by property id's and/or gnaf id's, returning any id's that did
    not exist within the portfolio

    Args:
        portfolio_id (str):
        body (Any): Portfolio Details

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PropertyRadarRemoveFromPortfolioResponse200]
    """

    return sync_detailed(
        portfolio_id=portfolio_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    portfolio_id: str,
    *,
    client: AuthenticatedClient,
    body: Any,
) -> Response[Union[Any, PropertyRadarRemoveFromPortfolioResponse200]]:
    """Remove Properties from Portfolio

     Removes properties from a portfolio by property id's and/or gnaf id's, returning any id's that did
    not exist within the portfolio

    Args:
        portfolio_id (str):
        body (Any): Portfolio Details

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PropertyRadarRemoveFromPortfolioResponse200]]
    """

    kwargs = _get_kwargs(
        portfolio_id=portfolio_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    portfolio_id: str,
    *,
    client: AuthenticatedClient,
    body: Any,
) -> Optional[Union[Any, PropertyRadarRemoveFromPortfolioResponse200]]:
    """Remove Properties from Portfolio

     Removes properties from a portfolio by property id's and/or gnaf id's, returning any id's that did
    not exist within the portfolio

    Args:
        portfolio_id (str):
        body (Any): Portfolio Details

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PropertyRadarRemoveFromPortfolioResponse200]
    """

    return (
        await asyncio_detailed(
            portfolio_id=portfolio_id,
            client=client,
            body=body,
        )
    ).parsed
