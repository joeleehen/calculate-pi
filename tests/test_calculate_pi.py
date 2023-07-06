import os
import pytest
from click.testing import CliRunner

from calculate_pi import pi

RESPONSE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'responses')
VERSION = '0.1.0'


def get_response_text(response_file):
    with open(response_file) as f: response_content = f.read()
    return response_content


class TestCalculatePI(object):

    @pytest.fixture()
    def runner(self):
        return CliRunner()

    def test_print_help_succeeds(self, runner):
        response_text = get_response_text(os.path.join(RESPONSE_DIR, 'help.txt'))
        result = runner.invoke(pi.main, ['--help'])
        assert result.exit_code == 0
        assert result.output == response_text

    def test_print_version_succeeds(self, runner):
        version_string = 'version {}'.format(pi.VERSION)
        result = runner.invoke(pi.main, ['--version'])
        assert result.exit_code == 0
        assert version_string in result.output
