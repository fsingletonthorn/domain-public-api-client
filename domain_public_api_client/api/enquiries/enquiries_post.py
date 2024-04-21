from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.domain_enquiry_service_v1_model_group_enquiry_service_models_enquiry_response import (
    DomainEnquiryServiceV1ModelGroupEnquiryServiceModelsEnquiryResponse,
)
from ...models.domain_public_adapter_web_api_models_v1_enquiries_enquiry import (
    DomainPublicAdapterWebApiModelsV1EnquiriesEnquiry,
)
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        DomainPublicAdapterWebApiModelsV1EnquiriesEnquiry,
        DomainPublicAdapterWebApiModelsV1EnquiriesEnquiry,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v1/enquiries",
    }

    if isinstance(body, DomainPublicAdapterWebApiModelsV1EnquiriesEnquiry):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, DomainPublicAdapterWebApiModelsV1EnquiriesEnquiry):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DomainEnquiryServiceV1ModelGroupEnquiryServiceModelsEnquiryResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DomainEnquiryServiceV1ModelGroupEnquiryServiceModelsEnquiryResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DomainEnquiryServiceV1ModelGroupEnquiryServiceModelsEnquiryResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        DomainPublicAdapterWebApiModelsV1EnquiriesEnquiry,
        DomainPublicAdapterWebApiModelsV1EnquiriesEnquiry,
    ],
) -> Response[DomainEnquiryServiceV1ModelGroupEnquiryServiceModelsEnquiryResponse]:
    """Sends an enquiry for listing, agency, etc... (based on the enquiry type and referenceid).
    Recipients and template will be automatically selected.

    Args:
        body (DomainPublicAdapterWebApiModelsV1EnquiriesEnquiry): An enquiry with associated
            reference (eg. listing)
        body (DomainPublicAdapterWebApiModelsV1EnquiriesEnquiry): An enquiry with associated
            reference (eg. listing)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DomainEnquiryServiceV1ModelGroupEnquiryServiceModelsEnquiryResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: Union[
        DomainPublicAdapterWebApiModelsV1EnquiriesEnquiry,
        DomainPublicAdapterWebApiModelsV1EnquiriesEnquiry,
    ],
) -> Optional[DomainEnquiryServiceV1ModelGroupEnquiryServiceModelsEnquiryResponse]:
    """Sends an enquiry for listing, agency, etc... (based on the enquiry type and referenceid).
    Recipients and template will be automatically selected.

    Args:
        body (DomainPublicAdapterWebApiModelsV1EnquiriesEnquiry): An enquiry with associated
            reference (eg. listing)
        body (DomainPublicAdapterWebApiModelsV1EnquiriesEnquiry): An enquiry with associated
            reference (eg. listing)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DomainEnquiryServiceV1ModelGroupEnquiryServiceModelsEnquiryResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: Union[
        DomainPublicAdapterWebApiModelsV1EnquiriesEnquiry,
        DomainPublicAdapterWebApiModelsV1EnquiriesEnquiry,
    ],
) -> Response[DomainEnquiryServiceV1ModelGroupEnquiryServiceModelsEnquiryResponse]:
    """Sends an enquiry for listing, agency, etc... (based on the enquiry type and referenceid).
    Recipients and template will be automatically selected.

    Args:
        body (DomainPublicAdapterWebApiModelsV1EnquiriesEnquiry): An enquiry with associated
            reference (eg. listing)
        body (DomainPublicAdapterWebApiModelsV1EnquiriesEnquiry): An enquiry with associated
            reference (eg. listing)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DomainEnquiryServiceV1ModelGroupEnquiryServiceModelsEnquiryResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: Union[
        DomainPublicAdapterWebApiModelsV1EnquiriesEnquiry,
        DomainPublicAdapterWebApiModelsV1EnquiriesEnquiry,
    ],
) -> Optional[DomainEnquiryServiceV1ModelGroupEnquiryServiceModelsEnquiryResponse]:
    """Sends an enquiry for listing, agency, etc... (based on the enquiry type and referenceid).
    Recipients and template will be automatically selected.

    Args:
        body (DomainPublicAdapterWebApiModelsV1EnquiriesEnquiry): An enquiry with associated
            reference (eg. listing)
        body (DomainPublicAdapterWebApiModelsV1EnquiriesEnquiry): An enquiry with associated
            reference (eg. listing)

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DomainEnquiryServiceV1ModelGroupEnquiryServiceModelsEnquiryResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
