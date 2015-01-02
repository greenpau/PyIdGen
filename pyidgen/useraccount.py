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
import string;
import hashlib;

class UserAccount:
    'Represents a computer user account'

    def __init__(self, uid_fname="John", uid_lname="Doe", uid_format="LLLLLFFN", pwd_length=7, pwd_complexity="High", email_format="F.L", uid=None, pwd=None):
        '''Initialize a person based on a provided criteria.'''

        self.FirstName   = uid_fname;
        self.LastName    = uid_lname;
        self.UIDFormat   = uid_format;
        self.EmailFormat = email_format;
        self.PWDLength   = pwd_length;
        self.PWDStrength = pwd_complexity;

        if uid is not None:
            self.uid = uid;
        else:
            self._get_uid();
        self._get_password();
        self._get_email();

    def _get_uid(self):
        '''Generate username and e-mail address'''

        name   = list(self.FirstName);
        family = list(self.LastName);
        x = 0; y = 0;
        uid_chars = [];
        for i in list(self.UIDFormat):
            if (i == 'L'):
                try:
                    family[x];
                    uid_chars.append(family[x]);
                    x += 1;
                    continue;
                except IndexError:
                    pass;

                try:
                    name[y]
                    uid_chars.append(name[y]);
                    y += 1;
                    continue;
                except IndexError:
                    pass;

                uid_chars.append(str(random.randint(0, 9)));

            if (i == 'F'):
                try:
                    name[y]
                    uid_chars.append(name[y]);
                    y += 1;
                    continue;
                except IndexError:
                    pass

                try:
                    family[x];
                    uid_chars.append(family[x]);
                    x += 1;
                    continue;
                except IndexError:
                    pass;

                uid_chars.append(str(random.randint(0, 9)));

            if (i == 'N'):
                uid_chars.append(str(random.randint(0, 9)));
        self.uid = ''.join(uid_chars).lower();
        return;

    def _get_password(self):
        '''Generate a password. Complexity Levels are:
           High = uppercase, lower case, digits and symbols
           Medium = uppercase, lower case, digits and equal to or greater than 8 chars long
           Low = uppercase, lower case, digits and less than 8 chars long
        '''
        chars_up  = string.ascii_uppercase;
        chars_low = string.ascii_lowercase;
        chars_dgt = string.digits;
        chars_sym = '~!@#$%^&*()_-+={}[]\|:;<>?/';
        if self.PWDStrength == 'High':
            chars = chars_up + chars_low + chars_dgt + chars_sym;
            if self.PWDLength < 8:
                self.PWDLength = random.randint(8, 20);
        elif self.PWDStrength == 'Medium':
            chars = chars_up + chars_low + chars_dgt;
            if self.PWDLength < 8:
                self.PWDLength = random.randint(8, 20);
        else:
            chars = chars_up + chars_low + chars_dgt;
        self.pwd  = ''.join(random.choice(chars) for _ in range(self.PWDLength));

        try:
            self.md5  = hashlib.md5(self.pwd).hexdigest();
        except:
            self.md5  = hashlib.md5(self.pwd.encode('utf-8')).hexdigest();

        try:
            self.sha1  = hashlib.sha1(self.pwd).hexdigest();
        except:
            self.sha1  = hashlib.sha1(self.pwd.encode('utf-8')).hexdigest();

        try:
            self.sha512  = hashlib.sha512(self.pwd).hexdigest();
        except:
            self.sha512  = hashlib.sha512(self.pwd.encode('utf-8')).hexdigest();

        return;

    def _get_email(self):
        '''Generate username and e-mail address'''
        email_domains = ['ymail.com','gmail.com','aol.com','icloud.com','outlook.com','hotmail.com'];
        if self.EmailFormat == 'F.L':
           self.email = self.FirstName.title() + "." + self.LastName.title() + "@" + random.choice(email_domains);
        elif self.EmailFormat == 'f.l':
           self.email = self.FirstName.lower() + "." + self.LastName.lower() + "@" + random.choice(email_domains);
        elif self.EmailFormat == 'U':
           self.email = self.uid.upper() + "@" + random.choice(email_domains);
        elif self.EmailFormat == 'u':
           self.email = self.uid.lower() + "@" + random.choice(email_domains);
        else:
           self.email = self.LastName + "." + self.FirstName + "@" + random.choice(email_domains);
        return;
