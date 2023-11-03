from ..base import AdyenServiceBase


class TransferInstrumentsApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(TransferInstrumentsApi, self).__init__(client=client)
        self.service = "legalEntityManagement"
        self.baseUrl = "https://kyc-test.adyen.com/lem/v3"

    def delete_transfer_instrument(self, id, idempotency_key=None, **kwargs):
        """
        Delete a transfer instrument
        """
        endpoint = self.baseUrl + f"/transferInstruments/{id}"
        method = "DELETE"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_transfer_instrument(self, id, idempotency_key=None, **kwargs):
        """
        Get a transfer instrument
        """
        endpoint = self.baseUrl + f"/transferInstruments/{id}"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def update_transfer_instrument(self, request, id, idempotency_key=None, **kwargs):
        """
        Update a transfer instrument
        """
        endpoint = self.baseUrl + f"/transferInstruments/{id}"
        method = "PATCH"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def create_transfer_instrument(self, request, idempotency_key=None, **kwargs):
        """
        Create a transfer instrument
        """
        endpoint = self.baseUrl + f"/transferInstruments"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

