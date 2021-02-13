from kubernetes import client, config
from kubernetes.client.rest import ApiException
from pprint import pprint


def create_configmap(api_instance, configmap):
    try:
        api_response = api_instance.create_namespaced_config_map(
            namespace="umbertorace",
            body=configmap,
            pretty = 'pretty_example',
        )
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CoreV1Api->create_namespaced_config_map: %s\n" % e)


def create_configmap_object():
    # Configureate ConfigMap metadata
    metadata = client.V1ObjectMeta(
        annotations=dict(app="test", person="chummy"),
        deletion_grace_period_seconds=30,
        labels=dict(app="test", person="chummy"),
        name="activities",
        namespace="umbertorace",
    )
    # Get File Content
    with open('/MyApp/Activities.csv', 'r') as f:
        file_content=f.read()
    # Instantiate the configmap object
    configmap = client.V1ConfigMap(
        api_version="v1",
        kind="ConfigMap",
        data=dict(activities=file_content),
        metadata=metadata
    )

    return configmap

def main():
    config.load_kube_config()
    configuration = client.Configuration()
    #api_instance = client.CoreV1Api(client.ApiClient(configuration))
    api_instance = client.CoreV1Api()
    configmap = create_configmap_object()
    create_configmap(api_instance, configmap)

if __name__ == '__main__':
    main()
