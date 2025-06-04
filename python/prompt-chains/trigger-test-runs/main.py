import os

import dotenv
from maxim import Maxim
from maxim.models import LocalData
from maxim.models.dataset import DataStructure

dotenv.load_dotenv()

client = Maxim({"base_url": "http://localhost:3000"})

list_of_urls: list[LocalData] = [
    {
        "input": "https://images.unsplash.com/photo-1748783266580-a5b05c4e54b1?q=80&w=3174&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    }
]

data_structure: DataStructure = {"input": "FILE_URL_VARIABLE"}

WORKSPACE_ID = os.getenv("MAXIM_WORKSPACE_ID")
PROMPT_CHAIN_VERSION_ID = os.getenv("MAXIM_PROMPT_CHAIN_VERSION_ID")

if __name__ == "__main__":
    client.create_test_run(
        name="Local dataset test run from SDK", in_workspace_id=WORKSPACE_ID
    ).with_concurrency(2).with_data(list_of_urls).with_data_structure(
        data_structure
    ).with_prompt_chain_version_id(PROMPT_CHAIN_VERSION_ID).run()
