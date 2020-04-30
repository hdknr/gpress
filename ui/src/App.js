import React from 'react';
import './App.css';
import { ApolloProvider } from "react-apollo";
import gql from "graphql-tag";
import ApolloClient from 'apollo-boost';
import { Query } from "react-apollo";
import Cookies from 'js-cookie'

const client = new ApolloClient({
  uri: "http://ubn1804:9000/api/graphql/",
  credentials: 'include',
  request: (operation) => {
    const csrfToken = Cookies.get('csrftoken')
    operation.setContext({
      headers: { 
        "X-CSRFTOKEN": csrfToken }
    })
  },
})

const PostSet = () => (
  <Query
    query={gql`
    {
      post_set(first:10) {
        pageInfo {
          startCursor
          endCursor
        }
        edges {
          node {
            id, pk, post_title
          }
        }
        
      }
    }
    `}
  >
    {({ loading, error, data }) => {
      if (loading) return <p>Loading...</p>;
      if (error) return <p>Error :( {`${error}`}</p>;

      return data.post_set.edges.map(({ node }) => (
        <div key={node.pk}>
          <p>{`${node.pk}: ${node.post_title}`}</p>
        </div>
      ));
    }}
  </Query>
);


function App() {
  return (
    <div className="App">
      <ApolloProvider client={client}>
        <div>
          <h2>Wordpress Posts</h2>
        </div>
        <PostSet />
      </ApolloProvider>
    </div>
  );
}

export default App;
