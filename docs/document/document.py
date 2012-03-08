"""Base class for a document object

Examples
--------

### Ex 1. Constructing a document

    >>> document = Document(name='file', file_name='file.py', 42)
    >>> document.filename
    'file.py'
    >>>
"""
import codecs
import os

__author__ = ['Michael Van Veen (michael@mvanveen.net)']


class Document(object):
  """Base class for a document object"""

  #TODO: property for python path
  _doc_type = 'doc'
  def __init__(self, name=None, filename=None, line_no=None, source=None,
              _type=None, doc_type=None, *args, **kw):

    super(Document, self).__init__(*args, **kw)
    self._line_no  = int(line_no) if line_no else None
    self._filename = self._get_filename(filename, name)
    self._name = self._get_name(filename, name)
    self._type = _type

    self._source = self._get_source(source)


  def _get_filename(self, filename, name):
    """Private method called by constructor to setup filename"""
    if filename:
      return str(filename)

    elif name:
      return os.path.abspath(
        os.path.join(os.getcwd(), '.'.join((name,'py')))
      )


  def _get_name(self, filename, name):
    """Private method called by constructor to setup name"""
    if name:
      #TODO: custom exception
      return unicode(name)

    elif filename:
      file_tuple = os.path.splitext(os.path.split(filename)[-1])
      #TODO: handle conversion from python path str to filestr
      return file_tuple[0]


  def _get_source(self, source):
    """Private method called by constructor to setup name"""
    if source:
      return unicode(source)

    elif self._filename is not None:
      with self.open('r') as file_obj:
        return file_obj.read()


  @property
  def filename(self):
    """Represents the filename for a document"""
    # TODO: make sure it's not a python path
    if self._filename:
      return os.path.relpath(self._filename)
    else:
      return None


  @property
  def name(self):
    """Represents an identifier for a document"""
    return self._name


  @property
  def source(self):
    """Represents the source code for a document"""
    return self._source


  @property
  def line_no(self):
    """A string representing the line_no of a document"""
    print self._line_no
    return os.path.relpath(self._line_no)


  @property
  def source(self):
    """Returns source code for a document
    """
    return self._source


  @property
  def line_no(self):
    return self._line_no


  def open(self, *args, **kw):
    """Returns a file object of the file name.

    >>> document = Document('file', 'file.py')
    >>> with document.open('r') as file_obj:
    >>>   assert file_obj.read()
    >>>
    """
    if not kw.has_key('encoding'):
      kw['encoding'] = 'utf-8'

    #TODO: make exception
    assert self.filename

    return codecs.open(self.filename, *args, **kw)


  def __repr__(self, *args, **kw):
    doc_type = 'doc'
    if self._type:
      doc_type = self._doc_type

    return '<[%s] %s>' % (doc_type, self._name)