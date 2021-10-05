from gendiff.parsers import PARSERS as FORMATS


def get_file(file_path):
    return open(file_path, 'r')


def get_extension(file_path):
    file_name = file_path.split('/')[-1]
    file_format = file_name.split('.')[-1]
    supported = ', '.join(FORMATS)
    message = 'File {n} has wrong format: {f}. Supported formats: {sup}'.format  # noqa: E501
    if file_format not in FORMATS:
        raise RuntimeError(message(
            n=file_name,
            f=file_format,
            sup=supported,
        ))
    return file_format


def data_and_format(source, data=get_file, data_format=get_extension):
    return data(source), data_format(source)
