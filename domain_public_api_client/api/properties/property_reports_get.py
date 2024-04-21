from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domain_property_report_service_v1_model_property_report_generation_result import (
    DomainPropertyReportServiceV1ModelPropertyReportGenerationResult,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    property_type: str,
    street_number: str,
    street_name: str,
    suburb: str,
    state: str,
    unit_number: Union[Unset, str] = UNSET,
    street_type: Union[Unset, str] = UNSET,
    postcode: Union[Unset, str] = UNSET,
    area_size: Union[Unset, int] = UNSET,
    bedrooms: Union[Unset, int] = UNSET,
    bathrooms: Union[Unset, int] = UNSET,
    parking: Union[Unset, int] = UNSET,
    prepared_for: Union[Unset, str] = UNSET,
    product_code: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["propertyType"] = property_type

    params["streetNumber"] = street_number

    params["streetName"] = street_name

    params["suburb"] = suburb

    params["state"] = state

    params["unitNumber"] = unit_number

    params["streetType"] = street_type

    params["postcode"] = postcode

    params["areaSize"] = area_size

    params["bedrooms"] = bedrooms

    params["bathrooms"] = bathrooms

    params["parking"] = parking

    params["preparedFor"] = prepared_for

    params["productCode"] = product_code

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v1/propertyReports",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DomainPropertyReportServiceV1ModelPropertyReportGenerationResult]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DomainPropertyReportServiceV1ModelPropertyReportGenerationResult.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DomainPropertyReportServiceV1ModelPropertyReportGenerationResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    property_type: str,
    street_number: str,
    street_name: str,
    suburb: str,
    state: str,
    unit_number: Union[Unset, str] = UNSET,
    street_type: Union[Unset, str] = UNSET,
    postcode: Union[Unset, str] = UNSET,
    area_size: Union[Unset, int] = UNSET,
    bedrooms: Union[Unset, int] = UNSET,
    bathrooms: Union[Unset, int] = UNSET,
    parking: Union[Unset, int] = UNSET,
    prepared_for: Union[Unset, str] = UNSET,
    product_code: Union[Unset, str] = UNSET,
) -> Response[DomainPropertyReportServiceV1ModelPropertyReportGenerationResult]:
    """Retrieves a property report based on query parameters

    Args:
        property_type (str):
        street_number (str):
        street_name (str):
        suburb (str):
        state (str):
        unit_number (Union[Unset, str]):
        street_type (Union[Unset, str]):
        postcode (Union[Unset, str]):
        area_size (Union[Unset, int]):
        bedrooms (Union[Unset, int]):
        bathrooms (Union[Unset, int]):
        parking (Union[Unset, int]):
        prepared_for (Union[Unset, str]):
        product_code (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DomainPropertyReportServiceV1ModelPropertyReportGenerationResult]
    """

    kwargs = _get_kwargs(
        property_type=property_type,
        street_number=street_number,
        street_name=street_name,
        suburb=suburb,
        state=state,
        unit_number=unit_number,
        street_type=street_type,
        postcode=postcode,
        area_size=area_size,
        bedrooms=bedrooms,
        bathrooms=bathrooms,
        parking=parking,
        prepared_for=prepared_for,
        product_code=product_code,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    property_type: str,
    street_number: str,
    street_name: str,
    suburb: str,
    state: str,
    unit_number: Union[Unset, str] = UNSET,
    street_type: Union[Unset, str] = UNSET,
    postcode: Union[Unset, str] = UNSET,
    area_size: Union[Unset, int] = UNSET,
    bedrooms: Union[Unset, int] = UNSET,
    bathrooms: Union[Unset, int] = UNSET,
    parking: Union[Unset, int] = UNSET,
    prepared_for: Union[Unset, str] = UNSET,
    product_code: Union[Unset, str] = UNSET,
) -> Optional[DomainPropertyReportServiceV1ModelPropertyReportGenerationResult]:
    """Retrieves a property report based on query parameters

    Args:
        property_type (str):
        street_number (str):
        street_name (str):
        suburb (str):
        state (str):
        unit_number (Union[Unset, str]):
        street_type (Union[Unset, str]):
        postcode (Union[Unset, str]):
        area_size (Union[Unset, int]):
        bedrooms (Union[Unset, int]):
        bathrooms (Union[Unset, int]):
        parking (Union[Unset, int]):
        prepared_for (Union[Unset, str]):
        product_code (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DomainPropertyReportServiceV1ModelPropertyReportGenerationResult
    """

    return sync_detailed(
        client=client,
        property_type=property_type,
        street_number=street_number,
        street_name=street_name,
        suburb=suburb,
        state=state,
        unit_number=unit_number,
        street_type=street_type,
        postcode=postcode,
        area_size=area_size,
        bedrooms=bedrooms,
        bathrooms=bathrooms,
        parking=parking,
        prepared_for=prepared_for,
        product_code=product_code,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    property_type: str,
    street_number: str,
    street_name: str,
    suburb: str,
    state: str,
    unit_number: Union[Unset, str] = UNSET,
    street_type: Union[Unset, str] = UNSET,
    postcode: Union[Unset, str] = UNSET,
    area_size: Union[Unset, int] = UNSET,
    bedrooms: Union[Unset, int] = UNSET,
    bathrooms: Union[Unset, int] = UNSET,
    parking: Union[Unset, int] = UNSET,
    prepared_for: Union[Unset, str] = UNSET,
    product_code: Union[Unset, str] = UNSET,
) -> Response[DomainPropertyReportServiceV1ModelPropertyReportGenerationResult]:
    """Retrieves a property report based on query parameters

    Args:
        property_type (str):
        street_number (str):
        street_name (str):
        suburb (str):
        state (str):
        unit_number (Union[Unset, str]):
        street_type (Union[Unset, str]):
        postcode (Union[Unset, str]):
        area_size (Union[Unset, int]):
        bedrooms (Union[Unset, int]):
        bathrooms (Union[Unset, int]):
        parking (Union[Unset, int]):
        prepared_for (Union[Unset, str]):
        product_code (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DomainPropertyReportServiceV1ModelPropertyReportGenerationResult]
    """

    kwargs = _get_kwargs(
        property_type=property_type,
        street_number=street_number,
        street_name=street_name,
        suburb=suburb,
        state=state,
        unit_number=unit_number,
        street_type=street_type,
        postcode=postcode,
        area_size=area_size,
        bedrooms=bedrooms,
        bathrooms=bathrooms,
        parking=parking,
        prepared_for=prepared_for,
        product_code=product_code,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    property_type: str,
    street_number: str,
    street_name: str,
    suburb: str,
    state: str,
    unit_number: Union[Unset, str] = UNSET,
    street_type: Union[Unset, str] = UNSET,
    postcode: Union[Unset, str] = UNSET,
    area_size: Union[Unset, int] = UNSET,
    bedrooms: Union[Unset, int] = UNSET,
    bathrooms: Union[Unset, int] = UNSET,
    parking: Union[Unset, int] = UNSET,
    prepared_for: Union[Unset, str] = UNSET,
    product_code: Union[Unset, str] = UNSET,
) -> Optional[DomainPropertyReportServiceV1ModelPropertyReportGenerationResult]:
    """Retrieves a property report based on query parameters

    Args:
        property_type (str):
        street_number (str):
        street_name (str):
        suburb (str):
        state (str):
        unit_number (Union[Unset, str]):
        street_type (Union[Unset, str]):
        postcode (Union[Unset, str]):
        area_size (Union[Unset, int]):
        bedrooms (Union[Unset, int]):
        bathrooms (Union[Unset, int]):
        parking (Union[Unset, int]):
        prepared_for (Union[Unset, str]):
        product_code (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DomainPropertyReportServiceV1ModelPropertyReportGenerationResult
    """

    return (
        await asyncio_detailed(
            client=client,
            property_type=property_type,
            street_number=street_number,
            street_name=street_name,
            suburb=suburb,
            state=state,
            unit_number=unit_number,
            street_type=street_type,
            postcode=postcode,
            area_size=area_size,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            parking=parking,
            prepared_for=prepared_for,
            product_code=product_code,
        )
    ).parsed
