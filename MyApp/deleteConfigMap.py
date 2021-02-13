from kubernetes import client, config
from kubernetes.client.rest import ApiException
from pprint import pprint


def deleteConfigMap(api_instance,namespace,name):
        print("delete config map")
        body = client.V1DeleteOptions()  # V1DeleteOptions |
        pretty = 'pretty_example'  # str | If 'true', then the output is pretty printed. (optional)

        try:
           api_response = api_instance.delete_namespaced_config_map(name=name, namespace=namespace, body=body)
           print(api_response)
        except ApiException as e:
          print("Exception when calling CoreV1Api->delete_namespaced_config_map: %s\n" % e)

def main():
    config.load_kube_config()
    configuration = client.Configuration()
    api_instance = client.CoreV1Api()
    deleteConfigMap(api_instance,"umbertorace","activities")

if __name__ == '__main__':
    main()
