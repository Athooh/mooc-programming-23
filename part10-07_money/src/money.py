# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self._euros = euros
        self._cents = cents

    def __str__(self):
        if self._cents < 10:
            self._cents = str(0) + str(self._cents)
        return f"{self._euros}.{self._cents} eur"

    def __eq__(self, another):
        return self._euros == another._euros and self._cents == another._cents

    def __lt__(self, another):
        if self._euros == another._euros:
            return self._cents < another._cents
        return self._euros < another._euros
    
    def __gt__(self, another):
        if self._euros == another._euros:
            return self._cents > another._cents
        return self._euros > another._euros
    
    def __ne__(self, another):
        return not self.__eq__(another)
    
    def __sub__(self, another):
        result_euros = self._euros - another._euros
        result_cents = self._cents - another._cents

        if result_cents < 0:
            result_euros -= 1
            result_cents += 100

        if result_euros < 0 or result_cents < 0:
            raise ValueError("A negative result is not allowed")

        return Money(result_euros, result_cents)

    def __add__(self, another):
        result_euros = self._euros + another._euros
        result_cents = self._cents + another._cents

        if result_cents >= 100:
            result_euros += 1
            result_cents -= 100

        return Money(result_euros, result_cents)

if __name__ == "__main__":
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2-e1
