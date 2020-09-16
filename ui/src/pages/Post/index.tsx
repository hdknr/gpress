import React from 'react';
import { Switch, Route } from 'react-router-dom';
import { List } from './List';
import { Detail } from './Detail';

export const Post: React.FunctionComponent = () => {
    return (
        <Switch>
            <Route path="/frontend/post/:postId" component={Detail} />
            <Route path="/frontend/post/" component={List} />
        </Switch>
    );
};
