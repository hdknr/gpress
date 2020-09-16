import graphene
import channels_graphql_ws
from logging import getLogger
logger = getLogger()


class GraphqlWsConsumer(channels_graphql_ws.GraphqlWsConsumer):
    """Channels WebSocket consumer which provides GraphQL API."""

    async def on_connect(self, payload):
        """New client connection handler."""
        # You can `raise` from here to reject the connection.
        await self.channel_layer.group_add("sample", self.channel_name)
        logger.debug(f"on_connect ---------------{self.channel_name}")

    # ---- DEBUG
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

