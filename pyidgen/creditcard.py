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

class CreditCard:
    'Represents random credit card'

    def __init__(self, issuer=None):
        '''Initialize'''

        ccs = {   'American Express': { 'Code':   "CID",
                                        'Format': "NNNN"
                                      },
                  'Diners Club':      { 'Code':   "Security Code",
                                        'Format': "NNN",
                                        'Number': "36NN-NNNNNN-NNNN"
                                      },
                  'Discover':         { 'Code':   "CID",
                                        'Format': "NNN"
                                      },
                  'JCB':              { 'Code':   "WRONG",
                                        'Format': "NNN"
                                      },
                  'Mastercard':       { 'Code':   "CVC2",
                                        'Format': "NNN"
                                      },
                  'Visa':             { 'Code':   "CVV2",
                                        'Format': "NNN"
                                      }
        };



        self.Number      = "4485 4270 6121 5902";
        self.Issuer      = "Visa";
        self.Code        = "020"; 
        self.CodeName    = "CCV2";
        self.ExpireMonth = "12";
        self.ExpireYear  = "2017";
        return;

