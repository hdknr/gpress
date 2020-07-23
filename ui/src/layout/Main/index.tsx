import React from 'react';
import { Switch, Route } from 'react-router-dom';
import { Top, Post} from '../../pages';

export const Main: React.FunctionComponent = () => {
    return (
        <div className="App-Main">
            <Switch>
                <Route path="/" exact>
                    <Top/>
                </Route>
                <Route path="/post" exact>
                    <Post/>
                </Route>
            </Switch>
        </div>);
};
