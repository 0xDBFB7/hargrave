import hargrave
import hargrave_fs
import pytest
import os
import hargrave_conf

############Settings############
#hargrave_conf must be properly configured for this test to pass.
@pytest.fixture
def delete_root_json():
    try:
        os.remove(hargrave_conf.ROOT_JSON_FILE)
    except:
        pass
    yield
    try:
        os.remove(hargrave_conf.ROOT_JSON_FILE)
    except:
        pass

@pytest.fixture
def existing_project():
    try:
        os.remove(hargrave_conf.ROOT_JSON_FILE)
    except:
        pass
    yield
    try:
        os.remove(hargrave_conf.ROOT_JSON_FILE)
    except:
        pass


#this test is quite overloaded.
def test_root_json(delete_root_json):
    assert hargrave_fs.get_root_json()["settings"]['project_rel_archive_dir'] == "sources/"
    test = hargrave_fs.get_root_json()
    test["settings"]['a'] = 5
    hargrave_fs.write_root_json(test)
    assert hargrave_fs.get_root_json()["settings"]['a'] == 5

##########"New project" form######

def test_new_project_validation(delete_root_json):
    new_project_dict = {"display_name":"test","project_id":"test",
    "start_date":"2018-10-27 12:05 PM","author":"0xDBFB7"}
    assert hargrave.validate_project_form(new_project_dict) == 0

    new_project_dict = {"display_name":"test","project_id":"test",
    "start_date":"2018-10-27 12:05 PM","author":""}
    assert hargrave.validate_project_form(new_project_dict)["success"] == 0

##########Make sure that new projects can't overwrite old.######
def test_project_creation_existing():
