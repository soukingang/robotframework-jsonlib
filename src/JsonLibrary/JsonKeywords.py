import demjson
import paramiko
import os
import robot
from robot.libraries.BuiltIn import BuiltIn


class JsonKeywords(object):
    ROBOT_LIBRARY_SCOPE = 'Global'

    def __init__(self):
        self._cache = robot.utils.ConnectionCache('Nothing')
        self.builtin = BuiltIn()

    def _decode_file(self, file):
        if os.path.isfile(file):
            return demjson.decode_file(filename)
        
    def _encode_to_file(self, json, file, ow=True):
        if os.path.isfile(file):
            return demjson._encode_to_file(json,file,overwrite=ow)

    def _insert_row(self, key, value, file):
        mjson = self._decode_file(file)
        mjson[key] = value
        self._encode_to_file(mjson, file)

    def _clear_value(self, key, file):
        mjson = self._decode_file(file)
        mjson[key] = ''
        self._encode_to_file(mjson, file)

    def insert_ip(self, value, file):
        self._insert_row('ipv4', value, file)

    def insert_url(self, value, file):
        self._insert_row('url', value, file)

    def insert_domain(self, value, file):
        self._insert_row('domain', value, file)

    def clear_ip(self, file):
        self._clear_value('ipv4', file)

    def clear_url(self, file):
        self._clear_value('url', file)

    def clear_domain(self, file):
        self._clear_value('domain', file)

    def upload_files(self, ip, uname, passwd, remote_dir):
        local_dir = r'./conf/'
        t = paramiko.Transport((ip,22))
        t.connect(username=uname,password=passwd)
        sftp=paramiko.SFTPClient.from_transport(t)
        files=os.listdir(local_dir)
        print files
        for f in files:
            print 'Uploading ',os.path.join(local_dir,f)
            sftp.put(os.path.join(local_dir,f),os.path.join(remote_dir,f))
        t.close()
