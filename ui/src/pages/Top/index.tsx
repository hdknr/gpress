import React from 'react';
import { Link } from 'react-router-dom';


export const Top: React.FunctionComponent = () => {
    return (
        <div>
            <h4>Top</h4>
            <Link to='/frontend/post'>投稿</Link>
        </div>
    );
};
