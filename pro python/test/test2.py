import unittest

from YaUpload import YaUpload

class TestYaUpload(unittest.TestCase):
    def setUp(self) -> None:
        token = ...
        self.obj = YaUpload(token)
    
    def tearDown(self) -> None:
        return super().tearDown()

    def test_upload_dir(self):
        path_to_dir = "yaUpload"
        self.assertEqual(str(self.obj.upload_dir(path_to_dir)),"<Response [201]>")

    if __name__ == "__main__":
        unittest.main()

