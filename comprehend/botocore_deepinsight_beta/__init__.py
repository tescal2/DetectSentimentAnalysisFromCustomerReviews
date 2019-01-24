import os


def setup_aws_data_path(envroot=None):
    """Sets up the AWS_DATA_PATH environment variable to find the deepinsight models.
        Should automatically locate proper path for code running in:
            Deployed Apollo Environment
            brazil-runtime-exec
        If no envroot is supplied and not running in Brazil or Apollo (for ex, if running in Glue or Lambda Python script), the current directory is used.

    :param str envroot: Directory containing deepinsight models directory
    """
    if envroot is None:
        apollo_root = os.environ.get('ENVROOT', None)
        brazil_home = os.environ.get('BRAZIL_BUILD_HOME', None)
        if apollo_root is not None:
            envroot = apollo_root
        elif brazil_home is not None:
            path_vals = os.environ.get('PATH').split(':')
            brazil_bin = None
            for path in path_vals:
                if path.endswith('runtime/bin') and '/env/' in path:
                    brazil_bin = path
                    break
            if brazil_bin is None:
                raise Exception('Running in Brazil environment and unable to determine env runtime')
            envroot = brazil_bin.rsplit(os.sep, 1)[0]
        else:
            envroot = os.getcwd()
    aws_data_path = set(os.environ.get('AWS_DATA_PATH', '').split(os.pathsep))
    aws_data_path.add(os.path.join(envroot, 'models'))
    os.environ.update({'AWS_DATA_PATH': os.pathsep.join(aws_data_path)})