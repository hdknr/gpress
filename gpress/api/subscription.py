import channels_graphql_ws
import graphene
from logging import getLogger

logger = getLogger()


class LatestPost(channels_graphql_ws.Subscription):
    # Subscription payload.
    title = graphene.String()

    class Arguments:
        """That is how subscription arguments are defined."""
        arg1 = graphene.String()
        arg2 = graphene.String()

    @staticmethod
    def subscribe(root, info, arg1, arg2):
        """Called when user subscribes."""
        logger.debug(f'LatestPost.subscribe {root} {info} {arg1} {arg2}')
        # Return the list of subscription group names.
        return ['group42', 'sample']

    @staticmethod
    def publish(payload, info, arg1, arg2):
        """Called to notify the client."""
        logger.debug(f'LatestPost.publish {payload} {info} {arg1} {arg2}')

        # Here `payload` contains the `payload` from the `broadcast()`
        # invocation (see below). You can return `MySubscription.SKIP`
        # if you wish to suppress the notification to a particular
        # client. For example, this allows to avoid notifications for
        # the actions made by this particular client.

        return LatestPost(**payload)


class Subscription(graphene.ObjectType):
    """Root GraphQL subscription."""
    latestpost = LatestPost.Field()
