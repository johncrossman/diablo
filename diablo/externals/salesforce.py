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

from diablo import BASE_DIR, cachify
from flask import current_app as app
from simple_salesforce import Salesforce


@cachify('salesforce_capture_enabled_rooms')
def get_capture_enabled_rooms():
    sf = Salesforce(
        username=app.config['SALESFORCE_USERNAME'],
        password=app.config['SALESFORCE_PASSWORD'],
        domain=app.config['SALESFORCE_DOMAIN'],
        security_token=app.config['SALESFORCE_TOKEN'],
    )

    with open(f'{BASE_DIR}/diablo/soql/get_all_rooms.soql', 'r') as file:
        rooms = []
        result = sf.query(file.read())
        for row in result['records']:
            rooms.append({
                'building': _translate_salesforce_building(row['Building__c']),
                'roomNumber': row['Room_Number_Text__c'],
                'capabilities': row['Recording_Capabilities__c'],
            })
        return rooms


def _translate_salesforce_building(building_name):
    return 'Genetics & Plant Bio' if building_name == 'GPB' else building_name