import ctypes
class Array :
  def __init__( self, ukuran ):
    assert ukuran > 0, "array harus memiliki elemen sebanyak > 0"
    self.ukuran = ukuran
    PyArrayType = ctypes.py_object * ukuran
    self.anggota = PyArrayType()
    self.isidata( None )

  def getlength( self ):
    return self.ukuran

  def getitem( self, index ):
    assert index >= 0 and index < self.getlength(), "out of range"
    return self.anggota[ index ]

  def setitem( self, index, value ):
    assert index >= 0 and index < self.getlength(), "out of range" #ada perubahan
    self.anggota[index ] = value

  def isidata( self, value ):
    ukuran = self.getlength()
    for i in range(ukuran ) :
      self.anggota[i] = value

  def getMax(self):
    array_list = list(self.anggota)
    sorted_array = sorted(array_list)
    return sorted_array[-1]

  def cariposisi(self, val):
    new = []
    if self.anggota[val] > val:
      for i in range(self.getlength()):
        new.append(1)
      return new
    else:
      for i in range(self.getlength()):
        new.append(0)
      return new

objek = Array(10)
objek.isidata(10)
objek.setitem(2,8)
objek.setitem(4,100)
# objek.setitem(9,2)
objek.setitem(0,50)
print(objek.getitem(2))
print(objek.getitem(4))
print(objek.getitem(8))
print(objek.getitem(9))
print(objek.getMax())
print(objek.cariposisi(2))
# print(objek.cariposisi(9))