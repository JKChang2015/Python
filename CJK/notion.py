# notion
# Created by JKChang
# 06/12/2019, 13:07
# Tag:
# Description: 

from notion.client import NotionClient
from notion.client import NotionClient

token = '0d8f78c9d64c583b2af4eb98888af3bd40cedd65ad4a0ca560d5501dd94bfeea3d5ec71ce0fbd8977e250b944dc8a3f21d8d85378cb4b15728dd48d98679e85963beebe25ac1ca4d4a2d1e72b8e9'

client = NotionClient(token_v2=token)


page = 'https://www.notion.so/jkchang/a483746f734c435dbe211ad2e2ff1aed?v=e15c98ee493244ecbb31b4578198375f'

print("The old title is:", page.title)