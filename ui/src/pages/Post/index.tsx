import React from 'react';
import { Switch, Route } from 'react-router-dom';
import { List } from './List';
import { Detail } from './Detail';

export const Post: React.FunctionComponent = () => {
    return (
        <Switch>
            <Route path="/post/:postId">
                <Detail />
            </Route>
            <Route path="/post/">
                <List />
            </Route>
        </Switch>
    );
};
