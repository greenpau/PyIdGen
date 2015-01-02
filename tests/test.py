#!/usr/bin/env python

#------------------------------------------------------------------------------------------#
# File:      tests.py                                                                      #
# Purpose:   User Profile Generation Tool                                                  #
#            for Quality Assurance and Information Security Testing                        #
# Author:    Paul Greenberg                                                                #
# Version:   1.0                                                                           #
# Copyright: (c) 2013 Paul Greenberg <paul@greenberg.pro>                                  #
# -----------------------------------------------------------------------------------------#

import sys;
if sys.version_info[0] < 3:
    sys.stderr.write('PyIdGen requires Python 3 or higher.\n')
    exit(1);

import argparse;
import pprint;
from pyidgen import Person, PostalAddress, SSN, DriverLicense, UserAccount, Phone, CreditCard;
from string import Template;

def main():
    func = 'main()';
    parser = argparse.ArgumentParser(description='QA/Security User Profile Generation Tool.');
    parser.add_argument('-f', '--first', dest='ifname', metavar='FIRST_NAME', type=str, help='First Name');
    parser.add_argument('-l', '--last',  dest='ilname', metavar='LAST_NAME',  type=str, help='Last Name');
    args = parser.parse_args();

    p = Person();
    template = "\tFirst Name:     {0}\n" + \
               "\tMiddle Name:    {1}\n" + \
               "\tLast Name:      {2}\n" + \
               "\tMiddle Initial: {3}\n" + \
               "\tFull Name:      {4}\n" + \
               "\tAge:            {5}\n" + \
               "\tDOB:            {6}\n" + \
               "\tSex:            {7}\n" + \
               "\tHeight:         {8}\n" + \
               "\tHair Color:     {9}\n" + \
               "\tEye Color:      {10}\n";
              
    print("Personal Information:");
    print(template.format(p.FirstName, p.MiddleName, p.LastName, p.MiddleInitial, p.FullName, p.Age, p.DOB, p.Sex, p.Height, p.Hair, p.Eyes));

    a = PostalAddress();
    #a = PostalAddress(zip="11364");
    #a = PostalAddress(county="Queens");
    #a = PostalAddress(county="Queens",zip="11363");
    #a = PostalAddress(state="NY");
    #a = PostalAddress("11364");
    #a = PostalAddress("11364", None, "Queens", "NY");
    #a = PostalAddress(None, None, "Queens", None);
    #a = PostalAddress(None, None, None, "NY");
    
    if a.Address2 == '':
        template = "\t{0}\n\t{2}, {3} {4}";
    else:
        template = "\t{0}\n\t{1}\n\t{2}, {3} {4}";
    print("Postal Address:");
    print(template.format(a.Address1, a.Address2, a.City, a.State, a.ZipCode));

    # s = SSN('AZ');
    #s = SSN(a.State);
    s = SSN();
    print("\nSSN# " + s.Id + ", issued in " + s.State);

    print("\nDriver's License Information:");
    dl = DriverLicense(a.State, 'A', '01/01/1950', '2y15d');
    template = "\tID:       {0}\n" + \
               "\tState:    {1}\n" + \
               "\tClass:    {2}\n" + \
               "\tIssued:   {3}\n" + \
               "\tExpires:  {4}";
    print(template.format(dl.Id, dl.State, dl.Class, dl.Issued, dl.Expires));
    
    #ua = UserAccount();
    #ua = UserAccount(p.FirstName, p.LastName);
    #ua = UserAccount(p.FirstName, p.LastName, "LLLLLFFF");
    #ua = UserAccount(p.FirstName, p.LastName, "LLLLLFFF", email_format="u");
    #ua = UserAccount(p.FirstName, p.LastName, "LLLLLFFF", email_format="U");
    #ua = UserAccount(p.FirstName, p.LastName, "LLLLLFFF", email_format="F.L");
    #ua = UserAccount(p.FirstName, p.LastName, "LLLLLFFF", email_format="f.l");
    ua = UserAccount(p.FirstName, p.LastName, "LLLLLFFN", email_format="f.l");
    print("\nComputer Account Information:");
    print("\tUser ID:           " + ua.uid);
    print("\tE-mail Address:    " + ua.email);
    print("\tPassword (clear):  " + ua.pwd);
    print("\tPassword (md5):    " + ua.md5);
    print("\tPassword (sha1):   " + ua.sha1);
    print("\tPassword (sha512): " + ua.sha512);

    print("\nContact Information:");
    template = "\tPhone Number: {0}\n" + \
               "\t\tType:       {1}\n" + \
               "\t\tState:      {2}\n" + \
               "\t\tIdentifier: {3}";
    ph = Phone(a.State);
    print(template.format(ph.Number, ph.Type, ph.State, ph.Identifier));
    ph = Phone('NY');
    print(template.format(ph.Number, ph.Type, ph.State, ph.Identifier));
    ph = Phone(format="AAA.NNN.NNNN");
    print(template.format(ph.Number, ph.Type, ph.State, ph.Identifier));
    ph = Phone();
    print(template.format(ph.Number, ph.Type, ph.State, ph.Identifier));    

    print("\nCredit Cards:");
    template = "\tNumber: {0}\n" + \
               "\t\tIssuer:   {1}\n" + \
               "\t\tCode:     {2} ({3})\n" + \
               "\t\tExpires : {4}/{5}";
    cc = CreditCard(); 
    print(template.format(cc.Number, cc.Issuer, cc.Code, cc.CodeName, cc.ExpireMonth, cc.ExpireYear));
    cc = CreditCard(); 
    print(template.format(cc.Number, cc.Issuer, cc.Code, cc.CodeName, cc.ExpireMonth, cc.ExpireYear));
    cc = CreditCard(); 
    print(template.format(cc.Number, cc.Issuer, cc.Code, cc.CodeName, cc.ExpireMonth, cc.ExpireYear));
    cc = CreditCard(); 
    print(template.format(cc.Number, cc.Issuer, cc.Code, cc.CodeName, cc.ExpireMonth, cc.ExpireYear));

    print("----------------------------------------------");
    return 0;



if __name__ == '__main__':
    main();
