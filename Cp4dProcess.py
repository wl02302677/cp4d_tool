import os

import requests
import json
import yaml

from factory.CardFactory import CardFactory

class Cp4dProcess:
    def __init__(self):
        config_file = './config/config.yaml'
        if not os.path.exists(config_file):
            raise Exception("There is no configuration file '{}'".format(config_file))
        else:
            with open(config_file) as f:
                config = yaml.safe_load(f)
        self.basic_url = config['host_url']
        self.token = config['token']
        self.content_type = 'application/json'

    def get_cus_card_list(self):
        res = requests.get(self.basic_url,
                           headers={'Authorization': self.token, 'Content-Type': self.content_type},
                           verify=False)
        print(res.text)

    def create_card(self, card_name, data, permissions, order, title):
        card_factory = CardFactory()
        card_data = card_factory.init_card('ContentBlockCardCreator').create_card(data, permissions, order, title)
        card_data = json.dumps(card_data.__dict__)
        # card_data = card_creator.create_card(data, permissions, order, title)

        target_card_url = self.basic_url + '/' + card_name
        res = requests.put(target_card_url,
                           data=card_data,
                           headers={'Authorization': self.token, 'Content-Type': self.content_type},
                           verify=False)
        print(res.text)

    def delete_card(self, card_name):
        target_card_url = self.basic_url + '/' + card_name
        res = requests.delete(target_card_url,
                              headers={'Authorization': self.token},
                              verify=False)
        print(res.text)

    def update_card(self, card_name, card_data_u):
        target_card_url = self.basic_url + '/' + card_name
        res = requests.patch(target_card_url,
                             data=card_data_u,
                             headers={'Authorization': self.token, 'Content-Type': self.content_type},
                             verify=False)


if __name__ == '__main__':
    card_name = 'ibm_test_2'
    order = 2
    permissions = ["access_catalog"]
    title = "Customer factory test2"
    # TODO: different kind template's data object
    data = {
        "content_block_data": {
            "rows": [
                {
                    "content": "cp4d customer factory document",
                    "type": "text",
                    "nav_url": "https://www.ibm.com/docs/en/cloud-paks/cp-data/4.0?topic=resources-home-page-custom-cards-apis#custom-kpi__legend",
                    "window_open_target": ""
                },
                {
                    "content": "https://www.ibm.com/docs/en/cloud-paks/cp-data/4.0?topic=resources-home-page-custom-cards-apis#custom-kpi__legend",
                    "type": "link",
                    "nav_url": "https://www.ibm.com/docs/en/cloud-paks/cp-data/4.0?topic=resources-home-page-custom-cards-apis#custom-kpi__legend",
                    "window_open_target": "_blank"
                }
            ]
        }
    }

    process = Cp4dProcess()
    # factory.create_card(card_name, data, permissions, order, title)
    process.delete_card(card_name)
