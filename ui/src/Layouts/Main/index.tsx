import React from 'react';
import { Switch, Route } from 'react-router-dom';
import { Top, Post} from '../../Pages';

export const Main: React.FunctionComponent = () => {
    return (
        <div className="App-Main">
            <Switch>
                <Route path="/" exact>
                    <Top/>
                </Route>
                <Route path="/post" >
                    <Post/>
                </Route>
            </Switch>
        </div>);
};
