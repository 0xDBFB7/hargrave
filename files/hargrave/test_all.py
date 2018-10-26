import hargrave
import pytest
#hargrave_conf must be properly configured for this test to pass.
@pytest.fixture
def delete_settings():
    try:
        os.remove(hargrave_conf.SETTINGS_FILE)
    except:
        pass

#this test is kinda overloaded.
def test_settings(delete_settings):
    delete_settings()
    assert hargrave.get_settings()['project_rel_archive_dir'] == "sources"
    test = hargrave.get_settings()
    test['a'] = 5
    hargrave.write_settings()
    assert hargrave.get_settings()['project_rel_archive_dir'] == "sources"
    delete_settings()
