import hargrave
import hargrave_fs
import pytest
import os
import hargrave_conf

############Settings############
#hargrave_conf must be properly configured for this test to pass.
@pytest.fixture
def delete_settings():
    try:
        os.remove(hargrave_conf.SETTINGS_FILE)
    except:
        pass
    yield
    try:
        os.remove(hargrave_conf.ROOT_JSON_FILE)
    except:
        pass

#this test is quite overloaded.
def test_settings(delete_all):
    assert hargrave_fs.get_root_json()["settings"]['project_rel_archive_dir'] == "sources"
    test = hargrave_fs.get_root_json()
    test["settings"]['a'] = 5
    hargrave_fs.write_root_json(test)
    assert hargrave_fs.get_settings()['a'] == 5
##########"New project" form######

def test_new_project_validation(delete_all):
    new_project_dict = {"display_name":"test","project_id":"test",
    "start_date":"2018-10-27 12:05 PM","author":"0xDBFB7"}
    assert hargrave.validate_project_form(new_project_dict) == 0
    new_project_dict = {"display_name":"test","project_id":"test",
    "start_date":"2018-10-27 12:05 PM","author":""}
    assert hargrave.validate_project_form(new_project_dict)["success"] == 0
