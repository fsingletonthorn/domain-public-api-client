from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.demographics_v2_demographics_results import DemographicsV2DemographicsResults
from ...types import UNSET, Response, Unset


def _get_kwargs(
    state: str,
    suburb: str,
    postcode: str,
    *,
    types: Union[Unset, str] = UNSET,
    year: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["types"] = types

    params["year"] = year

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v2/demographics/{state}/{suburb}/{postcode}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DemographicsV2DemographicsResults]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DemographicsV2DemographicsResults.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DemographicsV2DemographicsResults]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    state: str,
    suburb: str,
    postcode: str,
    *,
    client: AuthenticatedClient,
    types: Union[Unset, str] = UNSET,
    year: Union[Unset, int] = UNSET,
) -> Response[DemographicsV2DemographicsResults]:
    """Search for demographics in a given geographic level.

     <br>Where available, all available topics and years will be returned if not supplied.
    <br>Note that not all suburbs will have data available for all years and topics.

    Args:
        state (str):
        suburb (str):
        postcode (str):
        types (Union[Unset, str]):
        year (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DemographicsV2DemographicsResults]
    """

    kwargs = _get_kwargs(
        state=state,
        suburb=suburb,
        postcode=postcode,
        types=types,
        year=year,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    state: str,
    suburb: str,
    postcode: str,
    *,
    client: AuthenticatedClient,
    types: Union[Unset, str] = UNSET,
    year: Union[Unset, int] = UNSET,
) -> Optional[DemographicsV2DemographicsResults]:
    """Search for demographics in a given geographic level.

     <br>Where available, all available topics and years will be returned if not supplied.
    <br>Note that not all suburbs will have data available for all years and topics.

    Args:
        state (str):
        suburb (str):
        postcode (str):
        types (Union[Unset, str]):
        year (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DemographicsV2DemographicsResults
    """

    return sync_detailed(
        state=state,
        suburb=suburb,
        postcode=postcode,
        client=client,
        types=types,
        year=year,
    ).parsed


async def asyncio_detailed(
    state: str,
    suburb: str,
    postcode: str,
    *,
    client: AuthenticatedClient,
    types: Union[Unset, str] = UNSET,
    year: Union[Unset, int] = UNSET,
) -> Response[DemographicsV2DemographicsResults]:
    """Search for demographics in a given geographic level.

     <br>Where available, all available topics and years will be returned if not supplied.
    <br>Note that not all suburbs will have data available for all years and topics.

    Args:
        state (str):
        suburb (str):
        postcode (str):
        types (Union[Unset, str]):
        year (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DemographicsV2DemographicsResults]
    """

    kwargs = _get_kwargs(
        state=state,
        suburb=suburb,
        postcode=postcode,
        types=types,
        year=year,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    state: str,
    suburb: str,
    postcode: str,
    *,
    client: AuthenticatedClient,
    types: Union[Unset, str] = UNSET,
    year: Union[Unset, int] = UNSET,
) -> Optional[DemographicsV2DemographicsResults]:
    """Search for demographics in a given geographic level.

     <br>Where available, all available topics and years will be returned if not supplied.
    <br>Note that not all suburbs will have data available for all years and topics.

    Args:
        state (str):
        suburb (str):
        postcode (str):
        types (Union[Unset, str]):
        year (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DemographicsV2DemographicsResults
    """

    return (
        await asyncio_detailed(
            state=state,
            suburb=suburb,
            postcode=postcode,
            client=client,
            types=types,
            year=year,
        )
    ).parsed
