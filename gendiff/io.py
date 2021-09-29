from gendiff.parsers import PARSERS as FORMATS


def get_file(file_path):
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
    file = open(file_path, 'r')
    return (file, file_format)
