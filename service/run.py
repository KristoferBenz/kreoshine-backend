"""
Service running module
"""
import argparse
import json
import os.path
import sys
from pathlib import Path

from aiohttp import web

from service.app import create_app


def get_config_file(parser: argparse.ArgumentParser) -> str:
    """
    Gets configuration
    """
    project_root = str(Path(__file__).parent.parent.resolve())
    path_to_config = os.path.join(project_root, 'settings/config.json')
    parser.add_argument(
        '--config',
        help=f'configuration file {path_to_config}',
        type=str,
        default=path_to_config)

    args, _ = parser.parse_known_args()
    if not args.config:
        parser.print_usage()
        sys.exit(1)
    return args.config


if __name__ == '__main__':
    parser_ = argparse.ArgumentParser(description='kreoshine service')

    config_file = get_config_file(parser_)
    with open(config_file) as f:
        config = json.load(f)

    app_config = config['application']
    app = create_app(config=config)
    web.run_app(
        app,
        host=app_config.get('host'),
        port=app_config.get('port'),
        access_log_format=config.get('access_log_format')
    )
