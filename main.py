class Calculation:
    @staticmethod
    def main(calcMode: str = "simple",
             is_display_every: bool = False):
        principal, annualInterestRate, year = Calculation.ask_info()

        def calc_function(year):
            if calcMode.lower() == "simple":
                return Calculation.calc_simple_interest(principal, annualInterestRate, year)
            elif calcMode.lower() == "compound":
                return Calculation.calc_compound_interest(principal, annualInterestRate, year)

        def displayResult(year):
            if is_display_every:
                for countYear in range(1, year + 1):
                    final_value = calc_function(countYear)
                    print(f"In year {countYear}, the deposit is {final_value} US dollars.")
            else:
                final_value = calc_function(year)
                print(f"Finally, after {year} year, you will get {final_value} US dollars.")

        displayResult(year)

    @staticmethod
    def ask_info():
        principal = float(input("Principal(By default, Unit: US$): "))
        annualInterestRate = float(input("The annual interest rate: "))
        year = int(input("How many years you want to deposit/loan: "))
        return (principal, annualInterestRate, year)

    @staticmethod
    def calc_simple_interest(principal: float,
                             annualInterestRate: float,
                             year: int):
        future_value = round(principal + (principal * annualInterestRate * year), 2)
        return future_value

    @staticmethod
    def calc_compound_interest(principal: float,
                               annualInterestRate: float,
                               year: int):
        future_value = round(principal * pow(1 + annualInterestRate, year), 2)
        return future_value


Calculation.main(is_display_every=True, calcMode="COMPOUND")
