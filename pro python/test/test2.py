import unittest

from YaUpload import YaUpload

class TestYaUpload(unittest.TestCase):
    def setUp(self) -> None:
        token = "AQAAAAAPQM_IAADLW2dT7_OrREV9k4loMsl7wxM"
        self.obj = YaUpload(token)
    
    def tearDown(self) -> None:
        return super().tearDown()

    def test_upload_dir(self):
        path_to_dir = "yaUpload"
        self.assertIn(str(self.obj.upload_dir(path_to_dir)),["<Response [201]>", "<Response [409]>"])

    if __name__ == "__main__":
        unittest.main()

