from abc import ABC, abstractmethod

class PaymentMethod(ABC):

    @abstractmethod
    def Authenticate():
        pass
    
    @abstractmethod
    def pay(amount):
        pass

class CreditCardPayment(PaymentMethod):

    def Authenticate(self):
        print("\nAuthenticating Credit Card...")

    def pay(self, amount):
        print(f"Paying ₹{amount} using Credit Card.")
    

class UPIPayment(PaymentMethod):
    
    def Authenticate(self):
        print("\nAuthenticating via UPI")

    def pay(self, amount):
        print(f"Paying ₹{amount} using UPI")

if __name__ == "__main__":
    payment_method=input("Enter payment method (card/upi) ").strip().lower()
    amount=int(input("Enter amount to pay: ₹ "))

    try:
        amount=float(amount)

    except ValueError:
        print("Invalid amount entered.")
        exit()


    if(payment_method=='card'):
        payment=CreditCardPayment()

    elif(payment_method=='upi'):
        payment=UPIPayment()

    else:
        print("Unsupported payment method.")
        exit()

    payment.Authenticate()
    payment.pay(amount)
    print("✅ Transaction complete. Thank you!")





    