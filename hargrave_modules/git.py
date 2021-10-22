
def check_git_status(input_dir):
    """
    A convienience function to see if the input directory is a git repo.
    Returns 0 if input is not inside a repo.
    """
    cmd = ['git', 'status']
    p = subprocess.Popen(cmd, cwd=input_dir)
    p.wait()
    return p.returncode == 0

def run_command(cmd,input_dir):
    """
    Another git convienience function, this time just running
    an arbitrary command in an arbitrary location and waiting until quit.
    """
    p = subprocess.Popen(cmd, cwd=input_dir,stdout=subprocess.PIPE)
    out, err = p.communicate()
    return out
