import unittest
import os
from nseinfo.parsing.NseScriptParser import NseScriptParser

CURR_DIR = os.path.dirname(os.path.realpath(__file__))

class TestParser(unittest.TestCase):
    def setUp(self):
        self.parser = NseScriptParser()

    def parse(self, data_file_name):
        with open(CURR_DIR + '/data/' + data_file_name) as data_file:
            return self.parser.parse(data_file_name, data_file.read())


    def test_parsing(self):
        script = self.parse('http-shellshock.nse')
        self.assertEquals(script.name, 'http-shellshock')
        self.assertEquals(script.short_description, 'Attempts to exploit the "shellshock" vulnerability (CVE-2014-6271 and CVE-2014-7169) in web applications.')
        self.assertEquals(set(script.categories), set(["exploit", "vuln", "intrusive"]))
        self.assertEquals(script.sample_usages, [
            'nmap -sV -p- --script http-shellshock <target>',
            'nmap -sV -p- --script http-shellshock --script-args uri=/cgi-bin/bin,cmd=ls <target>'
        ])

    def test_parsing2(self):
        script = self.parse('openvas-otp-brute.nse')
        self.assertEquals(script.full_description, 'Performs brute force password auditing against a OpenVAS vulnerability scanner daemon using the OTP 1.0 protocol.')

    def test_strips_html(self):
        script = self.parse('nfs-showmount.nse')
        self.assertEquals(script.short_description, 'Shows NFS exports, like the showmount -e command.')

    def test_parses_short_description_on_multiple_lines(self):
        script = self.parse('telnet-ntlm-info.nse')
        self.assertEquals(script.short_description, 'This script enumerates information from remote Microsoft Telnet services with NTLM authentication enabled.')

    def test_parses_description_alternative_format(self):
        script = self.parse('weblogic-t3-info.nse')
        self.assertEquals(script.short_description, 'Detect the T3 RMI protocol and Weblogic version')
        self.assertEquals(script.short_description, script.full_description)
"""
    def test_isupper(self):
        self.assertTrue('FOoO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
"""