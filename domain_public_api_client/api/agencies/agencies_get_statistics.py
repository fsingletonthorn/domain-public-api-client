from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agencies_get_statistics_channel import AgenciesGetStatisticsChannel
from ...models.agencies_get_statistics_status_filter import AgenciesGetStatisticsStatusFilter
from ...models.agencies_get_statistics_time_period import AgenciesGetStatisticsTimePeriod
from ...models.listing_performance_v1_statistics import ListingPerformanceV1Statistics
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    time_period: Union[Unset, AgenciesGetStatisticsTimePeriod] = AgenciesGetStatisticsTimePeriod.LAST7DAYS,
    status_filter: Union[Unset, AgenciesGetStatisticsStatusFilter] = AgenciesGetStatisticsStatusFilter.LIVEANDARCHIVED,
    channel: Union[Unset, AgenciesGetStatisticsChannel] = AgenciesGetStatisticsChannel.RESIDENTIAL,
    page_number: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 20,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_time_period: Union[Unset, str] = UNSET
    if not isinstance(time_period, Unset):
        json_time_period = time_period.value

    params["timePeriod"] = json_time_period

    json_status_filter: Union[Unset, str] = UNSET
    if not isinstance(status_filter, Unset):
        json_status_filter = status_filter.value

    params["statusFilter"] = json_status_filter

    json_channel: Union[Unset, str] = UNSET
    if not isinstance(channel, Unset):
        json_channel = channel.value

    params["channel"] = json_channel

    params["pageNumber"] = page_number

    params["pageSize"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v1/agencies/{id}/statistics",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["ListingPerformanceV1Statistics"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ListingPerformanceV1Statistics.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["ListingPerformanceV1Statistics"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    time_period: Union[Unset, AgenciesGetStatisticsTimePeriod] = AgenciesGetStatisticsTimePeriod.LAST7DAYS,
    status_filter: Union[Unset, AgenciesGetStatisticsStatusFilter] = AgenciesGetStatisticsStatusFilter.LIVEANDARCHIVED,
    channel: Union[Unset, AgenciesGetStatisticsChannel] = AgenciesGetStatisticsChannel.RESIDENTIAL,
    page_number: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 20,
) -> Response[List["ListingPerformanceV1Statistics"]]:
    """Retrieves statistics for a specific agency.

    Args:
        id (int):
        time_period (Union[Unset, AgenciesGetStatisticsTimePeriod]): Defines StatisticsTimePeriod
            Default: AgenciesGetStatisticsTimePeriod.LAST7DAYS.
        status_filter (Union[Unset, AgenciesGetStatisticsStatusFilter]): Which listings to filter
            based on status in lifecycle Default: AgenciesGetStatisticsStatusFilter.LIVEANDARCHIVED.
        channel (Union[Unset, AgenciesGetStatisticsChannel]): Channel of the listing Default:
            AgenciesGetStatisticsChannel.RESIDENTIAL.
        page_number (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['ListingPerformanceV1Statistics']]
    """

    kwargs = _get_kwargs(
        id=id,
        time_period=time_period,
        status_filter=status_filter,
        channel=channel,
        page_number=page_number,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    time_period: Union[Unset, AgenciesGetStatisticsTimePeriod] = AgenciesGetStatisticsTimePeriod.LAST7DAYS,
    status_filter: Union[Unset, AgenciesGetStatisticsStatusFilter] = AgenciesGetStatisticsStatusFilter.LIVEANDARCHIVED,
    channel: Union[Unset, AgenciesGetStatisticsChannel] = AgenciesGetStatisticsChannel.RESIDENTIAL,
    page_number: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 20,
) -> Optional[List["ListingPerformanceV1Statistics"]]:
    """Retrieves statistics for a specific agency.

    Args:
        id (int):
        time_period (Union[Unset, AgenciesGetStatisticsTimePeriod]): Defines StatisticsTimePeriod
            Default: AgenciesGetStatisticsTimePeriod.LAST7DAYS.
        status_filter (Union[Unset, AgenciesGetStatisticsStatusFilter]): Which listings to filter
            based on status in lifecycle Default: AgenciesGetStatisticsStatusFilter.LIVEANDARCHIVED.
        channel (Union[Unset, AgenciesGetStatisticsChannel]): Channel of the listing Default:
            AgenciesGetStatisticsChannel.RESIDENTIAL.
        page_number (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['ListingPerformanceV1Statistics']
    """

    return sync_detailed(
        id=id,
        client=client,
        time_period=time_period,
        status_filter=status_filter,
        channel=channel,
        page_number=page_number,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    time_period: Union[Unset, AgenciesGetStatisticsTimePeriod] = AgenciesGetStatisticsTimePeriod.LAST7DAYS,
    status_filter: Union[Unset, AgenciesGetStatisticsStatusFilter] = AgenciesGetStatisticsStatusFilter.LIVEANDARCHIVED,
    channel: Union[Unset, AgenciesGetStatisticsChannel] = AgenciesGetStatisticsChannel.RESIDENTIAL,
    page_number: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 20,
) -> Response[List["ListingPerformanceV1Statistics"]]:
    """Retrieves statistics for a specific agency.

    Args:
        id (int):
        time_period (Union[Unset, AgenciesGetStatisticsTimePeriod]): Defines StatisticsTimePeriod
            Default: AgenciesGetStatisticsTimePeriod.LAST7DAYS.
        status_filter (Union[Unset, AgenciesGetStatisticsStatusFilter]): Which listings to filter
            based on status in lifecycle Default: AgenciesGetStatisticsStatusFilter.LIVEANDARCHIVED.
        channel (Union[Unset, AgenciesGetStatisticsChannel]): Channel of the listing Default:
            AgenciesGetStatisticsChannel.RESIDENTIAL.
        page_number (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['ListingPerformanceV1Statistics']]
    """

    kwargs = _get_kwargs(
        id=id,
        time_period=time_period,
        status_filter=status_filter,
        channel=channel,
        page_number=page_number,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    time_period: Union[Unset, AgenciesGetStatisticsTimePeriod] = AgenciesGetStatisticsTimePeriod.LAST7DAYS,
    status_filter: Union[Unset, AgenciesGetStatisticsStatusFilter] = AgenciesGetStatisticsStatusFilter.LIVEANDARCHIVED,
    channel: Union[Unset, AgenciesGetStatisticsChannel] = AgenciesGetStatisticsChannel.RESIDENTIAL,
    page_number: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 20,
) -> Optional[List["ListingPerformanceV1Statistics"]]:
    """Retrieves statistics for a specific agency.

    Args:
        id (int):
        time_period (Union[Unset, AgenciesGetStatisticsTimePeriod]): Defines StatisticsTimePeriod
            Default: AgenciesGetStatisticsTimePeriod.LAST7DAYS.
        status_filter (Union[Unset, AgenciesGetStatisticsStatusFilter]): Which listings to filter
            based on status in lifecycle Default: AgenciesGetStatisticsStatusFilter.LIVEANDARCHIVED.
        channel (Union[Unset, AgenciesGetStatisticsChannel]): Channel of the listing Default:
            AgenciesGetStatisticsChannel.RESIDENTIAL.
        page_number (Union[Unset, int]):  Default: 1.
        page_size (Union[Unset, int]):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['ListingPerformanceV1Statistics']
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            time_period=time_period,
            status_filter=status_filter,
            channel=channel,
            page_number=page_number,
            page_size=page_size,
        )
    ).parsed
