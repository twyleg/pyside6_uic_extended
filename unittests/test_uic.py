# Copyright (C) 2023, twyleg
import unittest
import tempfile
import shutil
import os
from pathlib import Path
from pyside6_uic_extended.uic import compile

#
# Reminder - General naming convention for unit tests:
#               test_INITIALSTATE_ACTION_EXPECTATION
#


class CompileUiFiles(unittest.TestCase):
    def prepare_input_files(self) -> Path:
        current_dir = Path('.')
        working_dir = Path(tempfile.mkdtemp())
        working_dir_sub1 = working_dir / 'sub1'
        working_dir_sub2 = working_dir / 'sub1' / 'sub2'
        os.makedirs(working_dir_sub2)

        shutil.copy(current_dir / 'resources' / 'test1.ui', working_dir)
        shutil.copy(current_dir / 'resources' / 'test2.ui', working_dir)
        shutil.copy(current_dir / 'resources' / 'test3.ui', working_dir_sub1)
        shutil.copy(current_dir / 'resources' / 'test4.ui', working_dir_sub2)
        shutil.copy(current_dir / 'resources' / 'test5.ui', working_dir_sub2)
        return working_dir

    def expect_output_file_with_class_name(self, file_path: Path, class_name: str) -> None:
        self.assertTrue(os.path.exists(file_path))
        with open(file_path) as f:
            self.assertTrue(f'class {class_name}(object):' in f.read())

    def test_ExistingRecursiveInputFile_CompileNonRecursive_PyFilesGenerated(self):
        working_dir = self.prepare_input_files()
        compile(working_dir, False)
        self.expect_output_file_with_class_name(working_dir / 'test1.py', 'Ui_Test1')
        self.expect_output_file_with_class_name(working_dir / 'test2.py', 'Ui_Test2')

    def test_ExistingRecursiveInputFile_CompileRecursive_PyFilesGenerated(self):
        working_dir = self.prepare_input_files()
        compile(working_dir, True)
        self.expect_output_file_with_class_name(working_dir / 'test1.py', 'Ui_Test1')
        self.expect_output_file_with_class_name(working_dir / 'test2.py', 'Ui_Test2')
        self.expect_output_file_with_class_name(working_dir / 'sub1/test3.py', 'Ui_Test3')
        self.expect_output_file_with_class_name(working_dir / 'sub1/sub2/test4.py', 'Ui_Test4')
        self.expect_output_file_with_class_name(working_dir / 'sub1/sub2/test5.py', 'Ui_Test5')


if __name__ == '__main__':
    unittest.main()
