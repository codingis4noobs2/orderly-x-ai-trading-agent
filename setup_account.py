# setup_account.py

import os
import asyncio
from base58 import b58encode
from eth_rpc import *
from emp_orderly import EmpyrealOrderlySDK, Strategy, crossover, SMA, EmpOrderly
from emp_orderly_types import *
from emp_orderly.onboarding import *
from emp_orderly.utils.ed25519 import *
from emp_orderly.utils.orderly_id import from_address

from dotenv import load_dotenv, set_key

# Load existing .env file if it exists
load_dotenv()

# Utility function to write key-value pairs to .env file
def write_to_env(key: str, value: str):
    set_key(".env", key, value)

async def setup_orderly_account():
    """Create a new wallet, register it on Orderly, and store credentials in .env."""
    wallet = PrivateKeyWallet.create_new()
    print(f"New Wallet Created!\nAddress: {wallet.address}\nPrivate Key: {wallet.private_key}")

    write_to_env("WALLET_ADDRESS", wallet.address)
    write_to_env("PVT_HEX", wallet.private_key)

    try:
        await create_account(wallet)
        await asyncio.sleep(3)  # Wait for account creation to process
        print(f"Account created successfully for wallet: {wallet.address}")
    except Exception as e:
        print(f"Error creating Orderly account: {e}")
        return None

    key_bytes = publickey(bytes.fromhex(wallet.private_key.removeprefix("0x")))
    orderly_key = "ed25519:%s" % b58encode(key_bytes).decode("utf-8")

    write_to_env("ORDERLY_KEY", orderly_key)

    try:
        await add_access_key(wallet, orderly_key)
        print(f"Orderly key registered successfully: {orderly_key}")
    except Exception as e:
        print(f"Error registering orderly key: {e}")
        return None
    print("Account setup completed!")
    
    # Save the account address to .env
    write_to_env("ACCOUNT_ID", from_address(wallet.address))
    print(f"Account ID: {from_address(wallet.address)} stored in .env")

    write_to_env("GCP_PROJECT_ID", "")
    write_to_env("GOOGLE_APPLICATION_CREDENTIALS", "")

    return wallet.address

# Main function to run the setup
if __name__ == "__main__":
    try:
        # Create and set up the account
        asyncio.run(setup_orderly_account())
        print("Setup completed. Check the .env file for your account details.")
    except KeyboardInterrupt:
        print("Setup process interrupted.")
