import abc

class Scanner(abc.ABC):
    def __init__(self, serial_number):
        self.serial_number = serial_number

    def scan_document(self):
        return 'the document has been scanned'
    
    @abc.abstractmethod
    def get_scanner_status(self):
        return { 'max_resolution': '', 'serial_number': self.serial_number }

class Printer(abc.ABC):
    def print_document(self):
        return 'the document has been printed'
    
    @abc.abstractmethod
    def get_printer_status(self):
        return { 'max_resolution': '', 'serial_number': self.serial_number }

class MFD1(Scanner, Printer):
    def get_scanner_status(self):
        return { 'max_resolution': 'low', 'serial_number': self.serial_number }

    def get_printer_status(self):
        return { 'max_resolution': 'low', 'serial_number': self.serial_number }

class MFD2(Scanner, Printer):
    def get_scanner_status(self):
        return { 'max_resolution': 'high', 'serial_number': self.serial_number }

    def get_printer_status(self):
        return { 'max_resolution': 'high', 'serial_number': self.serial_number }
    
    def printing_operation_history(self):
        print('printing operation history')

class MFD3(MFD2):
    def fax_machine(self):
        print('fax machine')

mfd1 = MFD1(1)
print(mfd1.get_printer_status())
print(mfd1.get_scanner_status())
print(mfd1.print_document())
print(mfd1.scan_document())
print('===============')

mfd2 = MFD2(2)
print(mfd2.get_printer_status())
print(mfd2.get_scanner_status())
print(mfd2.print_document())
print(mfd2.scan_document())
mfd2.printing_operation_history()
print('===============')

mfd3 = MFD3(3)
print(mfd3.get_printer_status())
print(mfd3.get_scanner_status())
print(mfd3.print_document())
print(mfd3.scan_document())
mfd2.printing_operation_history()
mfd3.fax_machine()