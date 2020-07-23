# GraphQL Sample with Wordpress database

## Wordpress

~~~bash
$ anyenv install phpenv
$ phpenv install 7.3.17
$ phpenv global 7.3.17
~~~

~~~bash
$ vi $(phpenv prefix)/etc/php.ini
~~~

~~~ini
pdo_mysql.default_socket= /var/run/mysqld/mysqld.sock
mysqli.default_socket = /var/run/mysqld/mysqld.sock
~~~


~~~bash
$ curl -o bin/wp-cli.phar https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar 
$ chmod +x bin/wp-cli.phar
$ mkdir -p wordpress
$ bin/wp-cli.phar core download  --locale=ja --path=$PWD/wordpress/sample
~~~

~~~bash
$ cp server/wordpress/wp-config.php wordpress/sample
~~~

~~~bash
$ bin/wp-cli.phar server --host=0.0.0.0 --port=9100 --path=$PWD/wordpress/sample --url=http://ubn1804:9100/ --debug
~~~

## React

~~~bash
$ echo yarn >> $NODENV_ROOT/default-packages
$ nodenv install 13.11.0
$ nodenv global 13.11.0
$ npm uninstall -g create-react-app && npm install -g create-react-app
~~~

## GraphQL

~~~zsh
% npm install --save graphql
% npm install --save-dev @graphql-codegen/cli -g
% npm install --save-dev @graphql-codegen/typescript
% npm install --save-dev @graphql-codegen/typescript-operations
% npm install --save-dev @graphql-codegen/typescript-react-apollo
~~~

`graphql/index.tsx` の生成:

~~~zsh
% npm run gen:graphql
~~~

## Apollo

~~~zsh
% npm install @apollo/client graphql --save-dev
% npm install @apollo/react-common @apollo/react-hooks --save-dev
~~~