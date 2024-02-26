# Disable Tilt analytics
analytics_settings(enable=False)

# Disable Tilt redacted secret
secret_settings(disable_scrub=True)


# Function to remove security context from yaml before applying
# Tilt does not support security context
def remove_security_context(yaml):
    objects = read_yaml_stream(yaml)
    for o in objects:
        if o['kind'] == 'Deployment':
            o['spec']['template']['spec']['securityContext'] = {}
            o['spec']['template']['spec']['containers'][0]['securityContext'] = {}
    k8s_yaml(encode_yaml_stream(objects))

# K8s Manifest Files
yamls = [
    './k8s/user-service.yaml',
    './k8s/product-service.yaml'
]

for yaml in yamls:
    remove_security_context(yaml)

###
# Service : user-service
#
###
docker_build("user-service", 
            context='./user-service',
            live_update=[
                sync('./user-service', '/app'),
            ]
)

###
# Service : product-service
#
###
docker_build("product-service", 
            context='./product-service',
            live_update=[
                sync('./product-service', '/app'),
            ]
)
