=======
PyIdGen
=======

Overview
--------

This library is used to generate random user profiles with Personally
Identifiable Information (PII).

``tests/test.py`` script generates user identities in the following way:

::

    $ python3 tests/test.py

The script generates random Personally Identifiable Information (PII):

::

    Personal Information:
            First Name:     Vickey
            Middle Name:    Kasi
            Last Name:      Macbeth
            Middle Initial: K.
            Full Name:      Vickey Macbeth
            Age:            67
            DOB:            10/05/1946
            Sex:            Female
            Height:         4'1"
            Hair Color:     WHI
            Eye Color:      BLK

    Postal Address:
            7648 Gilgorm Road
            New York, NY 10005

    SSN# 529-80-2145, issued in UT

    Driver's License Information:
            ID:       865 244 023
            State:    NY
            Class:    D
            Issued:   01/01/1970
            Expires:  12/12/2018

    Computer Account Information:
            User ID:           macbevi5
            E-mail Address:    vickey.macbeth@ymail.com
            Password (clear):  L1XiNGv%
            Password (md5):    eaa14653852fe8ab0f18483d0bfdba26
            Password (sha1):   ab6b86e59f1ea4fabf0a9bd744e57107d892becb
            Password (sha512): 5a935814572e8c940a0359f3b1e7538e20bb45deb4a7ce747c43c4e0fcefda
                           40b302a0eb444feb85bc35737d90aab8fd1149e5ebe5450893d7ff63c77456ab28

    Contact Information:
            Phone Number: (563) 035-3637
                    Type:       VoIP
                    State:      IA
                    Identifier: Business
            Phone Number: (515) 457-4100
                    Type:       Cellular
                    State:      IA
                    Identifier: Business
            Phone Number: 712.288.9759
                    Type:       Cellular
                    State:      IA
                    Identifier: Home
            Phone Number: (319) 411-4461
                    Type:       Cellular
                    State:      IA
                    Identifier: Fax

    Credit Cards:
            Number: 4485 4270 6121 5902
                    Issuer:   Visa
                    Code:     020 (CCV2)
                    Expires : 12/2017
            Number: 4485 4270 6121 5902
                    Issuer:   Visa
                    Code:     020 (CCV2)
                    Expires : 12/2017
            Number: 4485 4270 6121 5902
                    Issuer:   Visa
                    Code:     020 (CCV2)
                    Expires : 12/2017
            Number: 4485 4270 6121 5902
                    Issuer:   Visa
                    Code:     020 (CCV2)
                    Expires : 12/2017

Classes
-------

PostalAddress
~~~~~~~~~~~~~

A developer may generate a random U.S. postal address, or may choose to
specify extra parameters, e.g. state, city, county, or zipcode. However,
the street address in ``PostalAddress()`` class will unlikely match a
real address from that zipcode or city, because the address generation
does not rely on a geo-location service of any kind.

::

    from pyidgen import PostalAddress;
    from string import Template;

    def main():
        a = PostalAddress();
        if a.Address2 == '':
            template = "{0}\n{2}, {3} {4}";
        else:
            template = "{0}\n{1}\n{2}, {3} {4}";
        print(template.format(a.Address1, a.Address2, a.City, a.State, a.ZipCode));

    if __name__ == '__main__':
        main();

There are a few ways to create ``PostalAddress()`` object:

::

    a = PostalAddress();
    a = PostalAddress(zip="11364");
    a = PostalAddress(county="Queens");
    a = PostalAddress(county="Queens",zip="11363");
    a = PostalAddress(state="NY");
    a = PostalAddress("11364");
    a = PostalAddress("11364", None, "Queens", "NY");
    a = PostalAddress(None, None, "Queens", None);
    a = PostalAddress(None, None, None, "NY");

The expected output is:

::

    9205 Shadow Lake Dr
    Oakland Gardens, NY 11364

    4957 Robert J Miller Air Park
    Oakland Gardens, NY 11364

    4485 Greenhill Dr
    Suite 919
    Truxton, NY 13158

    8731 County Route 17/2
    Arverne, NY 11692

    8463 Westmont Rd
    Jamaica, NY 11451

