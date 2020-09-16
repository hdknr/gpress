import React from 'react';
import { usePostSetLazyQuery } from "../../../graphql";


export const List: React.FunctionComponent = () => {
    const [
        getPostSet,
        { data, called, loading, error, fetchMore },
    ] = usePostSetLazyQuery({ variables: { first: 10 } });

    if (!called) {
        getPostSet()
    }

    if (loading) {
        return <div>Loading....</div>
    }

    if (error) {
        return <div>{JSON.stringify(error)}</div>
    }

    return (
        <div>
            <h4>Post List</h4>
            <div>
                <ul>
                    {data?.post_set?.edges.map((edge, index) => (
                        <li key={index}>
                            {edge?.node?.endpoint}
                        </li>
                    ))}
                </ul>

            </div>
        </div>
    );
};
