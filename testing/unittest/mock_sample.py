# -*- coding: utf-8 -*-

try:
    from unittest import mock
except ImportError:
    import mock

mock_obj = mock.Mock(return_value=100)

print mock_obj()
print mock_obj

mock_obj.name = 'テスト 太郎'
print mock_obj.name


