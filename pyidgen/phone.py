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

import random;

class Phone:
    'Represents random telephone number'

    def __init__(self, plan="NANP", state=None, type=None, ident=None, format="(AAA) NNN-NNNN"):
        '''Initialize the North American Numbering Plan (NANP)'''

        areas = {'AK': ['907'],
           'AL': ['205', '251', '256', '334', '659', '938'],
           'AR': ['327', '479', '501', '870'],
           'AS': ['684'],
           'AZ': ['480', '520', '602', '623', '928'],
           'CA': ['209', '213', '310', '323', '408', '415', '424', '442', '510', '530', '559', '562', '619', '626', '650', '657', '661', '669', '707', '714', '747', '760', '805', '818', '831', '858', '909', '916', '925', '949', '951'],
           'CO': ['303', '719', '720', '970'],
           'CT': ['203', '475', '860', '959'],
           'DC': ['202'],
           'DE': ['302'],
           'FL': ['239', '305', '321', '352', '386', '407', '561', '689', '727', '754', '772', '786', '813', '850', '863', '904', '941', '954'],
           'GA': ['229', '404', '470', '478', '678', '706', '762', '770', '912'],
           'GU': ['671'],
           'HI': ['808'],
           'IA': ['319', '515', '563', '641', '712'],
           'ID': ['208'],
           'IL': ['217', '224', '309', '312', '331', '447', '464', '618', '630', '708', '730', '773', '779', '815', '847', '872'],
           'IN': ['219', '260', '317', '574', '765', '812'],
           'KS': ['316', '620', '785', '913'],
           'KY': ['270', '364', '502', '606', '859'],
           'LA': ['225', '318', '337', '504', '985'],
           'MA': ['339', '351', '413', '508', '617', '774', '781', '857', '978'],
           'MD': ['227', '240', '301', '410', '443', '667'],
           'ME': ['207'],
           'MI': ['231', '248', '269', '313', '517', '586', '616', '679', '734', '810', '906', '947', '989'],
           'MN': ['218', '320', '507', '612', '651', '763', '952'],
           'MO': ['314', '417', '557', '573', '636', '660', '816', '975'],
           'MS': ['228', '601', '662', '769'],
           'MT': ['406'],
           'NC': ['252', '336', '704', '828', '910', '919', '980', '984'],
           'ND': ['701'],
           'NE': ['308', '402', '531'],
           'NH': ['603'],
           'NJ': ['201', '551', '609', '732', '848', '856', '862', '908', '973'],
           'NM': ['505', '575'],
           'NV': ['702', '725', '775'],
           'NY': ['212', '315', '347', '516', '518', '585', '607', '631', '646', '716', '718', '845', '914', '917', '929'],
           'OH': ['216', '234', '283', '330', '380', '419', '440', '513', '567', '614', '740', '937'],
           'OK': ['405', '539', '580', '918'],
           'OR': ['458', '503', '541', '971'],
           'PA': ['215', '267', '272', '412', '484', '570', '610', '717', '724', '814', '878'],
           'RI': ['401'],
           'SC': ['803', '843', '864'],
           'SD': ['605'],
           'TN': ['423', '615', '731', '865', '901', '931'],
           'TX': ['210', '214', '254', '281', '325', '361', '409', '430', '432', '469', '512', '682', '713', '737', '806', '817', '830', '832', '903', '915', '936', '940', '956', '972', '979'],
           'UT': ['385', '435', '801'],
           'VA': ['276', '434', '540', '571', '703', '757', '804'],
           'VT': ['802'],
           'WA': ['206', '253', '360', '425', '509', '564'],
           'WI': ['262', '274', '414', '534', '608', '715', '920'],
           'WV': ['304', '681'],
           'WY': ['307']};

        types  = ['Landline', 'Cellular', 'VoIP'];
        idents = ['Home', 'Cell', 'Business', 'Fax'];

        if state is not None:
            if state not in areas:
                state = None;
        if state is None:
            for x in areas.keys():
                state = x;
                break;
        self.State = state;
        v = [];
        for x in areas[state]:
            v.append(x);

        if type is None:
            self.Type = random.choice(types);
        else:
            self.Type = str(type);

        if ident is None:
            self.Identifier = random.choice(idents);
        else:
            self.Identifier = str(type);

        self.Number = '';
        for i in format:
            if i != 'N':
                self.Number += i;
            else:
                self.Number += str(random.randint(0,9));
        self.Number = self.Number.replace('AAA', random.choice(v));
        return;
