import hargrave

def test_root_json_write():
    #Here we're making sure that the root json creation functionality.
    write_json(hargrave_conf.ROOT_JSON_FILE, ["test":"a"])
    assert read_json(hargrave_conf.ROOT_JSON_FILE)["test"] == "a"
    
