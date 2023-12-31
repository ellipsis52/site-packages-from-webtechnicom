from ..base import AdyenServiceBase


class InitializationApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(InitializationApi, self).__init__(client=client)
        self.service = "payouts"
        self.baseUrl = "https://pal-test.adyen.com/pal/servlet/Payout/v68"

    def store_detail(self, request, idempotency_key=None, **kwargs):
        """
        Store payout details
        """
        endpoint = self.baseUrl + f"/storeDetail"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def store_detail_and_submit_third_party(self, request, idempotency_key=None, **kwargs):
        """
        Store details and submit a payout
        """
        endpoint = self.baseUrl + f"/storeDetailAndSubmitThirdParty"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def submit_third_party(self, request, idempotency_key=None, **kwargs):
        """
        Submit a payout
        """
        endpoint = self.baseUrl + f"/submitThirdParty"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

