import ovh
import requests
import os
import json

# Replace these with your actual API credentials
API_ENDPOINT = "ovh-eu"
APP_KEY = os.getenv("OVH_APP_KEY")
APP_SECRET = os.getenv("OVH_APP_SECRET")
CONSUMER_KEY = os.getenv("OVH_CONSUMER_KEY")
serviceName = "samplegiova"
customHostname = "servicetestovhhyper"
installRTM = False
installSqlServer = False
noRaid = True
softRaidDevices = None
sshKeyName = "test-ssh-key"
templateName = "debian11_64"
# order
duration = "P1M"
pricingMode = "default"
planCode = "22sk011"
pricingMode = "default"
#https://www.ovh.it/order/dedicated/?configure=1&v=2&ecorange=#/dedicated/configure?selection=~(datacenters~(~(id~'fr~quantity~1~availability~'1_h_high))~invoiceName~'KS-12~memory~'ram-64g-sk051~planCode~'22sk051~storage~'softraid-2x480ssd-sk051~bandwidth~'bandwidth-100-included-ks~duration~'P1M~pricingMode~'default)

client = ovh.Client(
        endpoint = API_ENDPOINT,
        application_key = APP_KEY,
        application_secret = APP_SECRET,
        consumer_key = CONSUMER_KEY
        )

## Create a session with OVH API
#session = requests.Session()
#session.headers = {
#    "X-Ovh-Application": APP_KEY,
#    "Content-type": "application/json"
#}
#session.auth = (APP_KEY, APP_SECRET)

# Step 1: Start a new order for a dedicated server
def start_install():
    response = client.post('/dedicated/server/' + serviceName + '/install/start',
           details = {
               customHostname: customHostname,
               installRTM: installRTM,
               installSqlServer: installSqlServer,
               noRaid: noRaid,
               softRaidDevices: softRaidDevices,
               sshKeyName: sshKeyName
               }, 
            templateName = templateName
            )
    return response

def get_service():
    response = client.get('/order/dedicated/server')
    return response

def create_cart():
    response = client.post('/order/cart',
            description = "giova test cart",
            ovhSubsidiary = "IT")
    return response

def cart_dedicated(cartId):
    response = client.get('/order/cart/' + cartId + '/dedicated')
    print(json.dumps(response))
    return response

def order_host(cartId):
    response = client.post('/order/cart/' + cartId + '/dedicated',
            duration = duration,
            planCode = planCode,
            pricingMode = pricingMode,
            quantity = 1
            )
# Step 2: Add desired configurations to the order
#def configure_order(order_id, configuration_id):
#    response = session.post(f"{API_ENDPOINT}/order/dedicated/server/{order_id}/configure", json={
#        "duration": 1,  # Change to desired duration
#        "planCode": configuration_id  # The code for the dedicated server configuration
#    })
#    return response.json()
#
## Step 3: Finalize the order
#def finalize_order(order_id):
#    response = session.post(f"{API_ENDPOINT}/order/dedicated/server/{order_id}/checkout")
#    return response.json()

#def welcome():
#    response = client.get('/me')['firstname']
#    return response

# Main function
def main():
    try:
        # Step n: Start the setup
        #start_install_result = start_install()
        get_cart_id = create_cart()
        print("Cart id: %s" % get_cart_id["cartId"])
        order_host_result = order_host(get_cart_id["cartId"])
        print(order_host_result)
        #result = order_host(get_cart_id["cartId"])
        #order_id = order_info["orderId"]
        #
        ## Step 2: Configure the order (replace 'config_id' with the actual configuration ID)
        #config_id = "your_configuration_id"
        #configure_order(order_id, config_id)
        #
        ## Step 3: Finalize the order
        #finalize_order(order_id)
        #
        #print("Order successfully placed!")

        #welcome_response = welcome()
        #print(welcome_response)

    
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()

