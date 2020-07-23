import gql from 'graphql-tag';
import * as ApolloReactCommon from '@apollo/react-common';
import * as ApolloReactHooks from '@apollo/react-hooks';
export type Maybe<T> = T | null;
export type Exact<T extends { [key: string]: any }> = { [K in keyof T]: T[K] };
/** All built-in and custom scalars, mapped to their actual values */
export type Scalars = {
  ID: string;
  String: string;
  Boolean: boolean;
  Int: number;
  Float: number;
  DateTime: any;
  GenericScalar: any;
  JSONString: any;
};


export type ErrorType = {
  __typename?: 'ErrorType';
  field: Scalars['String'];
  messages: Array<Scalars['String']>;
};



export type Mutation = {
  __typename?: 'Mutation';
  post?: Maybe<PostPayload>;
  postmeta?: Maybe<PostmetaPayload>;
};


export type MutationPostArgs = {
  input: PostInput;
};


export type MutationPostmetaArgs = {
  input: PostmetaInput;
};

export type Node = {
  id: Scalars['ID'];
};

export type PageInfo = {
  __typename?: 'PageInfo';
  hasNextPage: Scalars['Boolean'];
  hasPreviousPage: Scalars['Boolean'];
  startCursor?: Maybe<Scalars['String']>;
  endCursor?: Maybe<Scalars['String']>;
};

export type Post = Node & {
  __typename?: 'Post';
  id: Scalars['ID'];
  post_author: Scalars['Int'];
  post_date: Scalars['DateTime'];
  post_date_gmt: Scalars['DateTime'];
  post_content: Scalars['String'];
  post_title: Scalars['String'];
  post_excerpt: Scalars['String'];
  post_status: Scalars['String'];
  comment_status: Scalars['String'];
  ping_status: Scalars['String'];
  post_password: Scalars['String'];
  post_name: Scalars['String'];
  to_ping: Scalars['String'];
  pinged: Scalars['String'];
  post_modified: Scalars['DateTime'];
  post_modified_gmt: Scalars['DateTime'];
  post_content_filtered: Scalars['String'];
  post_parent: Scalars['Int'];
  guid: Scalars['String'];
  menu_order: Scalars['Int'];
  post_type: Scalars['String'];
  post_mime_type: Scalars['String'];
  comment_count: Scalars['Int'];
  postmeta_set: PostmetaConnection;
  pk?: Maybe<Scalars['Int']>;
  endpoint?: Maybe<Scalars['String']>;
};


export type PostPostmeta_SetArgs = {
  before?: Maybe<Scalars['String']>;
  after?: Maybe<Scalars['String']>;
  first?: Maybe<Scalars['Int']>;
  last?: Maybe<Scalars['Int']>;
  post?: Maybe<Scalars['ID']>;
  meta_key?: Maybe<Scalars['String']>;
  meta_value?: Maybe<Scalars['String']>;
  pk?: Maybe<Scalars['Float']>;
};

export type PostInput = {
  post_author: Scalars['Int'];
  post_date: Scalars['DateTime'];
  post_date_gmt: Scalars['DateTime'];
  post_content: Scalars['String'];
  post_title: Scalars['String'];
  post_excerpt: Scalars['String'];
  post_status: Scalars['String'];
  comment_status: Scalars['String'];
  ping_status: Scalars['String'];
  post_password: Scalars['String'];
  post_name: Scalars['String'];
  to_ping: Scalars['String'];
  pinged: Scalars['String'];
  post_modified: Scalars['DateTime'];
  post_modified_gmt: Scalars['DateTime'];
  post_content_filtered: Scalars['String'];
  post_parent: Scalars['Int'];
  guid: Scalars['String'];
  menu_order: Scalars['Int'];
  post_type: Scalars['String'];
  post_mime_type: Scalars['String'];
  comment_count: Scalars['Int'];
  clientMutationId?: Maybe<Scalars['String']>;
};

export type PostNodeSetConnection = {
  __typename?: 'PostNodeSetConnection';
  pageInfo: PageInfo;
  edges: Array<Maybe<PostNodeSetEdge>>;
  total_count?: Maybe<Scalars['Int']>;
  records?: Maybe<Scalars['Int']>;
};

export type PostNodeSetEdge = {
  __typename?: 'PostNodeSetEdge';
  node?: Maybe<Post>;
  cursor: Scalars['String'];
};

export type PostPayload = {
  __typename?: 'PostPayload';
  id?: Maybe<Scalars['Int']>;
  endpoint?: Maybe<Scalars['String']>;
  post_author?: Maybe<Scalars['Int']>;
  post_date?: Maybe<Scalars['DateTime']>;
  post_date_gmt?: Maybe<Scalars['DateTime']>;
  post_content?: Maybe<Scalars['String']>;
  post_title?: Maybe<Scalars['String']>;
  post_excerpt?: Maybe<Scalars['String']>;
  post_status?: Maybe<Scalars['String']>;
  comment_status?: Maybe<Scalars['String']>;
  ping_status?: Maybe<Scalars['String']>;
  post_password?: Maybe<Scalars['String']>;
  post_name?: Maybe<Scalars['String']>;
  to_ping?: Maybe<Scalars['String']>;
  pinged?: Maybe<Scalars['String']>;
  post_modified?: Maybe<Scalars['DateTime']>;
  post_modified_gmt?: Maybe<Scalars['DateTime']>;
  post_content_filtered?: Maybe<Scalars['String']>;
  post_parent?: Maybe<Scalars['Int']>;
  guid?: Maybe<Scalars['String']>;
  menu_order?: Maybe<Scalars['Int']>;
  post_type?: Maybe<Scalars['String']>;
  post_mime_type?: Maybe<Scalars['String']>;
  comment_count?: Maybe<Scalars['Int']>;
  errors?: Maybe<Array<Maybe<ErrorType>>>;
  clientMutationId?: Maybe<Scalars['String']>;
};

export type Postmeta = Node & {
  __typename?: 'Postmeta';
  id: Scalars['ID'];
  post: Post;
  meta_key?: Maybe<Scalars['String']>;
  meta_value?: Maybe<Scalars['String']>;
  pk?: Maybe<Scalars['Int']>;
  endpoint?: Maybe<Scalars['String']>;
  meta_value_obj?: Maybe<Scalars['GenericScalar']>;
};

export type PostmetaConnection = {
  __typename?: 'PostmetaConnection';
  pageInfo: PageInfo;
  edges: Array<Maybe<PostmetaEdge>>;
};

export type PostmetaEdge = {
  __typename?: 'PostmetaEdge';
  node?: Maybe<Postmeta>;
  cursor: Scalars['String'];
};

export type PostmetaInput = {
  meta_key?: Maybe<Scalars['String']>;
  meta_value?: Maybe<Scalars['String']>;
  post: Scalars['String'];
  clientMutationId?: Maybe<Scalars['String']>;
};

export type PostmetaNodeSetConnection = {
  __typename?: 'PostmetaNodeSetConnection';
  pageInfo: PageInfo;
  edges: Array<Maybe<PostmetaNodeSetEdge>>;
  total_count?: Maybe<Scalars['Int']>;
  records?: Maybe<Scalars['Int']>;
};

export type PostmetaNodeSetEdge = {
  __typename?: 'PostmetaNodeSetEdge';
  node?: Maybe<Postmeta>;
  cursor: Scalars['String'];
};

export type PostmetaPayload = {
  __typename?: 'PostmetaPayload';
  id?: Maybe<Scalars['Int']>;
  endpoint?: Maybe<Scalars['String']>;
  meta_value_obj?: Maybe<Scalars['JSONString']>;
  meta_key?: Maybe<Scalars['String']>;
  meta_value?: Maybe<Scalars['String']>;
  post?: Maybe<Scalars['String']>;
  errors?: Maybe<Array<Maybe<ErrorType>>>;
  clientMutationId?: Maybe<Scalars['String']>;
};

export type Query = {
  __typename?: 'Query';
  post?: Maybe<Post>;
  post_set?: Maybe<PostNodeSetConnection>;
  postmeta?: Maybe<Postmeta>;
  postmeta_set?: Maybe<PostmetaNodeSetConnection>;
};


export type QueryPostArgs = {
  id: Scalars['ID'];
};


export type QueryPost_SetArgs = {
  before?: Maybe<Scalars['String']>;
  after?: Maybe<Scalars['String']>;
  first?: Maybe<Scalars['Int']>;
  last?: Maybe<Scalars['Int']>;
  post_author?: Maybe<Scalars['Int']>;
  post_date?: Maybe<Scalars['DateTime']>;
  post_date_gmt?: Maybe<Scalars['DateTime']>;
  post_content?: Maybe<Scalars['String']>;
  post_title?: Maybe<Scalars['String']>;
  post_excerpt?: Maybe<Scalars['String']>;
  post_status?: Maybe<Scalars['String']>;
  comment_status?: Maybe<Scalars['String']>;
  ping_status?: Maybe<Scalars['String']>;
  post_password?: Maybe<Scalars['String']>;
  post_name?: Maybe<Scalars['String']>;
  to_ping?: Maybe<Scalars['String']>;
  pinged?: Maybe<Scalars['String']>;
  post_modified?: Maybe<Scalars['DateTime']>;
  post_modified_gmt?: Maybe<Scalars['DateTime']>;
  post_content_filtered?: Maybe<Scalars['String']>;
  post_parent?: Maybe<Scalars['Int']>;
  guid?: Maybe<Scalars['String']>;
  menu_order?: Maybe<Scalars['Int']>;
  post_type?: Maybe<Scalars['String']>;
  post_mime_type?: Maybe<Scalars['String']>;
  comment_count?: Maybe<Scalars['Int']>;
  pk?: Maybe<Scalars['Float']>;
};


export type QueryPostmetaArgs = {
  id: Scalars['ID'];
};


export type QueryPostmeta_SetArgs = {
  before?: Maybe<Scalars['String']>;
  after?: Maybe<Scalars['String']>;
  first?: Maybe<Scalars['Int']>;
  last?: Maybe<Scalars['Int']>;
  post?: Maybe<Scalars['ID']>;
  meta_key?: Maybe<Scalars['String']>;
  meta_value?: Maybe<Scalars['String']>;
  pk?: Maybe<Scalars['Float']>;
};

export type PostSetQueryVariables = Exact<{
  first?: Maybe<Scalars['Int']>;
  after?: Maybe<Scalars['String']>;
  before?: Maybe<Scalars['String']>;
}>;


export type PostSetQuery = (
  { __typename?: 'Query' }
  & { post_set?: Maybe<(
    { __typename?: 'PostNodeSetConnection' }
    & { pageInfo: (
      { __typename?: 'PageInfo' }
      & Pick<PageInfo, 'startCursor' | 'endCursor' | 'hasNextPage' | 'hasPreviousPage'>
    ), edges: Array<Maybe<(
      { __typename?: 'PostNodeSetEdge' }
      & { node?: Maybe<(
        { __typename?: 'Post' }
        & Pick<Post, 'pk' | 'id' | 'endpoint'>
      )> }
    )>> }
  )> }
);


export const PostSetDocument = gql`
    query postSet($first: Int, $after: String, $before: String) {
  post_set(first: $first, after: $after, before: $before) {
    pageInfo {
      startCursor
      endCursor
      hasNextPage
      hasPreviousPage
    }
    edges {
      node {
        pk
        id
        endpoint
      }
    }
  }
}
    `;

/**
 * __usePostSetQuery__
 *
 * To run a query within a React component, call `usePostSetQuery` and pass it any options that fit your needs.
 * When your component renders, `usePostSetQuery` returns an object from Apollo Client that contains loading, error, and data properties
 * you can use to render your UI.
 *
 * @param baseOptions options that will be passed into the query, supported options are listed on: https://www.apollographql.com/docs/react/api/react-hooks/#options;
 *
 * @example
 * const { data, loading, error } = usePostSetQuery({
 *   variables: {
 *      first: // value for 'first'
 *      after: // value for 'after'
 *      before: // value for 'before'
 *   },
 * });
 */
export function usePostSetQuery(baseOptions?: ApolloReactHooks.QueryHookOptions<PostSetQuery, PostSetQueryVariables>) {
        return ApolloReactHooks.useQuery<PostSetQuery, PostSetQueryVariables>(PostSetDocument, baseOptions);
      }
export function usePostSetLazyQuery(baseOptions?: ApolloReactHooks.LazyQueryHookOptions<PostSetQuery, PostSetQueryVariables>) {
          return ApolloReactHooks.useLazyQuery<PostSetQuery, PostSetQueryVariables>(PostSetDocument, baseOptions);
        }
export type PostSetQueryHookResult = ReturnType<typeof usePostSetQuery>;
export type PostSetLazyQueryHookResult = ReturnType<typeof usePostSetLazyQuery>;
export type PostSetQueryResult = ApolloReactCommon.QueryResult<PostSetQuery, PostSetQueryVariables>;