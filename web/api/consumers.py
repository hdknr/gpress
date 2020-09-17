import channels_graphql_ws
from logging import getLogger
logger = getLogger()


class GraphqlWsConsumer(channels_graphql_ws.GraphqlWsConsumer):
    """Channels WebSocket consumer which provides GraphQL API."""

    async def on_connect(self, payload):
        """New client connection handler."""
        # You can `raise` from here to reject the connection.
        logger.debug(f"on_connect ---------------{self.channel_name} {payload}")
