from unittest.mock import patch

from django.test import TransactionTestCase

from codecov_auth.tests.factories import OwnerFactory
from graphql_api.tests.helper import GraphQLTestHelper

query = """
mutation($input: ActivateComponentMeasurementsInput!) {
  activateComponentMeasurements(input: $input) {
    error {
      __typename
    }
  }
}
"""


class ActivateComponentMeasurementsTestCase(GraphQLTestHelper, TransactionTestCase):
    def setUp(self):
        self.user = OwnerFactory()

    def test_when_unauthenticated(self):
        data = self.gql_request(
            query, variables={"input": {"owner": "codecov", "repoName": "test-repo"}}
        )
        assert (
            data["activateComponentMeasurements"]["error"]["__typename"]
            == "UnauthenticatedError"
        )

    @patch(
        "core.commands.repository.interactors.activate_component_measurements.ActivateComponentMeasurementsInteractor.execute"
    )
    def test_when_authenticated(self, execute):
        data = self.gql_request(
            query,
            user=self.user,
            variables={"input": {"owner": "codecov", "repoName": "test-repo"}},
        )
        assert data == {"activateComponentMeasurements": None}
