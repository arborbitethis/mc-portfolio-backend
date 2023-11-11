# mc-portfolio-backend

get info for the azure credentials secret

az ad sp create-for-rbac --name "githubAction" --role contributor \
                            --scopes /subscriptions/<subscription>/resourceGroups/<resourcegroup> \
                                                    --sdk-auth

automation todo...

1. push image to ECR, get image URI back
2. start up postgres task, apply database seed files?? <- extract databse URL
3. create/update task definition for ECS (fargate)
4. create service 

do I need to shutdown old service?





