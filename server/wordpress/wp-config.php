<?php

/**
 * WordPress の基本設定
 *
 * このファイルは、インストール時に wp-config.php 作成ウィザードが利用します。
 * ウィザードを介さずにこのファイルを "wp-config.php" という名前でコピーして
 * 直接編集して値を入力してもかまいません。
 *
 * このファイルは、以下の設定を含みます。
 *
 * * MySQL 設定
 * * 秘密鍵
 * * データベーステーブル接頭辞
 * * ABSPATH
 *
 * @link http://wpdocs.osdn.jp/wp-config.php_%E3%81%AE%E7%B7%A8%E9%9B%86
 *
 * @package WordPress
 */

// 注意:
// Windows の "メモ帳" でこのファイルを編集しないでください !
// 問題なく使えるテキストエディタ
// (http://wpdocs.osdn.jp/%E7%94%A8%E8%AA%9E%E9%9B%86#.E3.83.86.E3.82.AD.E3.82.B9.E3.83.88.E3.82.A8.E3.83.87.E3.82.A3.E3.82.BF 参照)
// を使用し、必ず UTF-8 の BOM なし (UTF-8N) で保存してください。

// ** MySQL 設定 - この情報はホスティング先から入手してください。 ** //
/** WordPress のためのデータベース名 */
define('DB_NAME', 'wparticle');

/** MySQL データベースのユーザー名 */
define('DB_USER', 'wparticle');

/** MySQL データベースのパスワード */
define('DB_PASSWORD', 'wparticle');

/** MySQL のホスト名 */
define('DB_HOST', 'localhost');

/** データベースのテーブルを作成する際のデータベースの文字セット */
define('DB_CHARSET', 'utf8');

/** データベースの照合順序 (ほとんどの場合変更する必要はありません) */
define('DB_COLLATE', '');

/**#@+
 * 認証用ユニークキー
 *
 * それぞれを異なるユニーク (一意) な文字列に変更してください。
 * {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org の秘密鍵サービス} で自動生成することもできます。
 * 後でいつでも変更して、既存のすべての cookie を無効にできます。これにより、すべてのユーザーを強制的に再ログインさせることになります。
 *
 * @since 2.6.0
 */
define('AUTH_KEY',         'U.V^b|I (^BB#]-vDOr4(cvvcY/ZJDYQJ575Pcu=uX=1s~em,*vlv&.+@VxI#CV2');
define('SECURE_AUTH_KEY',  '8<Uv(xpy<-?v:i$LcO k:|@=ack1c#Rb=k4m 8YF/WY/c>SWF9SE6adv8!z$NY5l');
define('LOGGED_IN_KEY',    'eVH1^LqY3-EA%r+MM@B4^8f! Q]L;lVsMu@*kbT%fGy4S]2&(s @1h-3&Sk1sy|u');
define('NONCE_KEY',        'YZ%}++mW:_*[-.1.e[-5[^W.V>[|m|:!`%}@h;E+Ojq|F^4m1IWiIpSE=l>]!#rs');
define('AUTH_SALT',        '-9v*8:y>5l_h#rSzzion%5s{t-#-rpQ_C0ToPH#a1WB7z-rffbK?PS?PvR&-+/0k');
define('SECURE_AUTH_SALT', 'ko-f(~TS0Z:E(0,3vIXlrDDT^Rc+gc6^Ary5~y&[4j4vwM+4|mXk7sG3Bb~|aw+y');
define('LOGGED_IN_SALT',   '{(fhn!,Qu,OQ)Br;7p$?7h}|y}s / 945NEppw~1fT#%Q6CBi/u >M<TI6-UO10Z');
define('NONCE_SALT',       'tn:8`eA5-{|&9Q];UU@|LaS7Z[,K&v<PDy{ZAweS`F[amw+KnC De>Wl<]1Z21O&');

/**#@-*/

/**
 * WordPress データベーステーブルの接頭辞
 *
 * それぞれにユニーク (一意) な接頭辞を与えることで一つのデータベースに複数の WordPress を
 * インストールすることができます。半角英数字と下線のみを使用してください。
 */
$table_prefix = 'wp_';

/**
 * 開発者へ: WordPress デバッグモード
 *
 * この値を true にすると、開発中に注意 (notice) を表示します。
 * テーマおよびプラグインの開発者には、その開発環境においてこの WP_DEBUG を使用することを強く推奨します。
 *
 * その他のデバッグに利用できる定数については Codex をご覧ください。
 *
 * @link http://wpdocs.osdn.jp/WordPress%E3%81%A7%E3%81%AE%E3%83%87%E3%83%90%E3%83%83%E3%82%B0
 */
# define( 'WP_DEBUG', false );
define('WP_DEBUG', true);

# NOTE: wp-cli.phar .... --url=https://example.com/column
$HTTP_HOST =  $_SERVER['HTTP_HOST'];
$SCHEME = 'http';  # $SCHEME = 'https';

define('WP_SITEURL', $SCHEME . '://' . $HTTP_HOST . '/');
define('WP_HOME', $SCHEME . '://' . $HTTP_HOST . '/');

if (WP_DEBUG) {
    define('WP_DEBUG_LOG', true);     // debug.log ファイルに記録

    //define( 'WP_DEBUG_DISPLAY', false ); //ブラウザ上に表示しない
    //@ini_set( 'display_errors',0 ); 	// ブラウザ上に表示しない
}

/* 編集が必要なのはここまでです ! WordPress でのパブリッシングをお楽しみください。 */

/** Absolute path to the WordPress directory. */
if (!defined('ABSPATH')) {
    define('ABSPATH', dirname(__FILE__) . '/');
}

/** Sets up WordPress vars and included files. */
require_once(ABSPATH . 'wp-settings.php');