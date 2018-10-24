import hargrave

def test_root_json_write():
    write_json(hargrave_conf.ROOT_JSON_FILE, ["test":"a"])
    assert read_json(hargrave_conf.ROOT_JSON_FILE)["test"] == "a"
