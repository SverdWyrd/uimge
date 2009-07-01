# -*- coding: utf-8 -*-
from base_host import test_host, findall
def test(host):
    if __name__ == '__main__':
        test_host( host)
@test
class Host_pu_pikucha:
    host='pikucha.ru'
    action = 'http://pikucha.ru/upload'
    form = {
            'MAX_FILE_SIZE':'10485760',
            'description':'on',
            'description_value':'uimge',
            'upload':'',
            'Submit': '',
            }

    def as_file(self, _file):
        return {'image': _file }
    def postload(self ):
        _src = self.get_src()
        _url = findall('\[img\]http://pikucha.ru/([\d]{4,10})/thumbnail/(.*?)\[/img\]',_src)[0]
        self.img_url = 'http://pikucha.ru/%s/%s'%_url
        self.img_thumb_url = 'http://pikucha.ru/%s/thumbnail/%s'%_url
