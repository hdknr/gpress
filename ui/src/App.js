import React from 'react';
import './App.css';
import { ApolloProvider } from "react-apollo";
import gql from "graphql-tag";
import ApolloClient from 'apollo-boost';
import { Query } from "react-apollo";
import Cookies from 'js-cookie'
// import { createHttpLink, HttpLink } from "apollo-link-http";
import { HttpLink } from "apollo-link-http";
// import { InMemoryCache } from 'apollo-cache-inmemory';
import { InMemoryCache} from 'apollo-cache-inmemory';



const URI = "http://ubn1804:9000/api/graphql/"

/*
const link1 = createHttpLink({
  uri: URI,
  //credentials: 'same-origin'
  credentials: 'include'
});
*/

const client = new ApolloClient({
  uri: URI,
  credentials: 'include',
  request: (operation) => {
    console.log(operation.getContext())
    console.log(operation)
    const csrfToken = Cookies.get('csrftoken')
    operation.setContext({
      headers: { 
        "X-CSRFToken": csrfToken ,
        'X-Requested-With': 'XMLHttpRequest',
      }
    })
  },
})

/*
const cache = new InMemoryCache();
const link = new HttpLink({
  uri: '/graphql/xxxxxx/',
});

const client = new ApolloClient({
  cache,
  link
});
*/

// const link = new HttpLink({ uri: URI });
// const client = new ApolloClient({link: link})

//////////

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
