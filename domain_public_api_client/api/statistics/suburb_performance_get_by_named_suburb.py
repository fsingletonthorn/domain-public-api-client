from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.suburb_performance_get_by_named_suburb_period_size import SuburbPerformanceGetByNamedSuburbPeriodSize
from ...models.suburb_performance_get_by_named_suburb_property_category import (
    SuburbPerformanceGetByNamedSuburbPropertyCategory,
)
from ...models.suburb_performance_statistics_v3_suburb_performance import SuburbPerformanceStatisticsV3SuburbPerformance
from ...types import UNSET, Response, Unset


def _get_kwargs(
    state: str,
    suburb: str,
    postcode: str,
    *,
    property_category: Union[
        Unset, SuburbPerformanceGetByNamedSuburbPropertyCategory
    ] = SuburbPerformanceGetByNamedSuburbPropertyCategory.HOUSE,
    bedrooms: Union[Unset, int] = UNSET,
    period_size: Union[
        Unset, SuburbPerformanceGetByNamedSuburbPeriodSize
    ] = SuburbPerformanceGetByNamedSuburbPeriodSize.QUARTERS,
    starting_period_relative_to_current: Union[Unset, int] = 1,
    total_periods: Union[Unset, int] = 4,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_property_category: Union[Unset, str] = UNSET
    if not isinstance(property_category, Unset):
        json_property_category = property_category.value

    params["propertyCategory"] = json_property_category

    params["bedrooms"] = bedrooms

    json_period_size: Union[Unset, str] = UNSET
    if not isinstance(period_size, Unset):
        json_period_size = period_size.value

    params["periodSize"] = json_period_size

    params["startingPeriodRelativeToCurrent"] = starting_period_relative_to_current

    params["totalPeriods"] = total_periods

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v2/suburbPerformanceStatistics/{state}/{suburb}/{postcode}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SuburbPerformanceStatisticsV3SuburbPerformance]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SuburbPerformanceStatisticsV3SuburbPerformance.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SuburbPerformanceStatisticsV3SuburbPerformance]:
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
    property_category: Union[
        Unset, SuburbPerformanceGetByNamedSuburbPropertyCategory
    ] = SuburbPerformanceGetByNamedSuburbPropertyCategory.HOUSE,
    bedrooms: Union[Unset, int] = UNSET,
    period_size: Union[
        Unset, SuburbPerformanceGetByNamedSuburbPeriodSize
    ] = SuburbPerformanceGetByNamedSuburbPeriodSize.QUARTERS,
    starting_period_relative_to_current: Union[Unset, int] = 1,
    total_periods: Union[Unset, int] = 4,
) -> Response[SuburbPerformanceStatisticsV3SuburbPerformance]:
    """Search for sales statistics in a given geographic level.

     - Standard Auction Clearance Rate formula is: `AuctionNumberSold / (AuctionNumberAuctioned +
    AuctionNumberWithdrawn)`
    - The Rate is considered Not Statistic Reliable if: `AuctionNumberAuctioned + AuctionNumberWithdrawn
    < 10`
    - APM Standard Gross Rental Yield formula is: `(MedianRentListingPrice* 52) / MedianSoldPrice`
    - The Yield is considered Not Available if: `MedianRentListingPrice is null or MedianSoldPrice is
    null`

    Args:
        state (str):
        suburb (str):
        postcode (str):
        property_category (Union[Unset, SuburbPerformanceGetByNamedSuburbPropertyCategory]):
            Default: SuburbPerformanceGetByNamedSuburbPropertyCategory.HOUSE.
        bedrooms (Union[Unset, int]):
        period_size (Union[Unset, SuburbPerformanceGetByNamedSuburbPeriodSize]):  Default:
            SuburbPerformanceGetByNamedSuburbPeriodSize.QUARTERS.
        starting_period_relative_to_current (Union[Unset, int]):  Default: 1.
        total_periods (Union[Unset, int]):  Default: 4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SuburbPerformanceStatisticsV3SuburbPerformance]
    """

    kwargs = _get_kwargs(
        state=state,
        suburb=suburb,
        postcode=postcode,
        property_category=property_category,
        bedrooms=bedrooms,
        period_size=period_size,
        starting_period_relative_to_current=starting_period_relative_to_current,
        total_periods=total_periods,
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
    property_category: Union[
        Unset, SuburbPerformanceGetByNamedSuburbPropertyCategory
    ] = SuburbPerformanceGetByNamedSuburbPropertyCategory.HOUSE,
    bedrooms: Union[Unset, int] = UNSET,
    period_size: Union[
        Unset, SuburbPerformanceGetByNamedSuburbPeriodSize
    ] = SuburbPerformanceGetByNamedSuburbPeriodSize.QUARTERS,
    starting_period_relative_to_current: Union[Unset, int] = 1,
    total_periods: Union[Unset, int] = 4,
) -> Optional[SuburbPerformanceStatisticsV3SuburbPerformance]:
    """Search for sales statistics in a given geographic level.

     - Standard Auction Clearance Rate formula is: `AuctionNumberSold / (AuctionNumberAuctioned +
    AuctionNumberWithdrawn)`
    - The Rate is considered Not Statistic Reliable if: `AuctionNumberAuctioned + AuctionNumberWithdrawn
    < 10`
    - APM Standard Gross Rental Yield formula is: `(MedianRentListingPrice* 52) / MedianSoldPrice`
    - The Yield is considered Not Available if: `MedianRentListingPrice is null or MedianSoldPrice is
    null`

    Args:
        state (str):
        suburb (str):
        postcode (str):
        property_category (Union[Unset, SuburbPerformanceGetByNamedSuburbPropertyCategory]):
            Default: SuburbPerformanceGetByNamedSuburbPropertyCategory.HOUSE.
        bedrooms (Union[Unset, int]):
        period_size (Union[Unset, SuburbPerformanceGetByNamedSuburbPeriodSize]):  Default:
            SuburbPerformanceGetByNamedSuburbPeriodSize.QUARTERS.
        starting_period_relative_to_current (Union[Unset, int]):  Default: 1.
        total_periods (Union[Unset, int]):  Default: 4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SuburbPerformanceStatisticsV3SuburbPerformance
    """

    return sync_detailed(
        state=state,
        suburb=suburb,
        postcode=postcode,
        client=client,
        property_category=property_category,
        bedrooms=bedrooms,
        period_size=period_size,
        starting_period_relative_to_current=starting_period_relative_to_current,
        total_periods=total_periods,
    ).parsed


async def asyncio_detailed(
    state: str,
    suburb: str,
    postcode: str,
    *,
    client: AuthenticatedClient,
    property_category: Union[
        Unset, SuburbPerformanceGetByNamedSuburbPropertyCategory
    ] = SuburbPerformanceGetByNamedSuburbPropertyCategory.HOUSE,
    bedrooms: Union[Unset, int] = UNSET,
    period_size: Union[
        Unset, SuburbPerformanceGetByNamedSuburbPeriodSize
    ] = SuburbPerformanceGetByNamedSuburbPeriodSize.QUARTERS,
    starting_period_relative_to_current: Union[Unset, int] = 1,
    total_periods: Union[Unset, int] = 4,
) -> Response[SuburbPerformanceStatisticsV3SuburbPerformance]:
    """Search for sales statistics in a given geographic level.

     - Standard Auction Clearance Rate formula is: `AuctionNumberSold / (AuctionNumberAuctioned +
    AuctionNumberWithdrawn)`
    - The Rate is considered Not Statistic Reliable if: `AuctionNumberAuctioned + AuctionNumberWithdrawn
    < 10`
    - APM Standard Gross Rental Yield formula is: `(MedianRentListingPrice* 52) / MedianSoldPrice`
    - The Yield is considered Not Available if: `MedianRentListingPrice is null or MedianSoldPrice is
    null`

    Args:
        state (str):
        suburb (str):
        postcode (str):
        property_category (Union[Unset, SuburbPerformanceGetByNamedSuburbPropertyCategory]):
            Default: SuburbPerformanceGetByNamedSuburbPropertyCategory.HOUSE.
        bedrooms (Union[Unset, int]):
        period_size (Union[Unset, SuburbPerformanceGetByNamedSuburbPeriodSize]):  Default:
            SuburbPerformanceGetByNamedSuburbPeriodSize.QUARTERS.
        starting_period_relative_to_current (Union[Unset, int]):  Default: 1.
        total_periods (Union[Unset, int]):  Default: 4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SuburbPerformanceStatisticsV3SuburbPerformance]
    """

    kwargs = _get_kwargs(
        state=state,
        suburb=suburb,
        postcode=postcode,
        property_category=property_category,
        bedrooms=bedrooms,
        period_size=period_size,
        starting_period_relative_to_current=starting_period_relative_to_current,
        total_periods=total_periods,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    state: str,
    suburb: str,
    postcode: str,
    *,
    client: AuthenticatedClient,
    property_category: Union[
        Unset, SuburbPerformanceGetByNamedSuburbPropertyCategory
    ] = SuburbPerformanceGetByNamedSuburbPropertyCategory.HOUSE,
    bedrooms: Union[Unset, int] = UNSET,
    period_size: Union[
        Unset, SuburbPerformanceGetByNamedSuburbPeriodSize
    ] = SuburbPerformanceGetByNamedSuburbPeriodSize.QUARTERS,
    starting_period_relative_to_current: Union[Unset, int] = 1,
    total_periods: Union[Unset, int] = 4,
) -> Optional[SuburbPerformanceStatisticsV3SuburbPerformance]:
    """Search for sales statistics in a given geographic level.

     - Standard Auction Clearance Rate formula is: `AuctionNumberSold / (AuctionNumberAuctioned +
    AuctionNumberWithdrawn)`
    - The Rate is considered Not Statistic Reliable if: `AuctionNumberAuctioned + AuctionNumberWithdrawn
    < 10`
    - APM Standard Gross Rental Yield formula is: `(MedianRentListingPrice* 52) / MedianSoldPrice`
    - The Yield is considered Not Available if: `MedianRentListingPrice is null or MedianSoldPrice is
    null`

    Args:
        state (str):
        suburb (str):
        postcode (str):
        property_category (Union[Unset, SuburbPerformanceGetByNamedSuburbPropertyCategory]):
            Default: SuburbPerformanceGetByNamedSuburbPropertyCategory.HOUSE.
        bedrooms (Union[Unset, int]):
        period_size (Union[Unset, SuburbPerformanceGetByNamedSuburbPeriodSize]):  Default:
            SuburbPerformanceGetByNamedSuburbPeriodSize.QUARTERS.
        starting_period_relative_to_current (Union[Unset, int]):  Default: 1.
        total_periods (Union[Unset, int]):  Default: 4.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SuburbPerformanceStatisticsV3SuburbPerformance
    """

    return (
        await asyncio_detailed(
            state=state,
            suburb=suburb,
            postcode=postcode,
            client=client,
            property_category=property_category,
            bedrooms=bedrooms,
            period_size=period_size,
            starting_period_relative_to_current=starting_period_relative_to_current,
            total_periods=total_periods,
        )
    ).parsed
