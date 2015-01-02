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

class DriverLicense:
    'Represents a State issued driver license'

    def __init__(self, id_state=None, id_class=None, id_issued=None, id_expires=None):
        '''Initialize'''
        self.Id = '';        
        for i in range(9):
            if i in [3,6]:
                self.Id += ' ';
            self.Id += str(random.randint(0,9));
        self.State   = 'NY';
        self.Class   = 'D';
        #today = datetime.date.today();
        #self.DOB = datetime.date(today.year - self.Age, today.month - random.randint(0, today.month - 1), today.day - random.randint(0, today.day - 1)).strftime("%m/%d/%Y");
        self.Issued  = '01/01/1970';
        self.Expires = '12/12/2018';
        return;
