#   PyIdGen - User Profile Generation Library for Quality Assurance and Information Security Testing
#   Copyright (C) 2013 Paul Greenberg <paul@greenberg.pro>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import random

class SSN:
    'Represents a Social Security Number'

    def __init__(self, state=None):
        '''Initialize SSN. Any number beginning with 000 will NEVER be a valid SSN.
           Group Numbers: from 01 through 99
           Serial Numbers: from 0001 through 9999
        '''

        areas = {'NH': '001-003', 'ME': '004-007', 'VT': '008-009', 'MA': '010-034',
                 'RI': '035-039', 'CT': '040-049', 'NY': '050-134', 'NJ': '135-158',
                 'PA': '159-211', 'MD': '212-220', 'DE': '221-222', 'VA': '223-231',
                 'NC': '232',     'WV': '232-236', 'SC': '247-251', 'GA': '252-260',
                 'FL': '261-267', 'OH': '268-302', 'IN': '303-317', 'IL': '318-361',
                 'MI': '362-386', 'WI': '387-399', 'KY': '400-407', 'TN': '408-415',
                 'AL': '416-424', 'MS': '425-428', 'AR': '429-432', 'LA': '433-439',
                 'OK': '440-448', 'TX': '449-467', 'MN': '468-477', 'IO': '478-485',
                 'MO': '486-500', 'ND': '501-502', 'SD': '503-504', 'NE': '505-508',
                 'KS': '509-515', 'MT': '516-517', 'ID': '518-519', 'WY': '520',
                 'CO': '521-524', 'NM': '525,585', 'AZ': '526-527', 'UT': '528-529',
                 'NV': '530,680', 'WA': '531-539', 'OR': '540-544', 'CA': '545-573',
                 'AK': '574',     'HI': '575-576', 'DC': '577-579', 'PR': '580-584',
                 'NOT_ISSUED': '750-772,587-665,667-679,681-690,691-699,237-246'
        };

        if state is not None:
            if state not in areas:
                state = None;

        if state is None:
            for x in areas.keys():
                state = x;
                break;

        v = [];
        x = areas[state];
        y = x.split(',')
        for i in y:
            if '-' in i:
                z = i.split('-');
                z1 = int(z[0].lstrip('0'));
                z2 = int(z[1].lstrip('0')) + 1;
                for j in range( z1, z2 ):
                    z3 = str(j).zfill(3);
                    v.append(z3);
            else:
                v.append(i);

        area       = random.choice(v);
        group      = str(random.randint(1,99));
        serial     = str(random.randint(1,9999));
        self.Id    = area + '-' + group.zfill(2) + '-' + serial.zfill(4);
        self.State = state;
        return;
