Player Exchange System - Python
import web3

# Connect to the Ethereum node
w3 = web3.Web3(web3.Web3.HTTPProvider("http://localhost:8545"))

# Load the ABI and address of the deployed exchange contract
with open("exchange.json") as f:
    data = json.load(f)
abi = data["abi"]
address = data["address"]

# Create a contract instance
exchange = w3.eth.contract(abi=abi, address=address)

class Exchange:
    def __init__(self):
        self.offers = []
    
    def create_offer(self, player, item, price):
        # Create a new offer to sell an item
        offer_id = len(self.offers)
        self.offers.append({"player": player, "item": item, "price": price})
        # Store the offer data in the contract
        exchange.functions.createOffer(offer_id, player.name, item.name, price).transact()
    
    def cancel_offer(self, player, offer_id):
        # Cancel an existing offer
        offer = self.offers[offer_id]
        if offer["player"] == player:
            self.offers[offer_id] = None
            # Remove the offer data from the contract
            exchange.functions.c
Here are the details of the smart contract functions:








import json
from web3 import Web3

# Connect to the Ethereum node
w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))

# Load the ABI and address of the deployed exchange contract
with open("exchange.json") as f:
    data = json.load(f)
abi = data["abi"]
address = data["address"]

# Create a contract instance
exchange = w3.eth.contract(abi=abi, address=address)

class Exchange:
    def __init__(self):
        # Initialize an empty dictionary to store the offers
        self.offers = {}
    
    def create_offer(self, player, item, price):
        """
        Creates a new offer to sell an item.
        
        Parameters:
            player (Player): The player who is making the offer.
            item (Item): The item being offered for sale.
            price (int): The price of the item in wei.
        """
        # Generate a unique ID for the offer
        offer_id = len(self.offers)
        # Store the offer data in the dictionary
        self.offers[offer_id] = {"player": player, "item": item, "price": price}
        # Store the offer data in the contract
        exchange.functions.createOffer(offer_id, player.name, item.name, price).transact({"from": player.address})
    
    def cancel_offer(self, player, offer_id):
        """
        Cancels an existing offer.
        
        Parameters:
            player (Player): The player who is cancelling the offer.
            offer_id (int): The ID of the offer to cancel.
        """
        # Retrieve the offer data from the dictionary
        offer = self.offers[offer_id]
        # Check if the player who made the offer is cancelling it
        if offer["player"] == player:
            # Remove the offer data from the dictionary
            del self.offers[offer_id]
            # Remove the offer data from the contract
            exchange.functions.cancelOffer(offer_id).transact({"from": player.address})
    