"""
    1. Complete the `MiniVenmo.create_user()` method to allow our application to create new users.

    2. Complete the `User.pay()` method to allow users to pay each other. Consider the following: if user A is paying
     user B, user's A balance should be used if there's enough balance to cover the whole payment, if not, user's A
     credit card should be charged instead.

    3. Venmo has the Feed functionality, that shows the payments that users have been doing in the app. If Bobby paid
    Carol $5, and then Carol paid Bobby $15, it should look something like this

    Bobby paid Carol $5.00 for Coffee
    Carol paid Bobby $15.00 for Lunch

    Implement `MiniVenmo.render_feed()` method so the MiniVenmo application can render the feed.


    4. Now users should be able to add friends. Implement the `User.add_friend()` method to allow users to add friends.

    5. Now modify the methods involved in rendering the feed to also show when user's added each other as friends.

    Note: you should implement the Unit Tests in order to check that your code is working

"""

import uuid
import unittest
import re


class UsernameException(Exception):
    pass


class PaymentException(Exception):
    pass


class CreditCardException(Exception):
    pass


class Payment:

    def __init__(self, amount, actor, target, note):
        self.id = str(uuid.uuid4())
        self.amount = float(amount)
        self.actor = actor
        self.target = target
        self.note = note


class User:

    def __init__(self, username):
        self.credit_card_number = None
        self.balance = 0.0
        self._payments = []
        self._friends = []

        if self._is_valid_username(username):
            self.username = username
        else:
            raise UsernameException('Username not valid.')

    def retrieve_feed(self):
        feed = []
        for payment in self._payments:
            # Bobby paid Carol $5.00 for Coffee
            feed.append(f"{self.username} paid {payment.target.username} {payment.amount} for {payment.note}")
        return feed

    def add_friend(self, new_friend):
        # TODO: add code here
        self._friends.append(new_friend)

    def add_to_balance(self, amount):
        self.balance += float(amount)

    def add_credit_card(self, credit_card_number):
        if self.credit_card_number is not None:
            raise CreditCardException('Only one credit card per user!')

        if self._is_valid_credit_card(credit_card_number):
            self.credit_card_number = credit_card_number
        else:
            raise CreditCardException('Invalid credit card number.')

    def _save_payment(self, payment, target):
        # Save each payment made and received for the user to retrieve them in retrieve_feed
        self._payments.append(payment)
        target._payments.append(payment)

    def pay(self, target, amount, note):
        # TODO: add logic to pay with card or balance
        if amount <= self.balance:
            p = self.pay_with_balance(target, amount, note)
            self._save_payment(p, target)
        else:
            p = self.pay_with_card(target, amount, note)
            self._save_payment(p, target)

    def pay_with_card(self, target, amount, note):
        amount = float(amount)

        if self.username == target.username:
            raise PaymentException('User cannot pay themselves.')
        elif amount <= 0.0:
            raise PaymentException('Amount must be a non-negative number.')
        elif self.credit_card_number is None:
            raise PaymentException(
                'Must have a credit card to make a payment.')

        self._charge_credit_card(self.credit_card_number)
        payment = Payment(amount, self, target, note)
        target.add_to_balance(amount)

        return payment

    def pay_with_balance(self, target, amount, note):
        # TODO: add code here
        self.balance -= amount
        payment = Payment(amount, self, target, note)
        target.add_to_balance(amount)

        return payment

    def _is_valid_credit_card(self, credit_card_number):
        return credit_card_number in ["4111111111111111", "4242424242424242"]

    def _is_valid_username(self, username):
        return re.match('^[A-Za-z0-9_\\-]{4,15}$', username)

    def _charge_credit_card(self, credit_card_number):
        # magic method that charges a credit card thru the card processor
        pass


class MiniVenmo:

    @staticmethod
    def create_user(username, balance, credit_card_number):
        # TODO: add code here
        user = User(username)
        user.add_to_balance(balance)
        user.add_credit_card(credit_card_number)
        return user

    @staticmethod
    def render_feed(feed):
        # Bobby paid Carol $5.00 for Coffee
        # Carol paid Bobby $15.00 for Lunch
        # TODO: add code here
        for f in feed:
            print(f)

    @classmethod
    def run(cls):
        venmo = cls()

        bobby = venmo.create_user("Bobby", 5.00, "4111111111111111")
        carol = venmo.create_user("Carol", 10.00, "4242424242424242")

        try:
            # should complete using balance
            bobby.pay(carol, 5.00, "Coffee")

            # should complete using card
            carol.pay(bobby, 15.00, "Lunch")
        except PaymentException as e:
            print(e)

        feed = bobby.retrieve_feed()
        venmo.render_feed(feed)

        bobby.add_friend(carol)


class TestUser(unittest.TestCase):

    def test_this_works(self):
        with self.assertRaises(UsernameException):
            raise UsernameException()

    # def test_create_already_existing_user(self):
    #     user1 = MiniVenmo.create_user("gonzalo", 10.0, "4111111111111111")
    #     user2 = MiniVenmo.create_user("gonzalo", 10.0, "4111111111111111")
    #     self.assertRaises(UsernameException)

    def test_pay_with_balance(self):
        user1 = MiniVenmo.create_user("gonzalo", 10.0, "4111111111111111")
        user2 = MiniVenmo.create_user("lucvvoo", 10.0, "4242424242424242")
        user1.pay(user2, 9.0, "Pedido")
        assert user2.balance == 19.0

    def test_pay_with_credit_card(self):
        user1 = MiniVenmo.create_user("gonzalo", 10.0, "4111111111111111")
        user2 = MiniVenmo.create_user("lucvvoo", 10.0, "4242424242424242")
        user1.pay(user2, 11.0, "Pedido 2")
        user1.retrieve_feed
        assert user2.balance == 21.0

    def test_cant_pay_themself(self):
        user1 = MiniVenmo.create_user("gonzalo", 10.0, "4111111111111111")
        user1.pay(user1, 8.0, "Transf")
        print(user1.balance)
        self.assertRaises(PaymentException)


if __name__ == '__main__':
    unittest.main()
