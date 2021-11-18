import unittest

class UnitTesting(unittest.TestCase):
    
    def test_symbol(self):
        self.assertTrue(self.isalpha())
        self.assertFalse(self.isalpha())

        self.assertEqual(TestCase.ispper())
        self.assertFalse(TestCase.ispper())

        if len(self) > 7 or len(self) < 1:
            return ValueError("A stock symbol must be a maximum of 7 characters and a minimium of 1.")
        

    def test_chart(self):
        self.assertTrue(self.isnumeric())
        self.assertFalse(self.isnumeric())

        if len(self) > 2 or len(self) < 1:
            return ValueError("Chart type must be either 1 or 2.")

    def test_time(self):
        self.assertTrue(self.isnumeric())
        self.assertFalse(self.isnumeric())

        if len(self) > 4 or len(self) < 1:
            return ValueError("Time series must be between 1 and 4.")

    def test_date(self):
        format = "%Y-%m-d"
        try:
            datetime.datetime.strptime(self, format)
            print("OK")
        except ValueError:
            print("Incorrect date string format.")

            
            
