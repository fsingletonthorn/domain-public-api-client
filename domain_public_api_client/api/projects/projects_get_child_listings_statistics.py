from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.listing_performance_v1_project_listing_statistics_report import (
    ListingPerformanceV1ProjectListingStatisticsReport,
)
from ...models.projects_get_child_listings_statistics_time_period import ProjectsGetChildListingsStatisticsTimePeriod
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    time_period: Union[
        Unset, ProjectsGetChildListingsStatisticsTimePeriod
    ] = ProjectsGetChildListingsStatisticsTimePeriod.LAST7DAYS,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_time_period: Union[Unset, str] = UNSET
    if not isinstance(time_period, Unset):
        json_time_period = time_period.value

    params["timePeriod"] = json_time_period

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v1/projects/{id}/listings/statistics",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ListingPerformanceV1ProjectListingStatisticsReport]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListingPerformanceV1ProjectListingStatisticsReport.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ListingPerformanceV1ProjectListingStatisticsReport]:
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
    time_period: Union[
        Unset, ProjectsGetChildListingsStatisticsTimePeriod
    ] = ProjectsGetChildListingsStatisticsTimePeriod.LAST7DAYS,
) -> Response[ListingPerformanceV1ProjectListingStatisticsReport]:
    """Retrieves statistics for a specific project with a breakdown for listings.

    Args:
        id (int):
        time_period (Union[Unset, ProjectsGetChildListingsStatisticsTimePeriod]): Defines
            StatisticsTimePeriod Default: ProjectsGetChildListingsStatisticsTimePeriod.LAST7DAYS.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListingPerformanceV1ProjectListingStatisticsReport]
    """

    kwargs = _get_kwargs(
        id=id,
        time_period=time_period,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    time_period: Union[
        Unset, ProjectsGetChildListingsStatisticsTimePeriod
    ] = ProjectsGetChildListingsStatisticsTimePeriod.LAST7DAYS,
) -> Optional[ListingPerformanceV1ProjectListingStatisticsReport]:
    """Retrieves statistics for a specific project with a breakdown for listings.

    Args:
        id (int):
        time_period (Union[Unset, ProjectsGetChildListingsStatisticsTimePeriod]): Defines
            StatisticsTimePeriod Default: ProjectsGetChildListingsStatisticsTimePeriod.LAST7DAYS.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListingPerformanceV1ProjectListingStatisticsReport
    """

    return sync_detailed(
        id=id,
        client=client,
        time_period=time_period,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    time_period: Union[
        Unset, ProjectsGetChildListingsStatisticsTimePeriod
    ] = ProjectsGetChildListingsStatisticsTimePeriod.LAST7DAYS,
) -> Response[ListingPerformanceV1ProjectListingStatisticsReport]:
    """Retrieves statistics for a specific project with a breakdown for listings.

    Args:
        id (int):
        time_period (Union[Unset, ProjectsGetChildListingsStatisticsTimePeriod]): Defines
            StatisticsTimePeriod Default: ProjectsGetChildListingsStatisticsTimePeriod.LAST7DAYS.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListingPerformanceV1ProjectListingStatisticsReport]
    """

    kwargs = _get_kwargs(
        id=id,
        time_period=time_period,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    time_period: Union[
        Unset, ProjectsGetChildListingsStatisticsTimePeriod
    ] = ProjectsGetChildListingsStatisticsTimePeriod.LAST7DAYS,
) -> Optional[ListingPerformanceV1ProjectListingStatisticsReport]:
    """Retrieves statistics for a specific project with a breakdown for listings.

    Args:
        id (int):
        time_period (Union[Unset, ProjectsGetChildListingsStatisticsTimePeriod]): Defines
            StatisticsTimePeriod Default: ProjectsGetChildListingsStatisticsTimePeriod.LAST7DAYS.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListingPerformanceV1ProjectListingStatisticsReport
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            time_period=time_period,
        )
    ).parsed
