
def open_in_file_browser(project_id):
    """
    Opens the specified project in the local system's default file browser.
    This is of course completely useless when used on a server, but
    in my specific use case it's pretty helpful.
    """
    subprocess.call(["xdg-open", hargrave_conf.PROJECTS_DIR + project_id])
