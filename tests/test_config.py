import unittest

import pyconf


class ConfigNoneTestCase(unittest.TestCase):

    def setUp(self):
        self.obj = None
        self.config = pyconf.Config(self.obj)

    def tearDown(self):
        pass

    def test_call(self):
        self.assertEqual(self.config(), self.obj)

    def test_getitem(self):
        with self.assertRaises(TypeError):
            _ = self.config[0]
        with self.assertRaises(TypeError):
            _ = self.config['']

    def test_repr(self):
        self.assertEqual(repr(self.config), repr(self.obj))


class ConfigListTestCase(unittest.TestCase):

    def setUp(self):
        self.obj = ['zero',
                    'one',
                    'two',
                    [
                        "listelem1",
                        "listelem2",
                        3
                    ],
                    {
                        "setelem1",
                        "setelem2",
                        3
                    },
                    {
                        'zero': 0,
                        'one': 1,
                        'two': 2
                    }
                    ]
        self.config = pyconf.Config(self.obj)

    def tearDown(self):
        pass

    def test_call(self):
        self.assertEqual(self.config(), self.obj)
        self.assertEqual(self.config[5](), pyconf.Config(self.obj[5])())
        self.assertEqual(self.config[3](), pyconf.Config(self.obj[3])())
        self.assertEqual(self.config[4](), pyconf.Config(self.obj[4])())

    def test_getitem(self):
        self.assertEqual(self.config[0], self.obj[0])
        with self.assertRaises(TypeError):
            _ = self.config['']
        with self.assertRaises(IndexError):
            _ = self.config[len(self.obj)]

    def test_repr(self):
        self.assertEqual(repr(self.config), repr(self.obj))


class ConfigDictTestCase(unittest.TestCase):

    def setUp(self):
        self.obj = {'zero': 0,
                    'one': 1,
                    'two': 2,
                    'list': [
                        "listelem1",
                        "listelem2",
                        3
                    ],
                    'set': {
                        "setelem1",
                        "setelem2",
                        3
                    },
                    'dict': {
                        'zero': 0,
                        'one': 1,
                        'two': 2
                    }}
        self.config = pyconf.Config(self.obj)

    def tearDown(self):
        pass

    def test_call(self):
        self.assertEqual(self.config(), self.obj)
        self.assertEqual(self.config.dict(), pyconf.Config(self.obj['dict'])())
        self.assertEqual(self.config.list(), pyconf.Config(self.obj['list'])())
        self.assertEqual(self.config.set(), pyconf.Config(self.obj['set'])())

    def test_getitem(self):
        self.assertEqual(self.config['zero'], self.obj['zero'])
        self.assertEqual(self.config.zero, self.obj['zero'])
        with self.assertRaises(KeyError):
            _ = self.config[0]
        with self.assertRaises(KeyError):
            _ = self.config['non existent']

    def test_dir(self):
        for i in self.obj:
            self.assertIn(i, dir(self.config))

    def test_repr(self):
        self.assertEqual(repr(self.config), repr(self.obj))