"""
Copyright ©2020. The Regents of the University of California (Regents). All Rights Reserved.

Permission to use, copy, modify, and distribute this software and its documentation
for educational, research, and not-for-profit purposes, without fee and without a
signed licensing agreement, is hereby granted, provided that the above copyright
notice, this paragraph and the following two paragraphs appear in all copies,
modifications, and distributions.

Contact The Office of Technology Licensing, UC Berkeley, 2150 Shattuck Avenue,
Suite 510, Berkeley, CA 94720-1620, (510) 643-7201, otl@berkeley.edu,
http://ipira.berkeley.edu/industry-info for commercial licensing opportunities.

IN NO EVENT SHALL REGENTS BE LIABLE TO ANY PARTY FOR DIRECT, INDIRECT, SPECIAL,
INCIDENTAL, OR CONSEQUENTIAL DAMAGES, INCLUDING LOST PROFITS, ARISING OUT OF
THE USE OF THIS SOFTWARE AND ITS DOCUMENTATION, EVEN IF REGENTS HAS BEEN ADVISED
OF THE POSSIBILITY OF SUCH DAMAGE.

REGENTS SPECIFICALLY DISCLAIMS ANY WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE
SOFTWARE AND ACCOMPANYING DOCUMENTATION, IF ANY, PROVIDED HEREUNDER IS PROVIDED
"AS IS". REGENTS HAS NO OBLIGATION TO PROVIDE MAINTENANCE, SUPPORT, UPDATES,
ENHANCEMENTS, OR MODIFICATIONS.
"""

import logging
import os

# Base directory for the application (one level up from this config file).
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

CAS_SERVER = 'https://auth-test.berkeley.edu/cas/'

DIABLO_SUPPORT_EMAIL = 'course-capture-help@berkeley.edu'

CACHE_DEFAULT_TIMEOUT = 86400
CACHE_DIR = f'{BASE_DIR}/.flask_cache'
CACHE_THRESHOLD = 300
CACHE_TYPE = 'filesystem'

CURRENT_TERM = 2202

# Loch o' Data
DATA_LOCH_RDS_URI = 'postgres://foo:secret@secret-rds-url.com:5432/data_loch'
DATA_LOCH_SIS_SCHEMA = 'sis_data'

DEVELOPER_AUTH_ENABLED = False
DEVELOPER_AUTH_PASSWORD = 'another secret'

# Directory to search for mock fixtures, if running in "test" or "demo" mode.
FIXTURES_PATH = None

# Minutes of inactivity before session cookie is destroyed
INACTIVE_SESSION_LIFETIME = 20

# These "INDEX_HTML" defaults are good in diablo-[dev|qa|prod]. See development.py for local configs.
INDEX_HTML = 'dist/static/index.html'

LDAP_HOST = 'ldap-test.berkeley.edu'
LDAP_BIND = 'mybind'
LDAP_PASSWORD = 'secret'

# Logging
LOGGING_FORMAT = '[%(asctime)s] - %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
LOGGING_LOCATION = 'diablo.log'
LOGGING_LEVEL = logging.DEBUG
LOGGING_PROPAGATION_LEVEL = logging.INFO

REMEMBER_COOKIE_NAME = 'remember_diablo_token'

SALESFORCE_USERNAME = ''
SALESFORCE_PASSWORD = ''
SALESFORCE_DOMAIN = ''
SALESFORCE_TOKEN = ''

# Used to encrypt session cookie.
SECRET_KEY = 'secret'

# Save DB changes at the end of a request.
SQLALCHEMY_COMMIT_ON_TEARDOWN = True

# Override in local configs.
SQLALCHEMY_DATABASE_URI = 'postgres://diablo:diablo@localhost:5432/diablo'

# Disable an expensive bit of the ORM.
SQLALCHEMY_TRACK_MODIFICATIONS = False

# A common configuration; one request thread, one background worker thread.
THREADS_PER_PAGE = 2

TIMEZONE = 'America/Los_Angeles'

# This base-URL config should only be non-None in the "local" env where the Vue front-end runs on port 8080.
VUE_LOCALHOST_BASE_URL = None

# We keep these out of alphabetical sort above for readability's sake.
HOST = '0.0.0.0'
PORT = 5000