import React from 'react';
import { Link } from 'react-router-dom';
import { useLatestPostSubscription } from '../../graphql';


export const Top: React.FunctionComponent = () => {
    // https://www.apollographql.com/docs/react/data/subscriptions/#usesubscription-api-reference
    const {
        data, loading, error,
    } = useLatestPostSubscription({ variables: { arg1: '', arg2: '' } });

    return (
        <div>
            <h4>Top</h4>
            <div>
                <span>{data?.latestpost?.title}</span>
            </div>
            <Link to='/frontend/post'>投稿</Link>
        </div>
    );
};
