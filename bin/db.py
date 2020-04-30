#!/usr/bin/env python
import click
import os
import re
import importlib.util

BIN = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(BIN)


def bin_file(name):
    return os.path.join(BIN, name)


def import_settings(path):
    spec = importlib.util.spec_from_file_location("local_settings", path)
    settings = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(settings)
    return settings


def wp_config_db(wp_config):
    p = re.compile(
            r'define[^\'"]*[\'"]'
            r'DB_(?P<key>[^\'"]*)[\'"]'
            r'[^\'"]*[\'"](?P<value>[^\'"]*)[\'"]', re.MULTILINE)
    with open(wp_config) as conf:
        source = conf.read()
        if ma := p.finditer(source):
            databases = {'default': dict([i.groups() for i in ma])}
            return type('conf', (object, ), {'DATABASES': databases})()

    return {}


@click.group()
@click.option('--settings', '-s', default=None)
@click.pass_context
def db(ctx, settings):
    settings = settings or os.path.join(BASE, 'web/app/local_settings.py')
    if settings.endswith('wp-config.php'):
        ctx.obj['settings'] = wp_config_db(settings)
    else:
        ctx.obj['settings'] = import_settings(settings)


@db.command()
@click.option('--database', '-d', default='default')
@click.pass_context
def createdb(ctx, database):
    settings = ctx.obj['settings']
    SCRIPT = '''CREATE DATABASE {NAME}
DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
GRANT ALL on {NAME}.*
to '{USER}'@'{HOST}'
identified by '{PASSWORD}' WITH GRANT OPTION; '''
    print(SCRIPT.format(**settings.DATABASES[database]))


@db.command()
@click.option('--database', '-d', default='default')
@click.pass_context
def dumpschema(ctx, database):
    settings = import_settings(ctx.obj['settings'])
    CMD = 'mysqldump -u {USER} --password={PASSWORD} -h {HOST} {NAME} -d'
    print(CMD.format(**settings.DATABASES[database]))


@db.command()
@click.option('--database', '-d', default='default')
@click.option('--table', '-t', default='', help="Table")
@click.pass_context
def dump(ctx, database, table):
    settings = import_settings(ctx.obj['settings'])
    options = [
        '-c',       # --complete-insert
        '--skip-extended-insert',
    ]
    opts = ' '.join(options)
    CMD = 'mysqldump {OPTS} -u {USER} --password={PASSWORD} -h {HOST} {NAME} {TABLE}'
    print(CMD.format(TABLE=table, OPTS=opts, **settings.DATABASES[database]))


@db.command()
@click.option('--database', '-d', default='default')
@click.option('--out', '-o', default=None, help="output directory")
@click.pass_context
def spy(ctx, database, out):
    # sudo apt-get install openjdk-8-jdk libmysql-java -y
    # UBUNTU    (TODO)
    CONNECTOR = "/usr/share/java/mysql-connector-java.jar"
    settings = import_settings(ctx.obj['settings'])
    OUT = out or settings.DATABASES[database]['NAME']
    JAR = bin_file('schemaspy.jar')
    SCRIPT = '''java -jar {JAR}  -t mysql -s {NAME} -o {OUT} -host {HOST} -db {NAME} -u {USER} -p {PASSWORD} -dp {CONNECTOR}'''
    click.echo(
        SCRIPT.format(JAR=JAR, CONNECTOR=CONNECTOR, OUT=OUT, **settings.DATABASES[database]))


if __name__ == '__main__':
    db(obj={})
